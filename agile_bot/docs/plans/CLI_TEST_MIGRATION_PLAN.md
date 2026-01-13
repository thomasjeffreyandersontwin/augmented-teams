# CLI Test Migration Plan

## Overview

This plan shows how to migrate CLI tests from the current structure to follow the domain test patterns with CLI-specific channel helpers.

**Goal:** Apply the 25 test rules to CLI tests while maintaining separation of concerns:
- **Domain tests** - Test business logic using `BotTestHelper`
- **CLI tests** - Test command parsing and channel output (TTY/Markdown/JSON), delegating to domain logic

## Core Principle: Mirror Domain Test Patterns

**CRITICAL:** CLI tests should match domain test patterns as closely as possible:
- ✅ **Same method signatures** across channels (TTY/Markdown use identical names)
- ✅ **Same test structure** (Given-When-Then, same helper patterns)
- ✅ **Same organization** (story-based classes, scenario-based methods)
- ✅ **Same vocabulary** (behavior, action, position, instructions)
- ✅ **Parallel helpers** (CLI helpers mirror domain helpers conceptually)

**What differs:**
- ❌ Internal assertions check different things (ANSI codes vs markdown vs JSON fields)
- ❌ What's being tested differs (display output vs business logic)

**Rationale:** Whenever possible, use similar methods and tests across domain and CLI. Even though internal asserts and what you're testing is different, the structure, naming, and patterns should be consistent. This applies even across different output channels - try to match the domain pattern first, then adapt for channel-specific needs.

## Key Insight: Mirror Production Architecture

**Production Code Structure:**
- Domain objects (Bot, Behavior, Action, etc.) - Format-agnostic
- Channel adapters (TTYAdapter, MarkdownAdapter, JSONAdapter) - Serialize domain objects
- Each adapter has methods like `serialize()`, `to_dict()`, etc.

**Test Helper Structure (should mirror this):**
- Domain helpers (StateTestHelper, BehaviorTestHelper, etc.) - Format-agnostic
- Channel helpers (TTYBotTestHelper, PipeBotTestHelper, JsonBotTestHelper) - Identical signatures
- Each helper has similar methods with appropriate verbs for the channel

## Current Problems

### Rule Violations in Existing CLI Tests

1. **❌ assert_full_results** - Tests cherry-pick fields instead of asserting full output strings
   - Example: `assert '➤' in status_section` instead of comparing full section
   
2. **❌ object_oriented_test_helpers** - Missing consolidated CLI channel helpers
   - Tests have inline string parsing (`extract_status_section`, `extract_footer_section`)
   - Should use channel helper objects that return complete expected outputs
   
3. **❌ standard_test_data_sets** - No standard CLI output fixtures
   - Each test creates ad-hoc assertions
   - Should have standard expected outputs from helpers

4. **❌ helper_extraction_and_reuse** - Duplicate helper functions
   - `assert_valid_json()` duplicated in 5 files
   - `extract_status_section()` duplicated in 3 files

5. **❌ use_class_based_organization** - Inconsistent class naming
   - Uses "InTTYMode" suffix instead of story-based names
   - Should map to story names from domain tests

## Pattern Consistency Example

**Domain Test:**
```python
def test_navigate_to_behavior(self, tmp_path):
    # Given
    helper = BotTestHelper(tmp_path)
    helper.state.set_state('shape', 'clarify')
    
    # When
    bot_result = helper.bot.execute('discovery', action_name='validate')
    
    # Then
    helper.behaviors.assert_at_behavior_action('discovery', 'validate')
    helper.behaviors.assert_bot_result_success(bot_result, 'discovery', 'validate')
```

**CLI Test (TTY) - Mirrors Domain Pattern:**
```python
def test_navigate_to_behavior_cli_tty(self, tmp_path):
    # Given - Creates domain helper internally
    helper = TTYBotTestHelper(tmp_path)
    helper.domain.state.set_state('shape', 'clarify')
    
    # When - SAME action (via CLI channel)
    cli_response = helper.cli_session.execute_command('discovery.validate')
    
    # Then - SAME domain assertion
    helper.domain.behaviors.assert_at_behavior_action('discovery', 'validate')
    
    # And - PARALLEL CLI assertion (same method name across TTY/Pipe/JSON)
    helper.navigation.assert_current_position_shows(cli_response.output, 'discovery', 'validate')
```

**CLI Test (Pipe) - IDENTICAL structure to TTY:**
```python
def test_navigate_to_behavior_cli_pipe(self, tmp_path):
    # Given - Creates domain helper internally
    helper = PipeBotTestHelper(tmp_path)  # Only this line changes
    helper.domain.state.set_state('shape', 'clarify')
    
    # When - SAME action (via CLI channel)
    cli_response = helper.cli_session.execute_command('discovery.validate')
    
    # Then - SAME domain assertion
    helper.domain.behaviors.assert_at_behavior_action('discovery', 'validate')
    
    # And - SAME method name as TTY (implementation differs internally)
    helper.navigation.assert_current_position_shows(cli_response.output, 'discovery', 'validate')
```

**Key Observations:**
- ✅ Test structure is IDENTICAL (Given-When-Then)
- ✅ Helper usage pattern is IDENTICAL (domain + channel helper)
- ✅ Method names are IDENTICAL across TTY/Markdown (`assert_current_position_shows`)
- ✅ Only difference: which helper instance and internal assertion logic
- ✅ Tests are parameterizable because structure/API is consistent

## Migration Architecture

### Helper Architecture (Mirrors Production)

**Domain Test Helper (format-agnostic):**
```
BotTestHelper
├── .bot                    # Production Bot instance
├── .workspace              # Test workspace
├── .state                  # StateTestHelper (domain)
├── .behaviors              # BehaviorTestHelper (domain)
├── .navigation             # NavigationTestHelper (domain) - EXTRACT from existing tests
└── .scope                  # ScopeTestHelper (domain)
```

**CLI Channel Test Helpers (inherit from CLIBotTestHelper):**
```
TTYBotTestHelper(CLIBotTestHelper)
├── .domain                 # BotTestHelper (created in __init__)
├── .cli_session            # CLISession(mode='tty')
├── .bot                    # TTYBotHelper (class name has channel prefix)
├── .instructions           # TTYInstructionsHelper
├── .scope                  # TTYScopeHelper
├── .navigation             # TTYNavigationHelper
└── .help                   # TTYHelpHelper

PipeBotTestHelper(CLIBotTestHelper)
├── .domain                 # BotTestHelper (created in __init__)
├── .cli_session            # CLISession(mode='pipe')
├── .bot                    # PipeBotHelper (class name has channel prefix)
├── .instructions           # PipeInstructionsHelper
├── .scope                  # PipeScopeHelper
├── .navigation             # PipeNavigationHelper
└── .help                   # PipeHelpHelper

JsonBotTestHelper(CLIBotTestHelper)
├── .domain                 # BotTestHelper (created in __init__)
├── .cli_session            # CLISession(mode='json')
├── .bot                    # JsonBotHelper (class name has channel prefix)
├── .instructions           # JsonInstructionsHelper
├── .scope                  # JsonScopeHelper
├── .navigation             # JsonNavigationHelper
└── .help                   # JsonHelpHelper
```

**Property names stay the same (`.bot`, `.instructions`, `.scope`, `.navigation`, `.help`) across all channels for polymorphism.**
**Class names have channel prefix (TTY/Pipe/Json) to avoid confusion with domain helpers.**

**Key Principle:** Channel helpers return **hard-coded strings** that emulate exactly what the CLI should display for that channel. Methods use channel-appropriate verbs.

### Method Naming: Domain vs CLI Channels

**Pattern:** Domain helpers test business logic (objects/dicts). CLI helpers assert specific text/structure in formatted output.

Based on actual CLI test assertions, here's what gets checked:

