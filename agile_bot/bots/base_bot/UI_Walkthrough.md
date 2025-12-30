# UI Walkthrough - REPL Commands

This document contains the output of various REPL commands.

Generated: Tue Dec 30 14:05:01 EST 2025


## Command: Empty command (nothing)

```
Command: 
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================

```

---

## Command: Status command

```
Command: status
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


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
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
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
code.render.instructions
```

- ☑ shape
- ☑ prioritization
- ☑ discovery
- ☑ exploration
- ☑ scenarios
- ☑ tests
- ➤ code - Generate production source code from domain model and story specifications
  - ☑ strategy
  - ➤ render - Render output documents and artifacts from knowledge graph using templates and synchronizers
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
  - ☐ validate

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
**Actions:** strategy | render | validate

```

---

## Command: Help command

```
Command: help
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================

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
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
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
code.render.instructions
```

- ☑ shape
- ☑ prioritization
- ☑ discovery
- ☑ exploration
- ☑ scenarios
- ☑ tests
- ➤ code - Generate production source code from domain model and story specifications
  - ☑ strategy
  - ➤ render - Render output documents and artifacts from knowledge graph using templates and synchronizers
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
  - ☐ validate

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
**Actions:** strategy | render | validate

```

---

## Command: Scope with files (multiple entries)

```
Command: scope "file:/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py, /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py, /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot.py"
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================

## 🎯 **Scope**
**Filter:** /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py, /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py, /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot.py/*

```
└── 📁 src
    ├── 📁 actions
    │   ├── 📄 action.py
    │   └── 📄 actions.py
    └── 📁 bot
        └── 📄 bot.py
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

## Command: Scope with stories (multiple entries)

