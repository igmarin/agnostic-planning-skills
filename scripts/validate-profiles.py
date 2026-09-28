#!/usr/bin/env python3
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT.parent
profiles = json.loads((ROOT / "profiles.json").read_text())["profiles"]
fixtures = json.loads((ROOT / "scripts/router-fixtures.json").read_text())
errors = []

def expand(profile_name, stack=()):
    if profile_name in stack or profile_name not in profiles:
        errors.append(f"invalid profile inheritance: {profile_name}")
        return {}
    profile = profiles[profile_name]
    repositories = {}
    parent = profile.get("extends")
    if parent:
        repositories.update(expand(parent, stack + (profile_name,)))
    for repository, names in profile.get("repositories", {}).items():
        repositories.setdefault(repository, []).extend(names)
    for repository, names in repositories.items():
        if len(names) != len(set(names)):
            errors.append(f"{profile_name}: duplicate skills in {repository}")
    return repositories

expanded = {name: expand(name) for name in profiles}
for profile_name, repositories in expanded.items():
    names = [name for skills in repositories.values() for name in skills]
    if len(names) != len(set(names)):
        errors.append(f"{profile_name}: duplicate skill names across repositories")
    for repository, names in repositories.items():
        repo = PROJECTS / repository
        registry_path = repo / "directory.json"
        if not registry_path.exists():
            errors.append(f"{profile_name}: missing repository {repository}")
            continue
        registry = json.loads(registry_path.read_text()).get("skills", {})
        for name in names:
            if name not in registry:
                errors.append(f"{profile_name}: {repository}/{name} is not registered")
            elif not (repo / registry[name]["path"]).is_file():
                errors.append(f"{profile_name}: {repository}/{name} has no SKILL.md")

def read_router_routes():
    router_path = ROOT / "skills/work-router/SKILL.md"
    try:
        router_text = router_path.read_text(encoding="utf-8")
    except OSError as error:
        errors.append(f"work-router: cannot read route contract: {error}")
        return {}

    section = re.search(r"^## Route by intent\s*$([\s\S]*?)(?=^## |\Z)", router_text, re.MULTILINE)
    if not section:
        errors.append("work-router: missing 'Route by intent' table")
        return {}

    routes = {}
    for line in section.group(1).splitlines():
        row = re.match(r"^\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$", line)
        if not row:
            continue
        intent, target = row.groups()
        if intent == "Request" or re.fullmatch(r"-+", intent):
            continue
        skills = re.findall(r"`([a-z][a-z0-9-]*)`", target)
        if len(skills) != 1:
            errors.append(f"work-router: route '{intent}' must name exactly one skill")
            continue
        if intent in routes:
            errors.append(f"work-router: duplicate route intent '{intent}'")
        routes[intent] = skills[0]
    return routes


def infer_task_intent(task, profile_name):
    task = task.lower()
    if profile_name == "foundation":
        if re.search(r"\b(review|audit)\b", task) and re.search(r"\b(brief|prd)\b", task):
            return "Review a product brief"
        if re.search(r"\b(brief|prd)\b", task):
            return "Draft a product brief"
    elif profile_name == "ruby-rails" and re.search(r"\brails\b", task):
        if re.search(r"\bmigration\b", task):
            return "Plan or review a Rails migration"
        if re.search(r"\b(review|audit)\b", task):
            return "Review Rails code"
        if re.search(r"\b(refactor|maintenance|maintain|cleanup)\b", task):
            return "Perform routine Rails maintenance"
        if re.search(r"\b(add|implement|build|create|feature|endpoint)\b", task):
            return "Implement a Rails feature"
    elif profile_name == "elixir-phoenix":
        if re.search(r"\b(ecto|database|query)\b", task):
            return "Implement Ecto/database work"
        if re.search(r"\b(elixir|phoenix)\b", task):
            return "Implement other Elixir/Phoenix work"
    elif profile_name == "rust" and re.search(r"\b(rust|crate|cargo)\b", task):
        return "Implement Rust work or verify a crate API"
    return None


