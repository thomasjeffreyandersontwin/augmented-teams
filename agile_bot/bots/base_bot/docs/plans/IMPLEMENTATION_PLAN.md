# Display REPL Status Panel - Implementation Plan

## Epic: View Bot Status in Panel

View bot workflow status in IDE panel to see current progress without switching to terminal.

---

### Feature: Transform CLI Output

#### Story: Load Bot Configuration

Load bot configuration from CLI output so users see which bot and workspace are active.

**Acceptance Criteria:**

**WHEN** CLI outputs bot section  
**THEN** panel reads bot name  
**AND** panel reads bot directory path  
**AND** panel reads workspace name  
**AND** panel reads workspace directory path

**WHEN** bot section is missing  
**THEN** panel shows "unknown bot" message

**WHEN** bot paths contain special characters  
**THEN** panel escapes HTML entities

**WHEN** workspace directory is very long  
**THEN** panel truncates with ellipsis

DONE

---

#### Story: Load Workflow Hierarchy

Load behavior hierarchy from CLI output so users see complete workflow structure.

**Acceptance Criteria:**

**WHEN** CLI outputs progress section  
**THEN** panel reads all behaviors  
**AND** panel reads nested actions per behavior  
**AND** panel reads nested operations per action

**WHEN** behavior has marker ➤  
**THEN** panel marks behavior as current

**WHEN** behavior has marker ☑  
**THEN** panel marks behavior as completed

**WHEN** behavior has marker ☐  
**THEN** panel marks behavior as pending

**WHEN** action or operation has status marker  
**THEN** panel applies same status rules

**WHEN** behavior has description text  
**THEN** panel preserves description

DONE
---

#### Story: Load Session Position

Load current session position so users know exact workflow location.

**Acceptance Criteria:**

**WHEN** CLI outputs current position "tests.build.confirm"  
**THEN** panel extracts behavior name "tests"  
**AND** panel extracts action name "build"  
**AND** panel extracts phase "confirm"  
**AND** panel calculates progress path "tests.build"

**WHEN** position has only behavior  
**THEN** panel shows behavior only

**WHEN** position format is invalid  
**THEN** panel shows empty position

DONE

---

#### Story: Detect Scope Type
`DONE`

Detect scope type from CLI output so users see appropriate scope content.

**Acceptance Criteria:**

**WHEN** CLI outputs scope with "file:" prefix  
**THEN** panel sets type to "files"  
**AND** panel loads file list

**WHEN** CLI outputs scope "all (entire project)"  
**THEN** panel sets type to "all"  
**AND** panel shows no file restrictions

**WHEN** CLI outputs scope with 🎯 emoji  
**THEN** panel sets type to "story"  
**AND** panel loads story tree

**WHEN** scope has graph links  
**THEN** panel extracts all link URLs  
**AND** panel extracts all link text

---

#### Story: Load Story Tree

Load story hierarchy from scope so users navigate story structure.

**Acceptance Criteria:**

**WHEN** scope type is "story"  
**THEN** panel parses epic lines with 🎯  
**AND** panel parses feature lines with ⚙️  
**AND** panel parses story lines with 📝

**WHEN** feature line has links  
**THEN** panel extracts file paths  
**AND** panel extracts line numbers

**WHEN** story line has multiple links  
**THEN** panel preserves all links in order

**WHEN** tree structure is deeply nested  
**THEN** panel maintains parent-child relationships

---

#### Story: Load File List

Load file paths from scope so users see files in current scope.

**Acceptance Criteria:**

**WHEN** scope type is "files"  
**THEN** panel finds "Files in scope:" section  
**AND** panel reads all lines starting with "- "

**WHEN** file path has extension  
**THEN** panel determines file type

**WHEN** file path is relative  
**THEN** panel preserves relative format

**WHEN** no files in scope  
**THEN** panel shows empty file list

---

#### Story: Load Parameter Documentation

Load CLI parameters from output so users know available arguments.

**Acceptance Criteria:**

**WHEN** CLI outputs Args section  
**THEN** panel finds code block after "Args:"  
**AND** panel parses each parameter line

**WHEN** parameter has format "--flag \"syntax\" # description"  
**THEN** panel extracts flag name  
**AND** panel extracts syntax example  
**AND** panel extracts description text

**WHEN** parameter has no syntax  
**THEN** panel stores empty syntax value

**WHEN** Args section is missing  
**THEN** panel shows empty parameters list

