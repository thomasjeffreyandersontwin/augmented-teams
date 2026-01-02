# Perform Behavior Action Test-to-Story Mapping Analysis

## Level 1: Test Class vs Story Document/Story Graph Mapping

### Test Classes in `test_perform_behavior_action.py` (19 total):

1. **TestInjectNextBehaviorReminder** (line 626)
   - ✅ Story Document: `📝 Inject Next Behavior Reminder.md` EXISTS
   - ❌ Story Graph: NO scenarios defined
   - ❌ Test Count: 3 test methods, 0 scenarios documented

2. **TestCloseCurrentAction** (line 699)
   - ✅ Story Document: `📝 Close Current Action.md` EXISTS
   - ❌ Story Graph: Has scenarios but needs verification
   - ❌ Test Count: 6 test methods, unknown scenarios documented

3. **TestInvokeBehaviorActionsInWorkflowOrder** (line 996)
   - ✅ Story Document: `📝 Invoke Behavior Actions in Workflow Order.md` EXISTS
   - ❌ Story Graph: Has scenarios but needs verification
   - ❌ Test Count: 1 test method (end-to-end), unknown scenarios documented

4. **TestInvokeBehaviorInActionOrder** (line 1593)
   - ✅ Story Document: `📝 Invoke Behavior in Workflow Order.md` EXISTS (NAMING MISMATCH)
   - ❌ Story Graph: NO scenarios defined
   - ❌ Test Count: 10 test methods, 0 scenarios documented

5. **TestExecuteBehavior** (line 2074)
   - ✅ Story Document: `📝 Execute Behavior.md` EXISTS
   - ❌ Story Graph: Maps to `test_bot_execute_behavior.py` (WRONG TEST FILE!)
   - ❌ Test Count: 4 test methods, 0 scenarios documented

6. **TestInsertContextIntoInstructions** (line 2170)
   - ❌ Story Document: MISSING
   - ❌ Story Graph: NOT FOUND
   - ❌ Test Count: 1 test method, 0 scenarios documented

7. **TestInjectStatusUpdateBreadcrumbsIntoInstructions** (line 2316)
   - ❌ Story Document: MISSING
   - ❌ Story Graph: NOT FOUND
   - ❌ Test Count: 4 test methods, 0 scenarios documented

8. **TestLoadBotConfiguration** (line 2721)
   - ❌ Story Document: MISSING
   - ❌ Story Graph: NOT FOUND
   - ❌ Test Count: 5 test methods, 0 scenarios documented

9. **TestLoadBehaviorConfiguration** (line 2817)
   - ❌ Story Document: MISSING
   - ❌ Story Graph: NOT FOUND
   - ❌ Test Count: 2 test methods, 0 scenarios documented

10. **TestLoadBotBehaviors** (line 2981)
    - ❌ Story Document: MISSING
    - ❌ Story Graph: NOT FOUND
    - ❌ Test Count: 9 test methods, 0 scenarios documented

11. **TestLoadActions** (line 3272)
    - ❌ Story Document: MISSING
    - ❌ Story Graph: NOT FOUND
    - ❌ Test Count: 12 test methods, 0 scenarios documented

12. **TestLoadBaseActionConfiguration** (line 3634)
    - ❌ Story Document: MISSING
    - ❌ Story Graph: NOT FOUND
    - ❌ Test Count: 1 test method, 0 scenarios documented

13. **TestAccessBotPaths** (line 3735)
    - ❌ Story Document: MISSING
    - ❌ Story Graph: NOT FOUND
    - ❌ Test Count: 7 test methods, 0 scenarios documented

14. **TestGetBaseInstructions** (line 3998)
    - ❌ Story Document: MISSING
    - ❌ Story Graph: NOT FOUND
    - ❌ Test Count: 1 test method (parameterized with 3 examples), 0 scenarios documented

15. **TestLoadBehaviorConfig** (line 4030)
    - ❌ Story Document: MISSING
    - ❌ Story Graph: NOT FOUND
    - ❌ Test Count: 2 test methods, 0 scenarios documented

16. **TestManageBehaviorsCollection** (line 4089)
    - ❌ Story Document: MISSING
    - ❌ Story Graph: NOT FOUND
    - ❌ Test Count: 8 test methods, 0 scenarios documented

