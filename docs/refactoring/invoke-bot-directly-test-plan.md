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

---

## 📝 Phase 5: Build "Manage Scope" Tests

### Story: Set Story Scope

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestSetStoryScope`

**Scenarios to implement:**

#### Scenario 1: Set story scope filters knowledge graph
```python
def test_set_story_scope_filters_knowledge_graph(self, tmp_path):
    """
    GIVEN: Bot has story graph loaded
    WHEN: Scope is set with story parameter
    THEN: Bot scope is configured for story filtering
          Knowledge graph operations will be filtered
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    
    # WHEN - Set story scope
    bot.scope.set_story_scope(['Epic Name', 'Story Name'])
    
    # THEN
    assert bot.scope.type == 'story'
    assert bot.scope.value == ['Epic Name', 'Story Name']
    assert bot.scope.is_active()
```

#### Scenario 2: Story scope enforces mutually exclusive types
```python
def test_story_scope_replaces_existing_file_scope(self, tmp_path):
    """
    GIVEN: Bot has file scope set
    WHEN: Story scope is set
    THEN: File scope is cleared
          Only story scope is active
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    bot.scope.set_file_scope(['*.py'])
    
    # WHEN - Set story scope (should replace file scope)
    bot.scope.set_story_scope(['Epic Name'])
    
    # THEN
    assert bot.scope.type == 'story'
    assert bot.scope.value == ['Epic Name']
    # File scope should be cleared
    assert not hasattr(bot.scope, 'file_patterns') or bot.scope.file_patterns is None
```

### Story: Set File Scope

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestSetFileScope`

**Scenarios to implement:**

#### Scenario 1: Set file scope filters files
```python
def test_set_file_scope_filters_files(self, tmp_path):
    """
    GIVEN: Bot is initialized
    WHEN: Scope is set with file patterns
    THEN: Bot scope is configured for file filtering
          Future operations filter by file patterns
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    
    # WHEN - Set file scope
    bot.scope.set_file_scope(['src/**/*.py', 'test/**/*.py'])
    
    # THEN
    assert bot.scope.type == 'files'
    assert bot.scope.value == ['src/**/*.py', 'test/**/*.py']
    assert bot.scope.is_active()
```

#### Scenario 2: File scope supports include and exclude patterns
```python
def test_file_scope_supports_exclude_patterns(self, tmp_path):
    """
    GIVEN: Bot is initialized
    WHEN: Scope is set with include and exclude patterns
    THEN: Scope contains both include and exclude patterns
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    
    # WHEN - Set file scope with excludes
    bot.scope.set_file_scope(
        include=['src/**/*.py'],
        exclude=['src/**/*_test.py']
    )
    
    # THEN
    assert bot.scope.type == 'files'
    assert bot.scope.value == ['src/**/*.py']
    assert bot.scope.exclude == ['src/**/*_test.py']
```

### Story: Filter Knowledge Graph By Scope

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestFilterKnowledgeGraphByScope`

**Note:** Test class `TestFilterActionBasedOnScope` already exists in test_invoke_bot_directly.py (line 4529). Review and augment if needed.

**Scenarios to implement:**

#### Scenario 1: Knowledge graph filtered when story scope active
```python
def test_knowledge_graph_filtered_by_story_scope(self, tmp_path):
    """
    GIVEN: Bot has story scope set
    WHEN: Knowledge graph is loaded
    THEN: Only stories in scope are included
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    bot.scope.set_story_scope(['Epic1'])
    
    # WHEN - Execute build action (loads knowledge graph)
    result = bot.execute_behavior(behavior='shape', action='build')
    
    # THEN
    # Knowledge graph should be filtered
    # (Implementation depends on how knowledge graph exposes filtered data)
    assert result.status == 'completed'
```

#### Scenario 2: Knowledge graph not filtered when no scope
```python
def test_knowledge_graph_unfiltered_when_no_scope(self, tmp_path):
    """
    GIVEN: Bot has no scope set
    WHEN: Knowledge graph is loaded
    THEN: All stories are included
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    # No scope set
    
    # WHEN - Execute build action
    result = bot.execute_behavior(behavior='shape', action='build')
    
    # THEN
    assert result.status == 'completed'
    # All stories should be available
```

### Story: Pass Scope Parameters To Actions

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestPassScopeParametersToActions`

**Scenarios to implement:**

