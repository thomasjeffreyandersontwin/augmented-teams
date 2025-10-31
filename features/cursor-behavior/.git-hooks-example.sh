#!/bin/bash
# Git pre-commit hook example for behavior consistency checking
# 
# To install:
# 1. Copy this file to .git/hooks/pre-commit
# 2. Make it executable: chmod +x .git/hooks/pre-commit
# 
# This will run behavior-consistency before each commit

echo "🔍 Checking behavior consistency before commit..."

# Change to repository root
cd "$(git rev-parse --show-toplevel)"

# Run consistency check
python features/cursor-behavior/cursor/behavior-consistency-cmd.py

# If consistency check finds issues, you can choose to:
# - Exit 1 to block the commit (uncomment next line)
# exit 1

# Or just warn and allow commit
echo "⚠️  Review .cursor/behavior-consistency-report.md for any issues"

