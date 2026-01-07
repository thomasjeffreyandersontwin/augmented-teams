# Test Plan: Invoke Bot Directly

## 📋 Overview

**Goal:** Build comprehensive tests for "Invoke Bot Directly" stories by:
1. Extracting core domain logic tests from REPL tests
2. Creating common test helpers for bot setup
3. Refactoring REPL tests to delegate to domain logic

## 🎯 Architecture Principles

### Test Hierarchy
```
┌─────────────────────────────────────────────────────────┐
│ test_invoke_bot_directly.py                             │
│ Tests CORE DOMAIN LOGIC (Bot, Behaviors, Actions)       │
│ - bot.behaviors.navigate_to(behavior_name)              │
│ - bot.behaviors.current.actions.close_current()         │
│ - bot.execute_behavior(behavior, action)                │
└─────────────────────────────────────────────────────────┘
                        ▲
                        │ delegates to
                        │
┌─────────────────────────────────────────────────────────┐
│ test_navigate_behaviors_using_repl_commands.py          │
│ Tests REPL COMMAND PARSING & DELEGATION                 │
│ - repl_session.read_and_execute_command('discovery')    │
│ - repl_session.read_and_execute_command('next')         │
│ - repl_session.read_and_execute_command('back')         │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ test_navigate_behaviors_using_domain_model.py           │
│ ALREADY CORRECT - Tests domain model directly           │
│ (Keep as is - this is the reference implementation)     │
└─────────────────────────────────────────────────────────┘
```

## 📝 Phase 1: Create Common Test Helpers

### File: `agile_bot/bots/base_bot/test/test_invoke_bot_helpers.py`

Create centralized helpers for bot setup that both Direct and REPL tests will use.

**Purpose:** DRY principle - setup bot once, reuse everywhere

**Common Helpers Needed:**