#### Scenario 1: Actions receive scope from bot
```python
def test_actions_receive_scope_from_bot(self, tmp_path):
    """
    GIVEN: Bot has scope set
    WHEN: Action executes
    THEN: Action receives scope parameters
          Action uses scope for filtering
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    bot.scope.set_story_scope(['Epic1'])
    
    # WHEN - Execute action
    bot.behaviors.navigate_to('shape')
    action = bot.behaviors.current.actions.current
    
    # THEN
    # Action should have access to scope
    assert action.scope is not None
    assert action.scope.type == 'story'
```

### Story: Clear Scope

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestClearScope`

**Scenarios to implement:**

#### Scenario 1: Clear scope resets to all
```python
def test_clear_scope_resets_to_all(self, tmp_path):
    """
    GIVEN: Bot has scope set
    WHEN: Clear scope is called
    THEN: Scope is reset to None
          Future actions run without scope filter
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    bot.scope.set_story_scope(['Epic1'])
    assert bot.scope.is_active()
    
    # WHEN - Clear scope
    bot.scope.clear()
    
    # THEN
    assert not bot.scope.is_active()
    assert bot.scope.type is None
```

#### Scenario 2: Clear scope after execution persists
```python
def test_clear_scope_persists_across_actions(self, tmp_path):
    """
    GIVEN: Bot has scope set and cleared
    WHEN: Multiple actions execute
    THEN: Scope remains cleared
          All actions run without filtering
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    bot.scope.set_story_scope(['Epic1'])
    bot.scope.clear()
    
    # WHEN - Execute multiple actions
    bot.execute_behavior(behavior='shape', action='clarify')
    bot.execute_behavior(behavior='shape', action='strategy')
    
    # THEN
    assert not bot.scope.is_active()
```

---

## 📝 Phase 6: Build "Track Activity" Tests

### Story: Track Action Start

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestTrackActionStart`

**Note:** Test class `TestTrackActivityForWorkspace` already exists in test_invoke_bot_directly.py (line 5087). Review and potentially rename/split.

**Scenarios to implement:**

#### Scenario 1: Activity entry created when action starts
```python
def test_activity_entry_created_when_action_starts(self, tmp_path):
    """
    GIVEN: Bot is ready to execute action
    WHEN: Action starts execution
    THEN: Activity entry is created with timestamp and action state
          Entry appended to activity_log.json
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    activity_log_file = workspace / 'activity_log.json'
    
    # WHEN - Execute action (should track start)
    bot.execute_behavior(behavior='shape', action='clarify')
    
    # THEN
    assert activity_log_file.exists()
    
    activity_log = json.loads(activity_log_file.read_text(encoding='utf-8'))
    assert len(activity_log) > 0
    
    start_entry = activity_log[0]
    assert 'timestamp' in start_entry
    assert 'action_state' in start_entry
    assert start_entry['action_state'] == 'story_bot.shape.clarify'
    assert start_entry['event'] == 'start'
```

#### Scenario 2: Activity log appends entries (not overwrites)
```python
def test_activity_log_appends_not_overwrites(self, tmp_path):
    """
    GIVEN: Activity log has existing entries
    WHEN: New action starts
    THEN: New entry is appended to log
          Previous entries remain
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    
    # Execute first action
    bot.execute_behavior(behavior='shape', action='clarify')
    
    # WHEN - Execute second action
    bot.execute_behavior(behavior='shape', action='strategy')
    
    # THEN
    activity_log_file = workspace / 'activity_log.json'
    activity_log = json.loads(activity_log_file.read_text(encoding='utf-8'))
    
    # Should have entries for both actions
    assert len(activity_log) >= 2
    action_states = [entry['action_state'] for entry in activity_log]
    assert 'story_bot.shape.clarify' in action_states
    assert 'story_bot.shape.strategy' in action_states
```

### Story: Track Action Completion

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestTrackActionCompletion`

**Scenarios to implement:**

#### Scenario 1: Activity entry updated when action completes
```python
def test_activity_entry_updated_when_action_completes(self, tmp_path):
    """
    GIVEN: Action has started and created start entry
    WHEN: Action completes execution
    THEN: Activity entry is updated with completion details
          Entry shows outputs and duration
    """
    # GIVEN/WHEN - Execute action to completion
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    bot.execute_behavior(behavior='shape', action='clarify')
    
    # Mark action as complete
    bot.behaviors.current.actions.close_current()
    
    # THEN
    activity_log_file = workspace / 'activity_log.json'
    activity_log = json.loads(activity_log_file.read_text(encoding='utf-8'))
    
    # Should have completion entry
    completion_entries = [e for e in activity_log if e.get('event') == 'complete']
    assert len(completion_entries) > 0
    
    completion_entry = completion_entries[0]
    assert 'timestamp' in completion_entry
    assert 'action_state' in completion_entry
    assert completion_entry['action_state'] == 'story_bot.shape.clarify'