router_routes = read_router_routes()
fixture_ids = set()
for fixture in fixtures:
    if fixture["id"] in fixture_ids:
        errors.append(f"duplicate router fixture id: {fixture['id']}")
    fixture_ids.add(fixture["id"])
    available = expanded.get(fixture["profile"], {}).get(fixture["repository"], [])
    expected_skill = fixture.get("expected_skill")
    if not isinstance(expected_skill, str) or expected_skill not in available:
        errors.append(f"fixture {fixture['id']}: expected skill is outside its profile")
    task = fixture.get("task", "").lower()
    expected_intent = fixture.get("expected_intent")
    task_intent = infer_task_intent(task, fixture.get("profile"))
    if task_intent is None:
        errors.append(f"fixture {fixture['id']}: cannot infer a route intent from task")
    elif task_intent != expected_intent:
        errors.append(
            f"fixture {fixture['id']}: task maps to '{task_intent}', not '{expected_intent}'"
        )
    routed_skill = router_routes.get(expected_intent)
    if routed_skill is None:
        errors.append(f"fixture {fixture['id']}: expected intent is missing from work-router")
    elif routed_skill != expected_skill:
        errors.append(
            f"fixture {fixture['id']}: work-router maps '{expected_intent}' to "
            f"'{routed_skill}', not '{expected_skill}'"
        )
    if re.search(r"\b(production|security|authorization|deploy|irreversible|delete|destructive)\b", task):
        expected_checkpoint = "high-risk"
    elif re.search(r"\b(new|unverified)\b", task) and re.search(r"\b(crate|external|third.party)\b", task) and re.search(r"\bapi\b", task):
        expected_checkpoint = "verify-api"
    else:
        expected_checkpoint = "none"
    if fixture.get("checkpoint") != expected_checkpoint:
        errors.append(f"fixture {fixture['id']}: expected checkpoint {expected_checkpoint}, got {fixture.get('checkpoint')}")

ignored = {".git", ".claude", "graphify-out", "target", "node_modules", ".venv", "vendor"}
machine_path = re.compile(
    r"/Users/[A-Za-z0-9._-]+(?=/|$)|/home/[A-Za-z0-9._-]+(?=/|$)|[A-Za-z]:\\Users\\[^\\\s]+",
    re.IGNORECASE,
)
repositories = {repo for profile in expanded.values() for repo in profile}
for repository in repositories:
    repo = PROJECTS / repository
    registry_path = repo / "directory.json"
    if not registry_path.exists():
        continue
    registry = json.loads(registry_path.read_text()).get("skills", {})
    groups_path = repo / "skills.sh.json"
    if groups_path.exists():
        try:
            groups = json.loads(groups_path.read_text()).get("groupings", [])
            grouped = [name for group in groups for name in group.get("skills", [])]
            if len(grouped) != len(set(grouped)):
                errors.append(f"{repository}: duplicate skills.sh.json group entries")
            if set(grouped) != set(registry):
                errors.append(f"{repository}: skills.sh.json groups do not match directory.json")
        except (json.JSONDecodeError, AttributeError):
            errors.append(f"{repository}: invalid skills.sh.json")

    for name, entry in registry.items():
        path = repo / entry["path"]
        if path.parent.name != name or ignored.intersection(path.parts):
            errors.append(f"{repository}/{name}: generated or mismatched registry path")
        text = path.read_text(errors="ignore") if path.is_file() else ""
        if machine_path.search(text):
            errors.append(f"{repository}/{entry['path']}: machine-specific path")
        if repository == "rust-core-skills" and "../../docs/agent-contract.md" in text:
            errors.append(f"{repository}/{name}: runtime rule depends on an uninstalled doc")
    for path in repo.rglob("*.md"):
        if ignored.intersection(path.parts) or path.name in {"report.md", ".aider.chat.history.md"}:
            continue
        text = path.read_text(errors="ignore")
        if machine_path.search(text):
            errors.append(f"{repository}/{path.relative_to(repo)}: machine-specific path")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target or ":" in target or target.startswith("/"):
                continue
            if not (path.parent / target).exists():
                errors.append(f"{repository}/{path.relative_to(repo)}: broken link {target}")

