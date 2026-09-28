#!/usr/bin/env python3
"""Install one skill profile into a Codex-discoverable skills directory."""

import argparse
import contextlib
import json
import os
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_MANIFEST = ".skill-profile.json"
PENDING_MANIFEST = ".skill-profile-pending.json"
LEGACY_MANIFEST = ".dotskills-manifest.json"


def load_profiles():
    return json.loads((ROOT / "profiles.json").read_text())["profiles"]


def expand(profile_name, profiles, stack=()):
    if profile_name in stack or profile_name not in profiles:
        raise ValueError(f"invalid profile inheritance: {profile_name}")
    profile = profiles[profile_name]
    result = {}
    parent = profile.get("extends")
    if parent:
        result.update(expand(parent, profiles, stack + (profile_name,)))
    for repository, names in profile.get("repositories", {}).items():
        result.setdefault(repository, []).extend(names)
    return result


def source_directories(profile_name, projects_root):
    selected = expand(profile_name, load_profiles())
    sources = []
    seen_names = set()

    for repository, names in selected.items():
        repo_root = (projects_root / repository).resolve()
        registry_path = repo_root / "directory.json"
        if not registry_path.is_file():
            raise ValueError(f"missing skill registry: {registry_path}")
        registry = json.loads(registry_path.read_text()).get("skills", {})

        for name in names:
            if name in seen_names:
                raise ValueError(f"{profile_name}: duplicate skill name across repositories: {name}")
            seen_names.add(name)
            entry = registry.get(name)
            if not entry:
                raise ValueError(f"{repository}/{name} is not registered")

            skill_file = (repo_root / entry["path"]).resolve()
            try:
                skill_file.relative_to(repo_root)
            except ValueError as error:
                raise ValueError(f"{repository}/{name} resolves outside its source repository") from error
            if not skill_file.is_file() or skill_file.name != "SKILL.md":
                raise ValueError(f"missing SKILL.md: {repository}/{name}")

            skill_dir = skill_file.parent
            for item in skill_dir.rglob("*"):
                if item.is_symlink():
                    try:
                        item.resolve().relative_to(skill_dir)
                    except ValueError as error:
                        raise ValueError(f"{repository}/{name} contains a symlink outside its skill directory") from error
            sources.append((name, skill_dir))

    return sources


def read_manifest(path, label):
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot read {label}: {path}") from error
    if not isinstance(data, dict):
        raise ValueError(f"invalid {label}: {path}")
    skills = data.get("skills")
    if not isinstance(skills, list) or not all(isinstance(name, str) for name in skills):
        raise ValueError(f"invalid skills list in {label}: {path}")
    if any(not name or Path(name).name != name or name in {".", ".."} for name in skills):
        raise ValueError(f"invalid skill directory name in {label}: {path}")
    return data


@contextlib.contextmanager
def install_lock(output_root):
    """Serialize profile switches that target the same skills directory."""
    lock_path = output_root.parent / f".{output_root.name}.profile-install.lock"
    # Keep this inode: removing it can split concurrent waiters across lock files.
    if lock_path.is_symlink():
        raise ValueError(f"profile install lock must not be a symlink: {lock_path}")
    descriptor = os.open(
        lock_path,
        os.O_CREAT | os.O_RDWR | getattr(os, "O_NOFOLLOW", 0),
        0o600,
    )
    with os.fdopen(descriptor, "r+") as lock_file:
        if os.name == "nt":
            import msvcrt

            lock_file.seek(0, os.SEEK_END)
            if lock_file.tell() == 0:
                lock_file.write("\0")
                lock_file.flush()
            lock_file.seek(0)
            msvcrt.locking(lock_file.fileno(), msvcrt.LK_LOCK, 1)
            unlock = lambda: msvcrt.locking(lock_file.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            import fcntl

            fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
            unlock = lambda: fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
        try:
            yield
        finally:
            unlock()


def write_json_atomic(path, data):
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            delete=False,
        ) as file:
            temporary = Path(file.name)
            file.write(json.dumps(data, indent=2) + "\n")
        temporary.replace(path)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()


def legacy_skill_names(output_root, repositories):
    """Find old suite entries installed by the previous dot-skills mirror."""
    path = output_root / LEGACY_MANIFEST
    if not path.is_file():
        return set()
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid legacy install manifest: {path}") from error

    result = set()
    for key in data.get("skills", {}):
        repository, separator, name = key.partition(":")
        if separator and repository in repositories and name:
            result.add(name)
    return result