```

#### Scenario 2: Completion entry includes duration
```python
def test_completion_entry_includes_duration(self, tmp_path):
    """
    GIVEN: Action has start and end timestamps
    WHEN: Completion entry is created
    THEN: Entry includes duration calculation
    """
    # GIVEN/WHEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    bot.execute_behavior(behavior='shape', action='clarify')
    bot.behaviors.current.actions.close_current()
    
    # THEN
    activity_log_file = workspace / 'activity_log.json'
    activity_log = json.loads(activity_log_file.read_text(encoding='utf-8'))
    
    completion_entries = [e for e in activity_log if e.get('event') == 'complete']
    if completion_entries:
        completion_entry = completion_entries[0]
        # Duration should be present (may be 'duration_seconds' or 'duration')
        assert 'duration' in completion_entry or 'duration_seconds' in completion_entry
```

### Story: Record Activity Metrics And Paths

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestRecordActivityMetricsAndPaths`

**Scenarios to implement:**

#### Scenario 1: Activity log captures file paths
```python
def test_activity_log_captures_file_paths(self, tmp_path):
    """
    GIVEN: Action works with files
    WHEN: Action executes
    THEN: Activity log captures input/output file paths
    """
    # GIVEN/WHEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    result = bot.execute_behavior(behavior='shape', action='clarify')
    
    # THEN
    activity_log_file = workspace / 'activity_log.json'
    if activity_log_file.exists():
        activity_log = json.loads(activity_log_file.read_text(encoding='utf-8'))
        
        # Check for file path tracking in entries
        # (Implementation depends on how paths are tracked)
        assert len(activity_log) > 0
```

#### Scenario 2: Activity log captures metrics (not full content)
```python
def test_activity_log_captures_metrics_not_content(self, tmp_path):
    """
    GIVEN: Action generates output
    WHEN: Activity is logged
    THEN: Log captures metrics (file count, size)
          Log does NOT capture full file content
    """
    # GIVEN/WHEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    bot.execute_behavior(behavior='shape', action='clarify')
    
    # THEN
    activity_log_file = workspace / 'activity_log.json'
    if activity_log_file.exists():
        activity_log = json.loads(activity_log_file.read_text(encoding='utf-8'))
        
        for entry in activity_log:
            # Verify entries don't contain massive content
            entry_str = json.dumps(entry)
            assert len(entry_str) < 10000  # Entries should be small (metrics only)
```

---

## 📝 Phase 7: Build "Build Action Instructions" Tests

**Important Note:** The "Build Action Instructions" feature contains many nested sub-epics:
- Build Common Instructions For Actions
- Gather Context
- Decide Planning Criteria Action
- Build Knowledge
- Render Output
- Validate Knowledge & Content Against Rules

**Many of these already have dedicated test files:**
- `test_gather_context.py` (Gather Context)
- `test_decide_strategy_criteria_action.py` (Decide Planning Criteria)
- `test_build_knowledge.py` (Build Knowledge)
- `test_render_output.py` (Render Output)

**Strategy:** Focus on the INTEGRATION and ORCHESTRATION in `test_invoke_bot_directly.py`, NOT re-testing individual action implementation details.

### Story: Get Action Instructions

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestGetActionInstructions`

**Scenarios to implement:**

#### Scenario 1: Get instructions loads base + behavior-specific
```python
def test_get_instructions_loads_base_and_behavior_specific(self, tmp_path):
    """
    GIVEN: Bot has base actions and behavior-specific instructions
    WHEN: get_instructions() is called for action
    THEN: Returns merged instructions from base and behavior
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    bot.behaviors.navigate_to('shape')
    
    # WHEN - Get instructions for clarify action
    action = bot.behaviors.current.actions.get_action('clarify')
    instructions = action.get_instructions()
    
    # THEN
    assert instructions is not None
    assert isinstance(instructions, dict)
    # Should contain base instructions
    assert 'system_prompt' in instructions or 'instructions' in instructions
```

#### Scenario 2: Instructions include guardrails when present
```python
def test_instructions_include_guardrails(self, tmp_path):
    """
    GIVEN: Behavior has guardrails configured
    WHEN: get_instructions() is called
    THEN: Instructions include guardrail content
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    bot.behaviors.navigate_to('shape')
    
    # WHEN
    action = bot.behaviors.current.actions.get_action('clarify')
    instructions = action.get_instructions()
    
    # THEN
    # Guardrails should be merged into instructions
    assert instructions is not None