```python
# ============================================================================
# BOT SETUP HELPERS - Used by Direct and REPL tests
# ============================================================================

def setup_test_bot(tmp_path, behaviors: list[str]) -> tuple[Bot, Path]:
    """
    Setup test bot with behaviors for Invoke Bot tests.
    
    Returns: (bot, workspace_dir)
    
    Used by:
    - test_invoke_bot_directly.py (Direct invocation)
    - test_navigate_behaviors_using_repl_commands.py (REPL commands)
    - test_navigate_behaviors_using_domain_model.py (Domain model)
    
    Args:
        tmp_path: pytest tmp_path fixture
        behaviors: List of behavior names to create (e.g., ['shape', 'discovery'])
    
    Returns:
        tuple: (Bot instance, workspace_directory Path)
        
    Example:
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
        bot.behaviors.navigate_to('shape')
    """
    bot_dir = tmp_path / 'agile_bot' / 'bots' / 'story_bot'
    workspace_dir = tmp_path / 'workspace'
    bot_dir.mkdir(parents=True, exist_ok=True)
    workspace_dir.mkdir(parents=True, exist_ok=True)

    create_base_actions_structure(bot_dir)
    create_bot_config_file(bot_dir, 'story_bot', behaviors)

    for idx, behavior_name in enumerate(behaviors, start=1):
        create_actions_workflow_json(bot_dir, behavior_name, order=idx)
        create_minimal_guardrails_files(bot_dir, behavior_name, 'story_bot')

    bootstrap_env(bot_dir, workspace_dir)
    bot = Bot(
        bot_name='story_bot',
        bot_directory=bot_dir,
        config_path=bot_dir / 'bot_config.json'
    )
    return bot, workspace_dir


def create_behavior_action_state(workspace_dir: Path, bot_name: str, 
                                  behavior: str, action: str,
                                  operation: str = 'instructions') -> Path:
    """
    Create behavior_action_state.json file with specified state.
    
    Used by:
    - REPL tests (need initial state for command parsing)
    - Direct tests (need state for sequential navigation)
    
    Args:
        workspace_dir: Workspace directory path
        bot_name: Bot name (e.g., 'story_bot')
        behavior: Behavior name (e.g., 'shape')
        action: Action name (e.g., 'clarify')
        operation: Operation name (default: 'instructions')
        
    Returns:
        Path: state_file path
        
    Example:
        state_file = create_behavior_action_state(
            workspace, 'story_bot', 'shape', 'clarify', 'instructions'
        )
    """
    state_data = {
        'current_behavior': f'{bot_name}.{behavior}',
        'current_action': f'{bot_name}.{behavior}.{action}',
        'operation': operation,
        'working_directory': str(workspace_dir),
        'timestamp': '2025-12-26T10:00:00.000000'
    }
    
    state_file = workspace_dir / 'behavior_action_state.json'
    state_file.write_text(json.dumps(state_data), encoding='utf-8')
    return state_file


def read_behavior_action_state(workspace_dir: Path) -> dict:
    """
    Read and parse behavior_action_state.json.
    
    Used by:
    - Direct tests (verify state persistence)
    - REPL tests (verify command updates state)
    
    Returns:
        dict: Parsed state data
        
    Example:
        state = read_behavior_action_state(workspace)
        assert state['current_behavior'] == 'story_bot.shape'
    """
    state_file = workspace_dir / 'behavior_action_state.json'
    assert state_file.exists(), "State file should exist"
    return json.loads(state_file.read_text(encoding='utf-8'))


# ============================================================================
# ASSERTION HELPERS - Verify expected outcomes
# ============================================================================

def assert_bot_at_behavior_action(bot: Bot, behavior_name: str, 
                                   action_name: str):
    """
    Assert bot is at specified behavior and action.
    
    Used by:
    - Direct tests (verify navigation worked)
    - REPL tests (verify command navigated correctly)
    
    Example:
        assert_bot_at_behavior_action(bot, 'shape', 'clarify')
    """
    assert bot.behaviors.current.name == behavior_name
    assert bot.behaviors.current.actions.current_action_name == action_name


def assert_state_file_shows_behavior_action(workspace_dir: Path, 
                                              bot_name: str,
                                              behavior: str, 
                                              action: str):
    """
    Assert state file shows expected behavior and action.
    
    Used by:
    - Direct tests (verify state persistence)
    - REPL tests (verify commands persist state)
    
    Example:
        assert_state_file_shows_behavior_action(
            workspace, 'story_bot', 'shape', 'clarify'
        )
    """
    state = read_behavior_action_state(workspace_dir)
    assert state['current_behavior'] == f'{bot_name}.{behavior}'
    assert state['current_action'].startswith(f'{bot_name}.{behavior}.{action}')


def assert_action_in_completed_list(workspace_dir: Path, bot_name: str,
                                      behavior: str, action: str):
    """
    Assert action appears in completed_actions list in state file.
    
    Used by:
    - Direct tests (verify close_current marked action complete)
    - Sequential navigation tests
    
    Example:
        assert_action_in_completed_list(workspace, 'story_bot', 'shape', 'clarify')
    """
    state = read_behavior_action_state(workspace_dir)
    completed = [a.get('action_state') for a in state.get('completed_actions', [])]
    assert f'{bot_name}.{behavior}.{action}' in completed
```

## 📝 Phase 2: Build "Navigate And Execute Behaviors" Tests

### Story: Navigate To Behavior Action And Execute

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestNavigateToBehaviorActionAndExecute`

**Scenarios to implement:**

#### Scenario 1: Execute behavior with action parameter (happy_path)
```python
def test_execute_behavior_with_action_parameter(self, tmp_path):
    """
    GIVEN: Bot has behavior shape with action clarify
    WHEN: Bot.execute_behavior is called
    THEN: Action executes and returns BotResult with status completed
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    
    # WHEN
    result = bot.execute_behavior(behavior='shape', action='clarify')
    
    # THEN
    assert isinstance(result, BotResult)
    assert result.status == 'completed'
    assert_bot_at_behavior_action(bot, 'shape', 'clarify')
```

#### Scenario 2: Execute behavior without action forwards to current (happy_path)
```python
def test_execute_behavior_without_action_forwards_to_current(self, tmp_path):
    """
    GIVEN: Bot has behavior shape and workflow state shows current_action=strategy
    WHEN: Bot.execute_behavior is called without action parameter
    THEN: Forwards to current action (strategy)
          BotResult shows strategy was executed
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    create_behavior_action_state(workspace, 'story_bot', 'shape', 'strategy')
    bot.behaviors.load_state()  # Reload to pick up state
    
    # WHEN
    result = bot.execute_behavior(behavior='shape')  # No action param
    
    # THEN
    assert result.status == 'completed'
    assert_bot_at_behavior_action(bot, 'shape', 'strategy')