```
Command: scope "Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions"
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================

## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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

## Command: Behavior: shape

```
Command: shape
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**INSTRUCTIONS SECTION:**
☢️ This section contains both scope filter and a prompt that you must follow for the current action. ☢️
☢️ You MUST follow the instructions below in this section to the letter. ☢️
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```Outline a story map made up of epics, sub-epics, and stories

Gather context for story mapping

**Look for context in the following locations:**
- in this message and chat history
- in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/context/`
- generated files in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/`
  clarification.json, strategy.json

Review all provided context, then for each required question below, thoughtfully answer it by thoroughly examining the context provided. Present your answers to the user for review and final confirmation.

**Answer format:**
**Question:** [question text]
**Answer:** [your answer based on context]

If you can't answer from context, state: "[!] NOT ENOUGH INFORMATION - REQUIRES USER INPUT"
If a choice is needed, list available options and ask user to choose.
Don't guess or infer - be explicit when information is missing.

After presenting all answers, ask the user to review and confirm or provide corrections before proceeding.

**Key Questions:**
- Who are the distinct types of users (e.g., operational users, power users, compliance consumers, content creators, producers)?
- What are the key goals, behaviors, or decisions each group is trying to accomplish using this capability?
- Who are the primary users or stakeholder groups impacted?
- What is the first thing users will try to do with this new capability or system?
- What problems, inefficiencies, or workarounds is this request trying to eliminate?
- Where are users currently struggling, getting stuck, or experiencing delays in the process we're aiming to improve?
- What are the key drivers for customer value or business value that this capability addresses, and what specific customer or business outcomes are we trying to achieve?
- What is the user journey from start to finish for the primary use case, and what are the key stages or steps in the user journey?
- Where in the user journey are users experiencing frustration, friction, or unhappiness?
- What moments of delight or value should users experience during their journey?
- What are the critical pain points that prevent users from achieving their goals?
- What other systems, data sources, or tools does this capability need to interact with in order to deliver value?
- What are the key behaviors or integration points that define how these systems support or depend on one another?

**Evidence:**
Business model canvas, Journey maps or other design thinking artifacts, Technical specifications, Product charters, Business cases, Business models, Impact maps, R&D maps, User research, User journey maps, Similar systems, User interviews, Business process documentation, Business stakeholder interviews, Existing system documentation, Business glossaries or dictionaries, Financial statements, Industry literature

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Command: Behavior.Action: shape.build

```
Command: shape.build
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**INSTRUCTIONS SECTION:**
☢️ This section contains both scope filter and a prompt that you must follow for the current action. ☢️
☢️ You MUST follow the instructions below in this section to the letter. ☢️
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```Outline a story map made up of epics, sub-epics, and stories

Build initial story map structure using rules and context listed below
Apply story shaping rules when shaping Epics, Sub-Epics, Stories

**Look for context in the following locations:**
- in this message and chat history
- in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/context/`
- generated files in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/`
  clarification.json, strategy.json

Build knowledge graph for build
Base instructions for build
Use verb-noun format for actions
Review the template file at `story_bot/behaviors/shape/content/knowledge_graph/story-graph-outline.json`. It shows the exact structure (fields, nesting, types) that your knowledge graph output must follow during this behavior. Read this file to understand the required schema.

Create `story-graph.json` if it does not exist. Place file at `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/`. Using the template for guidance.

If the file already exists then make SAFE edits only. Preserve existing structure and content. Add or modify only what is necessary. Do NOT overwrite indiscriminately unless explicitly asked. When adding nodes to the graph follow the template and do not add extra elements that you might see in other nodes, they will be added as a part of later behaviors.
Epics should be organized in verb-noun format
Top-level features should follow the schema

When building or adding to the story graph follow these rules,
Rules to follow:

- **verb_noun_format**: Use verb-noun format consistently across all hierarchy levels. Actor --> verb noun [qualifiers]. Actor is documented separately, NOT in the name. Focus on specific actions with context.
  DO: Use specific verb-noun format with actor documented separately. Example: 'Places Order' with actor=Customer
  DON'T: Don't include actor in name or use generic operations. Example: 'Customer Places Order' (WRONG) → 'Places Order' with actor=Customer (CORRECT)

- **active_business_and_behavioral_language**: Use active business language focused on user/system behavior. Describe what actors do with clear action verbs, not technical implementation or passive constructions.
  DO: Use active voice with business language. Example: 'User submits order' (active voice, business language describing what actor does)
  DON'T: Don't use passive voice or technical implementation language. Example: 'Order is submitted' (passive voice, unclear actor) → 'User submits order' (active voice, clear actor)

- **outcome_oriented_language**: Use outcome-oriented language over mechanism-oriented language. Focus on what is created or achieved, not how it's shown or communicated.
  DO: Focus on outcomes and artifacts, not mechanisms. Example: 'Power Activation Animation' not 'Visualizing Power Activation'
  DON'T: Don't focus on communication mechanisms. Example: 'Showing Combat Results' (mechanism) → 'Combat Outcome Feedback' (outcome)

- **lightweight_and_precise**: Create lightweight but precise documentation during shaping. Focus on structure and scope, not detailed specifications.
  DO: Keep documentation lightweight and easy to walk through. Example: '(E) Manage Orders → (SE) Place Order → (S) Validate Order Items' (shows hierarchy, not specs)
  DON'T: Don't over-elaborate or add detailed specifications during shaping. Example: '(E) Manage Orders → Detailed API specs, database schema, UI mockups' (TOO MUCH)

- **valuable**: Stories must deliver independent value as complete functional accomplishments. Balance value with testability - stories should be valuable enough to matter but small enough to deliver quickly. Not just data access or isolated operations.
  DO: Create stories that deliver independent value. Example: 'User --> loads story graph' (value: see story structure)
  DON'T: Don't create stories without independent value or complete outcomes. Example: 'System --> reads all epics from diagram' (no value - what happens with the data?)

- **small_and_testable**: Stories must be testable as complete interactions and deliverable independently. Balance testability with maintaining value and behavioral focus - stories should be small enough to test but large enough to matter.
  DO: Create stories that can be tested and delivered independently. Example: 'Customer places order' (testable with clear acceptance criteria: order created, payment processed)
  DON'T: Don't create stories that can't be tested or delivered independently. Example: 'Add order button' (not testable - can't verify independently without full order flow context)

- **user_and_system_behavior**: Stories should capture both user and system behavior. User-facing stories show user actions with system responses. System stories capture system-to-system interactions and should be marked with story_type: 'system'. NOTE: This rule only applies when strategy decisions in planning.json specify flow_scope_and_granularity as 'Integration boundary level' or 'Intra-system level', OR drill_down_approach includes 'Dig deep on system interactions' or 'Dig deep on architectural pieces'. Check {project_area}/docs/stories/planning.json for these decisions.
  DO: Show both user and system behavior, mark system-to-system stories. Example: 'User submits order, System validates payment'
  DON'T: Don't show incomplete stories 'User enters order data' (WRONG - missing: what does system do in response?)

- **story_map_existing_code**: When creating story maps from code, start with the outermost layer (entry points), analyze operations, create epics from higher-order goals, and lay out the story journey.
  DO: Start with entry points and trace to epics and stories. Example: Operations 'render-outline, render-increments' → Goal 'Render StoryGraph' → Epic 'Render StoryGraph'
  DON'T: Don't start with internal classes or create epics from class structure. Example: Creating epics from class structure (WRONG) → Create epics from goals (CORRECT)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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
────────────────────────────────────────────────────────────
## 📍 **Progress**
**Current Position:**
```
shape.build.instructions
```

- ➤ shape - Outline a story map made up of epics, sub-epics, and stories
  - ☑ clarify
  - ☑ strategy
  - ➤ build
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Command: Behavior.Action.Operation: shape.build.instructions

```
Command: shape.build.instructions
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**INSTRUCTIONS SECTION:**
☢️ This section contains both scope filter and a prompt that you must follow for the current action. ☢️
☢️ You MUST follow the instructions below in this section to the letter. ☢️
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```Outline a story map made up of epics, sub-epics, and stories

Build initial story map structure using rules and context listed below
Apply story shaping rules when shaping Epics, Sub-Epics, Stories

**Look for context in the following locations:**
- in this message and chat history
- in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/context/`
- generated files in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/`
  clarification.json, strategy.json

Build knowledge graph for build
Base instructions for build
Use verb-noun format for actions
Review the template file at `story_bot/behaviors/shape/content/knowledge_graph/story-graph-outline.json`. It shows the exact structure (fields, nesting, types) that your knowledge graph output must follow during this behavior. Read this file to understand the required schema.

Create `story-graph.json` if it does not exist. Place file at `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/`. Using the template for guidance.

If the file already exists then make SAFE edits only. Preserve existing structure and content. Add or modify only what is necessary. Do NOT overwrite indiscriminately unless explicitly asked. When adding nodes to the graph follow the template and do not add extra elements that you might see in other nodes, they will be added as a part of later behaviors.
Epics should be organized in verb-noun format
Top-level features should follow the schema

When building or adding to the story graph follow these rules,
Rules to follow:

- **verb_noun_format**: Use verb-noun format consistently across all hierarchy levels. Actor --> verb noun [qualifiers]. Actor is documented separately, NOT in the name. Focus on specific actions with context.
  DO: Use specific verb-noun format with actor documented separately. Example: 'Places Order' with actor=Customer
  DON'T: Don't include actor in name or use generic operations. Example: 'Customer Places Order' (WRONG) → 'Places Order' with actor=Customer (CORRECT)

- **active_business_and_behavioral_language**: Use active business language focused on user/system behavior. Describe what actors do with clear action verbs, not technical implementation or passive constructions.
  DO: Use active voice with business language. Example: 'User submits order' (active voice, business language describing what actor does)
  DON'T: Don't use passive voice or technical implementation language. Example: 'Order is submitted' (passive voice, unclear actor) → 'User submits order' (active voice, clear actor)

- **outcome_oriented_language**: Use outcome-oriented language over mechanism-oriented language. Focus on what is created or achieved, not how it's shown or communicated.
  DO: Focus on outcomes and artifacts, not mechanisms. Example: 'Power Activation Animation' not 'Visualizing Power Activation'
  DON'T: Don't focus on communication mechanisms. Example: 'Showing Combat Results' (mechanism) → 'Combat Outcome Feedback' (outcome)

- **lightweight_and_precise**: Create lightweight but precise documentation during shaping. Focus on structure and scope, not detailed specifications.
  DO: Keep documentation lightweight and easy to walk through. Example: '(E) Manage Orders → (SE) Place Order → (S) Validate Order Items' (shows hierarchy, not specs)
  DON'T: Don't over-elaborate or add detailed specifications during shaping. Example: '(E) Manage Orders → Detailed API specs, database schema, UI mockups' (TOO MUCH)

- **valuable**: Stories must deliver independent value as complete functional accomplishments. Balance value with testability - stories should be valuable enough to matter but small enough to deliver quickly. Not just data access or isolated operations.
  DO: Create stories that deliver independent value. Example: 'User --> loads story graph' (value: see story structure)
  DON'T: Don't create stories without independent value or complete outcomes. Example: 'System --> reads all epics from diagram' (no value - what happens with the data?)

- **small_and_testable**: Stories must be testable as complete interactions and deliverable independently. Balance testability with maintaining value and behavioral focus - stories should be small enough to test but large enough to matter.
  DO: Create stories that can be tested and delivered independently. Example: 'Customer places order' (testable with clear acceptance criteria: order created, payment processed)
  DON'T: Don't create stories that can't be tested or delivered independently. Example: 'Add order button' (not testable - can't verify independently without full order flow context)

- **user_and_system_behavior**: Stories should capture both user and system behavior. User-facing stories show user actions with system responses. System stories capture system-to-system interactions and should be marked with story_type: 'system'. NOTE: This rule only applies when strategy decisions in planning.json specify flow_scope_and_granularity as 'Integration boundary level' or 'Intra-system level', OR drill_down_approach includes 'Dig deep on system interactions' or 'Dig deep on architectural pieces'. Check {project_area}/docs/stories/planning.json for these decisions.
  DO: Show both user and system behavior, mark system-to-system stories. Example: 'User submits order, System validates payment'
  DON'T: Don't show incomplete stories 'User enters order data' (WRONG - missing: what does system do in response?)

- **story_map_existing_code**: When creating story maps from code, start with the outermost layer (entry points), analyze operations, create epics from higher-order goals, and lay out the story journey.
  DO: Start with entry points and trace to epics and stories. Example: Operations 'render-outline, render-increments' → Goal 'Render StoryGraph' → Epic 'Render StoryGraph'
  DON'T: Don't start with internal classes or create epics from class structure. Example: Creating epics from class structure (WRONG) → Create epics from goals (CORRECT)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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
────────────────────────────────────────────────────────────
## 📍 **Progress**
**Current Position:**
```
shape.build.instructions
```

- ➤ shape - Outline a story map made up of epics, sub-epics, and stories
  - ☑ clarify
  - ☑ strategy
  - ➤ build
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Command: Behavior: discovery

```
Command: discovery
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**INSTRUCTIONS SECTION:**
☢️ This section contains both scope filter and a prompt that you must follow for the current action. ☢️
☢️ You MUST follow the instructions below in this section to the letter. ☢️
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```Create a complete list of stories with a well defined story flow for one increment

**Look for context in the following locations:**
- in this message and chat history
- in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/context/`
- generated files in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/`
  clarification.json, strategy.json

Review all provided context, then for each required question below, thoughtfully answer it by thoroughly examining the context provided. Present your answers to the user for review and final confirmation.

**Answer format:**
**Question:** [question text]
**Answer:** [your answer based on context]

If you can't answer from context, state: "[!] NOT ENOUGH INFORMATION - REQUIRES USER INPUT"
If a choice is needed, list available options and ask user to choose.
Don't guess or infer - be explicit when information is missing.

After presenting all answers, ask the user to review and confirm or provide corrections before proceeding.

**Key Questions:**
- What is the full scope of the next increment or release?
- What are the major workflows or process segments it touches?
- What systems, teams, or roles are involved across this flow?
- What story groupings or capabilities define this increment?
- What order or sequence do these stories need to follow?
- Where are the major transitions or integration points in the flow?
- Are any stories or features dependent on others being completed first?

**Evidence:**
Story map from shape stage, Increments document from prioritization stage, User experience and customer journey maps, Workflow diagrams or journey maps, Architecture or integration diagrams

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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
────────────────────────────────────────────────────────────
## 📍 **Progress**
**Current Position:**
```
discovery.clarify.instructions
```

- ☑ shape
- ☑ prioritization
- ➤ discovery - Create a complete list of stories with a well defined story flow for one increment
  - ➤ clarify - Gather context by asking required questions and collecting evidence in order to increase understanding
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
  - ☐ strategy
  - ☐ build
  - ☐ validate
  - ☐ render
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Command: Behavior.Action: discovery.clarify

```
Command: discovery.clarify
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**INSTRUCTIONS SECTION:**
☢️ This section contains both scope filter and a prompt that you must follow for the current action. ☢️
☢️ You MUST follow the instructions below in this section to the letter. ☢️
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```Create a complete list of stories with a well defined story flow for one increment

**Look for context in the following locations:**
- in this message and chat history
- in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/context/`
- generated files in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/`
  clarification.json, strategy.json

Review all provided context, then for each required question below, thoughtfully answer it by thoroughly examining the context provided. Present your answers to the user for review and final confirmation.

**Answer format:**
**Question:** [question text]
**Answer:** [your answer based on context]

If you can't answer from context, state: "[!] NOT ENOUGH INFORMATION - REQUIRES USER INPUT"
If a choice is needed, list available options and ask user to choose.
Don't guess or infer - be explicit when information is missing.

After presenting all answers, ask the user to review and confirm or provide corrections before proceeding.

**Key Questions:**
- What is the full scope of the next increment or release?
- What are the major workflows or process segments it touches?
- What systems, teams, or roles are involved across this flow?
- What story groupings or capabilities define this increment?
- What order or sequence do these stories need to follow?
- Where are the major transitions or integration points in the flow?
- Are any stories or features dependent on others being completed first?

**Evidence:**
Story map from shape stage, Increments document from prioritization stage, User experience and customer journey maps, Workflow diagrams or journey maps, Architecture or integration diagrams

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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
────────────────────────────────────────────────────────────
## 📍 **Progress**
**Current Position:**
```
discovery.clarify.instructions
```

- ☑ shape
- ☑ prioritization
- ➤ discovery - Create a complete list of stories with a well defined story flow for one increment
  - ➤ clarify - Gather context by asking required questions and collecting evidence in order to increase understanding
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
  - ☐ strategy
  - ☐ build
  - ☐ validate
  - ☐ render
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Command: Behavior.Action.Operation: discovery.clarify.instructions

```
Command: discovery.clarify.instructions
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**INSTRUCTIONS SECTION:**
☢️ This section contains both scope filter and a prompt that you must follow for the current action. ☢️
☢️ You MUST follow the instructions below in this section to the letter. ☢️
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```Create a complete list of stories with a well defined story flow for one increment

**Look for context in the following locations:**
- in this message and chat history
- in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/context/`
- generated files in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/`
  clarification.json, strategy.json

Review all provided context, then for each required question below, thoughtfully answer it by thoroughly examining the context provided. Present your answers to the user for review and final confirmation.

**Answer format:**
**Question:** [question text]
**Answer:** [your answer based on context]

If you can't answer from context, state: "[!] NOT ENOUGH INFORMATION - REQUIRES USER INPUT"
If a choice is needed, list available options and ask user to choose.
Don't guess or infer - be explicit when information is missing.

After presenting all answers, ask the user to review and confirm or provide corrections before proceeding.

**Key Questions:**
- What is the full scope of the next increment or release?
- What are the major workflows or process segments it touches?
- What systems, teams, or roles are involved across this flow?
- What story groupings or capabilities define this increment?
- What order or sequence do these stories need to follow?
- Where are the major transitions or integration points in the flow?
- Are any stories or features dependent on others being completed first?

**Evidence:**
Story map from shape stage, Increments document from prioritization stage, User experience and customer journey maps, Workflow diagrams or journey maps, Architecture or integration diagrams

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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
────────────────────────────────────────────────────────────
## 📍 **Progress**
**Current Position:**
```
discovery.clarify.instructions
```

- ☑ shape
- ☑ prioritization
- ➤ discovery - Create a complete list of stories with a well defined story flow for one increment
  - ➤ clarify - Gather context by asking required questions and collecting evidence in order to increase understanding
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
  - ☐ strategy
  - ☐ build
  - ☐ validate
  - ☐ render
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Command: Behavior: prioritization

```
Command: prioritization
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**INSTRUCTIONS SECTION:**
☢️ This section contains both scope filter and a prompt that you must follow for the current action. ☢️
☢️ You MUST follow the instructions below in this section to the letter. ☢️
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```Organize stories into delivery increments based on business value, dependencies, and risk

**Look for context in the following locations:**
- in this message and chat history
- in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/context/`
- generated files in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/`
  clarification.json, strategy.json

Review all provided context, then for each required question below, thoughtfully answer it by thoroughly examining the context provided. Present your answers to the user for review and final confirmation.

**Answer format:**
**Question:** [question text]
**Answer:** [your answer based on context]

If you can't answer from context, state: "[!] NOT ENOUGH INFORMATION - REQUIRES USER INPUT"
If a choice is needed, list available options and ask user to choose.
Don't guess or infer - be explicit when information is missing.

After presenting all answers, ask the user to review and confirm or provide corrections before proceeding.

**Key Questions:**
- Which areas of the story map carry the most business or delivery risk?
- Which areas are expected to deliver the most value if delivered early?
- Which areas are the most complex or hardest to implement, relative to their value?
- Do you want thin slices to be as end-to-end as possible?
- Are there any components, capabilities, or services that need to be reused across multiple stories or features?
- Are there any project or program constraints that impact delivery order?
- Are there users or groups that must go first to enable others to follow?

**Evidence:**
Story map from shape stage, Business cases or initiative briefs, Project charters and delivery timelines, Capability or architecture documents, User rollout or onboarding strategies, Value models or impact maps

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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
────────────────────────────────────────────────────────────
## 📍 **Progress**
**Current Position:**
```
prioritization.clarify.instructions
```

- ☑ shape
- ➤ prioritization - Organize stories into delivery increments based on business value, dependencies, and risk
  - ➤ clarify - Gather context by asking required questions and collecting evidence in order to increase understanding
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
  - ☐ strategy
  - ☐ build
  - ☐ validate
  - ☐ render
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Command: Behavior: exploration

```
Command: exploration
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**INSTRUCTIONS SECTION:**
☢️ This section contains both scope filter and a prompt that you must follow for the current action. ☢️
☢️ You MUST follow the instructions below in this section to the letter. ☢️
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```Define acceptance criteria (When/Then) for stories to establish clear success criteria

**Look for context in the following locations:**
- in this message and chat history
- in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/context/`
- generated files in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/`
  clarification.json, strategy.json

Review all provided context, then for each required question below, thoughtfully answer it by thoroughly examining the context provided. Present your answers to the user for review and final confirmation.

**Answer format:**
**Question:** [question text]
**Answer:** [your answer based on context]

If you can't answer from context, state: "[!] NOT ENOUGH INFORMATION - REQUIRES USER INPUT"
If a choice is needed, list available options and ask user to choose.
Don't guess or infer - be explicit when information is missing.

After presenting all answers, ask the user to review and confirm or provide corrections before proceeding.

**Key Questions:**
- Which increment are we exploring?
- What is the overarching outcome or user goal that unites this increment?
- What is the first thing the user will try to do in this flow?
- What system reactions are expected for each user input?
- Where do we 'pass the ball' between the user and system in this flow?
- What are the likely unknowns, edge cases, or domain complexities?
- Are there domain rules or constraints that govern this behavior?
- What parts of this increment are likely to involve integration or coordination across systems?
- Where do we face architectural risk or uncertainty that should be explored further before proceeding?

**Evidence:**
Story map from Shape stage (overarching epics, features, and stories), Discovery refinements from Discovery stage (enumerated stories for increment in focus), User interaction diagrams, Low fidelity UX flows, User Journeys or Workflow Diagrams, Domain Models or Business Rules Documentation, Behavior Maps or Interaction Scenarios, Assumptions and Known Risks Logged from Earlier Phases

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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
────────────────────────────────────────────────────────────
## 📍 **Progress**
**Current Position:**
```
exploration.clarify.instructions
```

- ☑ shape
- ☑ prioritization
- ☑ discovery
- ➤ exploration - Define acceptance criteria (When/Then) for stories to establish clear success criteria
  - ➤ clarify - Gather context by asking required questions and collecting evidence in order to increase understanding
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
  - ☐ strategy
  - ☐ build
  - ☐ validate
  - ☐ render
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Command: Behavior: scenarios

```
Command: scenarios
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**INSTRUCTIONS SECTION:**
☢️ This section contains both scope filter and a prompt that you must follow for the current action. ☢️
☢️ You MUST follow the instructions below in this section to the letter. ☢️
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```Write detailed plain-English scenarios (Given/When/Then) that specify exact behavior for each story

**Look for context in the following locations:**
- in this message and chat history
- in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/context/`
- generated files in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/`
  clarification.json, strategy.json

Review all provided context, then for each required question below, thoughtfully answer it by thoroughly examining the context provided. Present your answers to the user for review and final confirmation.

**Answer format:**
**Question:** [question text]
**Answer:** [your answer based on context]

If you can't answer from context, state: "[!] NOT ENOUGH INFORMATION - REQUIRES USER INPUT"
If a choice is needed, list available options and ask user to choose.
Don't guess or infer - be explicit when information is missing.

After presenting all answers, ask the user to review and confirm or provide corrections before proceeding.

**Key Questions:**
- What system and user actions initiate this story's flow?
- What is the intended system response after each user action?
- What preconditions or data states are required before this story can begin?
- What are the success criteria for the story (from a domain and user perspective)?
- What are the expected alternate flows, error paths, and edge cases?
- Are there any mandatory sequencing constraints within or across stories?
- What domain rules, calculations, or business policies does this story validate?
- Is the story testable independently (including setup and teardown conditions)?
- What external systems or services does this story need to interact with?
- What requests, responses, or contracts are involved in those system interactions?
- Are there system integration points that require validation or simulation?
- How do we handle failures, timeouts, or retries for those system calls?
- What data variations (e.g., boundary conditions, common examples) are required for test coverage?
- What are the input values needed to test each scenario?
- What are the expected output values for each input?
- Are there formulas or calculations that need multiple data points to validate?
- Are there domain entities with named values that should be tested?
- What are the boundary conditions (min, max, edge cases) for each data point?

**Evidence:**
Acceptance criteria from Exploration stage (Domain AC at feature level, Behavioral AC at story level), High fidelity UX flows, Domain models or ubiquitous language, Cross-functional walkthrough outputs, Integration contracts or API mocks, Behavior diagrams (state, sequence)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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
────────────────────────────────────────────────────────────
## 📍 **Progress**
**Current Position:**
```
scenarios.clarify.instructions
```

- ☑ shape
- ☑ prioritization
- ☑ discovery
- ☑ exploration
- ➤ scenarios - Write detailed plain-English scenarios (Given/When/Then) that specify exact behavior for each story
  - ➤ clarify - Gather context by asking required questions and collecting evidence in order to increase understanding
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
  - ☐ strategy
  - ☐ build
  - ☐ validate
  - ☐ render
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Command: Behavior: tests

```
Command: tests
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**INSTRUCTIONS SECTION:**
☢️ This section contains both scope filter and a prompt that you must follow for the current action. ☢️
☢️ You MUST follow the instructions below in this section to the letter. ☢️
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```Write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior

specification_tests: add test_file, test_class, and test_method fields to story-graph.json based on the test file updates / creations you are going to make

1. **test_file field** - Add to sub-epic level:
   - Format: "test_file": "test_<sub_epic_name>.py"
   - Example: "test_file": "test_generate_bot_server_and_tools.py"
   - Maps to the sub-epic that contains the stories being tested

2. **test_class field** - Add to story level (when applicable):
   - Format: "test_class": "Test<ExactStoryName>"
   - Example: "test_class": "TestGenerateBotTools"
   - Only add if the test file contains a test class (not standalone functions)
   - Maps to the exact story name that the test class validates

3. **test_method field** - Add to scenario level:
   - Format: "test_method": "test_<scenario_name_snake_case>"
   - Example: "test_method": "test_generator_creates_bot_tool_for_test_bot"
   - Maps to the exact scenario name that the test method validates
Refine domain model concepts, relationships, and responsibilities based on test file implementation patterns and requirements

**Look for context in the following locations:**
- in this message and chat history
- in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/context/`
- generated files in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/`
  clarification.json, strategy.json

Build knowledge graph for build
Base instructions for build
Use verb-noun format for actions
Epics should be organized in verb-noun format
Top-level features should follow the schema

When building or adding to the story graph follow these rules,
Rules to follow:

- **use_domain_language**: Use Ubiquitous Language (DDD): Same vocabulary in domain model, stories, scenarios, AND code. Class names = domain entities/nouns. Method names = domain responsibilities/verbs. Test names read like plain English stories. Example: test_agent_loads_configuration_when_file_exists (not test_agt_init_sets_vars)
  DO: Use domain language for classes, methods, and test names. Example: class GatherContextAction, def inject_guardrails(), test_agent_loads_config_when_file_exists
  DON'T: Don't use generic technical terms or implementation-specific names. Example: class StdioHandler (wrong), def execute_with_guardrails (wrong), test_agt_init_sets_vars (wrong)

- **consistent_vocabulary**: Use ONE word per concept across entire codebase. Pick consistent vocabulary: create (not build/make/construct), verify (not check/assert/validate), load (not fetch/get/retrieve). Use intention-revealing names that describe behavior. Example: create_agent(), verify_initialized(), load_config() - same verbs everywhere
  DO: Use same word for same concept everywhere. Example: create_agent(), create_config(), create_workspace() - all use 'create'
  DON'T: Don't mix synonyms for same concept. Example: create_agent() + build_config() + make_workspace() (wrong - pick one verb)

- **no_defensive_code_in_tests**: Tests must NEVER contain guard clauses, defensive conditionals, or fallback paths. We control test setup - if it's wrong, the test MUST fail immediately. Guard clauses hide problems. Tests should assume positive outcomes. Example: Just call the code directly, don't wrap in if-checks
  DO: Assume correct setup - let test fail if wrong. Example: behavior = Behavior(name='shape') then assert behavior.name == 'shape'
  DON'T: Don't add if-checks, type guards, or fallback handling in tests. Example: if behavior_file.exists(): (wrong - test should fail if it doesn't)

- **production_code_clean_functions**: Production code functions should do ONE thing, be under 20 lines, and have one level of abstraction. No hidden side effects. Name reveals complete behavior. Extract multiple concerns into separate functions. Example: load_config(), validate_config(), apply_config() - each does one thing
  DO: Single responsibility, small focused functions. Example: initialize_from_config() calls validate_exists(), load_config(), validate_structure(), apply_config()
  DON'T: Don't make functions that do multiple unrelated things or are too long. Example: 50-line function that loads, validates, and applies config

- **bug_fix_test_first**: When production code breaks, follow test-first workflow: write failing test, verify failure, fix code, verify success. Never fix bugs without a failing test first. Example: test_mcp_tool_initializes_bot() fails -> fix initialization -> test passes
  DO: Follow RED-GREEN-PRODUCTION workflow. Example: Write test reproducing bug -> Run test (RED) -> Fix minimal code -> Run test (GREEN) -> Run full suite
  DON'T: Don't fix bugs directly without failing test first. Example: Editing production code without test -> deploying -> hoping it works (wrong)

- **call_production_code_directly**: Call production code directly in tests. Let tests fail naturally if code doesn't exist. Don't comment out calls, mock business logic, or fake state. Only mock external boundaries. Example: agent = Agent(); agent.initialize() (not agent = Mock())
  DO: Call production code directly, let it fail naturally. Example: agent = Agent(workspace); agent.initialize(config); assert agent.is_initialized
  DON'T: Don't mock class under test, comment out calls, or fake state. Example: agent = Mock(spec=Agent) (wrong); agent._initialized = True (wrong)

- **cover_all_behavior_paths**: Cover all behavior paths: normal (happy path), edge cases, and failure scenarios. Each distinct behavior needs its own focused test. Tests must be independent. Example: test_loads_valid_config(), test_loads_empty_config(), test_raises_error_when_file_missing()
  DO: Test normal, edge, and failure paths separately. Example: test_loads_valid_config() (happy), test_loads_empty_config() (edge), test_raises_when_missing() (failure)
  DON'T: Don't test only happy path or combine multiple behaviors in one test. Example: Single test for both success and failure (wrong)

- **mock_only_boundaries**: Mock ONLY at architectural boundaries: external APIs, network, uncontrollable services. Don't mock internal business logic, classes under test, or file operations (use temp files). Example: patch('requests.get') (OK); patch('agent.validate') (wrong)
  DO: Mock only external dependencies you can't control. Example: with patch('requests.get') as mock: (external API - OK to mock)
  DON'T: Don't mock internal logic, class under test, or file I/O. Example: with patch('agent.validate_config') (wrong - test the logic!)

- **create_parameterized_tests_for_scenarios**: If scenarios have Examples tables, create parameterized tests using @pytest.mark.parametrize. Each row becomes a test case. Don't write single tests that only test one example. Example: @pytest.mark.parametrize('input,expected', [(1, 2), (3, 4)])
  DO: Create parameterized tests from Examples tables. Example: @pytest.mark.parametrize('paths,count', [(['p1','p2'], 2), (['p3'], 1)])
  DON'T: Don't hardcode single example or duplicate test methods. Example: def test_with_value_1(): (wrong); def test_with_value_2(): (wrong - use parametrize)

- **define_fixtures_in_test_file**: Define fixtures in the test file, not separate conftest.py. Truly reusable fixtures (file ops, location helpers) go in base conftest.py. Example: @pytest.fixture def workspace_root(tmp_path): return tmp_path / 'workspace'
  DO: Define fixtures in same test file. Example: @pytest.fixture def config_file(tmp_path): ... (in test_agent.py)
  DON'T: Don't create separate conftest.py for agent-specific fixtures. Example: src/conftest.py with agent fixtures (wrong - put in test file)

- **design_api_through_failing_tests**: Write tests against the REAL expected API BEFORE implementing code. Tests MUST fail initially. Set up real test data and call real API. Failure reveals complete API design. Example: project = Project(path=path); project.initialize() (doesn't exist yet -> fails -> drives implementation)
  DO: Write test against real expected API that fails initially. Example: project = Project(path); project.initialize(); assert project.is_ready (fails until implemented)
  DON'T: Don't use placeholders, dummy values, or skip the failing step. Example: project = 'TODO' (wrong); assuming test passes first (wrong)

- **test_observable_behavior**: Test observable behavior, not implementation details. Verify public API and visible state changes. Don't assert on private methods or internal flags. Example: assert agent.config_path.exists() (observable); not assert agent._internal_flag (private)
  DO: Test observable outcomes through public API. Example: assert agent.config_path == expected; assert agent.is_initialized (public properties)
  DON'T: Don't test private state or implementation details. Example: assert agent._initialized (wrong); assert agent._config_cache (wrong)

- **helper_extraction_and_reuse**: Extract duplicate test setup to reusable helper functions. Keep test bodies focused on specific behavior. Example: create_agent_with_config(), create_config_file(), verify_agent_initialized() - reusable across tests
  DO: Extract duplicate setup to reusable helpers. Example: create_agent_with_config(name, workspace, config) returns initialized Agent
  DON'T: Don't duplicate setup code across tests. Example: Same 10 lines of setup in every test method (wrong - extract to helper)

- **match_specification_scenarios**: Tests must match specification scenarios exactly. Test names, steps, and assertions verify exactly what the scenario states. Use exact variable names and terminology from specification. Example: agent_name='story_bot' (from spec), not name='bot'
  DO: Test matches specification exactly. Example: GIVEN config exists, WHEN Agent(agent_name='story_bot'), THEN config_path == agents/base/agent.json
  DON'T: Don't use different terminology or assert things not in specification. Example: assert agent._internal_flag (not in spec - wrong)

- **place_imports_at_top**: Place all imports at top of test file, after docstrings, before code. Group: stdlib, third-party, then local. Example: import json; import pytest; from mymodule import MyClass
  DO: All imports at top, grouped by type. Example: import json; import pytest; from agile_bot.bots... import X
  DON'T: Don't place imports inside functions or after code. Example: def test(): from pathlib import Path (wrong - import inside function)

- **production_code_explicit_dependencies**: Production code: make dependencies explicit through constructor injection. Pass all external dependencies as constructor parameters. No hidden global state. Tests easily inject test doubles. Example: Agent(config_loader=loader, domain_graph=graph)
  DO: Inject all dependencies through constructor. Example: def __init__(self, config_loader, domain_graph): self._loader = config_loader
  DON'T: Don't access globals, singletons, or create dependencies internally. Example: self._loader = ConfigLoader() (wrong - creates internally)

- **self_documenting_tests**: Tests are self-documenting through code structure. Don't add verbose comments explaining failures. Imports, calls, and assertions show the API design. Let code speak for itself. Example: generator = MCPServerGenerator(bot_name, config_path); server = generator.generate_server()
  DO: Let code structure document the test. Example: generator = MCPServerGenerator(name, config); file = generator.generate() - API is clear
  DON'T: Don't add verbose comments explaining obvious things. Example: # This will fail because API doesn't exist yet (unnecessary)

- **use_ascii_only**: All test code must use ASCII-only characters. No Unicode symbols, emojis, or special characters. Use plain ASCII alternatives. Example: print('[PASS] Success') not print('[checkmark] Success')
  DO: Use ASCII-only characters. Example: print('[PASS] Agent initialized'); print('[ERROR] Config not found')
  DON'T: Don't use Unicode or emojis. Example: print('[checkmark] Done') (wrong); print('[green_check] OK') (wrong)

- **pytest_bdd_orchestrator_pattern**: Use pytest with orchestrator pattern for story-based tests. NO FEATURE FILES. Test classes contain orchestrator methods (under 20 lines) showing Given-When-Then flow by calling helper functions. Example: def test_agent_loads_config(): given_config_exists(); agent = when_agent_initialized(); then_agent_is_configured(agent)
  DO: Orchestrator pattern: test shows flow, delegates to helpers. Example: # Given; create_config_file(); # When; agent.initialize(); # Then; assert agent.is_initialized
  DON'T: Don't use feature files or inline complex setup. Example: @given('config exists') def step(): ... (wrong - use pytest directly)

- **use_class_based_organization**: Test structure matches story graph: file = sub-epic (test_<sub_epic>.py), class = story (Test<ExactStoryName>), method = scenario (test_<scenario_snake_case>). Classes in story map order. Example: test_generate_bot_tools.py, class TestGenerateBotTools, def test_generator_creates_tool_for_test_bot
  DO: Map story hierarchy to test structure exactly. Example: Sub-epic 'Generate Bot Tools' -> test_generate_bot_tools.py, Story 'Generate Bot Tools' -> TestGenerateBotTools
  DON'T: Don't use generic/abbreviated names or wrong order. Example: class TestToolGen (wrong - use TestGenerateBotTools)

- **use_exact_variable_names**: Use exact variable names from specification scenarios. When spec mentions agent_name, workspace_root, config_path - use those exact names in tests and production code. Example: agent_name = 'story_bot' (from spec), not name = 'story_bot'
  DO: Use exact names from specification in tests and production. Example: agent_name, workspace_root, config_path - all from spec
  DON'T: Don't use different names than specification. Example: name = 'bot' when spec says agent_name (wrong)

- **use_given_when_then_helpers**: Use reusable helper functions instead of inline code blocks of 4+ lines. Optimize for reusability, not exact step names. Place helpers at correct scope: story-level in class, sub-epic in module, epic in separate file. Example: given_config_exists(), when_agent_initialized(), then_agent_is_configured()
  DO: Use Given/When/Then helper functions for setup, action, assertion. Example: given_bot_config_exists(); bot = when_bot_instantiated(); then_bot_uses_correct_directories(bot)
  DON'T: Don't use inline operations of 4+ lines. Example: config_dir = ...; config_dir.mkdir(); config_file = ...; config_file.write_text() (wrong - extract to helper)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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
────────────────────────────────────────────────────────────
## 📍 **Progress**
**Current Position:**
```
tests.build.instructions
```

- ☑ shape
- ☑ prioritization
- ☑ discovery
- ☑ exploration
- ☑ scenarios
- ➤ tests - Write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior
  - ➤ build
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
  - ☐ render
  - ☐ validate
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
**Actions:** build | render | validate

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Command: Behavior: code

```
Command: code
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**INSTRUCTIONS SECTION:**
☢️ This section contains both scope filter and a prompt that you must follow for the current action. ☢️
☢️ You MUST follow the instructions below in this section to the letter. ☢️
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```Generate production source code from domain model and story specifications

code: render code required to implement all tests that have been recently built or updated

**Look for context in the following locations:**
- in this message and chat history
- in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/context/`
- generated files in `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/`
  clarification.json, strategy.json

