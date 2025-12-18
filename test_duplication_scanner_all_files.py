#!/usr/bin/env python3
"""Test duplication scanner on all files in src directory"""

import sys
import logging
from pathlib import Path
from collections import defaultdict

# Set up logging to see what's happening
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(name)s - %(message)s'
)

# Add workspace to path
workspace_root = Path(__file__).parent
sys.path.insert(0, str(workspace_root))

from agile_bot.bots.base_bot.src.actions.validate.rule import Rule

# Load actual rule file
rule_file = Path("agile_bot/bots/story_bot/behaviors/code/rules/eliminate_duplication.json")
if not rule_file.exists():
    print(f"ERROR: Rule file not found: {rule_file}")
    exit(1)

rule_obj = Rule(rule_file, behavior_name="code", bot_name="story_bot")
scanner = rule_obj.scanner

if scanner is None:
    print("ERROR: Scanner is None!")
    exit(1)

# Find all Python files in src directory
src_dir = Path("agile_bot/bots/base_bot/src")
all_py_files = list(src_dir.rglob("*.py"))

print(f"Found {len(all_py_files)} Python files to scan")
print("=" * 80)

total_violations = 0
files_with_violations = []
files_scanned = 0
files_skipped = 0
files_errored = []

for file_path in all_py_files:
    # Skip __pycache__ and test files for now
    if '__pycache__' in str(file_path):
        continue
    
    files_scanned += 1
    try:
        violations = scanner.scan_code_file(file_path, rule_obj)
        
        if violations is None:
            print(f"ERROR: {file_path} returned None!")
            files_errored.append((file_path, "Returned None"))
            continue
        
        if violations:
            total_violations += len(violations)
            files_with_violations.append((file_path, len(violations)))
            print(f"\n[{len(violations)} violations] {file_path}")
            for i, v in enumerate(violations[:3], 1):  # Show first 3
                print(f"  {i}. Line {v.get('line_number', '?')}: {v.get('violation_message', '')[:100]}")
        
        if files_scanned % 10 == 0:
            print(f"Scanned {files_scanned} files... ({len(files_with_violations)} with violations)")
            
    except Exception as e:
        files_errored.append((file_path, str(e)))
        print(f"ERROR scanning {file_path}: {e}")

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Total files scanned: {files_scanned}")
print(f"Files with violations: {len(files_with_violations)}")
print(f"Total violations found: {total_violations}")
print(f"Files with errors: {len(files_errored)}")

if files_with_violations:
    print("\nFiles with violations:")
    for file_path, count in sorted(files_with_violations, key=lambda x: x[1], reverse=True):
        print(f"  {count:3d} violations: {file_path}")

if files_errored:
    print("\nFiles with errors:")
    for file_path, error in files_errored[:10]:
        print(f"  {file_path}: {error}")







