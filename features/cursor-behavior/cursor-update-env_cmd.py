#!/usr/bin/env python3
import argparse
import shutil
import subprocess
import sys
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
FEATURES_DIR = REPO_ROOT / "features"
CURSOR_RULES = REPO_ROOT / ".cursor" / "rules"
CURSOR_COMMAND_DOCS = REPO_ROOT / ".cursor" / "commands"
COMMANDS_DIR = REPO_ROOT / "commands"

SUPPORTED_RULE_EXTS = [".mdc"]
SUPPORTED_CMD_DOC_PATTERN = "-cmd.md"  # Pattern: *-cmd.md
SUPPORTED_CMD_FUNC_PATTERN = "_cmd.py"  # Pattern: *_cmd.py


def ensure_dirs() -> None:
    CURSOR_RULES.mkdir(parents=True, exist_ok=True)
    CURSOR_COMMAND_DOCS.mkdir(parents=True, exist_ok=True)
    COMMANDS_DIR.mkdir(parents=True, exist_ok=True)


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


def collect_command_functions(base: Path) -> List[Path]:
    """Collect command functions matching *_cmd.py pattern"""
    results: List[Path] = []
    for f in base.glob("*.py"):
        if f.name.endswith(SUPPORTED_CMD_FUNC_PATTERN):
            results.append(f)
    return results


def copy_if_changed(src: Path, dst: Path) -> None:
    if not dst.exists() or src.read_bytes() != dst.read_bytes():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"Synced: {src.relative_to(REPO_ROOT)} -> {dst.relative_to(REPO_ROOT)}")


def iter_feature_cursor_dirs(feature_name: str | None) -> List[Path]:
    dirs: List[Path] = []
    for feature in FEATURES_DIR.iterdir():
        if not feature.is_dir():
            continue
        if feature_name and feature.name != feature_name:
            continue
        cursor_dir = feature / "cursor"
        if cursor_dir.exists():
            dirs.append(cursor_dir)
        # Also check if files are directly in feature folder (cursor-behavior case)
        elif any(
            f.suffix == ".mdc" or (f.suffix == ".md" and "-cmd.md" in f.name) or (f.suffix == ".py" and "_cmd.py" in f.name)
            for f in feature.iterdir()
            if f.is_file()
        ):
            dirs.append(feature)
    return dirs


def sync_feature_to_env(feature_name: str | None) -> None:
    for cursor_dir in iter_feature_cursor_dirs(feature_name):
        # Rules
        for rf in collect_files(cursor_dir, SUPPORTED_RULE_EXTS):
            copy_if_changed(rf, CURSOR_RULES / rf.name)
        # Command docs (must match *-cmd.md pattern)
        for cd in collect_command_docs(cursor_dir):
            copy_if_changed(cd, CURSOR_COMMAND_DOCS / cd.name)
        # Command functions (must match *_cmd.py pattern)
        for cf in collect_command_functions(cursor_dir):
            copy_if_changed(cf, COMMANDS_DIR / cf.name)


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync feature-local Cursor assets to .cursor and commands")
    parser.add_argument("--feature", dest="feature", default=None, help="Optional feature name to scope sync")
    parser.add_argument("--no-index", action="store_true", help="Skip updating the index after sync")
    args = parser.parse_args()

    ensure_dirs()
    sync_feature_to_env(args.feature)
    
    # Update index after sync
    if not args.no_index:
        try:
            scan_script = REPO_ROOT / "features" / "cursor-behavior" / "cursor-scan-behavior-index_cmd.py"
            if scan_script.exists():
                print("\nUpdating index...")
                subprocess.run([sys.executable, str(scan_script)], check=False)
        except Exception as e:
            print(f"\nWarning: Could not update index: {e}")


if __name__ == "__main__":
    main()