17. **TestResolveBotPaths** (line 4292)
    - ❌ Story Document: MISSING
    - ❌ Story Graph: NOT FOUND
    - ❌ Test Count: 5 test methods, 0 scenarios documented

18. **TestFilterActionBasedOnScope** (line 4529)
    - ❌ Story Document: MISSING
    - ❌ Story Graph: NOT FOUND
    - ❌ Test Count: 9 test methods, 0 scenarios documented

19. **TestBootstrapWorkspace** (line 4697)
    - ✅ Story Document: `📝 Bootstrap Workspace.md` EXISTS
    - ✅ Story Graph: Maps correctly to `test_perform_behavior_action.py`
    - ❌ Test Count: 10 test methods, only 1 generic scenario documented

### Story Documents in Folder (8 total):

1. `📝 Bootstrap Workspace.md` - ✅ Has test class
2. `📝 Close Current Action.md` - ✅ Has test class
3. `📝 Execute Behavior.md` - ✅ Has test class (wrong file mapping)
4. `📝 Find Behavior Folder.md` - ✅ Has test class (different file: `test_utils.py`)
5. `📝 Inject Next Behavior Reminder.md` - ✅ Has test class
6. `📝 Invoke Behavior Actions in Workflow Order.md` - ✅ Has test class
7. `📝 Invoke Behavior in Workflow Order.md` - ✅ Has test class (name mismatch)
8. `📝 Load And Merge Behavior Action Instructions.md` - ❌ NO test class in this file!

### CRITICAL ISSUES IDENTIFIED:

#### Issue 1: Missing Story Documents (11 stories)
- TestInsertContextIntoInstructions
- TestInjectStatusUpdateBreadcrumbsIntoInstructions  
- TestLoadBotConfiguration
- TestLoadBehaviorConfiguration
- TestLoadBotBehaviors
- TestLoadActions
- TestLoadBaseActionConfiguration
- TestAccessBotPaths
- TestGetBaseInstructions
- TestLoadBehaviorConfig
- TestManageBehaviorsCollection
- TestResolveBotPaths
- TestFilterActionBasedOnScope

#### Issue 2: Wrong Test File Mappings
- "Execute Behavior" story maps to `test_bot_execute_behavior.py` but should map to `test_perform_behavior_action.py`
- "Invoke Behavior in Workflow Order" story maps to `test_workflow_action_sequence.py` but tests are in `test_perform_behavior_action.py`
- "Invoke Behavior Actions in Workflow Order" story maps to `test_complete_workflow_integration.py` but tests are in `test_perform_behavior_action.py`

#### Issue 3: Missing Scenarios
- All 8 existing story documents have only generic "happy_path" scenarios
- Real test methods are not documented as scenarios
- Story-graph.json has some scenarios but they don't match the actual test methods

#### Issue 4: Orphaned Story Document
- `📝 Load And Merge Behavior Action Instructions.md` exists but has no corresponding test class in `test_perform_behavior_action.py`
- This story is actually tested in `test_invoke_mcp.py::TestLoadAndMergeBehaviorActionInstructions`

## Level 2: Test Method-to-Scenario Mapping (Detailed Analysis)

### Bootstrap Workspace (TestBootstrapWorkspace)

**Test Methods (10):**
1. `test_bot_directory_from_environment_variable` - Verifies BOT_DIRECTORY env var is read
2. `test_workspace_directory_from_environment_variable` - Verifies WORKING_AREA env var is read
3. `test_workspace_directory_supports_legacy_working_dir_variable` - WORKING_DIR backward compatibility
4. `test_working_area_takes_precedence_over_working_dir` - WORKING_AREA > WORKING_DIR precedence
5. `test_entry_point_bootstraps_from_bot_config` - agent.json provides defaults
6. `test_environment_variable_takes_precedence_over_bot_config` - Env vars override agent.json
7. `test_missing_bot_config_with_preconfig_env_var_works` - Works with env vars only
8. `test_bot_initializes_with_bootstrapped_directories` - Bot uses bootstrapped paths
9. `test_behavior_action_state_created_in_workspace_directory` - State file in workspace
10. `test_bot_config_loaded_from_bot_directory` - Config loaded from bot dir
11. `test_behavior_folders_resolved_from_bot_directory` - Behaviors resolved from bot dir
12. `test_multiple_calls_use_cached_env_vars` - Environment caching works

