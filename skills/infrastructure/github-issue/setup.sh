#!/bin/bash
#
# Name:    setup.sh
# Purpose: Install symlinks for the github-issue skill across multiple
#          AI coding assistant tools (OpenCode, Cursor, VSCode, Agents).
#
# Usage:   ./setup.sh
#
# Requirements:
#   - The github-issue skill must be installed at ~/.opencode/skills/github-issue
#   - Write access to ~/.cursor/rules/, ~/.vscode/skills/, ~/.agents/skills/
#
# What it does:
#   Creates symbolic links so that OpenCode, Cursor, VSCode, and compatible
#   agent runners can discover and load the github-issue SKILL.md from a
#   single source (~/.opencode/skills/github-issue).
#   Skipped gracefully when a target directory does not exist.

set -e

SKILL_SOURCE="$HOME/.opencode/skills/github-issue"

echo "Setting up github-issue skill across tools..."

# Check if skill exists
if [ ! -d "$SKILL_SOURCE" ]; then
    echo "Error: Skill not found at $SKILL_SOURCE"
    echo "Please ensure the skill is installed at ~/.opencode/skills/github-issue"
    exit 1
fi

# OpenCode (already in place)
echo "✓ OpenCode: $SKILL_SOURCE"

# Cursor
CURSOR_RULES="$HOME/.cursor/rules/github-issue"
if [ -d "$HOME/.cursor/rules" ]; then
    if [ -L "$CURSOR_RULES" ] || [ -d "$CURSOR_RULES" ]; then
        echo "✓ Cursor: Already linked at $CURSOR_RULES"
    else
        ln -s "$SKILL_SOURCE" "$CURSOR_RULES"
        echo "✓ Cursor: Linked to $CURSOR_RULES"
    fi
else
    echo "⚠ Cursor: ~/.cursor/rules not found, skipping"
fi

# VSCode
VSCODE_SKILLS="$HOME/.vscode/skills/github-issue"
if [ -d "$HOME/.vscode/skills" ]; then
    if [ -L "$VSCODE_SKILLS" ] || [ -d "$VSCODE_SKILLS" ]; then
        echo "✓ VSCode: Already linked at $VSCODE_SKILLS"
    else
        ln -s "$SKILL_SOURCE" "$VSCODE_SKILLS"
        echo "✓ VSCode: Linked to $VSCODE_SKILLS"
    fi
else
    echo "⚠ VSCode: ~/.vscode/skills not found, skipping"
fi

# Agents (generic)
AGENTS_SKILLS="$HOME/.agents/skills/github-issue"
if [ -d "$HOME/.agents/skills" ]; then
    if [ -L "$AGENTS_SKILLS" ] || [ -d "$AGENTS_SKILLS" ]; then
        echo "✓ Agents: Already linked at $AGENTS_SKILLS"
    else
        ln -s "$SKILL_SOURCE" "$AGENTS_SKILLS"
        echo "✓ Agents: Linked to $AGENTS_SKILLS"
    fi
else
    echo "⚠ Agents: ~/.agents/skills not found, skipping"
fi

# GitHub Copilot (if using copilot-instructions.md)
COPILOT_INSTRUCTIONS="$HOME/.config/github-copilot/instructions.md"
if [ -d "$HOME/.config/github-copilot" ]; then
    echo "ℹ GitHub Copilot: You can add the skill to $COPILOT_INSTRUCTIONS"
    echo "  Or use project-level .github/copilot-instructions.md"
fi

echo ""
echo "Setup complete! The skill is now available in:"
echo "  - OpenCode (via ~/.opencode/skills/)"
echo "  - Cursor (via ~/.cursor/rules/)"
echo "  - VSCode (via ~/.vscode/skills/)"
echo "  - Agents (via ~/.agents/skills/)"
echo ""
echo "For other tools (Gemini, Devin, etc.), you can:"
echo "  1. Copy the SKILL.md to the tool's skill/rules directory"
echo "  2. Or reference it in your project's AGENTS.md or similar"
echo ""
echo "The skill requires the GitHub CLI (gh) to be installed and authenticated."
echo "Install: https://cli.github.com/"
echo "Auth: gh auth login"
