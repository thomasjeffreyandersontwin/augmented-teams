# Complete Current REPL Behavior Documentation

Tested: 2025-12-26
Environment: story_bot, demo/mob_minion workspace

This documents the ACTUAL behavior of the current REPL implementation by running real commands.
Tests should match this behavior, then Phase 3 will refactor to match target scenarios.

---

## Architecture (Current)

**Classes:**
- `REPLSession` - Main session manager
  - `.bot` - Direct Bot instance (NOT wrapped in CLIBot)
  - `.workspace_directory` - Path
  - `.help` - REPLHelp instance
  - `.status` - REPLStatus instance
  - `._commands` - Dict of command handlers

**Methods:**
- `detect_tty()` -> TTYDetectionResult
- `display_current_state()` -> REPLStateDisplay
- `read_and_execute_command(str)` -> REPLCommandResponse

**Result Types:**
- `REPLStateDisplay(output, state_loaded, current_behavior, current_action, breadcrumbs)`
- `REPLCommandResponse(output, response, status, action, scope_stored, scope, context_passed_to_action, repl_terminated)`
- `TTYDetectionResult(tty_detected, interactive_prompts_enabled)`

---

## Display Format (Current)

### Piped Mode Display
```
============================================================
STORY_BOT CLI

============================================================
AI AGENT INSTRUCTIONS - PIPED MODE
============================================================

*** THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND ***
[... AI instructions ...]

------------------------------------------------------------
Bot Path: C:\dev\augmented-teams\agile_bot\bots\story_bot
Work Path: C:\dev\augmented-teams\demo\mob_minion
------------------------------------------------------------
Scope Filter: "Create Mob, Edit Mob"
  - "Create Mob (no match)
  - Edit Mob" (no match)

------------------------------------------------------------
[x] shape
[*] discovery
  [x] clarify
  [*] build
    [*] instructions --path="..." --scope="..."
    [ ] submit --path="..." --scope="..."
    [ ] confirm
[ ] code
------------------------------------------------------------
Commands: status | back | current | next | path [dir] | scope [filter] | help | exit
```

### Interactive Mode Display
- Same as above BUT without "AI AGENT INSTRUCTIONS - PIPED MODE" section
- Shows interactive prompt at end (not in piped mode)

---

## Command Behavior (Current)

### Navigation Commands

**Command: `status`**
- Output: Full hierarchy display (same as initial display)
- Returns: REPLCommandResponse with output containing hierarchy

**Command: `next`**
- Navigates to next action in sequence
- Updates behavior_action_state.json
- Shows message: "Now at: [behavior].[action]"
- Returns: REPLCommandResponse

**Command: `back`**
- Navigates to previous action
- Updates behavior_action_state.json
- Shows message: "Now at: [behavior].[action]"
- Returns: REPLCommandResponse

**Command: `current`**
- Re-executes current operation
- Does not change position
- Returns: REPLCommandResponse with operation output

**Command: `discovery`** (behavior name)
- Navigates to behavior.clarify (first action)
- Updates state
- Shows: "Now at: discovery.clarify"
- Returns: REPLCommandResponse

**Command: `code.validate.instructions`** (full dot notation)
- Navigates to code.validate
- Executes instructions operation
- Shows full operation output (e.g., validation results)
- Updates state
- Returns: REPLCommandResponse

**Command: `help`**
- Shows help menu with:
  - Core commands section
  - Available behaviors/actions/operations
  - Examples
  - Other commands list
- Returns: REPLCommandResponse

**Command: `exit`**
- Exits REPL
- Returns: REPLCommandResponse with repl_terminated=True

### Scope Commands

**Current Implementation:**
- Scope is stored in REPLSession
- Displayed at top of hierarchy
- Format: `Scope Filter: "Create Mob, Edit Mob"`
- Shows validation: `- "Create Mob (no match)`
- Single Scope object (NOT split into KnowledgeGraphFilter + FileFilter)