def archive_paths(output_root, names):
    existing = [output_root / name for name in sorted(names) if (output_root / name).exists() or (output_root / name).is_symlink()]
    if not existing:
        return None

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    archive_root = output_root.parent / "skill-profile-backups" / stamp
    archive_root.mkdir(parents=True, exist_ok=False)
    for path in existing:
        if path.parent.resolve() != output_root.resolve():
            raise ValueError(f"refusing to archive path outside the skill root: {path}")
        path.rename(archive_root / path.name)
    return archive_root


def install(profile_name, output_root, projects_root, backup_conflicts=False):
    profiles = load_profiles()
    output_root = output_root.expanduser()
    if output_root.is_symlink():
        raise ValueError("Codex skills directory must not be a symlink")
    if output_root.exists() and not output_root.is_dir():
        raise ValueError(f"Codex skills path is not a directory: {output_root}")
    output_root.mkdir(parents=True, exist_ok=True)

    with install_lock(output_root):
        return install_locked(profile_name, output_root, projects_root, backup_conflicts, profiles)


def install_locked(profile_name, output_root, projects_root, backup_conflicts, profiles):
    sources = source_directories(profile_name, projects_root)
    repositories = {repository for profile in profiles.values() for repository in profile.get("repositories", {})}
    # Include inherited repositories when finding legacy entries.
    for name in profiles:
        repositories.update(expand(name, profiles))

    active_path = output_root / ACTIVE_MANIFEST
    pending_path = output_root / PENDING_MANIFEST
    if active_path.is_symlink():
        raise ValueError(f"active profile manifest must not be a symlink: {active_path}")
    if pending_path.is_symlink():
        raise ValueError(f"pending profile manifest must not be a symlink: {pending_path}")
    previous = read_manifest(active_path, "active profile manifest") if active_path.exists() else None
    pending = read_manifest(pending_path, "pending profile manifest") if pending_path.exists() else None
    previous_names = set(previous["skills"]) if previous else set()
    pending_names = set(pending["skills"]) if pending else set()
    selected_names = {name for name, _ in sources}

    legacy_names = legacy_skill_names(output_root, repositories) - previous_names - pending_names
    managed_names = previous_names | pending_names | legacy_names
    conflicts = {
        name for name in selected_names
        if (output_root / name).exists() or (output_root / name).is_symlink()
    } - managed_names
    if conflicts and not backup_conflicts:
        names = ", ".join(sorted(conflicts))
        raise ValueError(
            f"existing skills are not owned by this installer: {names}. "
            "Move them aside yourself or rerun with --backup-conflicts to preserve them in a backup."
        )

    archive_names = managed_names - selected_names
    if backup_conflicts:
        archive_names |= conflicts

    with tempfile.TemporaryDirectory(prefix=".skill-profile-stage-", dir=output_root.parent) as temp:
        staged = Path(temp)
        for name, source in sources:
            shutil.copytree(source, staged / name)

        recovery_names = managed_names | selected_names
        if backup_conflicts:
            recovery_names |= conflicts
        write_json_atomic(pending_path, {"profile": profile_name, "skills": sorted(recovery_names)})
        archived = archive_paths(output_root, archive_names)
        for name, source in sources:
            destination = output_root / name
            if destination.exists() or destination.is_symlink():
                if name not in managed_names and name not in conflicts:
                    raise ValueError(f"refusing to replace unmanaged skill: {destination}")
                if destination.is_dir() and not destination.is_symlink():
                    shutil.rmtree(destination)
                else:
                    destination.unlink()
            (staged / name).rename(destination)

    manifest = {
        "profile": profile_name,
        "skills": sorted(selected_names),
    }
    write_json_atomic(active_path, manifest)
    pending_path.unlink(missing_ok=True)
    return output_root, len(sources), archived


def main():
    profiles = load_profiles()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", choices=sorted(profiles))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path.home() / ".agents" / "skills",
        help="Codex skills directory (default: ~/.agents/skills)",
    )
    parser.add_argument(
        "--projects-root",
        type=Path,
        default=ROOT.parent,
        help="Directory containing the sibling source repositories (default: %(default)s)",
    )
    parser.add_argument(
        "--backup-conflicts",
        action="store_true",
        help="Preserve conflicting unmanaged skill folders in a timestamped backup before activation",
    )
    args = parser.parse_args()

    try:
        output, count, archived = install(args.profile, args.output, args.projects_root, args.backup_conflicts)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Profile install failed: {error}", file=sys.stderr)
        return 1

    print(f"Active profile: {args.profile} ({count} skills) -> {output}")
    if archived:
        print(f"Previous suite skills preserved at: {archived}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