```

#### Scenario 3: Execute behavior requires confirmation when out of order (happy_path)
```python
def test_execute_behavior_out_of_order_executes_directly(self, tmp_path):
    """
    GIVEN: Current behavior is discovery, requested behavior is shape
    WHEN: Bot.execute_behavior is called (going backwards)
    THEN: Executes directly without order checking
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
    create_behavior_action_state(workspace, 'story_bot', 'discovery', 'clarify')
    bot.behaviors.load_state()
    
    # WHEN - navigate backwards to shape
    result = bot.execute_behavior(behavior='shape', action='clarify')
    
    # THEN
    assert result.status == 'completed'
    assert_bot_at_behavior_action(bot, 'shape', 'clarify')
```

#### Scenario 4: Execute behavior handles entry workflow when no state (happy_path)
```python
def test_execute_behavior_starts_fresh_when_no_state(self, tmp_path):
    """
    GIVEN: No behavior_action_state.json exists
    WHEN: Bot.execute_behavior is called
    THEN: Executes directly (starts fresh workflow)
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    # No state file created - fresh start
    
    # WHEN
    result = bot.execute_behavior(behavior='shape', action='clarify')
    
    # THEN
    assert result.status == 'completed'
    assert_bot_at_behavior_action(bot, 'shape', 'clarify')
    # State file should be created
    assert_state_file_shows_behavior_action(workspace, 'story_bot', 'shape', 'clarify')
```

#### Consolidated Scenario: Complete workflow end-to-end
```python
def test_complete_workflow_end_to_end(self, tmp_path):
    """
    GIVEN: Bot has multiple behaviors with actions
    WHEN: All behaviors and actions executed in order
    THEN: Workflow completes all behaviors
          State shows final behavior/action
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
    
    # WHEN - Execute complete workflow
    # Shape behavior
    bot.execute_behavior(behavior='shape', action='clarify')
    bot.behaviors.current.actions.close_current()
    
    bot.execute_behavior(behavior='shape', action='strategy')
    bot.behaviors.current.actions.close_current()
    
    # Discovery behavior
    bot.execute_behavior(behavior='discovery', action='clarify')
    bot.behaviors.current.actions.close_current()
    
    # THEN
    assert_bot_at_behavior_action(bot, 'discovery', 'strategy')
    assert_action_in_completed_list(workspace, 'story_bot', 'shape', 'clarify')
    assert_action_in_completed_list(workspace, 'story_bot', 'shape', 'strategy')
    assert_action_in_completed_list(workspace, 'story_bot', 'discovery', 'clarify')
```

### Story: Navigate Sequentially

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestNavigateSequentially`

**Note:** Most of these scenarios are ALREADY tested in `test_navigate_behaviors_using_domain_model.py`. We should:
1. Keep those tests as-is (they're the reference implementation)
2. Add ONLY the scenarios that are missing

**Scenarios already covered by `test_navigate_behaviors_using_domain_model.py`:**
- ✅ test_navigate_sets_current_behavior_and_first_action → covers "starts at first action"
- ✅ test_close_current_advances_and_persists_state → covers "next action from current"
- ✅ test_remaining_actions_respects_completion → covers "completed actions tracking"

**New scenarios to add:**

#### Scenario 1: Behavior loads workflow order from behavior.json
```python
def test_behavior_loads_workflow_order_from_json(self, tmp_path):
    """
    GIVEN: behavior.json exists with actions_workflow configuration
    WHEN: behavior is initialized
    THEN: workflow states and transitions match configuration
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    behavior = bot.behaviors.get_behavior('shape')
    
    # WHEN
    action_names = behavior.actions.names
    
    # THEN
    assert action_names == ['clarify', 'strategy', 'validate', 'render']
    # Verify transitions
    assert behavior.actions.get_action('clarify').next_action == 'strategy'
    assert behavior.actions.get_action('strategy').next_action == 'validate'
