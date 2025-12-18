# Consolidated Function Migration Tracker

This document tracks the migration of consolidated test helper functions from the Downloads/test folder to the codebase.

## Migration Status Legend
- ⬜ Not Started
- 🔄 In Progress
- ✅ Complete
- ❌ Skipped (already exists or not needed)

---

## Migration Procedure (FOLLOW FOR EACH FUNCTION)

**For each row in the tables below, follow these steps IN ORDER:**

### Step 1: Review Instructions
- [ ] Read the function specification from the mapping table
- [ ] Identify source file (Downloads/test/) and target file (codebase)
- [ ] Check if function already exists in codebase (skip if identical)

### Step 2: Migrate the Function
- [ ] Copy/implement the consolidated function in the target file
- [ ] Ensure proper imports are added
- [ ] Update any callers to use the new consolidated function

### Step 3: Run Tests
- [ ] Run tests for the specific file modified:
  ```powershell
  cd c:\dev\augmented-teams
  python -m pytest agile_bot/bots/base_bot/test/<test_file>.py -v
  ```
- [ ] Fix any failing tests before proceeding

### Step 4: Commit Changes
- [ ] Stage the changes:
  ```powershell
  git add agile_bot/bots/base_bot/test/<files_changed>
  ```
- [ ] Commit with descriptive message:
  ```powershell
  git commit -m "migrate: add <function_name> consolidated helper"
  ```

### Step 5: Update Tracker
- [ ] Change status from ⬜ to ✅ (or ❌ if skipped)
- [ ] Add any relevant notes
- [ ] Update the Migration Summary totals at bottom

### Step 6: Proceed to Next Row
- [ ] Move to the next function in the table
- [ ] Repeat Steps 1-5

---

## 1. test_helpers.py Consolidated Functions

| Status | Function Name | Source Line | Notes |
|--------|--------------|-------------|-------|
| ✅ | `given_file_created()` | 561 | Core file creation helper |
| ✅ | `given_files_created()` | 614 | Batch file creation |
| ✅ | `given_environment_setup()` | 641 | Environment bootstrap |
| ✅ | `given_workflow_config()` | 744 | Workflow configuration |
| ✅ | `then_file_exists()` | 871 | File existence check |
| ✅ | `then_file_does_not_exist()` | 885 | File non-existence check |
| ✅ | `given_activity_tracker()` | 899 | Activity tracker setup |
| ✅ | `when_activity_tracks_start()` | 912 | Track activity start |
| ✅ | `then_environment_variables_not_set()` | 937 | Env var validation |
| ✅ | `then_function_returns_same_value()` | 954 | Function return check |
| ✅ | `then_environment_variable_matches()` | 967 | Env var match check |
| ✅ | `then_function_returns_path()` | 984 | Path return check |
| ✅ | `given_action_initialized()` | 1113 | Action initialization |
| ✅ | `when_action_tracks_start()` | 1178 | Action start tracking |
| ✅ | `when_action_tracks_completion()` | 1188 | Action completion tracking |
| ✅ | `when_action_finalizes()` | 1198 | Action finalization |
| ✅ | `when_action_injects()` | 1206 | Action injection |
| ✅ | `when_scanner_scans()` | 1234 | Scanner scan execution |
| ✅ | `then_activity_log_matches()` | 1285 | Activity log validation |
| ✅ | `then_scanners_match()` | 1374 | Scanner validation |
| ✅ | `then_action_instructions_match()` | 1522 | Instruction validation |
| ✅ | `when_scanner_created()` | 1552 | Scanner creation |
| ✅ | `when_story_graph_updated()` | 1658 | Story graph update |
| ✅ | `then_instructions_contain()` | 1682 | Instruction content check |
| ✅ | `then_instructions_do_not_contain()` | 1760 | Instruction exclusion check |
| ✅ | `then_template_variables_replaced()` | 1792 | Template var replacement |
| ✅ | `given_story_graph_dict()` | 2076 | Story graph dict creation |
| ✅ | `when_story_graph_copied()` | 2179 | Story graph copy |
| ✅ | `then_nodes_match()` | 2451 | Node matching |
| ✅ | `then_children_match()` | 2470 | Children matching |
| ✅ | `then_stories_match()` | 2490 | Stories matching |
| ✅ | `then_scenarios_match()` | 2509 | Scenarios matching |
| ✅ | `then_scenario_outlines_match()` | 2528 | Scenario outlines matching |
| ✅ | `given_template_variables()` | 2551 | Template variables setup |
| ✅ | `then_file_updated()` | 2567 | File update validation |
| ✅ | `then_instructions_match()` | 2588 | Instructions matching |
| ✅ | `given_action_outputs()` | 2604 | Action outputs setup |
| ✅ | `given_action_duration()` | 2619 | Action duration setup |
| ✅ | `given_action_config_copied()` | 2634 | Action config copy |
| ✅ | `given_action_setup()` | 2667 | Action setup |
| ✅ | `when_action_executes()` | 2722 | Action execution |
| ✅ | `given_directory_created()` | 489 | Directory creation |
| ✅ | `given_activity_log()` | 368 | Activity log creation |