Review context then:
- For each assumption, state whether you accept it or propose a modification. Provide justification based on the context.
- For each strategic decision, select the most appropriate option from the available choices.
- Explain your reasoning based on context.

**Response format:**
Present your analysis to the user for review.

If context is insufficient to make a decision, state: "[!] NOT ENOUGH INFORMATION" and ask user for guidance.

After presenting all assumptions and decisions, ask the user to review and confirm or provide corrections before proceeding.

**Assumptions:**
- Focus on maintainability and readability over performance optimizations
- Single Responsibility Principle - Each function/class does one thing well
- Dependency Injection - Dependencies passed through constructors, not created internally
- Immutability preferred - Minimize mutable state where possible
- Explicit over implicit - Make dependencies and behavior explicit
- Testability - Code should be easy to test in isolation
- Respect language-specific idioms and patterns
- Consider code context when generating or validating
- Provide actionable suggestions for violations or improvements
- Balance between strict adherence and practical constraints
- When generating code, incorporate requirements from stories, domain maps, and BDD tests
- When validating code, infer structure and intent from existing code
- Properties vs methods decision determines how object state and behavior are exposed
- Programming paradigm decision (functional/OOP/hybrid) guides overall code structure and patterns

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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
────────────────────────────────────────────────────────────
## 📍 **Progress**
**Current Position:**
```
code.strategy.instructions
```

