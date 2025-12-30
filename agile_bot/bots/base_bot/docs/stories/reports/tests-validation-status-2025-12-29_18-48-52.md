# Validation Status - tests
Started: 2025-12-29 18:48:52
Files: 36

## no_defensive_code_in_tests
**test_perform_behavior_action.py** - 4 violation(s)

[X] ERROR (line 4217)
Line 4217: CRITICAL - Variable truthiness check - test should fail if variable is None/empty. Guard clauses are FORBIDDEN in tests. Assume test code works - if setup is wrong, let the test fail. Remove the guard clause.

[X] ERROR (line 4219)
Line 4219: CRITICAL - Variable truthiness check - test should fail if variable is None/empty. Guard clauses are FORBIDDEN in tests. Assume test code works - if setup is wrong, let the test fail. Remove the guard clause.

[X] ERROR (line 4217)
Line 4217: CRITICAL - Guard clause detected. Guard clauses are FORBIDDEN in tests. Assume test code works correctly - if setup is wrong, let the test fail. Remove defensive checks.

[X] ERROR (line 4219)
Line 4219: CRITICAL - Guard clause detected. Guard clauses are FORBIDDEN in tests. Assume test code works correctly - if setup is wrong, let the test fail. Remove defensive checks.

---

## call_production_code_directly
**conftest.py** - 4 violation(s)

[X] ERROR (line 97)
Line 97 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 101)
Line 101 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 104)
Line 104 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 183)
Line 183 uses fake/stub implementation - tests should call real production code directly

---

## call_production_code_directly
**test_execute_in_headless_mode.py** - 1 violation(s)

[X] ERROR (line 4)
Line 4 uses fake/stub implementation - tests should call real production code directly

---

## call_production_code_directly
**test_perform_behavior_action.py** - 1 violation(s)

[X] ERROR (line 1631)
Test method 'test_behavior_requires_actions_workflow_json_no_fallback' (line 1631) is empty or only contains TODO comments. Tests must call production code directly from src folder, even if the code doesn't exist yet. The test should fail with ImportError or AttributeError if production code is missing.

---

## call_production_code_directly
**test_validate_knowledge_and_content_against_rules.py** - 2 violation(s)

[X] ERROR (line 741)
Line 741 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 787)
Line 787 uses fake/stub implementation - tests should call real production code directly

---

## match_specification_scenarios
**test_execute_in_headless_mode.py** - 2 violation(s)

[!] WARNING (line 449)
Line 449 uses generic variable name "config" - use exact variable names from specification

[!] WARNING (line 462)
Line 462 uses generic variable name "config" - use exact variable names from specification

---

## match_specification_scenarios
**test_generate_cli.py** - 16 violation(s)

[!] WARNING (line 249)
Test "test_generator_creates_command_files" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator creates command files
        GIVEN: Bot configuration exists with beha...

[!] WARNING (line 271)
Test "test_generator_removes_obsolete_command_files" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator removes obsolete command files
        GIVEN: Bot configuration exists
...

[!] WARNING (line 292)
Test "test_generator_updates_bot_registry" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator updates bot registry
        GIVEN: Bot configuration exists
        AN...

[!] WARNING (line 324)
Test "test_generator_creates_cli_help_content" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator creates CLI help content
        GIVEN: Bot has behaviors configured
  ...

[!] WARNING (line 359)
Test "test_generator_creates_cli_help_with_cli_syntax" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator creates CLI help with CLI syntax
        GIVEN: Bot has behaviors confi...

[!] WARNING (line 388)
Test "test_generator_creates_cursor_help_for_behaviors" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator creates cursor help for behaviors
        GIVEN: Bot has behaviors conf...

[!] WARNING (line 424)
Test "test_generator_creates_workspace_rules_file_with_trigger_patterns" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator creates workspace rules file with trigger patterns
        GIVEN: Bot c...

[!] WARNING (line 458)
Test "test_rules_file_includes_bot_goal_and_behavior_descriptions" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules file includes bot goal and behavior descriptions
        GIVEN: Bot config ...

[!] WARNING (line 507)
Test "test_rules_file_maps_trigger_patterns_to_tool_naming_conventions" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules file maps trigger patterns to tool naming conventions
        GIVEN: A bot ...

[!] WARNING (line 553)
Test "test_full_awareness_generation_workflow" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Full awareness generation workflow
        GIVEN: MCP Server Generator initialize...

[!] WARNING (line 627)
Test "test_action_factory_returns_clarify_action_class" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ActionFactory returns ClarifyContextAction for clarify
        GIVEN: ActionFacto...

[!] WARNING (line 643)
Test "test_action_factory_returns_strategy_action_class" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ActionFactory returns StrategyAction for strategy
        GIVEN: ActionFactory is...

[!] WARNING (line 659)
Test "test_action_factory_returns_none_for_unknown_action" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ActionFactory returns None for unknown action
        GIVEN: ActionFactory is ava...

[!] WARNING (line 675)
Test "test_parameters_extracted_from_clarify_context_use_dashes" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Parameters from ClarifyActionContext use dashes
        GIVEN: ClarifyActionConte...

[!] WARNING (line 692)
Test "test_parameters_extracted_from_strategy_context_use_dashes" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Parameters from StrategyActionContext use dashes
        GIVEN: StrategyActionCon...

[!] WARNING (line 709)
Test "test_all_known_actions_have_context_classes" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: All known actions have context classes
        GIVEN: List of known action names
...

---

## match_specification_scenarios
**test_helpers.py** - 4 violation(s)

[!] WARNING (line 2036)
Test "test_finds_exploration_folder_with_number_prefix" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Find exploration folder with number prefix
        GIVEN: Behavior folder exists ...

[!] WARNING (line 2056)
Test "test_handles_prioritization_folder_with_prefix" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Handles Prioritization Folder With Prefix
        GIVEN: Behavior folder exists a...

[!] WARNING (line 2074)
Test "test_handles_scenarios_folder_with_prefix" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Handles Scenarios Folder With Prefix
        GIVEN: Behavior folder exists as 'sc...

[!] WARNING (line 2092)
Test "test_handles_examples_folder_with_prefix" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Handles Examples Folder With Prefix
        GIVEN: Behavior folder exists as 'exa...

---

## match_specification_scenarios
**test_manage_bot_scope_through_cli.py** - 9 violation(s)

[!] WARNING (line 80)
Test "test_user_sets_knowledge_graph_scope_filter" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: User sets knowledge graph scope filter
        GIVEN: CLI is at shape.build.instr...

[!] WARNING (line 109)
Test "test_user_executes_build_with_active_knowledge_graph_scope" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: User executes build with active knowledge graph scope
        GIVEN: CLI is at sh...

[!] WARNING (line 145)
Test "test_user_sets_files_scope_filter" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: User sets files scope filter
        GIVEN: CLI is at code.validate.instructions