---

## 2. test_perform_behavior_action.py Consolidated Functions

| Status | Function Name | Source Line | Notes |
|--------|--------------|-------------|-------|
| ✅ | `given_completed_action()` | 121 | Completed action setup |
| ✅ | `given_completed_actions()` | 131 | Multiple completed actions |
| ✅ | `when_workflow_navigates()` | 164 | Workflow navigation |
| ✅ | `when_action_closes()` | 191 | Action close |
| ✅ | `then_bot_has_method()` | 260 | Bot method check |
| ✅ | `given_workflow_config()` | 314 | Workflow config (duplicate) |
| ✅ | `given_action_config()` | 404 | Action config |
| ✅ | `then_result_matches()` | 865 | Result matching |
| ✅ | `then_state_matches_multiple_behaviors()` | 954 | Multi-behavior state |
| ✅ | `given_behavior_config()` | 1079 | Behavior config |
| ✅ | `then_behavior_states_match()` | 1227 | Behavior states matching |
| ✅ | `then_behavior_transitions_match()` | 1238 | Behavior transitions matching |
| ✅ | `given_bot_paths()` | 1341 | Bot paths setup |
| ✅ | `given_behavior_config_from_paths()` | 1354 | Behavior config from paths |
| ✅ | `then_actions_sorted()` | 1383 | Actions sorting check |
| ✅ | `given_behaviors_instances()` | 1419 | Behavior instances |
| ✅ | `then_behavior_actions_order()` | 1440 | Behavior actions order |
| ✅ | `then_behaviors_orders_differ()` | 1452 | Behavior order difference |

---

## 3. test_validate_knowledge_and_content_against_rules.py Consolidated Functions

| Status | Function Name | Source Line | Notes |
|--------|--------------|-------------|-------|
| ✅ | `when_workflow_completion_checked()` | 335 | Workflow completion check |
| ✅ | `then_workflow_completion_matches()` | 357 | Workflow completion match |
| ✅ | `then_violations_match_scope()` | 412 | Violations scope match |
| ✅ | `then_stories_match()` | 437 | Stories matching |
| ✅ | `given_rule_file_created()` | 566 | Rule file creation |
| ✅ | `given_rule_object_for_scanner()` | 644 | Rule object setup |
| ✅ | `when_parameters_created()` | 730 | Parameters creation |
| ✅ | `given_scanner_test_setup()` | 1079 | Scanner test setup |
| ✅ | `given_file_created_if_needed()` | 1144 | Conditional file creation |
| ✅ | `given_bot_setup()` | 1244 | Bot setup |
| ✅ | `given_rule_content_dict()` | 1305 | Rule content dict |

---

## 4. test_build_knowledge.py Consolidated Functions