**Current Scenarios:** 1 generic
**Missing Scenarios:** 11

### Close Current Action (TestCloseCurrentAction)

**Test Methods (6):**
1. `test_close_current_action_marks_complete_and_transitions` - Close transitions to next
2. `test_close_action_at_final_action_stays_at_final` - Final action stays final
3. `test_close_final_action_transitions_to_next_behavior` - Final transitions to next behavior
4. `test_close_action_saves_to_completed_actions_list` - Saves to completed list
5. `test_close_handles_action_already_completed_gracefully` - Idempotent closing
6. `test_bot_class_has_close_current_action_method` - API exists on Bot class

**Current Scenarios:** 1 generic
**Missing Scenarios:** 5

### Execute Behavior (TestExecuteBehavior)

**Test Methods (4):**
1. `test_execute_behavior_with_action_parameter` - Execute specific action
2. `test_execute_behavior_without_action_forwards_to_current` - Forward to current when no action
3. `test_execute_behavior_requires_confirmation_when_out_of_order` - Out-of-order requires confirmation
4. `test_execute_behavior_handles_entry_workflow_when_no_state` - Entry workflow handling

**Current Scenarios:** 1 generic
**Missing Scenarios:** 3

### Inject Next Behavior Reminder (TestInjectNextBehaviorReminder)

**Test Methods (3):**
1. `test_next_behavior_reminder_injected_when_final_action` - SKIPPED (complex integration)
2. `test_next_behavior_reminder_not_injected_when_not_final_action` - No reminder for non-final
3. `test_next_behavior_reminder_not_injected_when_no_next_behavior` - No reminder at end

**Current Scenarios:** 1 generic
**Missing Scenarios:** 2 (1 skipped)

### Invoke Behavior In Action Order (TestInvokeBehaviorInActionOrder)

**Test Methods (10):**
1. `test_behavior_action_order_determines_next_action_from_current_action` - Next from current
2. `test_behavior_action_order_starts_at_first_action_when_no_completed_actions` - Start at first
3. `test_behavior_action_order_uses_current_action_when_provided` - Use current when set
4. `test_behavior_action_order_falls_back_to_completed_actions_when_current_action_missing` - Fallback logic
5. `test_behavior_action_order_starts_at_first_action_when_no_state_file_exists` - No state = first
6. `test_behavior_action_order_out_of_order_navigation_removes_completed_actions_after_target` - Out-of-order clears future
7. `test_behavior_loads_workflow_order_from_behavior_specific_actions_workflow` - Load from behavior.json
8. `test_behavior_requires_actions_workflow_json_no_fallback` - Requires actions_workflow
9. `test_behavior_loads_from_actions_workflow_json` - Load from file
10. `test_different_behaviors_can_have_different_action_orders` - Different orders per behavior
11. `test_workflow_transitions_built_correctly_from_actions_workflow_json` - Transitions correct

**Current Scenarios:** 1 generic
**Missing Scenarios:** 10

### Invoke Behavior Actions In Workflow Order (TestInvokeBehaviorActionsInWorkflowOrder)

**Test Methods (1):**
1. `test_complete_workflow_end_to_end` - Full workflow integration test

**Current Scenarios:** 1 generic (but may match)
**Missing Scenarios:** 0 (but needs verification)

## Summary Statistics

- **Total Test Classes:** 19
- **Story Documents:** 8
- **Missing Story Documents:** 11
- **Total Test Methods:** ~75+
- **Total Documented Scenarios:** ~8 (all generic)
- **Missing Scenarios:** ~67+
- **Wrong Test File Mappings:** 3
- **Orphaned Story Documents:** 1

## Recommendations

1. **Create 11 missing story documents** for test classes without stories
2. **Fix test file mappings** in story-graph.json (3 stories)
3. **Move orphaned story** (`Load And Merge Behavior Action Instructions`) to Invoke MCP sub-epic
4. **Reverse-engineer 67+ scenarios** from actual test methods
5. **Update all story documents** with real scenarios instead of generic placeholders
6. **Sync story-graph.json** with actual test structure in test_perform_behavior_action.py