with tempfile.TemporaryDirectory(prefix="skill-profile-check-") as temp_dir:
    for profile_name, repositories in expanded.items():
        install_root = Path(temp_dir) / profile_name
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts/install-profile.py"),
                profile_name,
                "--output",
                str(install_root),
                "--projects-root",
                str(PROJECTS),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode:
            errors.append(f"{profile_name}: clean install failed: {result.stderr.strip()}")
            continue

        installed = install_root
        expected = {name for names in repositories.values() for name in names}
        actual = {path.name for path in installed.iterdir() if path.is_dir() and not path.name.startswith(".")}
        if actual != expected:
            errors.append(f"{profile_name}: clean install skill set does not match profiles.json")
        try:
            manifest = json.loads((installed / ".skill-profile.json").read_text())
            if manifest.get("profile") != profile_name or set(manifest.get("skills", [])) != expected:
                errors.append(f"{profile_name}: generated profile manifest does not match installed skills")
        except (OSError, json.JSONDecodeError):
            errors.append(f"{profile_name}: generated profile manifest is missing or invalid")

        for path in installed.rglob("*.md"):
            text = path.read_text(errors="ignore")
            skill_root = next((parent for parent in path.parents if parent != installed and (parent / "SKILL.md").is_file()), path.parent)
            for target in re.findall(r"\]\(([^)]+)\)", text):
                target = target.split("#", 1)[0].split("?", 1)[0]
                if not target or ":" in target or target.startswith("/"):
                    continue
                if not (path.parent / target).exists():
                    errors.append(f"{profile_name}/{path.relative_to(installed)}: broken installed link {target}")
            for target in re.findall(r"`((?:assets|references)/[^`\n]+)`", text):
                if any(char in target for char in "*<> "):
                    continue
                if not (skill_root / target).exists():
                    errors.append(f"{profile_name}/{path.relative_to(installed)}: missing installed resource {target}")