| Status | Function Name | Source Line | Notes |
|--------|--------------|-------------|-------|
| ✅ | `when_story_map_created()` | 129 | Story map creation |
| ✅ | `then_nodes_match_expected_structure()` | 417 | Nodes structure check |
| ✅ | `then_location_matches()` | 429 | Location matching |
| ✅ | `then_story_map_matches()` | 498 | Story map matching |
| ✅ | `when_epic_children_retrieved()` | 646 | Epic children retrieval |

---

## 5. test_gather_context.py Consolidated Functions

| Status | Function Name | Source Line | Notes |
|--------|--------------|-------------|-------|
| ✅ | `given_action_outputs()` | 44 | Action outputs |
| ✅ | `given_action_duration()` | 61 | Action duration |
| ✅ | `given_activity_log_entries()` | 65 | Activity log entries |
| ✅ | `given_guardrails_data()` | 125 | Guardrails data |

---

## 6. test_generate_mcp_tools.py Consolidated Functions

| Status | Function Name | Source Line | Notes |
|--------|--------------|-------------|-------|
| ✅ | `given_behaviors_list()` | 33 | Behaviors list |
| ✅ | `given_trigger_patterns()` | 49 | Trigger patterns |
| ✅ | `given_fake_repo_root()` | 1191 | Fake repo root |

---

## 7. test_invoke_cli.py Consolidated Functions

| Status | Function Name | Source Line | Notes |
|--------|--------------|-------------|-------|
| ✅ | `when_all_combinations_tested()` | 346 | All combinations test |
| ✅ | `given_behavior_triggers_dict()` | 383 | Behavior triggers dict |
| ✅ | `given_behavior_config_from_trigger_config()` | 764 | Behavior config from triggers |
| ✅ | `when_priority_accessed()` | 742 | Priority access |

---

## 8. test_invoke_mcp.py Consolidated Functions

| Status | Function Name | Source Line | Notes |
|--------|--------------|-------------|-------|
| ✅ | `given_base_actions_setup()` | 37 | Base actions setup |
| ✅ | `when_instructions_load_and_merge()` | 286 | Instructions merge |
| ✅ | `then_merged_instructions_contain()` | 313 | Merged instructions check |

---

## 9. test_init_project.py Consolidated Functions

| Status | Function Name | Source Line | Notes |
|--------|--------------|-------------|-------|
| ✅ | `given_environment_variable_set()` | 76 | Env var set |
| ✅ | `given_override_directory()` | 130 | Override directory |
| ✅ | `when_bootstrap_logic_runs()` | 189 | Bootstrap logic |

---

## 10. test_render_output.py Consolidated Functions

| Status | Function Name | Source Line | Notes |
|--------|--------------|-------------|-------|
| ✅ | `given_render_configs_created()` | 83 | Render configs |
| ✅ | `when_render_configs_formatted()` | 254 | Render configs format |

---

## 11. test_decide_strategy_criteria_action.py Consolidated Functions

| Status | Function Name | Source Line | Notes |
|--------|--------------|-------------|-------|
| ✅ | `when_action_injects_strategy_criteria_and_assumptions()` | 129 | Strategy injection |

---

## Migration Summary

| Category | Total | Complete | Remaining |
|----------|-------|----------|-----------|
| test_helpers.py | 42 | 42 | 0 |
| test_perform_behavior_action.py | 18 | 18 | 0 |
| test_validate_knowledge...py | 11 | 11 | 0 |
| test_build_knowledge.py | 5 | 5 | 0 |
| test_gather_context.py | 4 | 4 | 0 |
| test_generate_mcp_tools.py | 3 | 3 | 0 |
| test_invoke_cli.py | 4 | 4 | 0 |
| test_invoke_mcp.py | 3 | 3 | 0 |
| test_init_project.py | 3 | 3 | 0 |
| test_render_output.py | 2 | 2 | 0 |
| test_decide_strategy...py | 1 | 1 | 0 |
| **TOTAL** | **96** | **96** | **0** |

---

*Last Updated: 2025-12-18 - All functions migrated*