```

#### Scenario 2: Different behaviors have different action orders
```python
def test_different_behaviors_have_different_action_orders(self, tmp_path):
    """
    GIVEN: two behaviors with different action orders in behavior.json
    WHEN: behaviors are initialized
    THEN: each behavior has its configured action order
          orders differ between behaviors
    """
    # GIVEN - Create behaviors with different action orders
    bot_dir = tmp_path / 'agile_bot' / 'bots' / 'story_bot'
    workspace_dir = tmp_path / 'workspace'
    bot_dir.mkdir(parents=True, exist_ok=True)
    workspace_dir.mkdir(parents=True, exist_ok=True)
    
    create_base_actions_structure(bot_dir)
    create_bot_config_file(bot_dir, 'story_bot', ['shape', 'discovery'])
    
    # shape: clarify → strategy → validate → render
    create_actions_workflow_json(bot_dir, 'shape', actions=[
        {'name': 'clarify', 'order': 1, 'next_action': 'strategy'},
        {'name': 'strategy', 'order': 2, 'next_action': 'validate'},
        {'name': 'validate', 'order': 3, 'next_action': 'render'},
        {'name': 'render', 'order': 4, 'next_action': None}
    ])
    
    # discovery: clarify → build → validate → render (different order!)
    create_actions_workflow_json(bot_dir, 'discovery', actions=[
        {'name': 'clarify', 'order': 1, 'next_action': 'build'},
        {'name': 'build', 'order': 2, 'next_action': 'validate'},
        {'name': 'validate', 'order': 3, 'next_action': 'render'},
        {'name': 'render', 'order': 4, 'next_action': None}
    ])
    
    bootstrap_env(bot_dir, workspace_dir)
    bot = Bot(bot_name='story_bot', bot_directory=bot_dir, 
              config_path=bot_dir / 'bot_config.json')
    
    # WHEN
    shape_actions = bot.behaviors.get_behavior('shape').actions.names
    discovery_actions = bot.behaviors.get_behavior('discovery').actions.names
    
    # THEN
    assert shape_actions == ['clarify', 'strategy', 'validate', 'render']
    assert discovery_actions == ['clarify', 'build', 'validate', 'render']
    assert shape_actions != discovery_actions  # Orders differ
