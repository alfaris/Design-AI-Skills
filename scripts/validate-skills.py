"""Validate the installable skills in this repository."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED_FRONTMATTER = {"name", "description"}
REQUIRED_AGENT_KEYS = {"display_name", "short_description", "default_prompt"}
FRONTMATTER_PATTERN = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
KEY_PATTERN = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s|$)")
LINK_PATTERN = re.compile(r"\[[^]]+\]\(([^)]+)\)")
SKIP_DIRECTORIES = {".git", "assets", "scripts"}
INSTALLER_REQUIREMENTS = (
    "https://raw.githubusercontent.com/alfaris/Design-AI-Skills-by-Faris/main",
    "design-audit-panel",
    "devils-advocate-and-convincer",
    "SKILL.md",
    "agents/openai.yaml",
    "references/",
    "file-writing permission",
    "الوصول إلى الويب",
)


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return {}, ["missing YAML frontmatter delimited by ---"]

    values: dict[str, str] = {}
    errors: list[str] = []
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key_match = KEY_PATTERN.match(line)
        if not key_match:
            errors.append(f"unsupported frontmatter line: {line!r}")
            continue
        key = key_match.group(1)
        value = line[key_match.end() :].strip().strip('"\'')
        values[key] = value
    return values, errors


def parse_agent_metadata(path: Path) -> tuple[set[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    keys = set()
    errors: list[str] = []
    in_interface = False
    for line in text.splitlines():
        if line.strip() == "interface:":
            in_interface = True
            continue
        if in_interface and line and not line.startswith((" ", "\t")):
            in_interface = False
        if in_interface:
            match = KEY_PATTERN.match(line.strip())
            if match:
                keys.add(match.group(1))
    if not in_interface and "interface:" not in text:
        errors.append("missing interface metadata")
    return keys, errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_path = skill_dir / "SKILL.md"
    if not skill_path.is_file():
        return ["missing SKILL.md"]

    frontmatter, frontmatter_errors = parse_frontmatter(skill_path)
    errors.extend(frontmatter_errors)
    missing = REQUIRED_FRONTMATTER - frontmatter.keys()
    errors.extend(f"missing frontmatter key: {key}" for key in sorted(missing))
    name = frontmatter.get("name")
    if name and name != skill_dir.name:
        errors.append(f"frontmatter name {name!r} does not match folder name {skill_dir.name!r}")

    agent_path = skill_dir / "agents" / "openai.yaml"
    if not agent_path.is_file():
        errors.append("missing agents/openai.yaml")
    else:
        agent_keys, agent_errors = parse_agent_metadata(agent_path)
        errors.extend(agent_errors)
        errors.extend(f"missing agent metadata key: {key}" for key in sorted(REQUIRED_AGENT_KEYS - agent_keys))

    for target in LINK_PATTERN.findall(skill_path.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        relative_target = target.split("#", 1)[0]
        if relative_target and not (skill_dir / relative_target).exists():
            errors.append(f"broken local link: {target}")
    return errors


def find_skill_directories(root: Path) -> list[Path]:
    return sorted(
        path.parent
        for path in root.glob("**/SKILL.md")
        if not any(part in SKIP_DIRECTORIES for part in path.parts)
    )


def validate_installer(root: Path) -> list[str]:
    installer_path = root / "INSTALL.md"
    if not installer_path.is_file():
        return ["missing INSTALL.md"]

    text = installer_path.read_text(encoding="utf-8")
    return [
        f"missing installer requirement: {requirement}"
        for requirement in INSTALLER_REQUIREMENTS
        if requirement not in text
    ]


def validate(root: Path) -> int:
    skill_dirs = find_skill_directories(root)
    if not skill_dirs:
        print("No SKILL.md files found.", file=sys.stderr)
        return 1

    errors_by_path: dict[Path, list[str]] = {}
    installer_errors = validate_installer(root)
    if installer_errors:
        errors_by_path[root / "INSTALL.md"] = installer_errors

    names: dict[str, Path] = {}
    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        frontmatter, _ = parse_frontmatter(skill_dir / "SKILL.md")
        name = frontmatter.get("name")
        if name:
            previous = names.get(name)
            if previous:
                errors.append(f"duplicate skill name {name!r} (also in {previous})")
            else:
                names[name] = skill_dir
        if errors:
            errors_by_path[skill_dir] = errors

    plugin_path = root / ".claude-plugin" / "plugin.json"
    if plugin_path.is_file():
        try:
            plugin = json.loads(plugin_path.read_text(encoding="utf-8"))
            for key in ("name", "version", "description"):
                if not isinstance(plugin.get(key), str) or not plugin[key].strip():
                    errors_by_path.setdefault(plugin_path, []).append(f"missing plugin key: {key}")
            version_path = root / "VERSION"
            if version_path.is_file() and plugin.get("version") != version_path.read_text(encoding="utf-8").strip():
                errors_by_path.setdefault(plugin_path, []).append("plugin version does not match VERSION")
        except (json.JSONDecodeError, OSError) as error:
            errors_by_path.setdefault(plugin_path, []).append(f"invalid plugin manifest: {error}")

    if errors_by_path:
        for path, errors in errors_by_path.items():
            for error in errors:
                print(f"{path}: {error}")
        print(f"Validation failed: {sum(len(errors) for errors in errors_by_path.values())} error(s).", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skill(s): " + ", ".join(path.name for path in skill_dirs))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    return validate(args.root.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