...

[!] WARNING (line 174)
Test "test_user_executes_validate_with_active_files_scope" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: User executes validate with active files scope
        GIVEN: CLI is at code.vali...

[!] WARNING (line 214)
Test "test_setting_file_scope_replaces_story_scope" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Setting file scope replaces existing story scope
        GIVEN: CLI has story sco...

[!] WARNING (line 252)
Test "test_setting_story_scope_replaces_file_scope" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Setting story scope replaces existing file scope
        GIVEN: CLI has file scop...

[!] WARNING (line 290)
Test "test_scope_only_has_one_type" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Scope object can only have one type at a time
        GIVEN: Any scope is set
   ...

[!] WARNING (line 318)
Test "test_user_clears_all_scope_filters" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: User clears all scope filters
        GIVEN: CLI is at shape.build.instructions
 ...

[!] WARNING (line 351)
Test "test_user_executes_build_after_clearing_scope" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: User executes build after clearing scope
        GIVEN: CLI is at shape.build.ins...

---

## match_specification_scenarios
**test_perform_behavior_action.py** - 99 violation(s)

[!] WARNING (line 4195)
Test method "test_bot_paths_uses_default_paths_when_environment_variables_not_set" has vague name - should clearly describe behavior from specification scenario

[!] WARNING (line 3975)
Line 3975 uses generic variable name "result" - use exact variable names from specification

[!] WARNING (line 3995)
Line 3995 uses generic variable name "result" - use exact variable names from specification

[!] WARNING (line 4014)
Line 4014 uses generic variable name "result" - use exact variable names from specification

[!] WARNING (line 4033)
Line 4033 uses generic variable name "result" - use exact variable names from specification

[!] WARNING (line 4053)
Line 4053 uses generic variable name "result" - use exact variable names from specification

[!] WARNING (line 630)
Test "test_next_behavior_reminder_injected_when_final_action" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Next behavior reminder is injected when action is final action
        GIVEN: val...

[!] WARNING (line 652)
Test "test_next_behavior_reminder_not_injected_when_not_final_action" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Next behavior reminder is NOT injected when action is not final
        GIVEN: va...

[!] WARNING (line 672)
Test "test_next_behavior_reminder_not_injected_when_no_next_behavior" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Next behavior reminder is NOT injected when current behavior is last in sequence
...

[!] WARNING (line 726)
Test "test_close_action_at_final_action_stays_at_final" has scenario but no matching story found in specification. Scenario: Scenario: Close final action stays at final action...

[!] WARNING (line 745)
Test "test_close_final_action_transitions_to_next_behavior" has scenario but no matching story found in specification. Scenario: Scenario: Close final action and verify it's marked complete...

[!] WARNING (line 762)
Test "test_close_action_saves_to_completed_actions_list" has scenario but no matching story found in specification. Scenario: Scenario: Closing action saves it to completed_actions list...

[!] WARNING (line 777)
Test "test_close_handles_action_already_completed_gracefully" has scenario but no matching story found in specification. Scenario: Scenario: Idempotent close (already completed)...

[!] WARNING (line 796)
Test "test_bot_class_has_close_current_action_method" has scenario but no matching story found in specification. Scenario: Scenario: Bot class exposes close_current_action method...

[!] WARNING (line 1025)
Test "test_complete_workflow_end_to_end" has scenario but no matching story found in specification. Scenario: 
        Complete end-to-end workflow test demonstrating all fixes working together.

        Flow:
...

[!] WARNING (line 1530)
Test "test_behavior_action_order_determines_next_action_from_current_action" has scenario but no matching story found in specification. Scenario: Scenario: Behavior action order determines next action from current_action (source of truth)...

[!] WARNING (line 1545)
Test "test_behavior_action_order_starts_at_first_action_when_no_completed_actions" has scenario but no matching story found in specification. Scenario: Scenario: No completed actions yet...

[!] WARNING (line 1556)
Test "test_behavior_action_order_uses_current_action_when_provided" has scenario but no matching story found in specification. Scenario: Scenario: Behavior action order uses current_action when provided...

[!] WARNING (line 1569)
Test "test_behavior_action_order_falls_back_to_completed_actions_when_current_action_missing" has scenario but no matching story found in specification. Scenario: Scenario: Behavior action order falls back to completed_actions when current_action is missing...

[!] WARNING (line 1581)
Test "test_behavior_action_order_starts_at_first_action_when_no_state_file_exists" has scenario but no matching story found in specification. Scenario: Scenario: No behavior_action_state.json file exists (fresh start)...

[!] WARNING (line 1594)
Test "test_behavior_action_order_out_of_order_navigation_removes_completed_actions_after_target" has scenario but no matching story found in specification. Scenario: Scenario: When navigating out of order, completed actions after target are removed...

[!] WARNING (line 1619)
Test "test_behavior_loads_workflow_order_from_behavior_specific_actions_workflow" has scenario but no matching story found in specification. Scenario: Scenario: Behavior loads workflow order from behaviors/{behavior_name}/behavior.json...

[!] WARNING (line 1631)
Test "test_behavior_requires_actions_workflow_json_no_fallback" has scenario but no matching story found in specification. Scenario: Scenario: Behavior REQUIRES behavior.json - no fallback exists...

[!] WARNING (line 1636)
Test "test_behavior_loads_from_actions_workflow_json" has scenario but no matching story found in specification. Scenario: Scenario: Behavior loads workflow order from behavior.json...

[!] WARNING (line 1673)
Test "test_different_behaviors_can_have_different_action_orders" has scenario but no matching story found in specification. Scenario: Scenario: Different behaviors can have different action orders...

[!] WARNING (line 1684)
Test "test_workflow_transitions_built_correctly_from_actions_workflow_json" has scenario but no matching story found in specification. Scenario: Scenario: Workflow transitions are built correctly from behavior.json...

[!] WARNING (line 1927)
Test "test_execute_behavior_with_action_parameter" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Execute behavior with action parameter
        GIVEN: Bot has behavior 'shape' wi...

[!] WARNING (line 1940)
Test "test_execute_behavior_without_action_forwards_to_current" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Execute behavior without action parameter forwards to current action
        GIVE...

[!] WARNING (line 1956)
Test "test_execute_behavior_requires_confirmation_when_out_of_order" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Execute behavior executes directly when called (no order checking)
        GIVEN:...

[!] WARNING (line 1971)
Test "test_execute_behavior_handles_entry_workflow_when_no_state" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Execute behavior executes directly when no workflow state exists
        GIVEN: N...

[!] WARNING (line 2023)
Test "test_action_loads_context_data_into_instructions" has scenario but no matching story found in specification. Scenario: Test that Action loads clarification, strategy, and context files into instructions....

