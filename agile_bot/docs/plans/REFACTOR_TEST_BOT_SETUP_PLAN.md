# Refactor Test Bot Setup - Consolidation Plan

## Problem Statement
Tests currently create bot structures from scratch in 85+ setup functions, causing:
- Path calculation broken after move to `domain/` subfolder  
- Tests eagerly load guardrails files causing FileNotFoundError
- Massive duplication of bot creation logic
- Tests write to production-like structures when they only need workspace state

## Goal
Use production story_bot (READ-ONLY) + temporary workspace (READ-WRITE) for all tests.

## Epic Structure (from story-graph.json)
```
Epic: Invoke Bot (line 1410)
├── Sub-Epic: Invoke MCP (test_invoke_mcp.py)
└── Sub-Epic: Invoke Bot Directly
    ├── Navigate And Execute Behaviors (test_invoke_bot_directly.py)
    ├── Manage Scope (test_manage_scope_bot_api.py)
    └── Build Action Instructions
        ├── Build Common Instructions For Actions
        ├── Gather Context (test_gather_context.py)
        ├── Decide Planning Criteria (test_decide_strategy_criteria_action.py)
        └── Build Knowledge (test_build_knowledge.py)
```

## File Naming Strategy
- **`test_invoke_bot_helpers.py`** - Common helpers for entire "Invoke Bot" epic
- **`test_invoke_bot_directly_helpers.py`** - Specific to "Invoke Bot Directly" sub-epic
- **`test_build_knowledge_helpers.py`** - Specific to "Build Knowledge" sub-epic (if needed)

## Implementation Steps

### Step 1: Fix Path Calculation
**Files:** `test_helpers.py`, `test_invoke_bot_helpers.py`  
**Change:** Update `.parent.parent.parent` → `.parent.parent.parent.parent`

**Expected Result:**
- Path resolves correctly to repo root
- Tests can find production story_bot

**Validation:** Run 1 passing test (e.g., `TestLoadBotConfiguration::test_bot_instantiation_with_bot_name_and_workspace`)

---

### Step 2: Create Single Bot Setup Function
**File:** `test_invoke_bot_helpers.py`  
**Function:** `setup_production_story_bot_for_test(tmp_path) -> tuple[Bot, Path]`

**Logic:**
```python
def setup_production_story_bot_for_test(tmp_path) -> tuple[Bot, Path]:
    """
    Use production story_bot READ-ONLY.
    Only create temp workspace for state files.
    """
    # FIXED: 4 levels up from agile_bot/test/domain/test_invoke_bot_helpers.py
    repo_root = Path(__file__).parent.parent.parent.parent
    production_bot_dir = repo_root / 'agile_bot' / 'bots' / 'story_bot'
    
    # Create ONLY workspace for test-specific state
    temp_workspace = tmp_path / 'workspace'
    temp_workspace.mkdir(parents=True, exist_ok=True)
    
    # Bootstrap environment pointing to production bot + temp workspace
    bootstrap_env(production_bot_dir, temp_workspace)
    
    config_path = production_bot_dir / 'bot_config.json'
    bot = Bot(
        bot_name='story_bot',
        bot_directory=production_bot_dir,  # READ-ONLY
        config_path=config_path
    )
    
    return bot, temp_workspace
```

**Expected Result:**
- Single bot setup function that works for all tests
- Uses production story_bot structure (read-only)
- Creates temp workspace for state files

**Validation:** Run 3 previously passing tests from TestLoadBotConfiguration

---

### Step 3: Create State Manipulation Helpers
**File:** `test_invoke_bot_helpers.py`  
**Functions:**
- `set_behavior_action_state(workspace, bot_name, behavior, action, completed=[])`
- `add_completed_action(workspace, bot_name, behavior, action)`
- `clear_behavior_action_state(workspace)`
- `create_test_story_graph(workspace, graph_data)`

**Expected Result:**
- Helpers write ONLY to workspace directory
- No bot structure creation/modification

**Validation:** Run TestNavigateSequentially tests (currently ERROR)

---

### Step 4: Remove Eager Loading from StrategyAction
**File:** `agile_bot/src/actions/strategy/strategy_action.py`  
**Change:** Make guardrails lazy-loaded (defer until actually needed)

**Expected Result:**
- TestLoadActions tests pass (currently 14 failures due to missing guardrails)
- Navigation doesn't trigger file loading

**Validation:** Run TestLoadActions tests

---

### Step 5: Update All Tests to Use New Setup
**Pattern:**
```python
# OLD (creating bot from scratch)
bot_dir = given_bot_directory_created(tmp_path, 'story_bot')
workspace = given_workspace_directory_setup(tmp_path, bot_dir)
bot = given_bot_with_multiple_behaviors_setup(...)

# NEW (use production bot)
bot, workspace = setup_production_story_bot_for_test(tmp_path)
set_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
```

**Expected Result:**
- All 124 tests updated
- No more bot structure creation
- All tests use production story_bot

**Validation:** Run full test suite

---

### Step 6: Remove Obsolete Bot Creation Functions
**Files:** `test_helpers.py`, `test_invoke_bot_directly.py`  
**Remove:** 85+ `given_bot_*`, `create_bot_*`, `given_behavior_*` functions

**Keep:**
- `bootstrap_env()` - Still needed for environment setup
- State manipulation helpers (from Step 3)
- Assertion helpers (e.g., `assert_bot_at_behavior_action()`)

**Expected Result:**
- Drastically reduced helper file size
- Only essential helpers remain

**Validation:** Run full test suite (should still pass)

---

### Step 7: Add Safety Guards
**File:** `test_helpers.py`  
**Function:** `_is_production_story_bot_path(path: Path) -> bool`

**Logic:**
```python
def _is_production_story_bot_path(path: Path) -> bool:
    """Check if path is in production story_bot directory."""
    return 'agile_bot/bots/story_bot' in str(path) and 'tmp' not in str(path)

def _guard_production_write(path: Path):
    """Raise error if attempting to write to production."""
    if _is_production_story_bot_path(path):
        raise RuntimeError(
            f"SAFETY: Cannot write to production story_bot: {path}\n"
            f"Tests should write only to workspace (tmp_path)"
        )
```

**Expected Result:**
- Tests fail-fast if they try to write to production bot
- Clear error message guides developers

**Validation:** Manually try to write to production path in test

---

## Files That Tests WRITE

### ✅ SHOULD WRITE (workspace only):
1. **`behavior_action_state.json`** - Test state tracking
2. **`activity_log.json`** - Activity tracking
3. **Build action outputs:** Generated story documents, knowledge graphs
4. **Validate action outputs:** Validation reports
5. **Render action outputs:** Rendered content
6. **Test data:** Mock story graphs for filtering tests

### ❌ SHOULD NOT WRITE (use production):
- `bot_config.json`
- `behavior.json`
- `actions_workflow.json`
- Guardrails files (typical_assumptions.json, etc.)
- Base action configs
- Instructions files
- Knowledge graph templates/configs

## Success Criteria
- ✅ All 124 tests passing
- ✅ Tests run faster (no bot structure creation)
- ✅ Only 1 bot setup function (vs 85+)
- ✅ Path calculation correct after folder move
- ✅ No writes to production story_bot
- ✅ Clear separation: bot structure (read) vs workspace state (write)

## Rollback Plan
If tests fail catastrophically:
1. Revert Step 5 changes (test updates)
2. Keep Step 1 (path fix) - it's independent and needed
3. Document which tests are incompatible with production bot approach
4. Consider hybrid: Use production bot for structure tests, temp bot for action execution tests
