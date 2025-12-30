# UI Walkthrough - REPL Commands

This document shows the results of running various REPL commands to demonstrate the CLI interface.

## Setup

```powershell
cd c:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\base_bot'
$env:WORKING_AREA = 'C:\dev\augmented-teams\agile_bot\bots\base_bot'
```

## Command: `status`

Shows the current state of the workflow, scope, and available commands.

```
echo 'status' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```

**Output:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🤖 Bot: story_bot
**Bot Path:**
```
C:\dev\augmented-teams\agile_bot\bots\story_bot
```

📂 **Workspace:** base_bot
```
C:\dev\augmented-teams\agile_bot\bots\base_bot
```

To change path:
```
path demo/mob_minion              # Change to specific project
path ../another_bot               # Change to relative path
```
────────────────────────────────────────────────────────────
Headless Mode:
  Status: Available (configured)
  API Key: key_2780b8...

  Usage:
    python agile_bot/bots/base_bot/src/repl_cli/repl_main.py headless "Your instruction"

  Examples:
    python agile_bot/bots/base_bot/src/repl_cli/repl_main.py headless "Create hello world"
    python agile_bot/bots/base_bot/src/repl_cli/repl_main.py --headless shape
    python agile_bot/bots/base_bot/src/repl_cli/repl_main.py --headless shape.build

  Active Session:
    Session ID: 2025-12-30-01-31-17
    Status: running
    Log: C:\dev\augmented-teams\agile_bot\bots\base_bot\logs\headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