[!] WARNING (line 2169)
Test "test_action_injects_workflow_breadcrumbs_when_bot_instance_exists" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Action injects workflow breadcrumbs when bot instance exists
        GIVEN: Bot i...

[!] WARNING (line 2201)
Test "test_breadcrumbs_show_completed_behaviors_when_all_actions_completed" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Breadcrumbs show completed behaviors when all actions completed
        GIVEN: Mu...

[!] WARNING (line 2224)
Test "test_breadcrumbs_show_next_step_command_when_next_action_exists" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Breadcrumbs show next step command when next action exists
        GIVEN: Current...

[!] WARNING (line 2247)
Test "test_breadcrumbs_not_injected_when_no_bot_instance" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Breadcrumbs are not injected when behavior has no bot instance
        GIVEN: Beh...

[!] WARNING (line 2574)
Test "test_bot_instantiation_with_bot_name_and_workspace" has scenario but no matching story found in specification. Scenario: Scenario: Bot can be instantiated with bot_name and workspace (BotConfig merged into Bot)....

[!] WARNING (line 2590)
Test "test_bot_name_property" has scenario but no matching story found in specification. Scenario: Scenario: Bot.name property returns bot name from config (BotConfig merged into Bot)....

[!] WARNING (line 2605)
Test "test_behaviors_names_property" has scenario but no matching story found in specification. Scenario: Scenario: Behaviors.names property discovers from folders....

[!] WARNING (line 2628)
Test "test_behaviors_names_empty_when_missing" has scenario but no matching story found in specification. Scenario: Scenario: Behaviors.names returns empty list when behaviors missing....

