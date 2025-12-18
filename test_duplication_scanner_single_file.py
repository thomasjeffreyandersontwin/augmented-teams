#!/usr/bin/env python3
"""Test duplication scanner on a single file."""

import sys
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Add workspace to path
workspace_root = Path(__file__).parent
sys.path.insert(0, str(workspace_root))

from agile_bot.bots.base_bot.src.actions.validate.rule import Rule
from agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner import DuplicationScanner

# Load rule
print("Loading duplication rule...")
rule_file = Path("agile_bot/bots/story_bot/behaviors/code/rules/eliminate_duplication.json")
rule_obj = Rule(rule_file, behavior_name="code", bot_name="story_bot")
print("Rule loaded successfully")

# Test on a single file
test_file = Path("agile_bot/bots/base_bot/src/actions/actions.py")
print(f"\nScanning single file: {test_file}")

scanner = DuplicationScanner()
violations = scanner.scan_code_file(test_file, rule_obj)

print(f"\nFound {len(violations)} violations")
for v in violations:
    print(f"  - Line {v.get('line_number')}: {v.get('violation_message', '')[:100]}...")

print("\nTest complete!")