```

#### Scenario 3: Out of order navigation removes completed actions after target
```python
def test_out_of_order_navigation_removes_completed_actions(self, tmp_path):
    """
    GIVEN: current_action: validate
           completed_actions: [clarify, strategy, build, render]
    WHEN: navigate out of order back to build
    THEN: current action is build
          render is removed from completed_actions
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    
    # Create state with completed actions including future action
    state_file = workspace / 'behavior_action_state.json'
    state_data = {
        'current_behavior': 'story_bot.shape',
        'current_action': 'story_bot.shape.validate',
        'completed_actions': [
            {'action_state': 'story_bot.shape.clarify', 'timestamp': '2025-01-01T10:00:00'},
            {'action_state': 'story_bot.shape.strategy', 'timestamp': '2025-01-01T10:01:00'},
            {'action_state': 'story_bot.shape.build', 'timestamp': '2025-01-01T10:02:00'},
            {'action_state': 'story_bot.shape.render', 'timestamp': '2025-01-01T10:03:00'}
        ]
    }
    state_file.write_text(json.dumps(state_data), encoding='utf-8')
    
    # WHEN - Navigate backwards to build
    bot.behaviors.navigate_to('shape')
    bot.behaviors.current.actions.navigate_to_action('build')
    
    # THEN
    assert_bot_at_behavior_action(bot, 'shape', 'build')
    
    state = read_behavior_action_state(workspace)
    completed = [a['action_state'] for a in state['completed_actions']]
    assert 'story_bot.shape.render' not in completed  # Removed!
    assert 'story_bot.shape.clarify' in completed  # Still there
    assert 'story_bot.shape.strategy' in completed  # Still there
```

## 📝 Phase 3: Refactor REPL Tests to Delegate

**Goal:** REPL tests should verify command parsing and delegation, NOT re-test domain logic.

### Pattern: Test Command Parsing, Assert Delegation Occurred

**BEFORE (Current - redundant domain testing):**
```python
def test_user_navigates_with_behavior_only(self, ...):
    # Setup
    repl_session = REPLSession(bot=bot, workspace_directory=workspace)
    
    # Execute REPL command
    cli_response = repl_session.read_and_execute_command('discovery')
    
    # Assert REPL response
    assert cli_response is not None
    assert 'discovery' in cli_response.output.lower()
```

**AFTER (Improved - verify delegation only):**
```python
def test_user_navigates_with_behavior_only(self, ...):
    """
    REPL Command: 'discovery'
    Delegates to: bot.behaviors.navigate_to('discovery')
    Domain logic tested in: test_invoke_bot_directly.py::TestNavigateToBehaviorActionAndExecute
    """
    # Setup
    repl_session = REPLSession(bot=bot, workspace_directory=workspace)
    
    # Execute REPL command
    cli_response = repl_session.read_and_execute_command('discovery')
    
    # Assert REPL parsing worked
    assert cli_response is not None
    assert cli_response.status in ['success', 'error', None]
    
    # Assert delegation occurred (domain logic invoked)
    assert_bot_at_behavior_action(bot, 'discovery', 'clarify')  # Uses helper!
```

### Refactoring Checklist for REPL Tests

For each REPL test:
1. ✅ Replace inline setup with `setup_test_bot()` helper
2. ✅ Replace inline assertions with assertion helpers
3. ✅ Add docstring comment: "Domain logic tested in: test_invoke_bot_directly.py::TestXXX"
4. ✅ Focus assertions on REPL-specific concerns (command parsing, output format)
5. ✅ Use delegation assertions to verify domain logic was called

**Files to refactor:**
- `test_navigate_behaviors_using_repl_commands.py` → use helpers, verify delegation
- `test_execute_actions_using_repl.py` → use helpers, verify delegation
- `test_manage_scope_using_repl.py` → use helpers, verify delegation

## 📝 Phase 4: Implementation Order

### Step 1: Create Common Helpers (1-2 hours)
- [ ] Create `test_invoke_bot_helpers.py`
- [ ] Implement `setup_test_bot()` helper
- [ ] Implement `create_behavior_action_state()` helper
- [ ] Implement `read_behavior_action_state()` helper
- [ ] Implement assertion helpers
- [ ] Run `test_navigate_behaviors_using_domain_model.py` with new helpers to verify they work

### Step 2: Build Navigate Tests in test_invoke_bot_directly.py (2-3 hours)
- [ ] Create `TestNavigateToBehaviorActionAndExecute` class
- [ ] Implement 4 core navigation scenarios
- [ ] Implement end-to-end workflow scenario
- [ ] Create `TestNavigateSequentially` class
- [ ] Implement 3 sequential navigation scenarios
- [ ] Run all tests - verify 100% pass

### Step 3: Refactor REPL Tests to Use Helpers (1-2 hours)
- [ ] Refactor `test_navigate_behaviors_using_repl_commands.py`
- [ ] Replace inline setup with `setup_test_bot()`
- [ ] Replace inline assertions with assertion helpers
- [ ] Add delegation docstrings
- [ ] Run all tests - verify 100% pass

### Step 4: Update story-graph.json with Test Mappings (30 min)
- [ ] Add `test_class` to "Navigate To Behavior Action And Execute" story
- [ ] Add `test_class` to "Navigate Sequentially" story
- [ ] Add `test_method` to each scenario
- [ ] Verify mappings are correct

## 📊 Success Criteria

- ✅ All domain logic for Navigate stories tested in `test_invoke_bot_directly.py`
- ✅ REPL tests refactored to use common helpers
- ✅ No redundant domain logic testing in REPL tests
- ✅ 100% test pass rate maintained
- ✅ story-graph.json updated with test mappings
- ✅ Pattern established for remaining stories (Manage Scope, Build Action Instructions, etc.)

## 🔄 Apply Same Pattern to Other Stories

Once Navigate is complete, apply same pattern to:
1. **Manage Scope** stories
2. **Build Action Instructions** stories
3. **Track Activity** stories

**Pattern:**
1. Extract domain logic tests → `test_invoke_bot_directly.py`
2. Use common helpers from `test_invoke_bot_helpers.py`
3. Refactor REPL tests to verify delegation only
4. Update story-graph.json mappings

## 📝 Notes

- Keep `test_navigate_behaviors_using_domain_model.py` as reference implementation
- Don't duplicate tests - if domain model already tests it, just reference it
- REPL tests should be THIN - just command parsing + delegation verification
- All assertion logic should be in helpers for reusability