[!] WARNING (line 2643)
Test "test_bot_base_actions_path_property" has scenario but no matching story found in specification. Scenario: Scenario: Bot.base_actions_path property returns path to base_actions directory (BotConfig merged in...

[!] WARNING (line 2670)
Test "test_behavior_config_loads_fields_and_actions" has scenario but no matching story found in specification. Scenario: Scenario: BehaviorConfig loads fields and sorts actions_workflow by order....

[!] WARNING (line 2834)
Test "test_load_behaviors_from_bot_config" has scenario but no matching story found in specification. Scenario: Scenario: Bot behaviors are loaded from BotConfig....

[!] WARNING (line 2846)
Test "test_load_behaviors_sets_first_as_current" has scenario but no matching story found in specification. Scenario: Scenario: When behaviors are loaded, first behavior is set as current....

[!] WARNING (line 2858)
Test "test_find_behavior_by_name" has scenario but no matching story found in specification. Scenario: Scenario: Behavior can be found by name when it exists....

[!] WARNING (line 2872)
Test "test_find_behavior_returns_none_when_not_found" has scenario but no matching story found in specification. Scenario: Scenario: Finding behavior by name returns None when behavior doesn't exist....

[!] WARNING (line 2885)
Test "test_get_next_behavior" has scenario but no matching story found in specification. Scenario: Scenario: Next behavior in sequence can be retrieved....

[!] WARNING (line 2899)
Test "test_get_next_behavior_returns_none_at_end" has scenario but no matching story found in specification. Scenario: Scenario: Getting next behavior returns None when at last behavior....

[!] WARNING (line 2913)
Test "test_iterate_all_behaviors" has scenario but no matching story found in specification. Scenario: Scenario: All behaviors can be iterated....

[!] WARNING (line 2929)
Test "test_check_behavior_exists" has scenario but no matching story found in specification. Scenario: Scenario: Can check if a behavior exists....

[!] WARNING (line 2944)
Test "test_navigate_to_behavior" has scenario but no matching story found in specification. Scenario: Scenario: Can navigate to a specific behavior....

[!] WARNING (line 2957)
Test "test_save_current_behavior_state" has scenario but no matching story found in specification. Scenario: Scenario: Current behavior state is persisted to behavior_action_state.json....

[!] WARNING (line 2971)
Test "test_load_behavior_state_from_file" has scenario but no matching story found in specification. Scenario: Scenario: Current behavior state is restored from behavior_action_state.json....

[!] WARNING (line 3125)
Test "test_load_actions_from_behavior_config" has scenario but no matching story found in specification. Scenario: Scenario: Actions are loaded from BehaviorConfig....

[!] WARNING (line 3147)
Test "test_load_actions_sets_first_as_current" has scenario but no matching story found in specification. Scenario: Scenario: When actions are loaded, first action is set as current....

[!] WARNING (line 3169)
Test "test_find_action_by_name" has scenario but no matching story found in specification. Scenario: Scenario: Action can be found by name when it exists....

[!] WARNING (line 3195)
Test "test_find_action_returns_none_when_not_found" has scenario but no matching story found in specification. Scenario: Scenario: Finding action by name returns None when action doesn't exist....

[!] WARNING (line 3216)
Test "test_find_action_by_order" has scenario but no matching story found in specification. Scenario: Scenario: Action can be found by order when it exists....

[!] WARNING (line 3241)
Test "test_get_next_action" has scenario but no matching story found in specification. Scenario: Scenario: Next action in sequence can be retrieved....

[!] WARNING (line 3267)
Test "test_get_next_action_returns_none_at_end" has scenario but no matching story found in specification. Scenario: Scenario: Getting next action returns None when at last action....

[!] WARNING (line 3291)
Test "test_iterate_all_actions" has scenario but no matching story found in specification. Scenario: Scenario: All actions can be iterated....

[!] WARNING (line 3319)
Test "test_navigate_to_action" has scenario but no matching story found in specification. Scenario: Scenario: Can navigate to a specific action....

[!] WARNING (line 3344)
Test "test_save_current_action_state" has scenario but no matching story found in specification. Scenario: Scenario: Current action state is persisted to behavior_action_state.json....

[!] WARNING (line 3369)
Test "test_load_action_state_from_file" has scenario but no matching story found in specification. Scenario: Scenario: Current action state is restored from behavior_action_state.json....

[!] WARNING (line 3394)
Test "test_close_current_action" has scenario but no matching story found in specification. Scenario: Scenario: Closing current action marks it complete and moves to next....

[!] WARNING (line 3426)
Test "test_action_merges_instructions_from_base_and_behavior" has scenario but no matching story found in specification. Scenario: Scenario: Action merges instructions from BaseActionConfig and Behavior config....

[!] WARNING (line 3487)
Test "test_action_loads_config_fields" has scenario but no matching story found in specification. Scenario: Scenario: Action loads fields from action_config.json (BaseActionConfig merged into Action)....

[!] WARNING (line 3588)
Test "test_bot_paths_instantiation_with_environment_variables" has scenario but no matching story found in specification. Scenario: Scenario: BotPaths can be instantiated when environment variables are set....

[!] WARNING (line 3600)
Test "test_bot_paths_workspace_directory_property" has scenario but no matching story found in specification. Scenario: Scenario: BotPaths.workspace_directory property returns workspace path from WORKING_AREA....

[!] WARNING (line 3611)
Test "test_bot_paths_bot_directory_property" has scenario but no matching story found in specification. Scenario: Scenario: BotPaths.bot_directory property returns bot directory from BOT_DIRECTORY....

[!] WARNING (line 3622)
Test "test_bot_paths_base_actions_directory_property" has scenario but no matching story found in specification. Scenario: Scenario: BotPaths.base_actions_directory property returns base_actions directory.
        
        ...

[!] WARNING (line 3639)
Test "test_bot_paths_python_workspace_root_property" has scenario but no matching story found in specification. Scenario: Scenario: BotPaths.python_workspace_root property returns Python workspace root....

[!] WARNING (line 3650)
Test "test_bot_paths_find_repo_root_method" has scenario but no matching story found in specification. Scenario: Scenario: BotPaths.find_repo_root() method returns repository root....

[!] WARNING (line 3662)
Test "test_bot_paths_instantiation_with_workspace_path" has scenario but no matching story found in specification. Scenario: Scenario: BotPaths can be instantiated with explicit workspace path....

[!] WARNING (line 3859)
Test "test_base_instructions_property_returns_instructions_from_config" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Base instructions property returns instructions from config
        GIVEN: BaseAc...

[!] WARNING (line 3883)
Test "test_behavior_config_loads_correct_behavior_from_behavior_json_file" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behavior config loads correct behavior from behavior.json file
        GIVEN: beh...

[!] WARNING (line 3907)
Test "test_behavior_config_provides_access_to_config_objects" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behavior config provides access to config objects
        GIVEN: BehaviorConfig l...

[!] WARNING (line 3942)
Test "test_behaviors_collection_loads_behaviors_from_bot_config" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors collection loads behaviors from bot config
        GIVEN: BotConfig wit...

[!] WARNING (line 3961)
Test "test_behaviors_find_by_name_returns_behavior_when_exists" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors find by name returns behavior when exists
        GIVEN: Behaviors coll...

[!] WARNING (line 3981)
Test "test_behaviors_find_by_name_returns_none_when_does_not_exist" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors find by name returns none when does not exist
        GIVEN: Behaviors ...

[!] WARNING (line 4000)
Test "test_behaviors_check_exists_returns_true_when_behavior_exists" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors check exists returns true when behavior exists
        GIVEN: Behaviors...

[!] WARNING (line 4019)
Test "test_behaviors_check_exists_returns_false_when_behavior_does_not_exist" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors check exists returns false when behavior does not exist
        GIVEN: ...

[!] WARNING (line 4038)
Test "test_behaviors_current_property_returns_current_behavior" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors current property returns current behavior
        GIVEN: Behaviors coll...

[!] WARNING (line 4059)
Test "test_behaviors_next_property_returns_next_behavior" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors next property returns next behavior
        GIVEN: Behaviors collection...

[!] WARNING (line 4080)
Test "test_behaviors_navigate_to_behavior_updates_current_behavior" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors navigate to behavior updates current behavior
        GIVEN: Behaviors ...

[!] WARNING (line 4099)
Test "test_behaviors_close_current_marks_behavior_and_action_complete" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors close current marks behavior and action complete
        GIVEN: Behavio...

[!] WARNING (line 4121)
Test "test_behaviors_execute_current_executes_current_behavior" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors execute current executes current behavior
        GIVEN: Behaviors coll...

[!] WARNING (line 4145)
Test "test_bot_paths_resolves_bot_directory_from_environment" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Bot paths resolves bot directory from environment
        GIVEN: BOT_DIRECTORY en...

[!] WARNING (line 4161)
Test "test_bot_paths_resolves_workspace_directory_from_environment" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Bot paths resolves workspace directory from environment
        GIVEN: WORKING_AR...

[!] WARNING (line 4177)
Test "test_bot_paths_properties_return_resolved_paths" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Bot paths properties return resolved paths
        GIVEN: BotPaths with resolved ...

[!] WARNING (line 4195)
Test "test_bot_paths_uses_default_paths_when_environment_variables_not_set" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Bot paths uses default paths when environment variables not set
        GIVEN: No...

[!] WARNING (line 4380)
Test "test_build_scope_filters_by_story_names" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: BuildScope filters story graph by story names
        GIVEN: Story graph with mul...

[!] WARNING (line 4398)
Test "test_build_scope_filters_by_epic_names" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: BuildScope filters story graph by epic names
        GIVEN: Story graph with mult...

[!] WARNING (line 4416)
Test "test_build_scope_filters_by_increment_priorities" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: BuildScope filters story graph by increment priorities
        GIVEN: Story graph...

[!] WARNING (line 4434)
Test "test_build_scope_returns_all_when_scope_is_all" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: BuildScope returns all when scope is all
        GIVEN: Story graph with multiple...

[!] WARNING (line 4451)
Test "test_validation_scope_filters_by_story_names" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ValidationScope filters story graph by story names
        GIVEN: Story graph wit...

[!] WARNING (line 4469)
Test "test_validation_scope_filters_by_epic_names" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ValidationScope filters story graph by epic names
        GIVEN: Story graph with...

[!] WARNING (line 4487)
Test "test_action_scope_filters_by_story_names" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ActionScope filters story graph by story names
        GIVEN: Story graph with mu...

[!] WARNING (line 4505)
Test "test_action_scope_filters_by_epic_names" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ActionScope filters story graph by epic names
        GIVEN: Story graph with mul...

[!] WARNING (line 4523)
Test "test_action_scope_returns_all_when_scope_is_all" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ActionScope returns all when scope is all
        GIVEN: Story graph with multipl...

---

## match_specification_scenarios
**test_validate_knowledge_and_content_against_rules.py** - 57 violation(s)

[!] WARNING (line 5472)
Line 5472 uses generic variable name "result" - use exact variable names from specification

[!] WARNING (line 5509)
Line 5509 uses generic variable name "result" - use exact variable names from specification

[!] WARNING (line 2254)
Test "test_track_activity_when_validate_action_starts" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Track activity when validate action starts
        GIVEN: behavior is 'exploratio...

[!] WARNING (line 2271)
Test "test_track_activity_when_validate_action_completes" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Track activity when validate action completes
        GIVEN: validate action star...

[!] WARNING (line 2304)
Test "test_track_multiple_validate_invocations_across_behaviors" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Track multiple validate invocations across behaviors
        GIVEN: activity log ...

[!] WARNING (line 2335)
Test "test_activity_log_maintains_chronological_order" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Activity Log Maintains Chronological Order
        GIVEN: activity log contains 1...

[!] WARNING (line 2368)
Test "test_validate_marks_workflow_as_complete" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: validate marks workflow as complete
        GIVEN: validate action is complete
  ...

[!] WARNING (line 2385)
Test "test_validate_does_not_inject_next_action_instructions" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: validate does NOT inject next action instructions
        GIVEN: validate action ...

[!] WARNING (line 2446)
Test "test_workflow_does_not_transition_after_validate" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Workflow does NOT transition after validate
        GIVEN: validate action is com...

[!] WARNING (line 2464)
Test "test_behavior_workflow_completes_at_terminal_action" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behavior workflow completes at terminal action
        GIVEN: exploration behavio...

[!] WARNING (line 2503)
Test "test_validate_returns_instructions_with_rules_as_context" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: validate returns instructions with rules as supporting context
        GIVEN: val...

[!] WARNING (line 2516)
Test "test_validate_provides_report_path_for_saving_validation_report" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: validate provides report_path for saving validation report
        GIVEN: validat...

[!] WARNING (line 2682)
Test "test_validate_raises_exception_when_story_graph_not_found" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ValidateRulesAction raises exception when story graph not found
        GIVEN: St...

[!] WARNING (line 2697)
Test "test_validate_raises_exception_when_story_graph_invalid_json" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ValidateRulesAction raises exception when story graph has syntax error
        GI...

[!] WARNING (line 3315)
Test "test_validate_respects_scope" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Validate that validate only processes stories within specified scope.
        
  ...

[!] WARNING (line 3356)
Test "test_validate_scope_extraction" has scenario but no matching story found in specification. Scenario: Test that scope extraction functions work correctly....

[!] WARNING (line 3396)
Test "test_validate_with_test_file_scope_parameter" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Validate test file using test_file scope parameter
        GIVEN: A test file exi...

[!] WARNING (line 3414)
Test "test_validate_with_test_files_scope_parameter" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Validate multiple test files using test_files scope parameter
        GIVEN: Mult...

[!] WARNING (line 3432)
Test "test_validate_verifies_test_files_passed_to_scanner" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Verify that test files from scope parameters are actually passed to TestScanner
 ...

[!] WARNING (line 3646)
Test "test_scanner_detects_violations" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Scanner detects violations in bad examples
        GIVEN: Scanner class path, beh...

[!] WARNING (line 3685)
Test "test_validate_code_files_action_accepts_test_files_parameter" has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction accepts test files via test_files parameter...

[!] WARNING (line 3714)
Test "test_validate_code_files_action_validates_each_file_from_parameters" has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction validates each file provided via test_files parameter...

[!] WARNING (line 3727)
Test "test_validate_code_files_action_merges_violations_from_knowledge_graph_and_files" has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction merges violations from knowledge graph validation and code file va...

[!] WARNING (line 3740)
Test "test_validate_code_files_action_works_for_tests_behavior" has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction works for tests behavior (test files)...

[!] WARNING (line 3769)
Test "test_validate_code_files_action_accepts_code_files_parameter" has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction accepts source files via code_files parameter...

[!] WARNING (line 3794)
Test "test_validate_code_files_action_works_for_code_behavior" has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction works for code behavior (source files)...

[!] WARNING (line 3813)
Test "test_validate_code_files_action_returns_early_when_no_files_provided" has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction returns knowledge graph results when no files provided...

[!] WARNING (line 4279)
Test "test_rules_loads_both_bot_level_and_behavior_specific_rules_when_instantiated_with_behavior" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules loads both bot-level and behavior-specific rules when instantiated with beh...

[!] WARNING (line 4312)
Test "test_find_by_name_returns_rule_when_rule_exists" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Find by name returns rule when rule exists
        GIVEN: Rules collection with r...

[!] WARNING (line 4336)
Test "test_find_by_name_returns_none_when_rule_does_not_exist" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Find by name returns none when rule does not exist
        GIVEN: Rules collectio...

[!] WARNING (line 4355)
Test "test_find_by_name_searches_both_bot_level_and_behavior_specific_rules" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Find by name searches both bot-level and behavior-specific rules
        GIVEN: R...

[!] WARNING (line 4389)
Test "test_iterate_returns_all_rules_in_collection" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Iterate returns all rules in collection
        GIVEN: Rules collection with mult...

[!] WARNING (line 4413)
Test "test_iterate_returns_empty_iterator_when_no_rules_loaded" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Iterate returns empty iterator when no rules loaded
        GIVEN: Rules collecti...

[!] WARNING (line 4432)
Test "test_iterate_includes_both_bot_level_and_behavior_specific_rules" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Iterate includes both bot-level and behavior-specific rules
        GIVEN: Rules ...

[!] WARNING (line 4462)
Test "test_rule_loads_from_json_file_path" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rule loads from JSON file path
        GIVEN: Rule JSON file exists
        WHEN:...

[!] WARNING (line 4481)
Test "test_rule_loads_embedded_rule_from_validation_rules_json" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rule loads embedded rule from validation_rules.json
        GIVEN: validation_rul...

[!] WARNING (line 4498)
Test "test_rule_extracts_name_from_file_path" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rule extracts name from file path
        GIVEN: Rule file 'test_rule.json'
     ...

[!] WARNING (line 4515)
Test "test_rule_extracts_name_from_embedded_rule_data" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rule extracts name from embedded rule data
        GIVEN: Embedded rule data with...

[!] WARNING (line 4545)
Test "test_rule_scanner_properties_return_scanner_instance_or_none" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rule scanner properties return scanner instance or None
        GIVEN: Rule with ...

[!] WARNING (line 4567)
Test "test_rule_provides_access_to_config_properties" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rule provides access to config properties
        GIVEN: Rule loaded with complet...

[!] WARNING (line 4603)
Test "test_validation_scope_created_with_different_parameter_combinations" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Validation scope created with different parameter combinations
        GIVEN: Par...

[!] WARNING (line 4621)
Test "test_scanner_loader_loads_scanner_from_exact_module_path" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Scanner loader loads scanner from exact module path
        GIVEN: Valid scanner ...

[!] WARNING (line 4638)
Test "test_scanner_loader_loads_scanner_from_base_bot_scanners_directory" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Scanner loader loads scanner from base_bot scanners directory
        GIVEN: Scan...

[!] WARNING (line 4655)
Test "test_scanner_loader_loads_scanner_from_bot_specific_scanners_directory" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Scanner loader loads scanner from bot-specific scanners directory
        GIVEN: ...

[!] WARNING (line 4673)
Test "test_scanner_loader_validates_scanner_inherits_from_scanner_base_class" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Scanner loader validates scanner inherits from Scanner base class
        GIVEN: ...

[!] WARNING (line 4699)
Test "test_action_uses_rules_collection_to_load_rules" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Action uses Rules collection to load rules
        GIVEN: ValidateRulesAction wit...

[!] WARNING (line 4715)
Test "test_action_uses_rule_class_to_access_rule_properties" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Action uses Rule class to access rule properties
        GIVEN: ValidateRulesActi...

[!] WARNING (line 4732)
Test "test_action_uses_scanner_loader_to_load_scanner_classes" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Action uses ScannerLoader to load scanner classes
        GIVEN: ValidateRulesAct...

[!] WARNING (line 4749)
Test "test_action_uses_validation_scope_to_define_validation_scope" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Action uses ValidationScope to define validation scope
        GIVEN: ValidateRul...

[!] WARNING (line 4770)
Test "test_action_uses_scanner_loader_service_to_load_scanner_classes" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Action uses ScannerLoader service to load scanner classes
        GIVEN: Rule wit...

[!] WARNING (line 4786)
Test "test_scanner_loader_loads_scanner_from_multiple_possible_paths" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ScannerLoader loads scanner from multiple possible paths
        GIVEN: ScannerLo...

[!] WARNING (line 4803)
Test "test_scanner_loader_validates_scanner_inherits_from_scanner_base_class" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ScannerLoader validates scanner inherits from Scanner base class
        GIVEN: S...

[!] WARNING (line 5372)
Test "test_rules_action_loads_rules_for_behavior" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules action loads rules for behavior
        GIVEN: behavior is 'code' with rule...

[!] WARNING (line 5403)
Test "test_formatted_rules_digest_returns_compact_format" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: formatted_rules_digest returns compact format
        GIVEN: behavior has 2 rules...

[!] WARNING (line 5443)
Test "test_rules_action_includes_message_in_context" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules action includes user message in context
        GIVEN: behavior is 'code' a...

[!] WARNING (line 5480)
Test "test_rules_action_outputs_to_ai_context_only" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules action outputs digest to AI context only (not display)
        GIVEN: behav...

[!] WARNING (line 5523)
Test "test_rules_action_is_not_workflow_action" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules action is not part of workflow
        GIVEN: rules action is initialized
 ...

---

## place_imports_at_top
**test_perform_behavior_action.py** - 4 violation(s)

[X] ERROR (line 3682)
Import statement found after non-import code. Move all imports to the top of the file.

```python
# ============================================================================

from unittest.mock import Mock
from agile_bot.bots.base_bot.src.bot.merged_instructions import MergedInstructions
```

[X] ERROR (line 3683)
Import statement found after non-import code. Move all imports to the top of the file.

```python

from unittest.mock import Mock
from agile_bot.bots.base_bot.src.bot.merged_instructions import MergedInstructions
# BaseActionConfig deleted - Action already has config loading
```

[X] ERROR (line 3686)
Import statement found after non-import code. Move all imports to the top of the file.

```python
# BaseActionConfig deleted - Action already has config loading
# BehaviorConfig merged into Behavior - use Behavior directly
from agile_bot.bots.base_bot.src.bot.behaviors import Behaviors
# BotConfig merged into Bot - use Bot directly
```

[X] ERROR (line 3688)
Import statement found after non-import code. Move all imports to the top of the file.

```python
from agile_bot.bots.base_bot.src.bot.behaviors import Behaviors
# BotConfig merged into Bot - use Bot directly
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths

```

---

## place_imports_at_top
**test_validate_knowledge_and_content_against_rules.py** - 4 violation(s)

[X] ERROR (line 2116)
Import statement found after non-import code. Move all imports to the top of the file.

```python


from agile_bot.bots.base_bot.test.test_helpers import create_validation_rules

```

[X] ERROR (line 3833)
Import statement found after non-import code. Move all imports to the top of the file.

```python
# ============================================================================

from agile_bot.bots.base_bot.src.actions.rules.rules import Rules
from agile_bot.bots.base_bot.src.actions.validate.validation_scope import ValidationScope
```

[X] ERROR (line 3834)
Import statement found after non-import code. Move all imports to the top of the file.

```python

from agile_bot.bots.base_bot.src.actions.rules.rules import Rules
from agile_bot.bots.base_bot.src.actions.validate.validation_scope import ValidationScope
from agile_bot.bots.base_bot.src.scanners.scanner_loader import ScannerLoader
```

[X] ERROR (line 3835)
Import statement found after non-import code. Move all imports to the top of the file.

```python
from agile_bot.bots.base_bot.src.actions.rules.rules import Rules
from agile_bot.bots.base_bot.src.actions.validate.validation_scope import ValidationScope
from agile_bot.bots.base_bot.src.scanners.scanner_loader import ScannerLoader

```

---

## use_class_based_organization
**conftest.py** - 1 violation(s)

[X] ERROR
Test file name "conftest" does not match any sub-epic name and test methods do not span multiple sub-epics - file should be named test_<sub_epic_name>.py.

---

## use_class_based_organization
**test_execute_in_headless_mode.py** - 1 violation(s)

[X] ERROR
Test method "test_appends_total_loops" appears abbreviated - should match scenario name exactly

---

## use_class_based_organization
**test_helpers.py** - 1 violation(s)

[X] ERROR
Test file name "test_helpers" does not match any sub-epic name and test methods do not span multiple sub-epics - file should be named test_<sub_epic_name>.py.

---

## use_class_based_organization
**test_perform_behavior_action.py** - 6 violation(s)

[X] ERROR
Test method "test_bot_name_property" appears abbreviated - should match scenario name exactly

[X] ERROR
Test method "test_get_next_behavior" appears abbreviated - should match scenario name exactly

[X] ERROR
Test method "test_find_action_by_name" appears abbreviated - should match scenario name exactly

[X] ERROR
Test method "test_get_next_action" appears abbreviated - should match scenario name exactly

[X] ERROR
Test method "test_iterate_all_actions" appears abbreviated - should match scenario name exactly

[X] ERROR
Test method "test_navigate_to_action" appears abbreviated - should match scenario name exactly

---

## use_class_based_organization
**test_validate_knowledge_and_content_against_rules.py** - 2 violation(s)

[X] ERROR
Test method "test_skiprule_via_scope" appears abbreviated - should match scenario name exactly

[X] ERROR
Test class "TestScanner" appears abbreviated - should match story name exactly (Test<ExactStoryName>)

---

## use_exact_variable_names
**test_execute_in_headless_mode.py** - 7 violation(s)

[!] WARNING (line 255)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 277)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 298)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 319)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 342)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 369)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 394)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