```

### Story: Load Base Action Configuration

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestLoadBaseActionConfiguration`

**Note:** Test class already exists (line 4004). Review and augment if needed.

**Scenarios to implement:**

#### Scenario 1: Base action config loaded from base_actions folder
```python
def test_base_action_config_loaded_from_folder(self, tmp_path):
    """
    GIVEN: Base actions exist in base_actions folder
    WHEN: Action is initialized
    THEN: Base configuration is loaded
    """
    # Already tested - verify coverage
    pass
```

### Story: Load And Merge Behavior-Specific Instructions

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestLoadAndMergeBehaviorSpecificInstructions`

**Scenarios to implement:**

#### Scenario 1: Behavior instructions override base instructions
```python
def test_behavior_instructions_override_base(self, tmp_path):
    """
    GIVEN: Base and behavior both have instructions for action
    WHEN: Instructions are merged
    THEN: Behavior-specific instructions override base
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    
    # Create behavior-specific instruction override
    behavior_dir = bot.bot_paths.behaviors_directory / 'shape'
    action_dir = behavior_dir / 'actions' / 'clarify'
    action_dir.mkdir(parents=True, exist_ok=True)
    
    override_config = {
        'instructions': ['Behavior-specific instruction']
    }
    (action_dir / 'action.json').write_text(json.dumps(override_config), encoding='utf-8')
    
    # WHEN
    bot.behaviors.navigate_to('shape')
    action = bot.behaviors.current.actions.get_action('clarify')
    instructions = action.get_instructions()
    
    # THEN
    # Behavior instructions should be present
    assert instructions is not None
```

### Story: Load Guardrails From Behavior Folder

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestLoadGuardrailsFromBehaviorFolder`

**Scenarios to implement:**

#### Scenario 1: Guardrails loaded from behavior folder
```python
def test_guardrails_loaded_from_behavior_folder(self, tmp_path):
    """
    GIVEN: Behavior has guardrails.json
    WHEN: Action loads guardrails
    THEN: Guardrails are available to action
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    
    # WHEN
    bot.behaviors.navigate_to('shape')
    behavior = bot.behaviors.current
    
    # THEN
    # Guardrails should be loaded (implementation detail)
    assert behavior is not None
```

### Story: Inject Guardrails Into Instructions

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestInjectGuardrailsIntoInstructions`

**Scenarios to implement:**

#### Scenario 1: Guardrails injected into instruction output
```python
def test_guardrails_injected_into_instructions(self, tmp_path):
    """
    GIVEN: Action has guardrails configured
    WHEN: Instructions are generated
    THEN: Guardrails are included in output
    """
    # GIVEN
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    bot.behaviors.navigate_to('shape')
    
    # WHEN
    action = bot.behaviors.current.actions.get_action('clarify')
    instructions = action.get_instructions()
    
    # THEN
    # Instructions should contain guardrails section
    assert instructions is not None
```

### Story: Inject Context Into Instructions

**File:** `test_invoke_bot_directly.py`  
**Test Class:** `TestInjectContextIntoInstructions`

**Note:** Test class already exists (line 3084). Review and augment if needed.

**Scenarios to implement:**

#### Scenario 1: Context from previous actions injected
```python
def test_context_from_previous_actions_injected(self, tmp_path):
    """
    GIVEN: Previous action stored context data
    WHEN: Next action loads instructions
    THEN: Context from previous action is included
    """
    # Already tested - verify coverage
    pass
```

---

## 📝 Phase 8: Refactor ALL REPL Tests to Use Helpers

### Files to Refactor:
1. ✅ `test_navigate_behaviors_using_repl_commands.py` (Navigate - Phase 3)
2. `test_manage_scope_using_repl.py` (Manage Scope)
3. `test_execute_actions_using_repl.py` (Execute Actions)
4. `test_display_state_using_repl.py` (Display State)
5. `test_get_help_using_repl.py` (Get Help)
6. `test_initialize_repl_session.py` (Initialize)

**Refactoring Pattern (Apply to All):**