with tempfile.TemporaryDirectory(prefix="skill-profile-switch-check-") as temp_dir:
    output = Path(temp_dir) / ".agents" / "skills"
    output.mkdir(parents=True)
    (output / "personal-tool").mkdir()
    (output / "personal-tool" / "SKILL.md").write_text("personal skill\n")
    for name in ("generate-tasks", "rails-agent-skills"):
        (output / name).mkdir()
        (output / name / "SKILL.md").write_text("legacy generated skill\n")
    (output / ".dotskills-manifest.json").write_text(json.dumps({
        "skills": {
            "agnostic-planning-skills:generate-tasks": {"path": "generate-tasks"},
            "rails-agent-skills:rails-agent-skills": {"path": "rails-agent-skills"},
            "unrelated:personal-tool": {"path": "personal-tool"},
        }
    }))

    def activate(profile_name):
        return subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts/install-profile.py"),
                profile_name,
                "--output",
                str(output),
                "--projects-root",
                str(PROJECTS),
            ],
            capture_output=True,
            text=True,
            check=False,
        )

    first = activate("ruby-rails")
    if first.returncode:
        errors.append(f"profile activation: {first.stderr.strip()}")
    else:
        active = json.loads((output / ".skill-profile.json").read_text())
        installed = {path.name for path in output.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()}
        expected = set(active["skills"]) | {"personal-tool"}
        if installed != expected:
            errors.append("profile activation did not preserve extras and install only the selected profile")
        if not list((output.parent / "skill-profile-backups").glob("*/generate-tasks")):
            errors.append("profile activation did not back up a legacy generated skill")

        second = activate("foundation")
        if second.returncode:
            errors.append(f"profile switch: {second.stderr.strip()}")
        else:
            active = json.loads((output / ".skill-profile.json").read_text())
            installed = {path.name for path in output.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()}
            expected = set(active["skills"]) | {"personal-tool"}
            if installed != expected:
                errors.append("profile switch left old profile skills active or removed an unrelated skill")
        if not list((output.parent / "skill-profile-backups").glob("*/rails-feature")):
            errors.append("profile switch did not archive retired profile skills")

        interrupted_skill = output / "rails-feature"
        interrupted_skill.mkdir(exist_ok=True)
        (interrupted_skill / "SKILL.md").write_text("partially installed skill\n")
        (output / ".skill-profile-pending.json").write_text(json.dumps({
            "profile": "ruby-rails",
            "skills": ["rails-feature", "rails-review"],
        }))

        recovered = activate("foundation")
        if recovered.returncode:
            errors.append(f"profile recovery: {recovered.stderr.strip()}")
        else:
            active = json.loads((output / ".skill-profile.json").read_text())
            installed = {path.name for path in output.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()}
            expected = set(active["skills"]) | {"personal-tool"}
            if active.get("profile") != "foundation" or installed != expected:
                errors.append("profile recovery left a mixed or incomplete skill set")
            if (output / ".skill-profile-pending.json").exists():
                errors.append("profile recovery left its pending marker behind")
            recovered_backups = (output.parent / "skill-profile-backups").glob("*/rails-feature/SKILL.md")
            if not any(path.read_text() == "partially installed skill\n" for path in recovered_backups):
                errors.append("profile recovery did not archive the interrupted skill")

for archive_field in (True, False):
    manifest_kind = "current" if archive_field else "legacy"
    with tempfile.TemporaryDirectory(prefix="skill-profile-conflict-recovery-") as temp_dir:
        output = Path(temp_dir) / ".agents" / "skills"
        output.mkdir(parents=True)
        personal_skill = output / "rails-feature"
        personal_skill.mkdir()
        (personal_skill / "SKILL.md").write_text("personal skill\n")
        pending = {"profile": "ruby-rails", "skills": ["rails-feature"]}
        if archive_field:
            pending["archive"] = ["rails-feature"]
        (output / ".skill-profile-pending.json").write_text(json.dumps(pending))

        recovered = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts/install-profile.py"),
                "ruby-rails",
                "--output",
                str(output),
                "--projects-root",
                str(PROJECTS),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if recovered.returncode:
            errors.append(f"conflict recovery ({manifest_kind} manifest): {recovered.stderr.strip()}")
            continue

        backups = (output.parent / "skill-profile-backups").glob("*/rails-feature/SKILL.md")
        if not any(path.read_text() == "personal skill\n" for path in backups):
            errors.append(f"conflict recovery did not preserve a personal skill ({manifest_kind} manifest)")

elixir_skills = PROJECTS / "elixir-phoenix-skills" / "skills"
fp_copies = sum(path.read_text(errors="ignore").count("Canonical FP bar:") for path in elixir_skills.glob("*/SKILL.md"))
if fp_copies:
    errors.append(f"Elixir baseline copied {fp_copies} times; keep it in elixir-essentials")
for repository in ("ruby-core-skills", "rails-agent-skills", "rust-core-skills"):
    repo = PROJECTS / repository
    for path in (repo / "skills").glob("*/SKILL.md"):
        text = path.read_text(errors="ignore")
        if "Apply the [execution contract]" in text or "../../docs/agent-contract.md" in text:
            errors.append(f"{repository}/{path.parent.name}: per-skill contract pointer")

if errors:
    print("Profile validation failed:")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)
print(f"Profiles OK: {len(profiles)} clean installs, {len(fixtures)} routing/checkpoint fixtures")
