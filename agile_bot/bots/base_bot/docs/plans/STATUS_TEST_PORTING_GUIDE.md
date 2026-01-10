# Status Domain Test Porting Guide

**Date**: 2026-01-08
**Purpose**: Specify exactly which existing tests to port for Status domain implementation

---

## Test Porting Strategy

**KEEP** existing Epic/Sub-Epic/Story test structure  
**RENAME** files only (REPL → CLI)  
**UPDATE** imports and class names (REPLSession → CLISession)  
**DO NOT** restructure tests or change test organization

---

## Files to Port

### 1. Direct API Tests (Already Work)

**Source**: `test_invoke_bot_directly.py`  
**Destination**: Copy to `agile_bot/test/test_api_status.py`  
**Action**: **COPY ENTIRE FILE** - no changes needed

**Reason**: These tests already test Bot domain methods directly. They work as-is for Status.

**Test Classes** (keep all):
- All existing test classes with Epic/Sub-Epic/Story structure
- All helper functions (`given_*`, `when_*`, `then_*`)
- All fixtures

---

### 2. CLI Navigation Tests (Rename REPL → CLI)

**Source**: `test_navigate_behaviors_using_repl_commands.py`  
**Destination**: Rename to `agile_bot/test/test_navigate_behaviors_using_cli_commands.py`  
**Action**: **RENAME FILE + UPDATE IMPORTS**

**Test Classes to Keep** (with Epic/Sub-Epic/Story structure):

```python
class TestNavigateToBehaviorActionAndExecute:
    """
    Story: Navigate to Behavior Action and Execute
    Epic: Invoke Bot Through CLI
    Sub-Epic: Navigate Behavior Action Status
    """
    def test_user_navigates_with_behavior_only(...)
    def test_user_navigates_with_behavior_dot_action(...)
    def test_user_navigates_with_full_dot_notation(...)
    def test_user_enters_invalid_behavior_in_dot_notation(...)

class TestNavigateSequentially:
    """
    Story: Navigate Sequentially
    Epic: Invoke Bot Through CLI
    Sub-Epic: Navigate Behavior Action Status
    """
    def test_user_navigates_with_next_command(...)
    def test_user_navigates_with_back_command(...)

class TestExitCLI:  # WAS: TestExitREPL
    """
    Story: Exit CLI
    Epic: Invoke Bot Through CLI
    """
    def test_user_exits_cli_with_exit_command(...)  # WAS: test_user_exits_repl_with_exit_command

class TestDisplayBotHierarchyTree:
    """
    Story: Display Bot Hierarchy Tree with Progress Indicators
    Epic: Invoke Bot Through CLI
    Sub-Epic: Navigate Behavior Action Status
    """
    def test_user_views_bot_hierarchy_with_status_command(...)  # KEEP THIS - tests Status!

class TestDisplayCurrentPosition:
    """
    Story: Display Current Position in CLI
    Epic: Invoke Bot Through CLI
    Sub-Epic: Navigate Behavior Action Status
    """
    def test_user_views_current_position_in_status(...)  # KEEP THIS - tests Status!
    def test_cli_displays_progress_section_with_current_position(...)  # KEEP THIS - tests Status!
    def test_cli_displays_behavior_in_progress_section(...)  # KEEP THIS - tests Status!
```

**Changes to Make**:
1. Rename file: `test_navigate_behaviors_using_repl_commands.py` → `test_navigate_behaviors_using_cli_commands.py`
2. Update imports:
   ```python
   # OLD
   from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
   
   # NEW
   from agile_bot.src.cli.cli_session import CLISession
   ```
3. Update class names:
   - `TestExitREPL` → `TestExitCLI`
4. Update method names:
   - `test_user_exits_repl_with_exit_command` → `test_user_exits_cli_with_exit_command`
5. Update variable names in tests:
   ```python
   # OLD
   repl_session = REPLSession(bot=bot, workspace_directory=workspace)
   cli_response = repl_session.read_and_execute_command('status')
   
   # NEW
   cli_session = CLISession(bot=bot, workspace_directory=workspace)
   cli_response = cli_session.read_and_execute_command('status')
   ```

**Keep**: All Epic/Sub-Epic/Story structure, all test organization, all helper functions

---

### 3. CLI Session Initialization Tests (Rename REPL → CLI)

**Source**: `test_initialize_repl_session.py`  
**Destination**: Rename to `agile_bot/test/test_initialize_cli_session.py`  
**Action**: **RENAME FILE + UPDATE IMPORTS**

**Test Classes to Keep** (with Epic/Sub-Epic/Story structure):