| Domain Helper Method | What It Tests | Corresponding CLI Assertions (from real tests) |
|---------------------|---------------|------------------------------------------------|
| `behaviors.assert_at_behavior_action(behavior, action)` | Bot state: `bot.behaviors.current.name == behavior`<br>`bot.behaviors.current.actions.current_action_name == action` | **TTY:** Checks output contains:<br>- `"Current Position:"` label<br>- `"{behavior}.{action}"` value<br>- `"➤"` marker<br>- Bolded behavior/action in footer<br><br>**Markdown:** Checks output contains:<br>- `"**Current Position:** {behavior}.{action}"`<br>- `"**{behavior}**"` and `"**{action}**"` in footer<br><br>**JSON:** Checks JSON contains:<br>- `bot_data['current_behavior'] == behavior` |
| `behaviors.assert_bot_result_success(result, behavior, action)` | Result dict has:<br>- `status == 'success'`<br>- `behavior == behavior`<br>- `action == action`<br>- `message == f'Executed {behavior}.{action}'` | **TTY:** Checks output contains:<br>- `"INSTRUCTIONS"` section<br>- `"Behavior Instructions - {behavior}"`<br>- `"Action Instructions - {action}"`<br>- `"CLI STATUS section"`<br><br>**Markdown:** Checks output contains:<br>- `"## Behavior Instructions - {behavior}"`<br>- `"## Action Instructions - {action}"`<br>- `"## CLI STATUS section"`<br><br>**JSON:** Checks JSON contains:<br>- `instructions_data['behavior_metadata']['name'] == behavior`<br>- `instructions_data['action_metadata']['name'] == action` |

**CLI Helper Methods by Channel:**

| Domain Helper Method | What's Being Checked | CLI Helper Method (Identical Across TTY/Pipe/JSON) | TTY Checks | Pipe Checks | JSON Checks |
|---------------------|---------------------|--------------------------------------------------|-----------|------------|------------|
| `behaviors.assert_bot_result_success(result, behavior, action)` | Instructions section shows behavior/action | `instructions.assert_section_shows_behavior_and_action(output, behavior, action)` | "INSTRUCTIONS" header, "Behavior Instructions - {behavior}", "Action Instructions - {action}" | "## INSTRUCTIONS", "## Behavior Instructions - {behavior}", "## Action Instructions - {action}" | `instructions['behavior_metadata']['name'] == behavior`, `instructions['action_metadata']['name'] == action` |
| `behaviors.assert_at_behavior_action(behavior, action)` | Current position shows | `navigation.assert_current_position_shows(output, behavior, action)` | "Current Position:", "{behavior}.{action}", "➤" marker, ANSI bold in footer | "**Current Position:**", "{behavior}.{action}", **bold** in footer | `data['current_behavior'] == behavior`, `data['current_action'] == action` |
| `behaviors.assert_bot_result_error_behavior_not_found(result, behavior)` | Error message for missing behavior | `bot.assert_error_shows_behavior_not_found(output, behavior)` | Red ANSI codes, "ERROR", "Behavior not found: {behavior}" | "## ERROR", "Behavior not found: {behavior}" | `error['status'] == 'error'`, `error['message']` contains behavior |
| `behaviors.assert_bot_result_error_action_not_found(result, action)` | Error message for missing action | `bot.assert_error_shows_action_not_found(output, action)` | Red ANSI codes, "ERROR", "Action not found: {action}" | "## ERROR", "Action not found: {action}" | `error['status'] == 'error'`, `error['message']` contains action |
| `behaviors.assert_shape_behavior_structure()` | Behavior has correct actions | `navigation.assert_behavior_tree_shows_actions(output, behavior, actions_list)` | Tree with "├──", "└──", action names listed | Markdown list with "- {action}" | `behavior_data['actions']` list matches |
| `state.assert_state_saved(behavior, action)` | State persisted to file | `bot.assert_status_shows_current_state(output, behavior, action)` | "CLI STATUS section", "Current Position: {behavior}.{action}" | "## CLI STATUS", "**Current Position:** {behavior}.{action}" | `status['current_behavior']`, `status['current_action']` |
| N/A (CLI-specific) | Complete status display exists | `bot.assert_status_section_present(output)` | "CLI STATUS section" header present | "## CLI STATUS" present | `data['status']` object exists |
| N/A (CLI-specific) | Help text displayed | `help.assert_help_shows_available_commands(output)` | Box-drawn table with commands | Markdown table with commands | `help['commands']` array |
| N/A (CLI-specific) | Scope display | `scope.assert_scope_shows_target(output, scope_type, target)` | "Scope:", "{scope_type}: {target}" | "**Scope:** {scope_type}: {target}" | `scope['type']`, `scope['target']` |

