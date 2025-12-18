# Plan: Eliminate Duplication Violations

**Created:** 2025-12-18  
**Status:** Planned  
**Violations:** 64 total (13 within-file, 51 cross-file)

---

## Rules Reference

All changes must comply with:

- **Coding Rules:** `agile_bot/bots/story_bot/behaviors/code/rules/`
- **Testing Rules:** `agile_bot/bots/story_bot/behaviors/code/rules/specializations/` (test-specific rules)

### Validation Commands

After each change, run:

```bash
# 1. Run tests
pytest agile_bot/bots/base_bot/test/ -v

# 2. Validate new/modified code against coding rules
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate <modified_file>

# 3. Validate new/modified tests against testing rules  
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate <modified_test_file>
```

**Key rules to watch:**
- `eliminate_duplication` - Don't introduce new duplication
- `keep_functions_small_focused` - Extracted methods should be focused
- `use_intention_revealing_names` - New method names must be clear
- `maintain_test_quality` - Any new tests must follow test rules

---

## Phase 1: Config Class Merges

These separations violate domain cohesion - a class should know how to load its own configuration.

| Merge | Keep | Delete | Files to Update |
|-------|------|--------|-----------------|
| Behavior + BehaviorConfig | `behavior.py` | `behavior_config.py` | None (not used elsewhere) |
| Bot + BotConfig | `bot.py` | `bot_config.py` | None (only used in bot.py) |
| Action already has config | `action.py` | `base_action_config.py` | `instructions.py` |

### 1.1 Merge BehaviorConfig → Behavior

**Location 1:** `src/bot/behavior.py` lines 20-34
```python
self.behavior_directory = self.bot_paths.bot_directory / "behaviors" / name
self.config_path = self.behavior_directory / "behavior.json"
if not self.config_path.exists():
    raise FileNotFoundError(...)
self._config = read_json_file(self.config_path)
```

**Location 2:** `src/bot/behavior_config.py` lines 13-26
```python
self.behavior_directory = self.bot_paths.bot_directory / "behaviors" / behavior_name
self.config_path = self.behavior_directory / "behavior.json"
if not self.config_path.exists():
    raise FileNotFoundError(...)
self._config = read_json_file(self.config_path)
```

**Action:**
- Add to `Behavior`: `base_actions_path`, `actions_workflow`, `action_names` properties
- Add type check for `bot_paths`
- Delete `behavior_config.py`

---

### 1.2 Merge BotConfig → Bot

**Location 1:** `src/bot/bot.py` - creates `BotConfig` as collaborator
**Location 2:** `src/bot/bot_config.py` - separate config class

**Action:**
- Add to `Bot`: `description`, `goal`, `instructions`, `mcp`, `trigger_words`, `working_area`, `base_actions_path` properties
- Load config directly in `Bot.__init__`
- Delete `bot_config.py`

---

### 1.3 Delete BaseActionConfig (Action already has this)

**Location 1:** `src/actions/action.py` lines 42-63 - already loads config
**Location 2:** `src/actions/base_action_config.py` - duplicate config loading

**Action:**
- Delete `base_action_config.py`
- Update `src/bot/instructions.py` to take `Action` instead of `BaseActionConfig`

---

## Phase 2: Within-File Method Extractions

### 2.1 CLI Domain - `src/cli/base_bot_cli.py`

| New Method | Location 1 | Location 2 |
|------------|------------|------------|
| `_navigate_to_first_behavior()` | `close_current_action()` lines 134-139 | `_route_to_current_behavior_and_action()` lines 191-196 |
| `_execute_current_action()` | `_route_to_behavior()` lines 181-186 | `_route_to_current_behavior_and_action()` lines 199-204 |
| `_output_help_lines()` | `help_behaviors_and_actions()` lines 291-301 | `help_cursor_commands()` lines 487-497 |

---

### 2.2 Router Domain - `src/cli/trigger_router.py`

| New Method | Location 1 | Location 2 |
|------------|------------|------------|
| `_load_patterns_from_json()` | `_load_bot_triggers()` lines 262-267 | `_load_patterns_from_file()` lines 379-384 |