🎯 Scope
🎯 Current Scope: all (entire project)

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```
────────────────────────────────────────────────────────────
## 📍 **Progress**
**Current Position:**
```
shape.clarify.instructions
```

- ➤ shape - Outline a story map made up of epics, sub-epics, and stories
  - ➤ clarify - Gather context by asking required questions and collecting evidence in order to increase understanding
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
  - ☐ strategy
  - ☐ build
  - ☐ validate
  - ☐ render
- ☐ prioritization
- ☐ discovery
- ☐ exploration
- ☐ scenarios
- ☐ tests
- ☐ code

Run:
```
echo 'behavior.action' | python repl_main.py           # Defaults to 'instructions' operation
echo 'behavior.action.operation' | python repl_main.py  # Runs operation
```

**Args:**
```
--scope "Epic, Sub Epic, Story"      # Filter by story names
--scope "file:path/one,path/two"     # Filter by file paths
--headless                             # Execute autonomously without user input
```
────────────────────────────────────────────────────────────
## 💻 **Commands:**
**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**

```
// Run
echo '[command]' | python repl_main.py
// to invoke commands
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Behaviors:** shape | prioritization | discovery | exploration | scenarios | tests | code
**Actions:** clarify | strategy | build | validate | render
```

---

## Command: `help`

Shows all available commands and their usage.

```
echo 'help' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```

**Output:**

```
Core Commands:
  echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation
  echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action

  Available Components:
    behaviors   -> shape | prioritization | discovery | exploration | scenarios | tests | code

    actions:
      clarify      - Gather context and answer key questions
      strategy     - Plan the approach for this behavior
      build        - Execute the main work of this behavior
      validate     - Verify work meets requirements
      render       - Generate final outputs and artifacts

    operations:
      instructions  [context, scope, or action-specific params]
      submit        [scope, decisions, assumptions, or action-specific params]
      confirm

  Examples:
    echo '.' | python repl_main.py                -> Execute current behavior.action.operation
    echo 'shape' | python repl_main.py            -> Jump to behavior and execute first action.operation
    echo 'build' | python repl_main.py            -> Jump to action and execute first operation
    echo 'submit scope="s1"' | python repl_main.py -> Jump to operation with params and execute
    echo 'shape.build' | python repl_main.py      -> Jump to behavior.action and execute first operation
    echo 'shape.build.submit' | python repl_main.py -> Jump to behavior.action.operation and execute
    python repl_main.py headless shape            -> Execute behavior in headless mode (unattended)

  Other Commands:
    echo 'status' | python repl_main.py           - Show full workflow hierarchy
    echo 'back' | python repl_main.py             - Go back to previous action
    echo 'current' | python repl_main.py          - Re-execute current operation
    echo 'next' | python repl_main.py             - Advance to next action
    echo 'path [dir]' | python repl_main.py       - Show/set working directory
    echo 'scope C:\full\path' | python repl_main.py - Set scope to COMPLETE folder path
    echo 'scope all' | python repl_main.py        - Clear scope filter
    echo 'headless "message"' | python repl_main.py - Execute message in headless mode
    echo 'help' | python repl_main.py             - Show this help
    echo 'exit' | python repl_main.py             - Exit CLI

  Scope Command Details:
    IMPORTANT: You can only have ONE scope type at a time (story OR files, never both).
    Setting a new scope REPLACES any previous scope.

    When passing file/folder paths to scope, you MUST provide the COMPLETE
    folder structure. Use ABSOLUTE paths or FULL relative paths from the work path.

    Usage (pick ONE - each replaces the previous scope):
      echo 'scope' | python repl_main.py                           - Show current scope
      echo 'scope all' | python repl_main.py                       - Clear scope filter
      echo 'scope "Story Name"' | python repl_main.py              - Filter by story (replaces file scope)
      echo 'scope "file:C:/path/to/src/**/*.py"' | python repl_main.py - Filter by files (replaces story scope)

    Examples (CORRECT - each sets a SINGLE scope type):
      scope "Enter Password, Authenticate User"                                        - Story scope
      scope "file:C:/dev/augmented-teams/agile_bot/bots/base_bot/src/**/*.py"          - File scope with glob

    Examples (INCORRECT - DO NOT USE):
      scope src              [X] partial path - missing parent directories
      scope repl_cli         [X] folder name only - incomplete structure
      scope ..\src           [X] relative navigation - use complete paths

  Headless Mode:
    Status: Available (API key configured)

    Usage:
      python agile_bot/bots/base_bot/src/repl_cli/repl_main.py headless "Your instruction"
      python agile_bot/bots/base_bot/src/repl_cli/repl_main.py headless shape.build
      python agile_bot/bots/base_bot/src/repl_cli/repl_main.py headless shape.build "context message"

    Commands:
      headless "text"                    Execute pass-through instruction
      headless shape                      Execute entire behavior
      headless shape.build                Execute single action
      headless shape.build.submit         Execute single operation
      headless shape.build "message"      Execute action with context message

    Options:
      --context file.md    Context file to include
      --timeout N          API timeout in seconds (default: 600, use 30 for tests)

    Examples:
      python agile_bot/bots/base_bot/src/repl_cli/repl_main.py headless "Create hello world function"
      python agile_bot/bots/base_bot/src/repl_cli/repl_main.py headless shape
      python agile_bot/bots/base_bot/src/repl_cli/repl_main.py headless shape.build --timeout 30
      python agile_bot/bots/base_bot/src/repl_cli/repl_main.py headless shape.build "Focus on error handling"
      python agile_bot/bots/base_bot/src/repl_cli/repl_main.py headless "Build feature" --context context.md
```

---

## Command: `scope` with Files

Sets the scope to specific files using glob patterns.

```
echo 'scope "file:agile_bot/bots/base_bot/src/repl_cli/**/*.py"' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```

**Output:**

```
## 🎯 **Scope**
**Filter:** agile_bot/bots/base_bot/src/repl_cli/**/*.py

```
  (no files found)
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```
```

**Note:** The "no files found" message indicates the path needs to be adjusted. File scope requires complete paths from the working area.

---

## Command: `scope` with Stories

Sets the scope to specific stories by name.

```
echo 'scope "Generate Bot Tools, Generate BOT CLI code"' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```

**Output:**

```
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```
```

---

## Command: `shape` (Behavior Navigation)

Navigates to the `shape` behavior and executes the first action's instructions.