**Command: `scope [filter]`**
- Sets scope filter
- Stores in session
- Updates display
- Format: `scope "Story1, Story2"` or `scope story="Story1"`

**Command: `scope` (no args)**
- Views current scope
- Shows stored scope value

**Command: `scope clear`**
- Clears stored scope
- Sets to None or empty

### Operation Execution

**Current Flow:**
1. Parse command (dot notation or simple)
2. If dot notation: `DotNotationCommand.execute()`
3. If simple: Look up in `_commands` dict
4. Execute command handler
5. Return REPLCommandResponse
6. Save state to behavior_action_state.json

**Scope Passing:**
- Currently: Scope stored in REPLSession
- Passed to action via context when executing
- NOT passed as CLI argument inline with command
- Format in state file: Uses single Scope object

---

## State Persistence (Current)

**File:** `workspace_directory/behavior_action_state.json`

**Format:**
```json
{
  "current_behavior": "story_bot.discovery",
  "current_action": "story_bot.discovery.build",
  "operation": "instructions",
  "working_directory": "C:\\dev\\augmented-teams\\demo\\mob_minion",
  "timestamp": "2025-12-26T..."
}
```

**When Saved:**
- After every navigation
- After every operation execution
- On exit

**When Loaded:**
- On REPLSession initialization
- Used to restore position

---

## TTY Detection (Current)

**Method:** `sys.stdin.isatty()`

**Results:**
- Interactive TTY: `isatty() == True`
  - Shows standard CLI display
  - Waits for interactive prompt
  - No "PIPED MODE" banner
  
- Piped Input: `isatty() == False`
  - Shows "PIPED MODE" banner with AI instructions
  - Processes one command and exits
  - No interactive prompt

**REPLSession Implementation:**
```python
def detect_tty(self) -> TTYDetectionResult:
    is_tty = sys.stdin.isatty()
    return TTYDetectionResult(
        tty_detected=is_tty,
        interactive_prompts_enabled=is_tty
    )
```

---

## Key Differences from Target Architecture

| Feature | Current | Target (in plan) |
|---------|---------|------------------|
| Bot wrapper | Direct `.bot` access | `.cli_bot` (CLIBot wrapper) |
| Behaviors access | `repl.bot.behaviors` | `repl.cli_bot.cli_behaviors` |
| Actions access | `behavior.actions` | `cli_behavior.cli_actions` |
| Scope architecture | Single `Scope` object | `KnowledgeGraphFilter` + `FileFilter` |
| Command parsing | Inline in REPLSession | `CommandParser` class |
| Status display | `REPLStatus` helper | `StatusDisplay` class |
| TTY detection | Inline method | `TTYDetector` class |

---

## Test Implications

**Tests Should Assert:**
1. ✅ `repl_session.bot` exists (not cli_bot)
2. ✅ `bot.bot_name == 'story_bot'`
3. ✅ `display_current_state()` returns `REPLStateDisplay` object
4. ✅ Access `cli_output.output` for display text
5. ✅ `detect_tty()` returns `TTYDetectionResult`
6. ✅ Check for "PIPED MODE" in output when piped
7. ✅ Check for behaviors list in output
8. ✅ Check for commands menu at bottom
9. ✅ State saved to `behavior_action_state.json`
10. ✅ Navigation updates state file

**Tests Should NOT Assert:**
- ❌ `repl_session.cli_bot` (doesn't exist yet)
- ❌ Separate KnowledgeGraphFilter/FileFilter (single Scope)
- ❌ CommandParser class (parsing is inline)
- ❌ StatusDisplay class (uses REPLStatus)

---

## Next Steps

1. Update all 49 test scenarios to match this current behavior
2. Run tests - should all pass
3. Phase 3: Refactor code to match target architecture in plan
4. Tests guide the refactoring (will initially fail, then pass as refactoring progresses)