---

### 2.3 Scope Domain - `src/actions/action_scope.py`

| New Method | Location 1 | Location 2 | Location 3 |
|------------|------------|------------|------------|
| `_extract_story_names()` | `_get_increment_story_names()` lines 147-153 | `_get_increment_story_names_by_name()` lines 163-169 | `_extract_story_names_from_epic()` lines 188-194 |

---

### 2.4 Actions Collection - `src/actions/actions.py`

| New Method | Location 1 | Location 2 |
|------------|------------|------------|
| `_get_state_file_path()` | `close_current()` lines 194-212 | `save_state()` lines 331-348 |

---

### 2.5 Knowledge Graph - `src/actions/build/knowledge_graph_spec.py`

| New Method | Location 1 | Location 2 |
|------------|------------|------------|
| `_set_default_config()` | `_load_config()` lines 23-31 | `_load_config()` lines 33-46 |

---

### 2.6 Knowledge Graph Template - `src/actions/build/knowledge_graph_template.py`

| Change | Location 1 | Location 2 |
|--------|------------|------------|
| `schema` delegates to `template_content` | `schema` property line 30 | `template_content` property (identical body) |

---

### 2.7 Render Domain - `src/actions/render/render_action.py`

| New Method | Location 1 | Location 2 |
|------------|------------|------------|
| `_format_instructions()` | `_format_render_configs()` lines 381-388 | `_format_template_instructions()` lines 463-470 |
| `_init_section_header()` | `_format_executed_synchronizers()` lines 418-422 | `_format_template_instructions()` lines 449-453 |

---

### 2.8 Rule Domain - `src/actions/validate/rule.py`

| New Method | Location 1 | Location 2 |
|------------|------------|------------|
| `_format_example()` | `formatted_text()` lines 235-243 | `formatted_text()` lines 249-257 |

---

## Phase 3: Cross-File Method Extractions

### 3.1 Bot Reminders - NEW MODULE

**New file:** `src/bot/reminders.py`

| New Function | Location 1 | Location 2 |
|--------------|------------|------------|
| `inject_reminder()` | `behaviors.py` : `_inject_next_behavior_reminder()` : 133-139 | `action.py` : `_inject_reminders_if_final()` : 554-561 |

---

## Summary

| Phase | Items | Files Changed | Files Deleted | Test Runs | Code Validations |
|-------|-------|---------------|---------------|-----------|------------------|
| 1. Config Merges | 3 | 4 | 3 | 3 | 3 |
| 2. Within-File | 11 | 8 | 0 | 7 | 7 |
| 3. Cross-File | 1 | 3 | 0 | 1 | 1 |
| **Total** | **15** | **15** | **3** | **11** | **11** |

**Approach:** 
1. Make change
2. Run tests - must pass
3. Run code scanner on modified files - must not introduce new violations
4. Only then proceed to next step

---

## False Positives (No Action Needed)

The following cross-file violations were flagged by the scanner but are structural coincidences, not real duplications:

| Pattern | Count | Reason |
|---------|-------|--------|
| `behavior.py` ↔ `validation_report_writer.py` | ~18 | Coincidental multiple `.get()` calls |
| `behavior.py` ↔ `bot.py` (collaborator creation) | ~4 | Both create objects in `__init__` but different objects |
| Other structural matches | ~25 | AST similarity without semantic duplication |

---

## Execution Order

**Rules:**
1. Run all tests after EVERY change
2. Run code scanner on modified files after EVERY change
3. Do not proceed until tests pass AND no new rule violations

### Step 1: Merge BehaviorConfig → Behavior
- [ ] Merge `behavior_config.py` properties into `behavior.py`
- [ ] Delete `behavior_config.py`
- [ ] **RUN TESTS:** `pytest agile_bot/bots/base_bot/test/ -v`
- [ ] **VALIDATE CODE:** `python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate agile_bot/bots/base_bot/src/bot/behavior.py`