- ☑ shape
- ☑ prioritization
- ☑ discovery
- ☑ exploration
- ☑ scenarios
- ☑ tests
- ➤ code - Generate production source code from domain model and story specifications
  - ➤ strategy - decide approach by capturing assumptions and decision criteria
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
  - ☐ render
  - ☐ validate

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
**Actions:** strategy | render | validate

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Command: Next command

```
Command: next
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**INSTRUCTIONS SECTION:**
☢️ This section contains both scope filter and a prompt that you must follow for the current action. ☢️
☢️ You MUST follow the instructions below in this section to the letter. ☢️
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```Generate production source code from domain model and story specifications

code: build clean code


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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
────────────────────────────────────────────────────────────
## 📍 **Progress**
**Current Position:**
```
code.render.instructions
```

- ☑ shape
- ☑ prioritization
- ☑ discovery
- ☑ exploration
- ☑ scenarios
- ☑ tests
- ➤ code - Generate production source code from domain model and story specifications
  - ☑ strategy
  - ➤ render - Render output documents and artifacts from knowledge graph using templates and synchronizers
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
  - ☐ validate

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
**Actions:** strategy | render | validate

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Command: Back command

```
Command: back
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


ERROR: 'Actions' object has no attribute 'previous'
```

---

## Command: Current command