---

#### Story: Load Run Examples

Load command examples from output so users see how to invoke actions.

**Acceptance Criteria:**

**WHEN** CLI outputs Run section  
**THEN** panel finds code block after "Run:"  
**AND** panel parses each command line

**WHEN** command has "# comment"  
**THEN** panel extracts command  
**AND** panel extracts description

**WHEN** line starts with "//"  
**THEN** panel skips comment line

**WHEN** Run section is missing  
**THEN** panel shows empty examples list

---

#### Story: Load Headless Status

Load headless mode information so users know about autonomous execution.

**Acceptance Criteria:**

**WHEN** CLI outputs Headless Mode section  
**THEN** panel reads status line  
**AND** panel reads API key prefix

**WHEN** active session exists  
**THEN** panel reads session ID  
**AND** panel reads log file path

**WHEN** headless section is missing  
**THEN** panel shows "unavailable" status

**WHEN** API key is present  
**THEN** panel masks sensitive portions

---

#### Story: Load Available Commands

Load command list from output so users know available CLI commands.

**Acceptance Criteria:**

**WHEN** CLI outputs Commands section  
**THEN** panel finds section with 💻 emoji  
**AND** panel extracts pipe-delimited text

**WHEN** commands are separated by "|"  
**THEN** panel splits into individual commands  
**AND** panel trims whitespace

**WHEN** Commands section is missing  
**THEN** panel shows "N/A" message

---

### Feature: Display Status Information

#### Story: Show Bot Identity

Show bot name and workspace so users know which bot is active.

**Acceptance Criteria:**

**WHEN** bot configuration loads  
**THEN** panel displays bot name as heading  
**AND** panel displays bot directory below  
**AND** panel displays workspace name and path  
**AND** panel displays current position

**WHEN** bot name is very long  
**THEN** panel wraps text appropriately

**WHEN** paths contain backslashes  
**THEN** panel displays correctly

**WHEN** user hovers over paths  
**THEN** panel shows full path in tooltip

---

#### Story: Show Workflow Status

Show behavior hierarchy with status so users see workflow progress.

**Acceptance Criteria:**

**WHEN** behavior hierarchy loads  
**THEN** panel displays all behaviors  
**AND** panel displays nested actions  
**AND** panel displays nested operations

**WHEN** behavior is current  
**THEN** panel highlights with yellow marker ➤  
**AND** panel shows description if present

**WHEN** behavior is completed  
**THEN** panel shows green marker ☑  
**AND** panel dims appearance

**WHEN** behavior is pending  
**THEN** panel shows gray marker ☐

**WHEN** user scans workflow  
**THEN** panel shows clear visual hierarchy

---

#### Story: Show Scope Content

Show scope filter and content so users see current work boundaries.

**Acceptance Criteria:**

**WHEN** scope type is "story"  
**THEN** panel displays epic/feature/story tree  
**AND** panel makes file links clickable

**WHEN** scope type is "files"  
**THEN** panel displays file path list  
**AND** panel shows file types

**WHEN** scope type is "all"  
**THEN** panel displays "All files in workspace"

**WHEN** scope has graph links  
**THEN** panel displays link buttons  
**AND** panel makes links clickable

**WHEN** user clicks scope link  
**THEN** panel opens file in editor

---

#### Story: Show Parameter Reference

Show parameters as table so users understand available options.

**Acceptance Criteria:**

**WHEN** parameters load  
**THEN** panel displays table with columns  
**AND** panel shows flag in monospace font  
**AND** panel shows syntax example  
**AND** panel shows description

**WHEN** parameter has no syntax  
**THEN** panel shows empty syntax cell

**WHEN** no parameters exist  
**THEN** panel hides parameter section

**WHEN** table has many rows  
**THEN** panel maintains readable spacing

---

#### Story: Show Command Examples

Show run examples so users see how to invoke commands.

**Acceptance Criteria:**

**WHEN** run examples load  
**THEN** panel displays each command in code block  
**AND** panel shows description below command

**WHEN** example has no description  
**THEN** panel shows command only

**WHEN** command is very long  
**THEN** panel wraps or scrolls horizontally

**WHEN** no examples exist  
**THEN** panel hides examples section

---

#### Story: Show Headless Information

Show headless mode status so users know about autonomous capabilities.

**Acceptance Criteria:**

**WHEN** headless status loads  
**THEN** panel displays status value  
**AND** panel displays masked API key