### Step 2: Merge BotConfig → Bot
- [ ] Merge `bot_config.py` properties into `bot.py`
- [ ] Delete `bot_config.py`
- [ ] **RUN TESTS:** `pytest agile_bot/bots/base_bot/test/ -v`
- [ ] **VALIDATE CODE:** `python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate agile_bot/bots/base_bot/src/bot/bot.py`

### Step 3: Delete BaseActionConfig
- [ ] Update `instructions.py` to take `Action` instead of `BaseActionConfig`
- [ ] Delete `base_action_config.py`
- [ ] **RUN TESTS:** `pytest agile_bot/bots/base_bot/test/ -v`
- [ ] **VALIDATE CODE:** `python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate agile_bot/bots/base_bot/src/bot/instructions.py`

### Step 4: CLI Extractions (base_bot_cli.py)
- [ ] Extract `_navigate_to_first_behavior()`
- [ ] Extract `_execute_current_action()`
- [ ] Extract `_output_help_lines()`
- [ ] **RUN TESTS:** `pytest agile_bot/bots/base_bot/test/ -v`
- [ ] **VALIDATE CODE:** `python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate agile_bot/bots/base_bot/src/cli/base_bot_cli.py`

### Step 5: Router Extraction (trigger_router.py)
- [ ] Extract `_load_patterns_from_json()`
- [ ] **RUN TESTS:** `pytest agile_bot/bots/base_bot/test/ -v`
- [ ] **VALIDATE CODE:** `python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate agile_bot/bots/base_bot/src/cli/trigger_router.py`

### Step 6: Scope Extraction (action_scope.py)
- [ ] Extract `_extract_story_names()`
- [ ] **RUN TESTS:** `pytest agile_bot/bots/base_bot/test/ -v`
- [ ] **VALIDATE CODE:** `python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate agile_bot/bots/base_bot/src/actions/action_scope.py`

### Step 7: Actions Extraction (actions.py)
- [ ] Extract `_get_state_file_path()`
- [ ] **RUN TESTS:** `pytest agile_bot/bots/base_bot/test/ -v`
- [ ] **VALIDATE CODE:** `python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate agile_bot/bots/base_bot/src/actions/actions.py`

### Step 8: Knowledge Graph Extractions
- [ ] Extract `_set_default_config()` in `knowledge_graph_spec.py`
- [ ] Make `schema` delegate to `template_content` in `knowledge_graph_template.py`
- [ ] **RUN TESTS:** `pytest agile_bot/bots/base_bot/test/ -v`
- [ ] **VALIDATE CODE:** `python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py agile_bot/bots/base_bot/src/actions/build/knowledge_graph_template.py`

### Step 9: Render Extractions (render_action.py)
- [ ] Extract `_format_instructions()`
- [ ] Extract `_init_section_header()`
- [ ] **RUN TESTS:** `pytest agile_bot/bots/base_bot/test/ -v`
- [ ] **VALIDATE CODE:** `python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate agile_bot/bots/base_bot/src/actions/render/render_action.py`

### Step 10: Rule Extraction (rule.py)
- [ ] Extract `_format_example()`
- [ ] **RUN TESTS:** `pytest agile_bot/bots/base_bot/test/ -v`
- [ ] **VALIDATE CODE:** `python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate agile_bot/bots/base_bot/src/actions/validate/rule.py`

### Step 11: Create Reminders Module
- [ ] Create `bot/reminders.py` with `inject_reminder()`
- [ ] Update `behaviors.py` to use it
- [ ] Update `action.py` to use it
- [ ] **RUN TESTS:** `pytest agile_bot/bots/base_bot/test/ -v`
- [ ] **VALIDATE CODE:** `python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate agile_bot/bots/base_bot/src/bot/reminders.py agile_bot/bots/base_bot/src/bot/behaviors.py agile_bot/bots/base_bot/src/actions/action.py`

### Step 12: Final Validation
- [ ] **RUN FULL TEST SUITE:** `pytest agile_bot/bots/base_bot/test/ -v`
- [ ] **VALIDATE ALL MODIFIED FILES:** Run code scanner on all files touched in this plan
- [ ] **VERIFY DUPLICATION REDUCED:** Re-run duplication scanner and confirm violation count decreased