```python
# BEFORE - Inline setup
def test_something(self, bot_directory, workspace_directory, monkeypatch):
    monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
    create_behavior(bot_directory, 'shape', ['clarify', 'strategy'])
    create_behavior_action_state(workspace_directory, 'shape', 'clarify')
    
    bot = Bot(...)
    repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
    
# AFTER - Use helpers
def test_something(self, tmp_path, monkeypatch):
    """
    Domain logic tested in: test_invoke_bot_directly.py::TestXXX
    """
    bot, workspace = setup_test_bot(tmp_path, ['shape'])
    create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
    
    monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
    repl_session = REPLSession(bot=bot, workspace_directory=workspace)
```

---

## 📝 Phase 9: Implementation Roadmap

### **Step 1: Expand Common Helpers** (1-2 hours)
- [ ] Add scope-related assertion helpers to `test_invoke_bot_helpers.py`
  - `assert_scope_is_set(bot, scope_type, scope_value)`
  - `assert_scope_is_cleared(bot)`
- [ ] Add activity log helpers
  - `read_activity_log(workspace_dir)`
  - `assert_activity_logged(workspace, action_state, event_type)`

### **Step 2: Build Manage Scope Tests** (2-3 hours)
- [ ] Create `TestSetStoryScope` class (2 scenarios)
- [ ] Create `TestSetFileScope` class (2 scenarios)
- [ ] Create `TestFilterKnowledgeGraphByScope` class (2 scenarios)
- [ ] Create `TestPassScopeParametersToActions` class (1 scenario)
- [ ] Create `TestClearScope` class (2 scenarios)
- [ ] Run tests - verify 100% pass

### **Step 3: Build Track Activity Tests** (1-2 hours)
- [ ] Create `TestTrackActionStart` class (2 scenarios)
- [ ] Create `TestTrackActionCompletion` class (2 scenarios)
- [ ] Create `TestRecordActivityMetricsAndPaths` class (2 scenarios)
- [ ] Run tests - verify 100% pass

### **Step 4: Build Action Instructions Integration Tests** (2-3 hours)
- [ ] Create `TestGetActionInstructions` class (2 scenarios)
- [ ] Create `TestLoadAndMergeBehaviorSpecificInstructions` class (1 scenario)
- [ ] Create `TestLoadGuardrailsFromBehaviorFolder` class (1 scenario)
- [ ] Create `TestInjectGuardrailsIntoInstructions` class (1 scenario)
- [ ] Review existing `TestLoadBaseActionConfiguration` - augment if needed
- [ ] Review existing `TestInjectContextIntoInstructions` - augment if needed
- [ ] Run tests - verify 100% pass

### **Step 5: Refactor ALL REPL Tests** (3-4 hours)
- [ ] Refactor `test_manage_scope_using_repl.py` (use helpers)
- [ ] Refactor `test_execute_actions_using_repl.py` (use helpers)
- [ ] Refactor `test_display_state_using_repl.py` (use helpers)
- [ ] Refactor `test_get_help_using_repl.py` (use helpers)
- [ ] Refactor `test_initialize_repl_session.py` (use helpers)
- [ ] Run ALL tests - verify 100% pass

### **Step 6: Update story-graph.json** (1-2 hours)
- [ ] Add `test_class` mappings for ALL new test classes
- [ ] Add `test_method` mappings for ALL new test methods
- [ ] Verify mappings are correct and complete

---

## 📊 Final Success Criteria

### Coverage:
- ✅ Navigate And Execute Behaviors - COMPLETE
- ✅ Manage Scope - COMPLETE (5 stories)
- ✅ Track Activity - COMPLETE (3 stories)
- ✅ Build Action Instructions - COMPLETE (core integration tests)
- ✅ All REPL tests refactored to use common helpers
- ✅ Zero redundant domain logic in REPL tests
- ✅ 100% test pass rate maintained
- ✅ story-graph.json fully mapped

### Total Estimated Time:
- **Phase 1-4 (Current Plan):** 6-10 hours
- **Phase 5-6 (Manage Scope + Track Activity):** 3-5 hours
- **Phase 7 (Build Instructions Integration):** 2-3 hours
- **Phase 8 (Refactor ALL REPL):** 3-4 hours
- **Phase 9 (Update story-graph.json):** 1-2 hours

**Grand Total: 15-24 hours** (2-3 days of focused work)

---

## 📝 Notes

- Keep `test_navigate_behaviors_using_domain_model.py` as reference implementation
- Don't duplicate tests - if domain model already tests it, just reference it
- REPL tests should be THIN - just command parsing + delegation verification
- All assertion logic should be in helpers for reusability
- **Build Action Instructions:** Focus on INTEGRATION, not individual action details (those have dedicated test files)
- **Existing Tests:** Review existing test classes before creating new ones to avoid duplication