```
echo 'shape' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```

**Output:**

Shows the full instructions for `shape.clarify.instructions` including:
- Scope filter (if set)
- Detailed instructions for gathering context
- Key questions to answer
- Evidence to look for
- Current CLI status with progress indicators

The output includes the complete workflow tree showing which behaviors/actions are complete (☑), current (➤), or pending (☐).

---

## Command: `shape.build` (Behavior.Action Navigation)

Navigates to `shape.build` action and executes its instructions.

```
echo 'shape.build' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```

**Output:**

Returns empty output - this is because the command navigates to the action but doesn't execute an operation. The REPL is waiting at `shape.build.instructions`.

---

## Command: `shape.build.instructions` (Full Navigation)

Navigates to and executes the specific operation.

```
echo 'shape.build.instructions' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```

**Output:**

Returns empty output in this case - the operation executed but produced no visible output in piped mode.

---

## Command: `next`

Advances to the next operation/action in the workflow.

```
echo 'next' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```

**Output:**

Shows the instructions for `shape.validate.instructions` including:
- Scanner violation review process
- Manual rule review checklist
- Unified violations table format
- Summary and recommendations format

The progress indicator updates to show `shape.validate` as current (➤) and previous actions as complete (☑).

---

## Command: `back`

Attempts to go back to the previous action in the workflow.

```
echo 'back' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```

**Output:**

```
ERROR: 'Actions' object has no attribute 'previous'
Traceback (most recent call last):
  File "C:\dev\augmented-teams\agile_bot\bots\base_bot\src\repl_cli\repl_main.py", line 373, in run_interactive_mode
    response = repl_session.read_and_execute_command(command)
  File "C:\dev\augmented-teams\agile_bot\bots\base_bot\src\repl_cli\repl_session.py", line 303, in read_and_execute_command
    return self._handle_simple_command(command)
  File "C:\dev\augmented-teams\agile_bot\bots\base_bot\src\repl_cli\repl_session.py", line 327, in _handle_simple_command
    return self._handle_back_command()
  File "C:\dev\augmented-teams\agile_bot\bots\base_bot\src\repl_cli\repl_session.py", line 479, in _handle_back_command
    prev_action = behavior.actions.previous
  File "C:\dev\augmented-teams\agile_bot\bots\base_bot\src\repl_cli\cli_bot\cli_actions\cli_actions.py", line 33, in previous
    domain_prev = self._actions.previous()
  File "C:\dev\augmented-teams\agile_bot\bots\base_bot\src\actions\actions.py", line 106, in __getattr__
    raise AttributeError(f"'{self.__class__.__name__}' object has no attribute 'previous'")
AttributeError: 'Actions' object has no attribute 'previous'
```

**Note:** This reveals a bug - the `Actions` class is missing a `previous()` method that the `back` command requires.

---

## Command: `nothing`

Attempts to run an unknown command.

```
echo 'nothing' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```

**Output:**

```
ERROR: Unknown command 'nothing'
```

---

## Summary

The REPL provides a powerful command-line interface for navigating and executing bot workflows:

1. **Status Commands**: `status`, `help` - Show current state and available commands
2. **Navigation Commands**: `<behavior>`, `<behavior>.<action>`, `<behavior>.<action>.<operation>` - Navigate and execute
3. **Workflow Commands**: `next`, `back`, `current` - Move through the workflow
4. **Scope Commands**: `scope "Story Names"`, `scope "file:path/**/*.py"`, `scope all` - Filter work
5. **Utility Commands**: `path [dir]`, `exit` - Manage environment

### Key Observations:

- Commands are piped via `echo` in PowerShell
- The REPL exits after processing each command (piped mode behavior)
- Scope can be set to either stories OR files (not both)
- Navigation automatically executes the `instructions` operation by default
- The workflow tracks progress with visual indicators (➤ current, ☑ complete, ☐ pending)
- Bug found: `back` command fails due to missing `previous()` method in Actions class