**WHEN** active session exists  
**THEN** panel displays session ID  
**AND** panel displays log path as link

**WHEN** user clicks log path  
**THEN** panel opens log file

**WHEN** headless unavailable  
**THEN** panel shows unavailable message

---

#### Story: Show Available Commands

Show command list in footer so users know CLI commands.

**Acceptance Criteria:**

**WHEN** commands load  
**THEN** panel displays in footer  
**AND** panel formats with border  
**AND** panel shows 💻 icon

**WHEN** command list is long  
**THEN** panel wraps naturally

---

### Feature: Manage Panel Interactions

#### Story: Refresh Status Data

Refresh panel data on demand so user sees latest workflow state.

**Acceptance Criteria:**

**WHEN** user clicks Refresh button  
**THEN** panel calls Python CLI subprocess  
**AND** panel sends "status" command  
**AND** panel reads new output

**WHEN** CLI returns data  
**THEN** panel transforms to structured format  
**AND** panel re-renders all sections

**WHEN** CLI fails  
**THEN** panel shows error message  
**AND** panel displays retry button

**WHEN** refresh takes too long  
**THEN** panel shows timeout after 10 seconds

---

#### Story: Open Scope Files

Click links in scope section to open files in editor.

**Acceptance Criteria:**

**WHEN** user clicks story link  
**THEN** panel extracts file path  
**AND** panel opens file in editor

**WHEN** link has line number  
**THEN** panel navigates to specific line

**WHEN** file does not exist  
**THEN** panel shows error notification

**WHEN** file path is relative  
**THEN** panel resolves from workspace root

---

#### Story: Maintain Single Panel

Maintain one panel instance so resources are managed efficiently.

**Acceptance Criteria:**

**WHEN** user runs "Show Bot Status" command  
**THEN** system checks for existing panel

**WHEN** panel already exists  
**THEN** system reveals existing panel  
**AND** system refreshes data

**WHEN** no panel exists  
**THEN** system creates new panel

**WHEN** user closes panel  
**THEN** system disposes resources

---

#### Story: Fetch CLI Status

Spawn Python CLI process so panel gets current data.

**Acceptance Criteria:**

**WHEN** panel requests status  
**THEN** system spawns "python repl_main.py"  
**AND** system sends "status\n" via stdin

**WHEN** CLI writes to stdout  
**THEN** system collects output

**WHEN** CLI writes to stderr  
**THEN** system collects error messages

**WHEN** process exits successfully  
**THEN** system returns stdout text

**WHEN** process fails  
**THEN** system throws error with stderr

---

## Technical Reference

### Architecture

```
Extension Entry Point (extension.js)
  ↓
Panel Controller (status_panel.js)
  ↓
Data Provider (status_data_provider.js) → Python CLI
  ↓
Adapter (cli_output_adapter.js) → Parse text to JSON
  ↓
Renderer (html_renderer.js) → Generate HTML
  ↓
Webview Display
```

### Domain Model Mapping

**Python CLI Domain** → **JavaScript JSON**

```
CLIBot → {name, botDirectory, workspaceName, workspaceDirectory}
CLIBehaviors → behaviors: [{name, description, isCurrent, isCompleted, actions: [...]}]
CLIActions → actions: [{name, description, isCurrent, isCompleted, operations: [...]}]
REPLSession → session: {currentPosition, progressPath, currentBehavior, ...}
Scope → scope: {type, filter, graphLinks, content}
```

### File Structure

```
display_panel/
├── IMPLEMENTATION_PLAN.md          # This file
├── QUICKSTART.md                   # User guide
└── extension/
    ├── package.json                # Extension manifest
    ├── extension.js                # Entry point
    ├── status_panel.js             # Panel controller
    ├── status_data_provider.js     # Python subprocess
    ├── cli_output_adapter.js       # Text → JSON adapter
    ├── html_renderer.js            # JSON → HTML renderer
    └── rebuild.ps1                 # Build script
```

### Success Criteria

✅ Panel opens from command palette  
✅ All bot info displayed  
✅ Behavior/action/operation hierarchy visible  
✅ Status markers correct  
✅ Descriptions visible  
✅ Scope displays correctly (story/files/all)  
✅ Links clickable  
✅ Parameters table readable  
✅ Run examples formatted  
✅ Headless section shows session  
✅ Refresh button works  
✅ Theme colors adapt to VS Code