---

## use_exact_variable_names
**test_perform_behavior_action.py** - 7 violation(s)

[!] WARNING (line 3871)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 3975)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 3995)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 4014)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 4033)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 4053)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 4074)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

---

## use_exact_variable_names
**test_validate_knowledge_and_content_against_rules.py** - 7 violation(s)

[!] WARNING (line 4330)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 4350)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 4408)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 4427)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 4453)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 5472)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 5509)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

---

## use_given_when_then_helpers
**test_generate_cli.py** - 4 violation(s)

[X] ERROR (line 340)
Lines 340-345: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
from agile_bot.bots.base_bot.src.bot.bot import Bot
bot = Bot(bot_name=bot_name, bot_directory=bot_dir, config_path=bot_config)
formatter = Mock()
...

[X] ERROR (line 374)
Lines 374-379: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
from agile_bot.bots.base_bot.src.bot.bot import Bot
bot = Bot(bot_name=bot_name, bot_directory=bot_dir, config_path=bot_config)
formatter = Mock()
...

[X] ERROR (line 406)
Lines 406-412: Multiple inline steps (7 lines) should be extracted into a Given/When/Then helper function. Block:
from agile_bot.bots.base_bot.src.bot.bot import Bot
bot = Bot(bot_name=bot_name, bot_directory=bot_dir, config_path=bot_config)
formatter = Mock()
...

