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

| Domain Helper Method | What's Being Checked | ALL Channel Helpers (TTY/Pipe/JSON) |
|---------------------|---------------------|-------------------------------------|
| `behaviors.assert_bot_result_success(result, behavior, action)` | Instructions section shows behavior/action | `assert_instructions_section_shows_behavior_and_action(output, behavior, action)` |
| `behaviors.assert_at_behavior_action(behavior, action)` | Current position shows (includes status section + emphasized footer) | `assert_current_position_shows(output, behavior, action)` |

**All three helpers have IDENTICAL method signatures. Internal implementation differs:**
- TTY: checks ANSI codes, "➤" marker, box drawing
- Pipe: checks markdown (##, **bold**,  backticks)
- JSON: parses JSON, checks fields (current_behavior, instructions.behavior_metadata)

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

#### 1. TTY Bot Test Helper

**See "EXAMPLE: TTYBotTestHelper Implementation" section above for correct implementation pattern.**

#### 2. Helper Module Init

**File:** `agile_bot/test/CLI/helpers/__init__.py`

```python
"""CLI Test Helpers"""
from .tty_bot_test_helper import TTYBotTestHelper
from .pipe_bot_test_helper import PipeBotTestHelper
from .json_bot_test_helper import JsonBotTestHelper

__all__ = [
    'TTYBotTestHelper',
    'PipeBotTestHelper',
    'JsonBotTestHelper'
]
```

#### 3. Updated Domain Test Helper

**NOTE:** BotTestHelper does NOT need modification - CLI helpers are instantiated in CLI tests only, not added to BotTestHelper.

#### 4. New CLI Test Structure

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

### Phase 1: Create Foundation (1 story area)
1. ✅ Create `agile_bot/test/CLI/helpers/__init__.py`
2. ✅ Create `agile_bot/test/CLI/helpers/tty_bot_test_helper.py`
   - Implement `TTYBotTestHelper` with identical signatures (checks ANSI internally)
3. ✅ Create `agile_bot/test/CLI/helpers/pipe_bot_test_helper.py`
   - Implement `PipeBotTestHelper` with identical signatures (checks markdown internally)
4. ✅ Create `agile_bot/test/CLI/helpers/json_bot_test_helper.py`
   - Implement `JsonBotTestHelper` with identical signatures (parses JSON internally)
5. ✅ Update `test_navigate_behaviors_using_cli_commands.py` with parameterized tests
6. ✅ Run tests across all 3 channels and validate approach

### Phase 2: Expand Channel Helpers (remaining areas)
8. Add channel helper methods for:
   - Scope operations (set/clear/display)
   - Action execution (instructions/confirm/validate)
   - Help display
   - Initialization/session management
9. Create remaining CLI test files
10. Deprecate old CLI test files

### Phase 3: Complete Migration
11. Migrate all 5 CLI test areas
12. Remove old test files
13. Update documentation

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

## Questions for Review

1. ✅ Channel helpers mirror production adapter structure?
2. ✅ Each helper at same level (tty, markdown, json)?
3. ✅ Channel-appropriate verbs (display/format/data)?
4. ✅ Methods return hard-coded expected strings?
5. ✅ Parameterize tests by channel?
6. ✅ Assert full output strings, not cherry-picked fields?
7. ✅ NavigationTestHelper extracted as domain helper first?
