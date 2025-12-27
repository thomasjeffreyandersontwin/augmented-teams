# Current Behavior: Initialize REPL Session

This document captures the ACTUAL current behavior of the REPL by testing it directly.
These scenarios will guide updating the tests to match reality before refactoring.

## Story: Launch CLI in Interactive Mode

### Test 1: Basic Launch
**Command:** Run REPL without piping (interactive TTY)
```bash
# Not easily testable - requires actual TTY
# Will test via mocking sys.stdin.isatty() = True
```

**Expected Behavior:**
- REPLSession created with bot instance
- bot.bot_name == 'story_bot'
- display_current_state() returns REPLStateDisplay object
- If no behaviors loaded: output = "No behaviors available"
- If behaviors loaded: output shows hierarchy tree

### Test 2: Load Existing State
**Command:** Launch with existing behavior_action_state.json
```bash
# Create state file first, then launch
```

**Expected Behavior:**
- REPLSession reads behavior_action_state.json from workspace
- Sets current behavior/action based on file
- display_current_state() shows current position
- state_loaded flag or current_behavior populated

## Story: Launch CLI in Pipe Mode

### Test 1: Piped Input Detected
**Command:**
```bash
echo "help" | python repl_main.py
```

**Actual Output:**
```
============================================================
STORY_BOT CLI

============================================================
AI AGENT INSTRUCTIONS - PIPED MODE
============================================================

*** THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND ***
...
```

**Expected Behavior:**
- sys.stdin.isatty() returns False
- REPLSession.detect_tty() returns TTYDetectionResult(tty_detected=False, interactive_prompts_enabled=False)
- Display shows "PIPED MODE" banner
- No interactive prompt shown

## Story: Display Piped Mode Instructions for AI Agents

### Test 1: Pipe Mode Shows Instructions
**Testing Now...**

