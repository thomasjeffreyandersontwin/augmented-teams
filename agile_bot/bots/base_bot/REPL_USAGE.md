# Interactive REPL Usage

The Base Bot Interactive REPL provides a command-line interface for navigating and executing bot workflows interactively.

## Launching the REPL

### Windows (PowerShell)
```powershell
cd c:\dev\augmented-teams\agile_bot\bots\story_bot
..\base_bot\repl.ps1
```

### Unix/Linux/Mac (Bash)
```bash
cd /path/to/augmented-teams/agile_bot/bots/story_bot
../base_bot/repl
```

### Direct Python
```bash
cd /path/to/augmented-teams
python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```

## Available Commands

### Navigation Commands
- `behavior <name>` - Switch to a specific behavior
- `action <name>` - Navigate to a specific action within current behavior
- `back` - Move back to the previous action
- `close` - Complete the current action and advance to next

### Execution Commands
- `run` - Execute the current action (mock mode - doesn't actually run)
- `y` or `yes` - Confirm action completion and advance to next action
- `current` - Display current action status with breadcrumbs

### Information Commands
- `help` - Show available actions for current behavior
- `help <action>` - Show detailed help for a specific action
- `status` - Show current workflow status with progress

### System Commands
- `exit` - Exit the REPL session

## Example Session

```
[story_bot] > behavior shape
OK behavior=shape
CURRENT: story_bot.shape.clarify
[shape] clarify* -> strategy -> build -> validate -> render

[story_bot] > help
Available Actions for behavior: shape
  clarify
  strategy
  build
  validate
  render

[story_bot] > run
EXECUTING shape.clarify...
[mock response - not executing real action]
Mock execution complete

[story_bot] > y
OK advancing to strategy
CURRENT: story_bot.shape.strategy
[shape] clarify [OK] -> strategy* -> build -> validate -> render

[story_bot] > action validate
OK action=validate
CURRENT: story_bot.shape.validate
[shape] clarify -> strategy -> build -> validate* -> render

[story_bot] > back
Moving back to previous action
CURRENT: story_bot.shape.build
[shape] clarify -> strategy -> build* -> validate -> render

[story_bot] > status
CURRENT: story_bot.shape.build
Working Directory: C:\dev\augmented-teams
[shape] clarify -> strategy -> build* -> validate -> render

## Behavior/Action Progress
shape

[story_bot] > exit
Goodbye!
```

## Features

### Workflow State Persistence
- The REPL automatically loads existing workflow state from `behavior_action_state.json`
- State is saved after each command
- You can pause and resume sessions without losing progress

### Breadcrumbs Display
- Shows your current position in the workflow
- Completed actions marked with `[OK]`
- Current action marked with `*`
- Future actions shown without marks

### Progress Tracking
- Displays completed actions in the "Behavior/Action Progress" section
- Tracks which actions have been completed with timestamps

## Notes

- Commands are currently stubbed (mock mode) - they don't execute real actions yet
- The REPL is designed for testing and exploration of workflow navigation
- State file location: `<workspace>/behavior_action_state.json`
- Bot configuration is loaded from the bot's `bot_config.json`

## Testing

55 out of 66 tests passing:
- ✅ All core navigation commands (behavior, action, back, close)
- ✅ Execution commands (run, y/yes)
- ✅ Information commands (help, status, current)
- ✅ Breadcrumbs and progress display
- ✅ State persistence
- ⏳ Parameter validation (not yet implemented)
- ⏳ Scope validation (not yet implemented)

Run tests:
```bash
cd c:\dev\augmented-teams
python -m pytest agile_bot/bots/base_bot/test/test_run_interactive_repl.py -v
```