```python
class TestStartCLISession:  # WAS: TestStartREPLSession
    """
    Story: Start CLI Session
    Epic: Invoke Bot Through CLI
    Sub-Epic: Initialize CLI Session
    """
    def test_cli_launches_in_interactive_mode(...)
    def test_cli_loads_existing_behavior_action_state_on_launch(...)

class TestStartCLIInPipeMode:  # WAS: TestStartREPLInPipeMode
    """
    Story: Start CLI in Pipe Mode
    Epic: Invoke Bot Through CLI
    Sub-Epic: Initialize CLI Session
    """
    def test_cli_launches_in_pipe_mode(...)

class TestDisplayPipedModeInstructionsForAIAgents:
    """
    Story: Display Piped Mode Instructions for AI Agents
    Epic: Invoke Bot Through CLI
    Sub-Epic: Initialize CLI Session
    """
    def test_cli_displays_piped_mode_instructions_in_pipe_mode(...)
    def test_cli_omits_piped_mode_instructions_in_interactive_mode(...)

class TestDetectAndConfigureTTYNonTTYInput:
    """
    Story: Detect and Configure TTY/Non-TTY Input
    Epic: Invoke Bot Through CLI
    Sub-Epic: Initialize CLI Session
    """
    def test_tty_detector_identifies_interactive_terminal(...)  # KEEP THIS - tests adapter selection!
    def test_tty_detector_identifies_piped_input(...)  # KEEP THIS - tests adapter selection!

class TestLoadWorkspaceContext:
    """
    Story: Load Workspace Context
    Epic: Invoke Bot Through CLI
    Sub-Epic: Initialize CLI Session
    """
    def test_cli_loads_and_displays_workspace_context(...)

class TestDisplayCLIHeader:
    """
    Story: Display CLI Header
    Epic: Invoke Bot Through CLI
    Sub-Epic: Initialize CLI Session
    """
    def test_cli_displays_bot_name_in_header(...)
    def test_cli_displays_working_area_in_header(...)

class TestDisplayHeadlessModeStatus:
    """
    Story: Display Headless Mode Status
    Epic: Invoke Bot Through CLI
    Sub-Epic: Initialize CLI Session
    """
    def test_cli_shows_headless_mode_when_active(...)
```

**Changes to Make**:
1. Rename file: `test_initialize_repl_session.py` → `test_initialize_cli_session.py`
2. Update imports:
   ```python
   # OLD
   from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
   
   # NEW
   from agile_bot.src.cli.cli_session import CLISession
   ```
3. Update class names:
   - `TestStartREPLSession` → `TestStartCLISession`
   - `TestStartREPLInPipeMode` → `TestStartCLIInPipeMode`
4. Update variable names in all tests:
   ```python
   # OLD
   repl_session = REPLSession(...)
   
   # NEW
   cli_session = CLISession(...)
   ```

**Keep**: All Epic/Sub-Epic/Story structure, all test organization, all helper functions

---

### 4. Panel Tests (NEW - No Existing Tests)

**Source**: Story scenarios from `docs/stories/` and `docs/crc/walkthrough-realizations.md`  
**Destination**: Create new `agile_bot/test/test_panel_status.js`  
**Action**: **WRITE NEW TESTS** (panel tests don't exist yet)

**Test Structure** (follow Epic/Sub-Epic/Story pattern):

```javascript
/**
 * Epic: Invoke Bot Through Panel
 * Sub-Epic: Manage Bot Information
 * Story: Open Panel
 */
describe('Open Panel', () => {
    it('should receive Status JSON from CLI subprocess', async () => {
        // Walkthrough Scenario 1, lines 37-90
    });
    
    it('should handle Status JSON when no current action', async () => {
        // Edge case: idle bot
    });
});

/**
 * Epic: Invoke Bot Through Panel
 * Sub-Epic: Manage Bot Information
 * Story: Refresh Panel
 */
describe('Refresh Panel', () => {
    it('should refresh status when user clicks refresh', async () => {
        // Walkthrough Scenario 2, lines 124-164
    });
});

/**
 * Epic: Invoke Bot Through Panel
 * Sub-Epic: Manage Bot Information
 * Story: Render Status View
 */
describe('StatusView HTML Rendering', () => {
    it('should render Status JSON to HTML', () => {
        // Walkthrough Scenario 1, lines 95-116
    });
    
    it('should render Status with no current action', () => {
        // Edge case: idle status rendering
    });
});
```

**Based On**:
- `docs/crc/walkthrough-realizations.md` Scenario 1 (lines 37-116)
- `docs/crc/walkthrough-realizations.md` Scenario 2 (lines 124-164)

---

## Summary

| Source File | Destination File | Action | Test Classes |
|-------------|------------------|--------|--------------|
| `test_invoke_bot_directly.py` | `test_api_status.py` | **COPY** | All (keep as-is) |
| `test_navigate_behaviors_using_repl_commands.py` | `test_navigate_behaviors_using_cli_commands.py` | **RENAME + UPDATE** | 5 classes (rename REPL→CLI) |
| `test_initialize_repl_session.py` | `test_initialize_cli_session.py` | **RENAME + UPDATE** | 7 classes (rename REPL→CLI) |
| N/A (new) | `test_panel_status.js` | **CREATE NEW** | 3 describe blocks |

**Total Tests**: ~50+ existing tests (just renamed), ~6 new panel tests

**Epic/Sub-Epic/Story Structure**: **PRESERVED** - no changes to test organization

**Only Changes**:
- File names (REPL → CLI)
- Import paths (old base_bot paths → new agile_bot paths)
- Class names (REPL → CLI)
- Variable names (repl_session → cli_session)