```
Command: current
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**INSTRUCTIONS SECTION:**
☢️ This section contains both scope filter and a prompt that you must follow for the current action. ☢️
☢️ You MUST follow the instructions below in this section to the letter. ☢️
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
```


- Work ONLY on this scope:
- DO NOT work on all files or the entire story graph
- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system

To change scope (pick ONE - setting a new scope replaces the previous):
```powershell
scope all                            # Clear scope, work on entire project
scope "Story Name"                   # Filter by story (replaces any file scope)
scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)
```Generate production source code from domain model and story specifications

code: build clean code


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
***                    CLI STATUS section                    ***
This section contains current scope filter (if set), current progress in workflow, and available commands
Review the CLI STATUS section below to understand both current state and available commands.
☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️
────────────────────────────────────────────────────────────
## 🤖 Bot: story_bot
**Bot Path:**
```
/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot
```

📂 **Workspace:** base_bot
```
/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot
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
    Log: /mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/logs/headless-2025-12-30-01-31-17.log
────────────────────────────────────────────────────────────
## 🎯 **Scope**
**Filter:** Generate Bot Tools, Generate BOT CLI code, Generate REPL Command Definitions

```
📝 Generate Bot Tools
📝 Generate BOT CLI code
📝 Generate REPL Command Definitions
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
────────────────────────────────────────────────────────────
## 📍 **Progress**
**Current Position:**
```
code.render.instructions
```