**All three helpers have IDENTICAL method signatures. Internal implementation differs:**
- TTY: checks ANSI codes, "➤" marker, box drawing, color codes
- Pipe: checks markdown (##, **bold**, lists, backticks)
- JSON: parses JSON, checks fields (current_behavior, instructions.behavior_metadata, etc.)

**Architecture:**

```python
class CLIBotTestHelper(BaseTestHelper):
    """Base for all CLI channel helpers - creates BotTestHelper internally"""
    
    def __init__(self, tmp_path, mode):
        self.domain = BotTestHelper(tmp_path)  # Create internally
        self.cli_session = CLISession(
            bot=self.domain.bot, 
            workspace_directory=self.domain.workspace, 
            mode=mode
        )

class TTYBotTestHelper(CLIBotTestHelper):
    """TTY - checks ANSI codes, box drawing, markers"""
    
    def __init__(self, tmp_path):
        super().__init__(tmp_path, mode='tty')
        self.bot = TTYBotHelper(self)
        self.instructions = TTYInstructionsHelper(self)
        self.scope = TTYScopeHelper(self)
        self.navigation = TTYNavigationHelper(self)
        self.help = TTYHelpHelper(self)

class PipeBotTestHelper(CLIBotTestHelper):
    """Pipe - checks markdown (##, **bold**, backticks)"""
    
    def __init__(self, tmp_path):
        super().__init__(tmp_path, mode='pipe')
        self.bot = PipeBotHelper(self)
        self.instructions = PipeInstructionsHelper(self)
        self.scope = PipeScopeHelper(self)
        self.navigation = PipeNavigationHelper(self)
        self.help = PipeHelpHelper(self)

class JsonBotTestHelper(CLIBotTestHelper):
    """JSON - parses JSON, checks data fields"""
    
    def __init__(self, tmp_path):
        super().__init__(tmp_path, mode='json')
        self.bot = JsonBotHelper(self)
        self.instructions = JsonInstructionsHelper(self)
        self.scope = JsonScopeHelper(self)
        self.navigation = JsonNavigationHelper(self)
        self.help = JsonHelpHelper(self)

# Example sub-helper
class TTYNavigationHelper:
    def __init__(self, parent):
        self.parent = parent
    
    def assert_current_position_shows(self, output: str, behavior: str, action: str):
        assert 'Current Position:' in output
        assert f'{behavior}.{action}' in output
        assert '➤' in output

class PipeNavigationHelper:
    def __init__(self, parent):
        self.parent = parent
    
    def assert_current_position_shows(self, output: str, behavior: str, action: str):
        assert '**Current Position:**' in output
        assert f'{behavior}.{action}' in output

class JsonNavigationHelper:
    def __init__(self, parent):
        self.parent = parent
    
    def assert_current_position_shows(self, output: str, behavior: str, action: str):
        import json
        data = json.loads(output)
        assert data['current_behavior'] == behavior
```

**Structure:**
```
TTYBotTestHelper(tmp_path)  # Creates BotTestHelper internally
├── .domain                # BotTestHelper (created internally)
│   ├── .bot              # Production Bot instance
│   ├── .workspace        # Test workspace
│   ├── .state            # StateTestHelper
│   └── .behaviors        # BehaviorTestHelper
├── .cli_session          # CLISession(mode='tty')
├── .bot                  # TTYBotHelper (status, metadata assertions)
├── .instructions         # TTYInstructionsHelper (instructions assertions)
├── .scope                # TTYScopeHelper (scope display assertions)
├── .navigation           # TTYNavigationHelper (position, hierarchy assertions)
└── .help                 # TTYHelpHelper (help display assertions)

PipeBotTestHelper / JsonBotTestHelper - same structure, different implementations
```

**Example Usage (Based on Real Tests):**

```python
# Domain Test - format agnostic
def test_navigate_to_behavior(self, tmp_path):
    helper = BotTestHelper(tmp_path)
    helper.state.set_state('shape', 'clarify')
    
    # Execute domain logic
    bot_result = helper.bot.execute('discovery', action_name='validate')
    
    # Assert domain state (format-agnostic)
    helper.behaviors.assert_at_behavior_action('discovery', 'validate')
    helper.behaviors.assert_bot_result_success(bot_result, 'discovery', 'validate')
```

```python
# CLI Test - TTY format specific
def test_navigate_to_behavior_cli_tty(self, tmp_path):
    """Based on actual test: test_user_navigates_with_behavior_only (line 82-142)"""
    helper = BotTestHelper(tmp_path)
    helper.state.set_state('shape', 'clarify')
    
    tty_helper = TTYBotTestHelper(helper)
    
    # Execute CLI command (production code)
    cli_response = tty_helper.cli_session.execute_command('discovery')
    
    # Assert domain state (reuse domain helper - format-agnostic)
    helper.behaviors.assert_at_behavior_action('discovery', 'clarify')
    
    # Assert TTY output format (CLI helper - checks complete display structure)
    tty_helper.assert_instructions_section_shows_behavior_and_action(
        cli_response.output, 'discovery', 'clarify')
    tty_helper.assert_current_position_shows(
        cli_response.output, 'discovery', 'clarify')  # Includes status, marker, emphasized footer
```

**Key Point:** CLI assertion names reflect EXACTLY what text/structure they're checking:
- `assert_instructions_section_shows_behavior_and_action` → checks for "Behavior Instructions - discovery" and "Action Instructions - clarify"
- `assert_current_position_shows` → checks for COMPLETE position display:
  - Status section with "Current Position: discovery.clarify"
  - Current marker "➤" symbol
  - Emphasized footer with ANSI bold codes around behavior/action names

### Example Usage - Parameterized Test

```python
@pytest.mark.parametrize("helper_class", [
    TTYBotTestHelper,
    PipeBotTestHelper,
    JsonBotTestHelper
])
def test_navigate_to_behavior(self, tmp_path, helper_class):
    # Given
    helper = helper_class(tmp_path)  # Creates BotTestHelper internally
    helper.domain.state.set_state('shape', 'clarify')
    
    # When
    cli_response = helper.cli_session.execute_command('discovery')
    
    # Then - Domain (same for all)
    helper.domain.behaviors.assert_at_behavior_action('discovery', 'clarify')
    
    # Then - Channel (IDENTICAL signatures, uses sub-helpers)
    helper.instructions.assert_section_shows_behavior_and_action(
        cli_response.output, 'discovery', 'clarify')
    helper.navigation.assert_current_position_shows(
        cli_response.output, 'discovery', 'clarify')
    helper.bot.assert_status_section_present(cli_response.output)
```

**Key Points:**
- ✅ `CLIBotTestHelper` creates `BotTestHelper` internally (no explicit passing)
- ✅ Access domain helper via `.domain` property
- ✅ Sub-helpers have **IDENTICAL signatures** across channels
- ✅ Tests **fully parameterizable** - one test runs against all 3 channels

## Detailed Migration Plan - Navigate Behaviors Area

### Files to Create

#### 1. Base CLI Test Helper

**File:** `agile_bot/test/CLI/helpers/cli_bot_test_helper.py`

```python
"""Base CLI Bot Test Helper - Creates domain helper internally"""
from pathlib import Path
from agile_bot.src.cli.cli_session import CLISession
from agile_bot.test.domain.bot_test_helper import BotTestHelper
from agile_bot.test.domain.helpers.base_helper import BaseHelper


class CLIBotTestHelper(BaseHelper):
    """Base class for all CLI channel helpers - manages domain helper and CLI session"""
    
    def __init__(self, tmp_path: Path, mode: str):
        """
        Initialize CLI helper with domain helper and CLI session.
        
        Args:
            tmp_path: Test temporary directory
            mode: CLI mode ('tty', 'pipe', or 'json')
        """
        # Create domain helper internally (encapsulation)
        self.domain = BotTestHelper(tmp_path)
        
        # Create CLI session with proper mode
        self.cli_session = CLISession(
            bot=self.domain.bot,
            workspace_directory=self.domain.workspace,
            mode=mode
        )
```

**Methods:** 7 total
- `__init__(tmp_path, mode)` - Initialize with domain helper and CLI session

#### 2. TTY Bot Test Helper

**File:** `agile_bot/test/CLI/helpers/tty_bot_test_helper.py`

**See "EXAMPLE: TTYBotTestHelper Implementation" section for complete pattern.**

**Structure:**
```python
class TTYBotTestHelper(CLIBotTestHelper):
    """TTY channel helper - checks ANSI codes, box drawing, markers"""
    
    def __init__(self, tmp_path):
        super().__init__(tmp_path, mode='tty')
        self.bot = TTYBotHelper(self)
        self.instructions = TTYInstructionsHelper(self)
        self.scope = TTYScopeHelper(self)
        self.navigation = TTYNavigationHelper(self)
        self.help = TTYHelpHelper(self)
```

**Sub-helpers to create:**
- `TTYBotHelper` (5 methods)
  - `assert_status_section_present(output)` - Check CLI STATUS section exists
  - `assert_error_shows_behavior_not_found(output, behavior)` - Check error format
  - `assert_error_shows_action_not_found(output, action)` - Check error format
  - `assert_status_shows_current_state(output, behavior, action)` - Check status display
  - `assert_bot_metadata_shown(output, bot_name)` - Check bot name in output

- `TTYInstructionsHelper` (3 methods)
  - `assert_section_shows_behavior_and_action(output, behavior, action)` - Check INSTRUCTIONS section
  - `assert_behavior_instructions_shown(output, behavior)` - Check behavior instructions
  - `assert_action_instructions_shown(output, action)` - Check action instructions

- `TTYNavigationHelper` (4 methods)
  - `assert_current_position_shows(output, behavior, action)` - Comprehensive position check
  - `assert_behavior_tree_shows_actions(output, behavior, actions_list)` - Check tree structure
  - `assert_current_marker_present(output)` - Check "➤" marker
  - `assert_footer_emphasizes_current(output, behavior, action)` - Check ANSI bold codes

- `TTYScopeHelper` (3 methods)
  - `assert_scope_shows_target(output, scope_type, target)` - Check scope display
  - `assert_scope_cleared_message(output)` - Check clear confirmation
  - `assert_scope_set_message(output, scope_type, target)` - Check set confirmation

- `TTYHelpHelper` (2 methods)
  - `assert_help_shows_available_commands(output)` - Check help table
  - `assert_help_shows_command_details(output, command)` - Check specific command help

**Total Methods:** 17 assertion methods across 5 sub-helpers

#### 3. Pipe Bot Test Helper

**File:** `agile_bot/test/CLI/helpers/pipe_bot_test_helper.py`

**Structure:**
```python
class PipeBotTestHelper(CLIBotTestHelper):
    """Pipe/Markdown channel helper - checks markdown formatting"""
    
    def __init__(self, tmp_path):
        super().__init__(tmp_path, mode='pipe')
        self.bot = PipeBotHelper(self)
        self.instructions = PipeInstructionsHelper(self)
        self.scope = PipeScopeHelper(self)
        self.navigation = PipeNavigationHelper(self)
        self.help = PipeHelpHelper(self)
```

**Sub-helpers:** Same structure as TTY, IDENTICAL method signatures
- `PipeBotHelper` (5 methods - same signatures as TTYBotHelper)
- `PipeInstructionsHelper` (3 methods - same signatures)
- `PipeNavigationHelper` (4 methods - same signatures)
- `PipeScopeHelper` (3 methods - same signatures)
- `PipeHelpHelper` (2 methods - same signatures)

**Total Methods:** 17 assertion methods (identical signatures to TTY)

#### 4. JSON Bot Test Helper

**File:** `agile_bot/test/CLI/helpers/json_bot_test_helper.py`

**Structure:**
```python
class JsonBotTestHelper(CLIBotTestHelper):
    """JSON channel helper - parses JSON and checks data fields"""
    
    def __init__(self, tmp_path):
        super().__init__(tmp_path, mode='json')
        self.bot = JsonBotHelper(self)
        self.instructions = JsonInstructionsHelper(self)
        self.scope = JsonScopeHelper(self)
        self.navigation = JsonNavigationHelper(self)
        self.help = JsonHelpHelper(self)
```

**Sub-helpers:** Same structure as TTY/Pipe, IDENTICAL method signatures
- `JsonBotHelper` (5 methods - same signatures as TTYBotHelper)
- `JsonInstructionsHelper` (3 methods - same signatures)
- `JsonNavigationHelper` (4 methods - same signatures)
- `JsonScopeHelper` (3 methods - same signatures)
- `JsonHelpHelper` (2 methods - same signatures)

**Total Methods:** 17 assertion methods (identical signatures to TTY/Pipe)

#### 5. Helper Module Init

**File:** `agile_bot/test/CLI/helpers/__init__.py`

```python
"""CLI Test Helpers"""
from .cli_bot_test_helper import CLIBotTestHelper
from .tty_bot_test_helper import TTYBotTestHelper
from .pipe_bot_test_helper import PipeBotTestHelper
from .json_bot_test_helper import JsonBotTestHelper

__all__ = [
    'CLIBotTestHelper',
    'TTYBotTestHelper',
    'PipeBotTestHelper',
    'JsonBotTestHelper'
]
```

#### 6. Updated Domain Test Helper (NavigationTestHelper)

**File:** `agile_bot/test/domain/helpers/navigation_helper.py` (NEW)

**Methods:** 4 total
- `navigate_to(behavior, action)` - Navigate to specific position
- `navigate_next()` - Navigate to next action
- `navigate_back()` - Navigate to previous action
- `assert_at_position(behavior, action)` - Assert current position

**Update:** `agile_bot/test/domain/bot_test_helper.py`
- Add `self.navigation = NavigationTestHelper(parent=self)` in `__init__`

#### 7. CLI Test Files (Updates to Existing)

**Files to UPDATE (not create):**
- `test_navigate_behaviors_using_cli_commands.py` - Add parameterized tests
- `test_initialize_cli_session.py` - Add parameterized tests
- `test_execute_actions_using_cli.py` - Add parameterized tests
- `test_manage_scope_using_cli.py` - Add parameterized tests
- `test_get_help_using_cli.py` - Add parameterized tests

**Pattern for each file:**

**File:** `agile_bot/test/CLI/test_navigate_behaviors_using_cli_commands.py` (REPLACE EXISTING)

```python
"""
Navigate Bot Behaviors Through CLI Tests

Maps to: test_navigate_and_execute_behaviors.py (domain logic)

CLI Focus:
- Command parsing (dot notation, next/back commands)
- Channel output verification (TTY, Markdown, JSON)
- Delegation to domain logic
"""

import pytest
from agile_bot.src.cli.cli_session import CLISession
from agile_bot.test.domain.bot_test_helper import BotTestHelper


class TestNavigateToBehaviorUsingCLI:
    """
    Story: Navigate To Behavior Using CLI Commands
    
    Domain logic: test_navigate_and_execute_behaviors.py::TestNavigateToBehavior
    CLI focus: Behavior command parsing and channel output (TTY, Markdown, JSON)
    """
    
    @pytest.mark.parametrize("mode,helper_attr,method_name", [
        ("tty", "tty", "show_navigation_success"),
        ("markdown", "markdown", "format_navigation_success"),
        ("json", "json", "navigation_result")
    ])
    def test_navigate_to_behavior_by_name(self, tmp_path, mode, helper_attr, method_name):
        """
        SCENARIO: Navigate to behavior by name (all channels)
        GIVEN: CLI session with multiple behaviors
        WHEN: user enters behavior name 'discovery'
        THEN: CLI navigates to discovery behavior
              Output matches expected format for channel
        
        Covers:
        - TTY mode: Full status display with ANSI codes
        - Markdown mode: Full status with markdown formatting
        - JSON mode: Complete JSON structure
        """
        # GIVEN: CLI session
        helper = BotTestHelper(tmp_path)
        helper.state.set_state('shape', 'clarify')
        
        cli_session = CLISession(
            bot=helper.bot, 
            workspace_directory=helper.workspace, 
            mode=mode
        )
        
        # WHEN: Navigate to discovery
        cli_response = cli_session.execute_command('discovery')
        
        # THEN: Domain assertion (format-agnostic)
        helper.behaviors.assert_at_behavior_action('discovery', 'clarify')
        
        # Channel assertion (format-specific) - assert FULL output
        # Mirrors production: TTYNavigation.serialize(), MarkdownNavigation.serialize(), etc.
        channel_helper = getattr(helper, channel)
        expected_output = channel_helper.navigation.serialize('discovery', 'clarify')
        
        assert cli_response.output.strip() == expected_output.strip()
    
    @pytest.mark.parametrize("mode,helper_attr,method_name", [
        ("tty", "tty", "show_navigation_success"),
        ("markdown", "markdown", "format_navigation_success"),
        ("json", "json", "navigation_result")
    ])
    def test_navigate_with_dot_notation(self, tmp_path, mode, helper_attr, method_name):
        """
        SCENARIO: Navigate with behavior.action dot notation (all channels)
        GIVEN: CLI session at shape.clarify
        WHEN: user enters 'discovery.validate'
        THEN: CLI navigates to discovery.validate
              Output matches expected format for channel
        """
        # GIVEN
        helper = BotTestHelper(tmp_path)
        helper.state.set_state('shape', 'clarify')
        
        cli_session = CLISession(
            bot=helper.bot, 
            workspace_directory=helper.workspace, 
            mode=mode
        )
        
        # WHEN
        cli_response = cli_session.execute_command('discovery.validate')
        
        # THEN: Domain assertion
        helper.behaviors.assert_at_behavior_action('discovery', 'validate')
        
        # Channel assertion
        channel_helper = getattr(helper, helper_attr)
        get_expected = getattr(channel_helper, method_name)
        expected = get_expected('discovery', 'validate')
        
        assert cli_response.output.strip() == expected.strip()
    
    @pytest.mark.parametrize("mode,helper_attr,error_method", [
        ("tty", "tty", "show_error"),
        ("markdown", "markdown", "format_error"),
        ("json", "json", "error_data")
    ])
    def test_navigate_to_invalid_behavior_shows_error(self, tmp_path, mode, helper_attr, error_method):
        """
        SCENARIO: Navigate to invalid behavior shows error (all channels)
        GIVEN: CLI session with shape behavior only
        WHEN: user enters 'invalid_behavior'
        THEN: CLI displays error message in appropriate channel format
        """
        # GIVEN
        helper = BotTestHelper(tmp_path)
        helper.state.set_state('shape', 'clarify')
        
        cli_session = CLISession(
            bot=helper.bot, 
            workspace_directory=helper.workspace, 
            mode=mode
        )
        
        # WHEN
        cli_response = cli_session.execute_command('invalid_behavior')
        
        # THEN: Assert error format
        channel_helper = getattr(helper, helper_attr)
        get_error = getattr(channel_helper, error_method)
        expected = get_error("Behavior 'invalid_behavior' not found")
        
        assert cli_response.output.strip() == expected.strip()


class TestNavigateSequentiallyUsingCLI:
    """
    Story: Navigate Sequentially Using CLI Commands (next/back)
    
    Domain logic: test_navigate_and_execute_behaviors.py::TestNavigateSequentially
    CLI focus: Sequential command parsing and channel output
    """
    
    @pytest.mark.parametrize("mode,helper_attr,method_name", [
        ("tty", "tty", "show_navigation_success"),
        ("markdown", "markdown", "format_navigation_success"),
        ("json", "json", "navigation_result")
    ])
    def test_navigate_with_next_command(self, tmp_path, mode, helper_attr, method_name):
        """
        SCENARIO: Navigate with next command (all channels)
        GIVEN: CLI at shape.clarify
        WHEN: user enters 'next'
        THEN: CLI advances to shape.strategy
              Output shows success in appropriate channel format
        """
        # GIVEN
        helper = BotTestHelper(tmp_path)
        helper.state.set_state('shape', 'clarify')
        
        cli_session = CLISession(
            bot=helper.bot, 
            workspace_directory=helper.workspace, 
            mode=mode
        )
        
        # WHEN
        cli_response = cli_session.execute_command('next')
        
        # THEN: Domain assertion
        helper.behaviors.assert_at_behavior_action('shape', 'strategy')
        
        # Channel assertion
        channel_helper = getattr(helper, helper_attr)
        get_expected = getattr(channel_helper, method_name)
        expected = get_expected('shape', 'strategy')
        
        assert cli_response.output.strip() == expected.strip()
    
    @pytest.mark.parametrize("mode,helper_attr,method_name", [
        ("tty", "tty", "show_navigation_success"),
        ("markdown", "markdown", "format_navigation_success"),
        ("json", "json", "navigation_result")
    ])
    def test_navigate_with_back_command(self, tmp_path, mode, helper_attr, method_name):
        """
        SCENARIO: Navigate with back command (all channels)
        GIVEN: CLI at shape.strategy
        WHEN: user enters 'back'
        THEN: CLI moves back to shape.clarify
              Output shows success in appropriate channel format
        """
        # GIVEN
        helper = BotTestHelper(tmp_path)
        helper.state.set_state('shape', 'strategy')
        
        cli_session = CLISession(
            bot=helper.bot, 
            workspace_directory=helper.workspace, 
            mode=mode
        )
        
        # WHEN
        cli_response = cli_session.execute_command('back')
        
        # THEN
        helper.behaviors.assert_at_behavior_action('shape', 'clarify')
        
        channel_helper = getattr(helper, helper_attr)
        get_expected = getattr(channel_helper, method_name)
        expected = get_expected('shape', 'clarify')
        
        assert cli_response.output.strip() == expected.strip()


class TestDisplayBotStatusUsingCLI:
    """
    Story: Display Bot Hierarchy and Status
    
    CLI-specific story: Shows bot hierarchy tree with progress indicators
    CLI focus: Status command and channel display format
    """
    
    @pytest.mark.parametrize("mode,helper_attr,method_name", [
        ("tty", "tty", "display_status"),
        ("markdown", "markdown", "format_status"),
        ("json", "json", "status_data")
    ])
    def test_display_status_shows_current_position(self, tmp_path, mode, helper_attr, method_name):
        """
        SCENARIO: Display status shows current position (all channels)
        GIVEN: CLI at exploration.validate
        WHEN: user enters 'status'
        THEN: CLI displays complete status with current position marked
              Output matches expected channel format
        """
        # GIVEN
        helper = BotTestHelper(tmp_path)
        helper.state.set_state('exploration', 'validate')
        
        cli_session = CLISession(
            bot=helper.bot, 
            workspace_directory=helper.workspace, 
            mode=mode
        )
        
        # WHEN
        cli_response = cli_session.execute_command('status')
        
        # THEN: Channel assertion
        channel_helper = getattr(helper, helper_attr)
        get_expected = getattr(channel_helper, method_name)
        expected = get_expected('exploration', 'validate')
        
        assert cli_response.output.strip() == expected.strip()
```

## Test Mapping

### Domain Test → CLI Test Mapping

| Domain Test File | Domain Class | CLI Test File | CLI Class | Key Difference |
|-----------------|--------------|---------------|-----------|----------------|
| `test_navigate_and_execute_behaviors.py` | `TestManageBehaviors` | N/A | N/A | Pure domain logic, no CLI interface |
| `test_navigate_and_execute_behaviors.py` | `TestNavigateToBehavior` | `test_navigate_behaviors_using_cli_commands.py` | `TestNavigateToBehaviorUsingCLI` | CLI adds command parsing + 3 channels |
| `test_navigate_and_execute_behaviors.py` | `TestNavigateSequentially` | `test_navigate_behaviors_using_cli_commands.py` | `TestNavigateSequentiallyUsingCLI` | CLI adds next/back commands |
| N/A | N/A | `test_navigate_behaviors_using_cli_commands.py` | `TestDisplayBotStatusUsingCLI` | CLI-specific story |

### Test Scenario Mapping (Navigate Behaviors Area)

| Domain Scenario | Domain Test Method | CLI Scenario | CLI Test Method | Parameterized? |
|----------------|-------------------|-------------|----------------|----------------|
| Navigate to behavior updates current | `test_behaviors_navigate_to_behavior_updates_current_behavior` | Navigate with behavior name via CLI | `test_navigate_to_behavior_by_name` | ✅ Yes (TTY/Pipe/JSON) |
| Execute behavior with action parameter | `test_execute_behavior_with_action_parameter` | Navigate with dot notation via CLI | `test_navigate_with_dot_notation` | ✅ Yes (TTY/Pipe/JSON) |
| Navigate to invalid behavior shows error | `test_navigate_to_invalid_behavior_raises_error` | Navigate to invalid behavior shows CLI error | `test_navigate_to_invalid_behavior_shows_error` | ✅ Yes (TTY/Pipe/JSON) |
| Navigate to next action | `test_navigate_to_next_action` | Navigate with 'next' command | `test_navigate_with_next_command` | ✅ Yes (TTY/Pipe/JSON) |
| Navigate to previous action | `test_navigate_to_previous_action` | Navigate with 'back' command | `test_navigate_with_back_command` | ✅ Yes (TTY/Pipe/JSON) |
| N/A (domain checks state directly) | N/A | Display status shows current position | `test_display_status_shows_current_position` | ✅ Yes (TTY/Pipe/JSON) |

### Test Scenario Mapping (Execute Actions Area)

| Domain Scenario | Domain Test Method | CLI Scenario | CLI Test Method | Parameterized? |
|----------------|-------------------|-------------|----------------|----------------|
| Execute current action | `test_execute_current_action_runs_action` | Execute action via CLI 'run' command | `test_execute_action_via_run_command` | ✅ Yes (TTY/Pipe/JSON) |
| Execute with scope | `test_execute_with_scope_applies_filters` | Execute with --scope parameter | `test_execute_with_scope_parameter` | ✅ Yes (TTY/Pipe/JSON) |
| Execute shows instructions | `test_execute_shows_instructions` | CLI shows instructions after execute | `test_cli_shows_instructions_after_execute` | ✅ Yes (TTY/Pipe/JSON) |

### Test Scenario Mapping (Manage Scope Area)

| Domain Scenario | Domain Test Method | CLI Scenario | CLI Test Method | Parameterized? |
|----------------|-------------------|-------------|----------------|----------------|
| Set scope to story | `test_set_scope_to_story` | Set scope via 'scope set' command | `test_scope_set_command` | ✅ Yes (TTY/Pipe/JSON) |
| Clear scope | `test_clear_scope` | Clear scope via 'scope clear' command | `test_scope_clear_command` | ✅ Yes (TTY/Pipe/JSON) |
| Display scope | `test_display_current_scope` | Display scope via 'scope' command | `test_scope_display_command` | ✅ Yes (TTY/Pipe/JSON) |

### Test Scenario Mapping (Get Help Area)

| Domain Scenario | Domain Test Method | CLI Scenario | CLI Test Method | Parameterized? |
|----------------|-------------------|-------------|----------------|----------------|
| N/A (domain has no help system) | N/A | Display help for all commands | `test_help_shows_all_commands` | ✅ Yes (TTY/Pipe/JSON) |
| N/A | N/A | Display help for specific command | `test_help_shows_command_details` | ✅ Yes (TTY/Pipe/JSON) |

### Test Scenario Mapping (Initialize Session Area)

| Domain Scenario | Domain Test Method | CLI Scenario | CLI Test Method | Parameterized? |
|----------------|-------------------|-------------|----------------|----------------|
| Bot loads configuration | `test_bot_loads_configuration_on_init` | CLI session initializes bot | `test_cli_session_initializes_bot` | ✅ Yes (TTY/Pipe/JSON) |
| Bot loads behaviors | `test_bot_loads_behaviors_on_init` | CLI session loads behaviors | `test_cli_session_loads_behaviors` | ✅ Yes (TTY/Pipe/JSON) |
| Bot restores state | `test_bot_restores_previous_state` | CLI session restores state | `test_cli_session_restores_state` | ✅ Yes (TTY/Pipe/JSON) |
| N/A (domain doesn't have mode) | N/A | CLI detects TTY mode automatically | `test_cli_detects_tty_mode` | ❌ No (TTY-specific) |
| N/A | N/A | CLI detects pipe mode automatically | `test_cli_detects_pipe_mode` | ❌ No (Pipe-specific) |
| N/A | N/A | CLI accepts JSON mode flag | `test_cli_accepts_json_mode_flag` | ❌ No (JSON-specific) |

### Complete Area Mapping

| Area | Current CLI File | Current Lines | New CLI File | Estimated Lines | Stories |
|------|-----------------|---------------|--------------|-----------------|---------|
| Navigate Behaviors | `test_navigate_behaviors_using_cli_commands.py` | 1316 | `test_navigate_behaviors_using_cli_commands.py` | ~400 | 3 |
| Initialize Session | `test_initialize_cli_session.py` | 631 | `test_initialize_cli_session.py` | ~250 | 4 |
| Execute Actions | `test_execute_actions_using_cli.py` | 612 | `test_execute_actions_using_cli.py` | ~300 | 2 |
| Manage Scope | `test_manage_scope_using_cli.py` | 475 | `test_manage_scope_using_cli.py` | ~200 | 1 |
| Get Help | `test_get_help_using_cli.py` | 300 | `test_get_help_using_cli.py` | ~150 | 1 |

### Helper Migration

| Current Helper (duplicated) | New Helper Location | Consolidation |
|---------------------------|-------------------|---------------|
| `assert_valid_json()` in 5 files | `JsonBotTestHelper` (internal method) | 5 → 1 |
| `extract_status_section()` in 3 files | `TTYBotTestHelper.display_status()` | 3 → 1 |
| `extract_footer_section()` in 3 files | Part of `display_status()` | 3 → 0 |
| `create_story_graph_with_multiple_results()` in 2 files | `StoryTestHelper.create_story_graph()` | 2 → 1 |

## Rule Compliance Matrix

| Rule | Before Migration | After Migration | Compliance |
|------|-----------------|----------------|------------|
| **assert_full_results** | `assert '➤' in output` | `assert output == expected` | ✅ PASS |
| **object_oriented_test_helpers** | Inline parsing functions | `helper.tty.display_status()` | ✅ PASS |
| **standard_test_data_sets** | Ad-hoc assertions | Standard channel outputs | ✅ PASS |
| **helper_extraction_and_reuse** | Duplicate functions × 5 | Single shared helpers | ✅ PASS |
| **use_class_based_organization** | `TestNavigateInTTYMode` | `TestNavigateToBehaviorUsingCLI` | ✅ PASS |
| **consistent_vocabulary** | Mixed terms | Channel-appropriate verbs | ✅ PASS |
| **use_domain_language** | Generic terms | `display`, `format`, `data` by channel | ✅ PASS |

## Complete File Inventory

### New Files to Create

| File | Type | Lines | Purpose |
|------|------|-------|---------|
| `agile_bot/test/CLI/helpers/cli_bot_test_helper.py` | Base Helper | ~30 | Base class for all CLI helpers, creates domain helper + CLI session |
| `agile_bot/test/CLI/helpers/tty_bot_test_helper.py` | Channel Helper | ~200 | TTY channel helper + 5 sub-helpers with 17 assertion methods |
| `agile_bot/test/CLI/helpers/pipe_bot_test_helper.py` | Channel Helper | ~200 | Pipe channel helper + 5 sub-helpers with 17 assertion methods |
| `agile_bot/test/CLI/helpers/json_bot_test_helper.py` | Channel Helper | ~200 | JSON channel helper + 5 sub-helpers with 17 assertion methods |
| `agile_bot/test/CLI/helpers/__init__.py` | Module Init | ~10 | Export all CLI helpers |
| `agile_bot/test/domain/helpers/navigation_helper.py` | Domain Helper | ~50 | Navigation operations (domain, not CLI-specific) |
| **TOTAL** | **6 new files** | **~690 lines** | **Complete CLI test infrastructure** |

### Files to Update

| File | Type | Changes | Impact |
|------|------|---------|--------|
| `agile_bot/test/domain/bot_test_helper.py` | Domain Helper | Add `self.navigation = NavigationTestHelper(parent=self)` | +1 line |
| `agile_bot/test/CLI/test_navigate_behaviors_using_cli_commands.py` | Test File | Replace ~1316 lines with ~400 parameterized tests | -916 lines |
| `agile_bot/test/CLI/test_initialize_cli_session.py` | Test File | Replace ~631 lines with ~250 parameterized tests | -381 lines |
| `agile_bot/test/CLI/test_execute_actions_using_cli.py` | Test File | Replace ~612 lines with ~300 parameterized tests | -312 lines |
| `agile_bot/test/CLI/test_manage_scope_using_cli.py` | Test File | Replace ~475 lines with ~200 parameterized tests | -275 lines |
| `agile_bot/test/CLI/test_get_help_using_cli.py` | Test File | Replace ~300 lines with ~150 parameterized tests | -150 lines |
| **TOTAL** | **6 files updated** | **Replace ~3334 lines with ~1300 lines** | **-2034 lines** |

### Helper Method Summary

| Helper Class | Sub-Helper | Methods | Method Signatures Identical Across Channels? |
|-------------|------------|---------|---------------------------------------------|
| `TTYBotTestHelper` | `TTYBotHelper` | 5 | ✅ Yes (TTY/Pipe/JSON) |
| | `TTYInstructionsHelper` | 3 | ✅ Yes |
| | `TTYNavigationHelper` | 4 | ✅ Yes |
| | `TTYScopeHelper` | 3 | ✅ Yes |
| | `TTYHelpHelper` | 2 | ✅ Yes |
| `PipeBotTestHelper` | `PipeBotHelper` | 5 | ✅ Yes (identical to TTY) |
| | `PipeInstructionsHelper` | 3 | ✅ Yes |
| | `PipeNavigationHelper` | 4 | ✅ Yes |
| | `PipeScopeHelper` | 3 | ✅ Yes |
| | `PipeHelpHelper` | 2 | ✅ Yes |
| `JsonBotTestHelper` | `JsonBotHelper` | 5 | ✅ Yes (identical to TTY/Pipe) |
| | `JsonInstructionsHelper` | 3 | ✅ Yes |
| | `JsonNavigationHelper` | 4 | ✅ Yes |
| | `JsonScopeHelper` | 3 | ✅ Yes |
| | `JsonHelpHelper` | 2 | ✅ Yes |
| **TOTAL** | **15 sub-helper classes** | **51 assertion methods** | **All identical signatures** |

### Test Count Summary

| Test Area | Current Tests (TTY/Pipe/JSON separate) | New Tests (Parameterized) | Reduction |
|-----------|----------------------------------------|---------------------------|-----------|
| Navigate Behaviors | ~20 × 3 = 60 test methods | ~20 parameterized = 20 methods | -67% methods |
| Initialize Session | ~15 × 3 = 45 test methods | ~15 parameterized = 15 methods | -67% methods |
| Execute Actions | ~12 × 3 = 36 test methods | ~12 parameterized = 12 methods | -67% methods |
| Manage Scope | ~8 × 3 = 24 test methods | ~8 parameterized = 8 methods | -67% methods |
| Get Help | ~6 × 3 = 18 test methods | ~6 parameterized = 6 methods | -67% methods |
| **TOTAL** | **~183 test methods** | **~61 test methods** | **-67% duplication eliminated** |

## Implementation Phases

### Phase 0: Extract NavigationTestHelper (Prerequisite)

**Why:** Navigation logic is currently scattered in domain tests. Extract to dedicated helper before CLI migration.

**Create:** `agile_bot/test/domain/helpers/navigation_helper.py`

```python
"""Navigation Test Helper - Domain navigation logic"""
from .base_helper import BaseTestHelper

class NavigationTestHelper(BaseTestHelper):
    """Helper for navigation operations - format-agnostic"""
    
    def navigate_to(self, behavior: str, action: str):
        """Navigate bot to specific behavior and action"""
        self.bot.behaviors.navigate_to(behavior)
        self.bot.behaviors.current.actions.navigate_to(action)
    
    def navigate_next(self):
        """Navigate to next action in workflow"""
        return self.bot.next()
    
    def navigate_back(self):
        """Navigate to previous action in workflow"""
        return self.bot.back()
    
    def assert_at_position(self, behavior: str, action: str):
        """Assert bot is at specific behavior/action"""
        assert self.bot.behaviors.current.name == behavior
        assert self.bot.behaviors.current.actions.current.action_name == action
```

**Update:** `agile_bot/test/domain/bot_test_helper.py`
```python
from agile_bot.test.domain.helpers import NavigationTestHelper

class BotTestHelper:
    def __init__(self, tmp_path: Path, workspace_directory: Path = None, bot_directory: Path = None):
        # ... existing initialization ...
        
        # Domain helpers
        self.state = StateTestHelper(parent=self)
        self.behaviors = BehaviorTestHelper(parent=self)
        self.navigation = NavigationTestHelper(parent=self)  # ADD
        self.scope = ScopeTestHelper(parent=self)
        # ... etc ...
```

**Refactor:** Update existing domain tests to use `helper.navigation.*` instead of direct bot calls.

---

### Phase 1: Create Foundation (1 story area - Navigate Behaviors)

**Goal:** Establish pattern with one complete area

**Steps:**
1. Create `agile_bot/test/domain/helpers/navigation_helper.py`
   - 4 methods: `navigate_to()`, `navigate_next()`, `navigate_back()`, `assert_at_position()`
   - Update `bot_test_helper.py` to add `self.navigation = NavigationTestHelper(parent=self)`

2. Create `agile_bot/test/CLI/helpers/cli_bot_test_helper.py`
   - Base class with `__init__(tmp_path, mode)`
   - Creates `self.domain = BotTestHelper(tmp_path)`
   - Creates `self.cli_session = CLISession(..., mode=mode)`

3. Create `agile_bot/test/CLI/helpers/tty_bot_test_helper.py`
   - `TTYBotTestHelper(CLIBotTestHelper)` with 5 sub-helpers
   - Implement 17 assertion methods across sub-helpers
   - Focus on Navigate Behaviors methods first

4. Create `agile_bot/test/CLI/helpers/pipe_bot_test_helper.py`
   - `PipeBotTestHelper(CLIBotTestHelper)` with 5 sub-helpers
   - IDENTICAL method signatures to TTY
   - Internal checks for markdown formatting

5. Create `agile_bot/test/CLI/helpers/json_bot_test_helper.py`
   - `JsonBotTestHelper(CLIBotTestHelper)` with 5 sub-helpers
   - IDENTICAL method signatures to TTY/Pipe
   - Internal checks parse JSON and validate fields

6. Create `agile_bot/test/CLI/helpers/__init__.py`
   - Export all 4 helpers

7. Update `test_navigate_behaviors_using_cli_commands.py`
   - Replace existing 3 classes (TTY/Pipe/JSON separate) with parameterized tests
   - ~1316 lines → ~400 lines
   - 3 test classes: `TestNavigateToBehaviorUsingCLI`, `TestNavigateSequentiallyUsingCLI`, `TestDisplayBotStatusUsingCLI`
   - ~20 test methods (each parameterized across 3 channels)

8. Run tests and validate
   - `pytest agile_bot/test/CLI/test_navigate_behaviors_using_cli_commands.py -v`
   - Should run ~60 test combinations (20 methods × 3 channels)
   - All should pass

**Deliverable:** Navigate Behaviors area complete with working parameterized tests

---

### Phase 2: Expand to Remaining Areas

**Goal:** Apply proven pattern to remaining 4 test areas

**Steps:**

1. **Initialize Session Area** (~631 → ~250 lines)
   - Add session-specific methods to helpers (if needed)
   - Update `test_initialize_cli_session.py` with parameterized tests
   - 4 story classes, ~15 test methods
   - Run and validate

2. **Execute Actions Area** (~612 → ~300 lines)
   - Add execution-specific methods to helpers (if needed)
   - Update `test_execute_actions_using_cli.py` with parameterized tests
   - 2 story classes, ~12 test methods
   - Run and validate

3. **Manage Scope Area** (~475 → ~200 lines)
   - Scope methods already in helpers from Phase 1
   - Update `test_manage_scope_using_cli.py` with parameterized tests
   - 1 story class, ~8 test methods
   - Run and validate

4. **Get Help Area** (~300 → ~150 lines)
   - Help methods already in helpers from Phase 1
   - Update `test_get_help_using_cli.py` with parameterized tests
   - 1 story class, ~6 test methods
   - Run and validate

**Deliverable:** All 5 CLI test areas migrated and passing

---

### Phase 3: Validation and Cleanup

**Goal:** Ensure quality and consistency

**Steps:**

1. Run full CLI test suite
   - `pytest agile_bot/test/CLI/ -v`
   - Should show ~61 test methods running
   - Each parameterized across 3 channels = ~183 total test runs
   - All should pass

2. Validate rule compliance
   - Run validation against 25 test rules
   - Check for violations
   - Fix any issues found

3. Update documentation
   - Update test README if exists
   - Document helper usage patterns
   - Add examples for future test writers

4. Code review and finalize
   - Review all helper code for consistency
   - Ensure all method signatures identical across channels
   - Verify parameterization works correctly
   - Check error messages are clear

**Deliverable:** Complete, validated, rule-compliant CLI test suite

---

### Success Criteria

- ✅ All 6 new files created (~690 lines)
- ✅ All 6 test files updated (~3334 → ~1300 lines, -61%)
- ✅ All 51 assertion methods implemented with identical signatures
- ✅ All ~61 test methods parameterized across 3 channels
- ✅ All ~183 test combinations passing
- ✅ All 25 test rules compliant
- ✅ No code duplication (5 duplicated helpers → 1 each)
- ✅ Clear, maintainable test code

## Benefits Summary

### Code Reduction
- **Before:** ~3,334 lines across 5 files (with duplication)
- **After:** ~1,300 lines across 5 files (no duplication)
- **Reduction:** ~61% fewer lines

### Architecture Improvements
1. **Mirrors production structure** - Test helpers parallel production adapters
2. **Channel-appropriate verbs** - TTY uses `display`, Markdown uses `format`, JSON uses `data`
3. **Same-level helpers** - Channel helpers at same level as domain helpers
4. **Single source of truth** - Each helper defines expected output once
5. **Parameterized by channel** - Test logic written once, runs for 3 channels

### Testing Improvements
1. **Comprehensive coverage** - Full output validation, not partial
2. **Clear separation** - Domain logic vs. channel formatting
3. **Better error messages** - Full diff on mismatch shows exact formatting issue
4. **Faster test writing** - Reuse helpers, parameterize channels
5. **Consistent vocabulary** - Each channel uses appropriate domain language

## Example: Before vs After

### Before (Current Pattern)

```python
class TestNavigateToBehaviorActionAndExecuteInTTYMode:
    def test_user_navigates_with_behavior_only(self, tmp_path):
        # Setup (15 lines)
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # Execute
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('discovery')
        
        # Assert (20+ lines of cherry-picked assertions)
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        assert 'discovery' in output
        assert 'INSTRUCTIONS' in output
        assert '➤' in status_section
        # ... more cherry-picking ...

class TestNavigateToBehaviorActionAndExecuteInPipeMode:
    def test_user_navigates_with_behavior_only(self, tmp_path):
        # Duplicate with mode='markdown' and different assertions
        pass

class TestNavigateToBehaviorActionAndExecuteInJSONMode:
    def test_user_navigates_with_behavior_only(self, tmp_path):
        # Duplicate with mode='json' and different assertions
        pass
```

### After (New Pattern)

```python
class TestNavigateToBehaviorUsingCLI:
    @pytest.mark.parametrize("mode,helper_attr,method_name", [
        ("tty", "tty", "show_navigation_success"),
        ("markdown", "markdown", "format_navigation_success"),
        ("json", "json", "navigation_result")
    ])
    def test_navigate_to_behavior_by_name(self, tmp_path, mode, helper_attr, method_name):
        # Setup (3 lines)
        helper = BotTestHelper(tmp_path)
        helper.state.set_state('shape', 'clarify')
        cli_session = CLISession(bot=helper.bot, workspace_directory=helper.workspace, mode=mode)
        
        # Execute (1 line)
        cli_response = cli_session.execute_command('discovery')
        
        # Assert (5 lines - full output comparison)
        helper.behaviors.assert_at_behavior_action('discovery', 'clarify')
        channel_helper = getattr(helper, helper_attr)
        get_expected = getattr(channel_helper, method_name)
        expected = get_expected('discovery', 'clarify')
        assert cli_response.output.strip() == expected.strip()
```

**Result:**
- 3 test classes → 1 test class
- ~100 lines → ~15 lines
- Cherry-picked assertions → Full output validation
- Duplicated code → Parameterized test
- Generic naming → Channel-appropriate verbs

## Next Steps

1. **Review this plan** - Confirm architecture mirrors production
2. **Start Phase 1** - Implement Navigate Behaviors area
3. **Validate approach** - Run tests, ensure channel helpers work correctly
4. **Expand to remaining areas** - Apply same pattern to other CLI test files

## Domain Stories vs CLI Channel Stories - Examples

### EXAMPLE: Domain Test Pattern (Existing)

**Domain Test Class:** `TestNavigateToBehaviorActionAndExecute`

```python
class TestNavigateToBehaviorActionAndExecute:

    def test_execute_behavior_with_action_parameter(self, tmp_path):
        """
        SCENARIO: Execute behavior with action parameter
        GIVEN: Bot has behavior 'shape' with action 'clarify'
        WHEN: Bot.execute_behavior('shape', action='clarify') is called
        THEN: Action executes and returns BotResult
        """
        # Given: Bot with shape behavior
        helper = BotTestHelper(tmp_path)
        helper.state.set_state('shape', 'clarify')
        
        # When: Execute behavior with action parameter
        bot_result = helper.bot.execute('shape', action_name='clarify')
        
        # Then: Action executes successfully with complete structure
        helper.behaviors.assert_bot_result_success(bot_result, 'shape', 'clarify')
```

**Domain Pattern:**
1. ✅ Setup with `helper.state.set_state()` 
2. ✅ Execute domain operation: `helper.bot.execute()`
3. ✅ Assert with helper: `helper.behaviors.assert_bot_result_success()`

---

### EXAMPLE: CLI Test Pattern (New - Following Domain Pattern)

**CLI Test Class:** `TestNavigateToBehaviorUsingCLI`

```python
class TestNavigateToBehaviorUsingCLI:

    def test_navigate_to_behavior_via_cli_tty(self, tmp_path):
        """
        SCENARIO: Navigate to behavior via CLI (TTY mode)
        GIVEN: CLI session at shape.clarify
        WHEN: User enters 'discovery' command
        THEN: CLI outputs navigation result in TTY format
        """
        # Given: Bot with state + TTY helper (helper provides cli_session)
        helper = BotTestHelper(tmp_path)
        helper.state.set_state('shape', 'clarify')
        
        tty_helper = TTYBotTestHelper(helper)
        
        # When: Execute CLI command directly via helper's cli_session (production code)
        cli_response = tty_helper.cli_session.execute_command('discovery')
        
        # Then: Assert domain state (reuse domain helper)
        helper.behaviors.assert_at_behavior_action('discovery', 'clarify')
        
        # And: Assert TTY format (use TTY helper - pass output + expected values)
        tty_helper.assert_instructions_section_shows_behavior_and_action(
            cli_response.output, 'discovery', 'clarify')
        tty_helper.assert_current_position_shows(
            cli_response.output, 'discovery', 'clarify')  # Comprehensive: status + marker + footer
```

**CLI Pattern (Same as Domain):**
1. ✅ Setup with `helper.state.set_state()` + create `tty_helper` (which creates cli_session)
2. ✅ Execute operation: `tty_helper.cli_session.execute_command()` (call production code directly)
3. ✅ Assert with helpers: `helper.behaviors.assert_*()` + `tty_helper.assert_*()` 

---

### EXAMPLE: TTYBotTestHelper Implementation

```python
class TTYBotTestHelper(BaseTestHelper):
    """Helper for TTY CLI output assertions - provides cli_session but doesn't wrap execute_command"""
    
    def __init__(self, bot_test_helper):
        """Initialize with domain helper - creates CLISession for convenience"""
        self.domain = bot_test_helper
        self.cli_session = CLISession(
            bot=bot_test_helper.bot,
            workspace_directory=bot_test_helper.workspace,
            mode='tty'
        )
    
    def assert_instructions_section_shows_behavior_and_action(self, output: str, behavior: str, action: str):
        """
        Assert TTY INSTRUCTIONS section shows correct behavior and action headers.
        
        Checks for:
        - "INSTRUCTIONS" section exists
        - "Behavior Instructions - {behavior}" header
        - "Action Instructions - {action}" header
        """
        assert 'INSTRUCTIONS' in output, "Missing INSTRUCTIONS section in TTY output"
        assert f'Behavior Instructions - {behavior}' in output, \
            f"Missing 'Behavior Instructions - {behavior}' header"
        assert f'Action Instructions - {action}' in output, \
            f"Missing 'Action Instructions - {action}' header"
    
    def assert_current_position_shows(self, output: str, behavior: str, action: str):
        """
        Assert TTY output shows COMPLETE current position display.
        
        Comprehensive check including:
        - "CLI STATUS section" exists
        - "Current Position:" label
        - "{behavior}.{action}" value
        - "➤" current position marker
        - "Behaviors:" and "Actions:" footer labels
        - Bolded behavior/action names (ANSI codes: \x1b[1m{name}\x1b[0m)
        """
        # Status section with position
        assert 'CLI STATUS section' in output, "Missing CLI STATUS section"
        assert 'Current Position:' in output, "Missing 'Current Position:' label"
        assert f'{behavior}.{action}' in output, \
            f"Missing position '{behavior}.{action}' in status"
        
        # Current marker
        assert '➤' in output, "Missing current position marker '➤'"
        
        # Emphasized footer
        assert 'Behaviors:' in output, "Missing 'Behaviors:' label in footer"
        assert 'Actions:' in output, "Missing 'Actions:' label in footer"
        
        behavior_bolded = (f'\x1b[1m{behavior}\x1b[0m' in output or 
                          f'[1m{behavior}[0m' in output)
        assert behavior_bolded, f"Behavior '{behavior}' not bolded in footer"
        
        action_bolded = (f'\x1b[1m{action}\x1b[0m' in output or 
                        f'[1m{action}[0m' in output)
        assert action_bolded, f"Action '{action}' not bolded in footer"
```

**Key Points:**
- ✅ Helper creates `cli_session` internally (convenience - avoids repeating parameters)
- ✅ Test directly calls `tty_helper.cli_session.execute_command()` (production code, not wrapped)
- ✅ Helper provides `assert_*()` methods (like `behaviors.assert_bot_result_success()`)
- ✅ Each assert method checks COMPLETE structure, not cherry-picking
- ✅ Clear error messages showing what's missing

**Pattern Matches Domain:**
- `helper.state.set_state()` → creates test state
- `tty_helper.cli_session.execute_command()` → call production code directly (helper provides session, doesn't wrap call)
- `helper.behaviors.assert_*()` → asserts domain state
- `tty_helper.assert_*()` → asserts TTY output format

---

## Quick Reference: Writing CLI Tests

### Test Template (Parameterized)

```python
class TestYourStoryUsingCLI:
    """
    Story: Your Story Name
    
    Domain logic: test_domain_file.py::TestYourStoryDomain
    CLI focus: Command parsing and channel output
    """
    
    @pytest.mark.parametrize("helper_class", [
        TTYBotTestHelper,
        PipeBotTestHelper,
        JsonBotTestHelper
    ])
    def test_your_scenario(self, tmp_path, helper_class):
        """
        SCENARIO: Your scenario description
        GIVEN: Initial state
        WHEN: User action
        THEN: Expected outcome
        """
        # Given - Setup domain state
        helper = helper_class(tmp_path)  # Creates domain helper internally
        helper.domain.state.set_state('shape', 'clarify')
        
        # When - Execute CLI command (production code)
        cli_response = helper.cli_session.execute_command('your_command')
        
        # Then - Assert domain (format-agnostic)
        helper.domain.behaviors.assert_at_behavior_action('expected_behavior', 'expected_action')
        
        # And - Assert CLI output (channel-specific, but identical method signature)
        helper.navigation.assert_current_position_shows(cli_response.output, 'expected_behavior', 'expected_action')
        helper.instructions.assert_section_shows_behavior_and_action(cli_response.output, 'expected_behavior', 'expected_action')
```

### Helper Method Patterns

**Domain Assertions (format-agnostic):**
```python
helper.domain.state.assert_state_saved(behavior, action)
helper.domain.behaviors.assert_at_behavior_action(behavior, action)
helper.domain.behaviors.assert_bot_result_success(result, behavior, action)
```

**CLI Assertions (channel-specific, identical signatures):**
```python
# All channels have these with IDENTICAL signatures:
helper.bot.assert_status_section_present(output)
helper.instructions.assert_section_shows_behavior_and_action(output, behavior, action)
helper.navigation.assert_current_position_shows(output, behavior, action)
helper.scope.assert_scope_shows_target(output, scope_type, target)
helper.help.assert_help_shows_available_commands(output)
```

### Key Principles

1. **Parameterize by channel** - Write test once, runs for TTY/Pipe/JSON
2. **Identical method signatures** - All channels have same assertion methods
3. **Internal differences** - Each channel checks different things internally (ANSI/Markdown/JSON)
4. **Domain first** - Assert domain state, then CLI output
5. **Call production code directly** - Don't wrap `execute_command()` in helpers
6. **Comprehensive assertions** - Check complete structures, not cherry-picked fields

### Common Mistakes to Avoid

❌ **Don't create separate test methods per channel:**
```python
def test_navigate_tty(self): ...
def test_navigate_pipe(self): ...
def test_navigate_json(self): ...
```

✅ **Do parameterize:**
```python
@pytest.mark.parametrize("helper_class", [TTYBotTestHelper, PipeBotTestHelper, JsonBotTestHelper])
def test_navigate(self, tmp_path, helper_class): ...
```

❌ **Don't cherry-pick fields:**
```python
assert '➤' in output
assert 'discovery' in output
```

✅ **Do use comprehensive helpers:**
```python
helper.navigation.assert_current_position_shows(output, 'discovery', 'clarify')
```

❌ **Don't use different method names per channel:**
```python
tty_helper.show_navigation_success()
pipe_helper.format_navigation_result()
json_helper.navigation_data()
```

✅ **Do use identical method names:**
```python
helper.navigation.assert_current_position_shows()  # Works for all channels
```

---

## Questions for Review

1. ✅ Channel helpers mirror production adapter structure?
2. ✅ Each helper at same level (tty, markdown, json)?
3. ✅ Channel-appropriate verbs (display/format/data)?
4. ✅ Methods return hard-coded expected strings?
5. ✅ Parameterize tests by channel?
6. ✅ Assert full output strings, not cherry-picked fields?
7. ✅ NavigationTestHelper extracted as domain helper first?
8. ✅ All method signatures identical across channels?
9. ✅ CLI helpers create domain helper internally?
10. ✅ Tests call production code directly (no wrappers)?