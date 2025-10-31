#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parents[1]
CURSOR_RULES = REPO_ROOT / ".cursor" / "rules"
CURSOR_COMMAND_DOCS = REPO_ROOT / ".cursor" / "commands"

SUPPORTED_RULE_EXTS = [".mdc"]
SUPPORTED_CMD_DOC_PATTERN = "-cmd.md"  # Pattern: *-cmd.md


def collect_files(base: Path, exts: List[str]) -> List[Path]:
    results: List[Path] = []
    for ext in exts:
        results.extend(base.glob(f"*{ext}"))
    return results


def collect_command_docs(base: Path) -> List[Path]:
    """Collect command docs matching *-cmd.md pattern"""
    results: List[Path] = []
    for f in base.glob("*.md"):
        if f.name.endswith(SUPPORTED_CMD_DOC_PATTERN):
            results.append(f)
    return results


def copy_if_changed(src: Path, dst: Path) -> None:
    if not dst.exists() or src.read_bytes() != dst.read_bytes():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"Synced: {src.relative_to(REPO_ROOT)} -> {dst.relative_to(REPO_ROOT)}")


def sync_env_to_feature(feature_name: str) -> None:
    feature_cursor = REPO_ROOT / "features" / feature_name / "cursor"
    feature_cursor.mkdir(parents=True, exist_ok=True)

    rule_files = collect_files(CURSOR_RULES, SUPPORTED_RULE_EXTS)
    cmd_docs = collect_command_docs(CURSOR_COMMAND_DOCS)

    for rf in rule_files:
        copy_if_changed(rf, feature_cursor / rf.name)

    for cd in cmd_docs:
        copy_if_changed(cd, feature_cursor / cd.name)


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync .cursor assets back into a feature-local cursor/ folder")
    parser.add_argument("--feature", dest="feature", required=True, help="Feature name to receive env assets")
    args = parser.parse_args()

    sync_env_to_feature(args.feature)


if __name__ == "__main__":
    main()