- ☑ shape
- ☑ prioritization
- ☑ discovery
- ☑ exploration
- ☑ scenarios
- ☑ tests
- ➤ code - Generate production source code from domain model and story specifications
  - ☑ strategy
  - ➤ render - Render output documents and artifacts from knowledge graph using templates and synchronizers
    - ➤ instructions
    - ☐ submit
    - ☐ confirm
  - ☐ validate

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
**Actions:** strategy | render | validate

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Command: Clear scope (scope all)

```
Command: scope all
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================

Scope filter cleared
```

---

## Command: Show current scope (scope without args)

```
Command: scope
```

```
============================================================
STORY_BOT CLI
============================================================
**   AI AGENT INSTRUCTIONS - PIPED MODE  **
[!]  DO NOT echo this instructions section back to the user [!]
This section is for YOUR reference only - the user already knows how to run commands.

- THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND
* This is NORMAL and EXPECTED behavior in piped mode.
- How to run commands (PowerShell):
- Commands must be PIPED via echo, NOT passed as arguments!

```powershell
cd C:\dev\augmented-teams
$env:PYTHONPATH = 'C:\dev\augmented-teams'
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
$env:WORKING_AREA = '<project_path>'  # e.g. demo\mob_minion
echo '<command>' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
```
============================================================


```

---