[X] ERROR (line 540)
Lines 540-546: Multiple inline steps (7 lines) should be extracted into a Given/When/Then helper function. Block:
"""
SCENARIO: Generator handles file write errors with clear error message
GIVEN: .cursor/rules/ directory is write-protected
...

---

## use_given_when_then_helpers
**test_manage_bot_scope_through_cli.py** - 8 violation(s)

[X] ERROR (line 96)
Lines 96-102: Multiple inline steps (7 lines) should be extracted into a Given/When/Then helper function. Block:
bot = Bot(
bot_name='story_bot',
bot_directory=bot_directory,
...

[X] ERROR (line 126)
Lines 126-131: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
bot = Bot(
bot_name='story_bot',
bot_directory=bot_directory,
...

[X] ERROR (line 161)
Lines 161-167: Multiple inline steps (7 lines) should be extracted into a Given/When/Then helper function. Block:
bot = Bot(
bot_name='story_bot',
bot_directory=bot_directory,
...

[X] ERROR (line 191)
Lines 191-196: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
bot = Bot(
bot_name='story_bot',
bot_directory=bot_directory,
...

[X] ERROR (line 230)
Lines 230-235: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
bot = Bot(
bot_name='story_bot',
bot_directory=bot_directory,
...

[X] ERROR (line 268)
Lines 268-273: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
bot = Bot(
bot_name='story_bot',
bot_directory=bot_directory,
...

[X] ERROR (line 335)
Lines 335-340: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
bot = Bot(
bot_name='story_bot',
bot_directory=bot_directory,
...

[X] ERROR (line 368)
Lines 368-373: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
bot = Bot(
bot_name='story_bot',
bot_directory=bot_directory,
...

---

## use_given_when_then_helpers
**test_navigate_bot_behaviors_and_actions_with_cli.py** - 3 violation(s)

[X] ERROR (line 48)
Lines 48-51: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
state = _read_state(workspace_dir)
assert state["current_behavior"] == "story_bot.shape"
if state.get("current_action"):
...

[X] ERROR (line 61)
Lines 61-65: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
assert actions.current_action_name == "strategy"
state = _read_state(workspace_dir)
completed = [a.get("action_state") for a in state.get("completed_actions", [])]
...

[X] ERROR (line 75)
Lines 75-78: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
actions.close_current()  # completes clarify, moves to strategy
remaining = actions.remaining_actions
assert "clarify" not in remaining
...

---

## use_given_when_then_helpers
**test_perform_behavior_action.py** - 27 violation(s)

[X] ERROR (line 1699)
Lines 1699-1704: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
actions = actions_workflow.get('actions', [])
if any(action.get('name') == 'build' for action in actions):
from agile_bot.bots.base_bot.test.test_build_knowledge import (
...

[X] ERROR (line 2026)
Lines 2026-2029: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
workspace_dir = tmp_path / "workspace"
workspace_dir.mkdir()
docs_dir = workspace_dir / "docs" / "stories"
...

[X] ERROR (line 2031)
Lines 2031-2052: Multiple inline steps (22 lines) should be extracted into a Given/When/Then helper function. Block:
clarification_data = {
"shape": {
"key_questions": {
...

[X] ERROR (line 2058)
Lines 2058-2069: Multiple inline steps (12 lines) should be extracted into a Given/When/Then helper function. Block:
strategy_data = {
"shape": {
"strategy_criteria": {
...

[X] ERROR (line 2075)
Lines 2075-2079: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
context_dir = docs_dir / "context"
context_dir.mkdir(parents=True)
(context_dir / "input.txt").write_text("Original input content")
...

[X] ERROR (line 2113)
Lines 2113-2118: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
assert 'context_files' in instructions
context_files = instructions['context_files']
assert isinstance(context_files, list)
...

[X] ERROR (line 2152)
Lines 2152-2155: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
import shutil
shutil.rmtree(context_dir)
action4 = Action(action_name="build", behavior=behavior, action_config=None)
...

[X] ERROR (line 2677)
Lines 2677-2693: Multiple inline steps (17 lines) should be extracted into a Given/When/Then helper function. Block:
workspace_dir = tmp_path
behavior = "tests"
behavior_config_data = {
...

[X] ERROR (line 2924)
Lines 2924-2927: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
assert len(behavior_names) == 3
assert 'shape' in behavior_names
assert 'prioritization' in behavior_names
...

[X] ERROR (line 3132)
Lines 3132-3135: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
actions_list = [
{"name": "clarify", "order": 1, "next_action": "strategy"},
{"name": "strategy", "order": 2, "next_action": "build"},
...

[X] ERROR (line 3154)
Lines 3154-3157: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
actions_list = [
{"name": "clarify", "order": 1},
{"name": "strategy", "order": 2},
...

[X] ERROR (line 3176)
Lines 3176-3180: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
actions_list = [
{"name": "clarify", "order": 1},
{"name": "strategy", "order": 2},
...

[X] ERROR (line 3223)
Lines 3223-3226: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
actions_list = [
{"name": "clarify", "order": 1},
{"name": "strategy", "order": 2},
...

[X] ERROR (line 3248)
Lines 3248-3252: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
actions_list = [
{"name": "clarify", "order": 1},
{"name": "strategy", "order": 2},
...

[X] ERROR (line 3274)
Lines 3274-3277: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
actions_list = [
{"name": "clarify", "order": 1},
{"name": "strategy", "order": 2},
...

[X] ERROR (line 3298)
Lines 3298-3302: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
actions_list = [
{"name": "clarify", "order": 1},
{"name": "strategy", "order": 2},
...

[X] ERROR (line 3314)
Lines 3314-3317: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
assert len(action_names) == 3
assert 'clarify' in action_names
assert 'strategy' in action_names
...

[X] ERROR (line 3326)
Lines 3326-3330: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
actions_list = [
{"name": "clarify", "order": 1},
{"name": "strategy", "order": 2},
...

[X] ERROR (line 3351)
Lines 3351-3354: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
actions_list = [
{"name": "clarify", "order": 1},
{"name": "strategy", "order": 2},
...

[X] ERROR (line 3377)
Lines 3377-3381: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
actions_list = [
{"name": "clarify", "order": 1},
{"name": "strategy", "order": 2},
...

[X] ERROR (line 3401)
Lines 3401-3404: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
actions_list = [
{"name": "clarify", "order": 1},
{"name": "strategy", "order": 2},
...

[X] ERROR (line 3419)
Lines 3419-3424: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
state_file = bot_paths.workspace_directory / 'behavior_action_state.json'
assert state_file.exists()
state_data = json.loads(state_file.read_text(encoding='utf-8'))
...

[X] ERROR (line 3444)
Lines 3444-3454: Multiple inline steps (11 lines) should be extracted into a Given/When/Then helper function. Block:
actions_list = [
{
"name": "clarify",
...

[X] ERROR (line 3493)
Lines 3493-3498: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
action_config_data = {
"name": "clarify",
"workflow": True,
...

[X] ERROR (line 3919)
Lines 3919-3929: Multiple inline steps (11 lines) should be extracted into a Given/When/Then helper function. Block:
workspace_dir = tmp_path
behavior = "shape"
behavior_config_data = {
...

[X] ERROR (line 4207)
Lines 4207-4211: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
try:
if 'BOT_DIRECTORY' in os.environ:
del os.environ['BOT_DIRECTORY']
...

[X] ERROR (line 4214)
Lines 4214-4220: Multiple inline steps (7 lines) should be extracted into a Given/When/Then helper function. Block:
with pytest.raises(RuntimeError):
BotPaths()
finally:
...

---

## use_given_when_then_helpers
**test_validate_knowledge_and_content_against_rules.py** - 24 violation(s)

[X] ERROR (line 3665)
Lines 3665-3668: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
if 'code' in behavior:
bad_example = {'code_files': [str(test_file)]}
elif 'tests' in behavior:
...

[X] ERROR (line 3694)
Lines 3694-3698: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
class TestExampleStory:
def test_example_scenario(self):
assert True
...

[X] ERROR (line 3700)
Lines 3700-3705: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
class TestAnotherStory:
def test_another_scenario(self):
assert True
...

[X] ERROR (line 3749)
Lines 3749-3752: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
class TestExampleStory:
def test_example_scenario(self):
assert True
...

[X] ERROR (line 5078)
Lines 5078-5085: Multiple inline steps (8 lines) should be extracted into a Given/When/Then helper function. Block:
bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
parameters = {
'scope': {
...

[X] ERROR (line 5097)
Lines 5097-5103: Multiple inline steps (7 lines) should be extracted into a Given/When/Then helper function. Block:
bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
parameters = {
'scope': {
...

[X] ERROR (line 5115)
Lines 5115-5123: Multiple inline steps (9 lines) should be extracted into a Given/When/Then helper function. Block:
bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
parameters = {
'scope': {
...

[X] ERROR (line 5131)
Lines 5131-5135: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
def test_force_full_flag_triggers_full_scan(self, bot_directory, workspace_directory):
from agile_bot.bots.base_bot.src.actions.rules.rules import ValidationContext
from agile_bot.bots.base_bot.src.bot.behavior import Behavior
...

[X] ERROR (line 5151)
Lines 5151-5155: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
def test_skip_cross_file_flag_disables_cross_file_scan(self, bot_directory, workspace_directory):
from agile_bot.bots.base_bot.src.actions.rules.rules import ValidationContext
from agile_bot.bots.base_bot.src.bot.behavior import Behavior
...

[X] ERROR (line 5255)
Lines 5255-5263: Multiple inline steps (9 lines) should be extracted into a Given/When/Then helper function. Block:
bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
parameters = {
'scope': {
...

[X] ERROR (line 5276)
Lines 5276-5283: Multiple inline steps (8 lines) should be extracted into a Given/When/Then helper function. Block:
bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
parameters = {
'scope': {
...

[X] ERROR (line 5299)
Lines 5299-5309: Multiple inline steps (11 lines) should be extracted into a Given/When/Then helper function. Block:
bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
parameters = {
'force_full': True,
...

[X] ERROR (line 5325)
Lines 5325-5337: Multiple inline steps (13 lines) should be extracted into a Given/When/Then helper function. Block:
bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
parameters = {
'force_full': True,
...

[X] ERROR (line 5339)
Lines 5339-5344: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
assert context.all_files is True
assert context.skip_cross_file is True
assert 'exclude' in parameters['scope']
...

[X] ERROR (line 5379)
Lines 5379-5382: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
from agile_bot.bots.base_bot.src.bot.behavior import Behavior
...

[X] ERROR (line 5387)
Lines 5387-5392: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
rules_dir = bot_directory / 'behaviors' / 'code' / 'rules'
rules_dir.mkdir(parents=True, exist_ok=True)
(rules_dir / 'test_rule.json').write_text(json.dumps({
...

[X] ERROR (line 5410)
Lines 5410-5413: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
from agile_bot.bots.base_bot.src.bot.behavior import Behavior
...

[X] ERROR (line 5418)
Lines 5418-5427: Multiple inline steps (10 lines) should be extracted into a Given/When/Then helper function. Block:
rules_dir = bot_directory / 'behaviors' / 'code' / 'rules'
rules_dir.mkdir(parents=True, exist_ok=True)
(rules_dir / 'rule_one.json').write_text(json.dumps({
...

[X] ERROR (line 5450)
Lines 5450-5454: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
from agile_bot.bots.base_bot.src.bot.behavior import Behavior
...

[X] ERROR (line 5459)
Lines 5459-5464: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
rules_dir = bot_directory / 'behaviors' / 'code' / 'rules'
rules_dir.mkdir(parents=True, exist_ok=True)
(rules_dir / 'test_rule.json').write_text(json.dumps({
...

[X] ERROR (line 5475)
Lines 5475-5478: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
instructions = result['instructions']
base_instructions = instructions.get('base_instructions', [])
instructions_text = '\n'.join(str(i) for i in base_instructions)
...

[X] ERROR (line 5487)
Lines 5487-5491: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
from agile_bot.bots.base_bot.src.bot.behavior import Behavior
...

[X] ERROR (line 5496)
Lines 5496-5501: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
rules_dir = bot_directory / 'behaviors' / 'code' / 'rules'
rules_dir.mkdir(parents=True, exist_ok=True)
(rules_dir / 'my_rule.json').write_text(json.dumps({
...

[X] ERROR (line 5530)
Lines 5530-5533: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
from agile_bot.bots.base_bot.src.bot.behavior import Behavior
...

---

Completed: 2025-12-29 18:49:02
Total violations: 305
Scanners executed: 15
