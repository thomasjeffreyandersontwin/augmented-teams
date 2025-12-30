# Validation Report - Shape

**Generated:** 2025-12-30 14:01:24
**Project:** base_bot
**Behavior:** shape
**Action:** validate

## Summary

Validated story map and domain model and 277 code file(s) and 36 test file(s) against **8 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `story-graph.json`
- **Test Files Scanned:**
  - `test\conftest.py`
  - `test\test_build_agile_bots.py`
  - `test\test_build_knowledge.py`
  - `test\test_current_initialize_repl_session.py`
  - `test\test_decide_strategy_criteria_action.py`
  - `test\test_display_bot_state_using_cli.py`
  - `test\test_display_bot_state_using_cli_current.py`
  - `test\test_document_headless_mode_requirements.py`
  - `test\test_execute_action_operation_through_cli.py`
  - `test\test_execute_action_operation_through_cli_current.py`
  - `test\test_execute_behavior_actions.py`
  - `test\test_execute_in_headless_mode.py`
  - `test\test_formatters.py`
  - `test\test_gather_context.py`
  - `test\test_generate_cli.py`
  - `test\test_generate_mcp_tools.py`
  - `test\test_generate_repl_cli.py`
  - `test\test_get_help_using_cli.py`
  - `test\test_get_help_using_cli_current.py`
  - `test\test_helpers.py`
  - `test\test_init_project.py`
  - `test\test_initialize_repl_session.py`
  - `test\test_initialize_repl_session_current.py`
  - `test\test_invoke_bot.py`
  - `test\test_invoke_cli.py`
  - `test\test_invoke_mcp.py`
  - `test\test_manage_bot_scope_through_cli.py`
  - `test\test_manage_bot_scope_through_cli_current.py`
  - `test\test_monitor_session.py`
  - `test\test_navigate_bot_behaviors_and_actions_with_cli.py`
  - `test\test_navigate_bot_behaviors_and_actions_with_cli_current.py`
  - `test\test_perform_behavior_action.py`
  - `test\test_render_output.py`
  - `test\test_resources.py`
  - `test\test_validate_knowledge_and_content_against_rules.py`
  - `test\test_validation_scope_and_file_filtering.py`
  - **Total:** 36 test file(s)
- **Code Files Scanned:**
  - `src\actions\action.py`
  - `src\actions\action_context.py`
  - `src\actions\action_factory.py`
  - `src\actions\action_scope.py`
  - `src\actions\action_state_manager.py`
  - `src\actions\actions.py`
  - `src\actions\activity_tracker.py`
  - `src\actions\build\build_action.py`
  - `src\actions\build\build_scope.py`
  - `src\actions\build\knowledge.py`
  - `src\actions\build\knowledge_graph_spec.py`
  - `src\actions\build\knowledge_graph_template.py`
  - `src\actions\clarify\clarify_action.py`
  - `src\actions\clarify\evidence.py`
  - `src\actions\clarify\key_questions.py`
  - `src\actions\clarify\required_context.py`
  - `src\actions\clarify\requirements_clarifications.py`
  - `src\actions\content.py`
  - `src\actions\context_data_injector.py`
  - `src\actions\guardrails.py`
  - `src\actions\help_action.py`
  - `src\actions\instructions.py`
  - `src\actions\render\evidence.py`
  - `src\actions\render\render_action.py`
  - `src\actions\render\render_config_loader.py`
  - `src\actions\render\render_instruction_builder.py`
  - `src\actions\render\render_spec.py`
  - `src\actions\render\synchronizer.py`
  - `src\actions\render\template.py`
  - `src\actions\rules\rule.py`
  - `src\actions\rules\rule_filter.py`
  - `src\actions\rules\rule_loader.py`
  - `src\actions\rules\rules.py`
  - `src\actions\rules\rules_action.py`
  - `src\actions\rules\rules_digest_guidance.py`
  - `src\actions\scope_matcher.py`
  - `src\actions\scoping_parameter.py`
  - `src\actions\strategy\assumptions.py`
  - `src\actions\strategy\json_persistent.py`
  - `src\actions\strategy\strategy.py`
  - `src\actions\strategy\strategy_action.py`
  - `src\actions\strategy\strategy_criteria.py`
  - `src\actions\strategy\strategy_criterias.py`
  - `src\actions\strategy\strategy_decision.py`
  - `src\actions\validate\background_validation_handler.py`
  - `src\actions\validate\file_discovery.py`
  - `src\actions\validate\file_link_builder.py`
  - `src\actions\validate\knowledge_graph.py`
  - `src\actions\validate\path_resolver.py`
  - `src\actions\validate\story_graph.py`
  - `src\actions\validate\validate_action.py`
  - `src\actions\validate\validation_executor.py`
  - `src\actions\validate\validation_report_builder.py`
  - `src\actions\validate\validation_report_formatter.py`
  - `src\actions\validate\validation_report_writer.py`
  - `src\actions\validate\validation_scope.py`
  - `src\actions\validate\validation_stats.py`
  - `src\actions\validate\validation_violations_builder.py`
  - `src\actions\validate\violation_formatter.py`
  - `src\actions\workflow_status_builder.py`
  - `src\base_bot_cli.py`
  - `src\bot\behavior.py`
  - `src\bot\behaviors.py`
  - `src\bot\bot.py`
  - `src\bot\bot_paths.py`
  - `src\bot\merged_instructions.py`
  - `src\bot\reminders.py`
  - `src\bot\workspace.py`
  - `src\cli\action_data_collector.py`
  - `src\cli\base_bot_cli.py`
  - `src\cli\cli_action_parsers.py`
  - `src\cli\cli_code_visitor.py`
  - `src\cli\cli_command_router.py`
  - `src\cli\cli_context_builder.py`
  - `src\cli\cli_executor.py`
  - `src\cli\cli_generator.py`
  - `src\cli\cli_help_generator.py`
  - `src\cli\cli_help_renderer_visitor.py`
  - `src\cli\cli_parameter_parser.py`
  - `src\cli\cli_parser_generator.py`
  - `src\cli\cli_parser_generator_visitor.py`
  - `src\cli\cli_script_generator.py`
  - `src\cli\cursor\command_file_visitor.py`
  - `src\cli\cursor\command_generator.py`
  - `src\cli\cursor\command_renderer_visitor.py`
  - `src\cli\cursor\help_renderer_visitor.py`
  - `src\cli\cursor_command_file_visitor.py`
  - `src\cli\cursor_command_generator.py`
  - `src\cli\cursor_command_renderer_visitor.py`
  - `src\cli\cursor_help_renderer_visitor.py`
  - `src\cli\description_extractor.py`
  - `src\cli\formatter.py`
  - `src\cli\help_renderer.py`
  - `src\cli\mcp_code_visitor.py`
  - `src\cli\parameter_info_builder.py`
  - `src\cli\type_hint_converter.py`
  - `src\ext\behavior_matcher.py`
  - `src\ext\bot_matcher.py`
  - `src\ext\trigger_domain.py`
  - `src\ext\trigger_router.py`
  - `src\ext\trigger_router_entry.py`
  - `src\ext\trigger_words.py`
  - `src\generator\action_data_collector.py`
  - `src\generator\help_context.py`
  - `src\generator\orchestrator.py`
  - `src\generator\visitor.py`
  - `src\mcp\mcp_code_generator.py`
  - `src\mcp\mcp_code_visitor.py`
  - `src\mcp\mcp_config_generator.py`
  - `src\mcp\mcp_server.py`
  - `src\mcp\mcp_server_generator.py`
  - `src\mcp\server_deployer.py`
  - `src\mcp\server_restart.py`
  - `src\repl_cli\cli_base.py`
  - `src\repl_cli\cli_bot\cli_actions\build_cli_action.py`
  - `src\repl_cli\cli_bot\cli_actions\clarify_cli_action.py`
  - `src\repl_cli\cli_bot\cli_actions\cli_action.py`
  - `src\repl_cli\cli_bot\cli_actions\cli_action_factory.py`
  - `src\repl_cli\cli_bot\cli_actions\cli_actions.py`
  - `src\repl_cli\cli_bot\cli_actions\render_cli_action.py`
  - `src\repl_cli\cli_bot\cli_actions\strategy_cli_action.py`
  - `src\repl_cli\cli_bot\cli_actions\validate_cli_action.py`
  - `src\repl_cli\cli_bot\cli_behavior.py`
  - `src\repl_cli\cli_bot\cli_behaviors.py`
  - `src\repl_cli\cli_bot\cli_bot.py`
  - `src\repl_cli\cli_scope.py`
  - `src\repl_cli\command_parser.py`
  - `src\repl_cli\formatters\formatter_factory.py`
  - `src\repl_cli\formatters\markdown_formatter.py`
  - `src\repl_cli\formatters\output_formatter.py`
  - `src\repl_cli\formatters\terminal_formatter.py`
  - `src\repl_cli\headless\cursor_api.py`
  - `src\repl_cli\headless\error_recovery.py`
  - `src\repl_cli\headless\execution_context.py`
  - `src\repl_cli\headless\execution_result.py`
  - `src\repl_cli\headless\headless_config.py`
  - `src\repl_cli\headless\headless_session.py`
  - `src\repl_cli\headless\non_recoverable_error.py`
  - `src\repl_cli\headless\recoverable_error.py`
  - `src\repl_cli\headless\session_log.py`
  - `src\repl_cli\message_parser.py`
  - `src\repl_cli\repl_help.py`
  - `src\repl_cli\repl_main.py`
  - `src\repl_cli\repl_results.py`
  - `src\repl_cli\repl_session.py`
  - `src\repl_cli\repl_status.py`
  - `src\repl_cli\status_display.py`
  - `src\scanners\abstraction_levels_scanner.py`
  - `src\scanners\ac_consolidation_scanner.py`
  - `src\scanners\active_language_scanner.py`
  - `src\scanners\arrange_act_assert_scanner.py`
  - `src\scanners\ascii_only_scanner.py`
  - `src\scanners\background_common_setup_scanner.py`
  - `src\scanners\bad_comments_scanner.py`
  - `src\scanners\behavioral_ac_scanner.py`
  - `src\scanners\business_readable_test_names_scanner.py`
  - `src\scanners\calculation_timing_code_scanner.py`
  - `src\scanners\calculation_timing_scanner.py`
  - `src\scanners\class_based_organization_scanner.py`
  - `src\scanners\class_size_scanner.py`
  - `src\scanners\clear_parameters_scanner.py`
  - `src\scanners\code_representation_code_scanner.py`
  - `src\scanners\code_representation_scanner.py`
  - `src\scanners\code_scanner.py`
  - `src\scanners\communication_verb_scanner.py`
  - `src\scanners\complete_refactoring_scanner.py`
  - `src\scanners\complexity_metrics.py`
  - `src\scanners\consistent_indentation_scanner.py`
  - `src\scanners\consistent_naming_scanner.py`
  - `src\scanners\consistent_vocabulary_scanner.py`
  - `src\scanners\cover_all_paths_scanner.py`
  - `src\scanners\delegation_code_scanner.py`
  - `src\scanners\delegation_scanner.py`
  - `src\scanners\dependency_chaining_code_scanner.py`
  - `src\scanners\dependency_chaining_scanner.py`
  - `src\scanners\descriptive_function_names_scanner.py`
  - `src\scanners\domain_concept_node.py`
  - `src\scanners\domain_grouping_code_scanner.py`
  - `src\scanners\domain_grouping_scanner.py`
  - `src\scanners\domain_language_code_scanner.py`
  - `src\scanners\domain_language_scanner.py`
  - `src\scanners\domain_scanner.py`
  - `src\scanners\duplication_scanner.py`
  - `src\scanners\encapsulation_scanner.py`
  - `src\scanners\enumerate_ac_permutations_scanner.py`
  - `src\scanners\enumerate_stories_scanner.py`
  - `src\scanners\error_handling_isolation_scanner.py`
  - `src\scanners\exact_variable_names_scanner.py`
  - `src\scanners\exception_classification_scanner.py`
  - `src\scanners\exception_handling_scanner.py`
  - `src\scanners\excessive_guards_scanner.py`
  - `src\scanners\exhaustive_decomposition_scanner.py`
  - `src\scanners\explicit_dependencies_scanner.py`
  - `src\scanners\fixture_placement_scanner.py`
  - `src\scanners\function_size_scanner.py`
  - `src\scanners\generic_capability_scanner.py`
  - `src\scanners\given_precondition_scanner.py`
  - `src\scanners\given_state_not_actions_scanner.py`
  - `src\scanners\given_when_then_helpers_scanner.py`
  - `src\scanners\implementation_details_scanner.py`
  - `src\scanners\import_placement_scanner.py`
  - `src\scanners\increment_folder_structure_scanner.py`
  - `src\scanners\intention_revealing_names_scanner.py`
  - `src\scanners\invest_principles_scanner.py`
  - `src\scanners\meaningful_context_scanner.py`
  - `src\scanners\minimize_mutable_state_scanner.py`
  - `src\scanners\mock_boundaries_scanner.py`
  - `src\scanners\natural_english_code_scanner.py`
  - `src\scanners\natural_english_scanner.py`
  - `src\scanners\no_fallbacks_scanner.py`
  - `src\scanners\no_guard_clauses_scanner.py`
  - `src\scanners\noun_redundancy_scanner.py`
  - `src\scanners\observable_behavior_scanner.py`
  - `src\scanners\one_concept_per_test_scanner.py`
  - `src\scanners\open_closed_principle_scanner.py`
  - `src\scanners\parameterized_tests_scanner.py`
  - `src\scanners\plain_english_scenarios_scanner.py`
  - `src\scanners\prefer_object_model_over_config_scanner.py`
  - `src\scanners\present_ac_consolidation_scanner.py`
  - `src\scanners\primitive_vs_object_scanner.py`
  - `src\scanners\property_encapsulation_code_scanner.py`
  - `src\scanners\property_encapsulation_scanner.py`
  - `src\scanners\real_implementations_scanner.py`
  - `src\scanners\resource_oriented_code_scanner.py`
  - `src\scanners\resource_oriented_design_scanner.py`
  - `src\scanners\resources\ast_elements.py`
  - `src\scanners\resources\block.py`
  - `src\scanners\resources\block_extractor.py`
  - `src\scanners\resources\file.py`
  - `src\scanners\resources\line.py`
  - `src\scanners\resources\scan.py`
  - `src\scanners\resources\scope.py`
  - `src\scanners\resources\violation.py`
  - `src\scanners\scanner.py`
  - `src\scanners\scanner_execution_error.py`
  - `src\scanners\scanner_loader.py`
  - `src\scanners\scanner_orchestrator.py`
  - `src\scanners\scanner_registry.py`
  - `src\scanners\scanner_status_formatter.py`
  - `src\scanners\scenario_outline_scanner.py`
  - `src\scanners\scenario_specific_given_scanner.py`
  - `src\scanners\scenarios_cover_all_cases_scanner.py`
  - `src\scanners\scenarios_on_story_docs_scanner.py`
  - `src\scanners\separate_concerns_scanner.py`
  - `src\scanners\simplify_control_flow_scanner.py`
  - `src\scanners\single_responsibility_scanner.py`
  - `src\scanners\specification_match_scanner.py`
  - `src\scanners\specificity_scanner.py`
  - `src\scanners\spine_optional_scanner.py`
  - `src\scanners\story_enumeration_scanner.py`
  - `src\scanners\story_filename_scanner.py`
  - `src\scanners\story_graph_match_scanner.py`
  - `src\scanners\story_map.py`
  - `src\scanners\story_scanner.py`
  - `src\scanners\story_sizing_scanner.py`
  - `src\scanners\swallowed_exceptions_scanner.py`
  - `src\scanners\technical_abstraction_code_scanner.py`
  - `src\scanners\technical_abstraction_scanner.py`
  - `src\scanners\technical_language_scanner.py`
  - `src\scanners\test_boundary_behavior_scanner.py`
  - `src\scanners\test_file_naming_scanner.py`
  - `src\scanners\test_quality_scanner.py`
  - `src\scanners\test_scanner.py`
  - `src\scanners\third_party_isolation_scanner.py`
  - `src\scanners\type_safety_scanner.py`
  - `src\scanners\ubiquitous_language_scanner.py`
  - `src\scanners\unnecessary_parameter_passing_scanner.py`
  - `src\scanners\useless_comments_scanner.py`
  - `src\scanners\validation_scanner_status_builder.py`
  - `src\scanners\verb_noun_scanner.py`
  - `src\scanners\vertical_density_scanner.py`
  - `src\scanners\vertical_slice_scanner.py`
  - `src\scanners\violation.py`
  - `src\scanners\vocabulary_helper.py`
  - `src\story_graph\domain.py`
  - `src\story_graph\nodes.py`
  - `src\utils.py`
  - **Total:** 277 src file(s)

## Scanner Execution Status

### 🟨 Overall Status: GOOD - Minor Issues

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 4 | Scanners ran without errors |
| 🟩 Clean Rules | 1 | No violations found |
| [i] No Scanner | 4 | Rule has no scanner configured |

**Total Rules:** 8
- **Rules with Scanners:** 4
  - 🟩 **Executed Successfully:** 4
- [i] **Rules without Scanners:** 4

### 🟩 Successfully Executed Scanners

- 🟨 **[Verb Noun Format](#verb-noun-format)** - 80 violation(s) (EXECUTION_SUCCESS) - [View Details](#verb-noun-format-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.verb_noun_scanner.VerbNounScanner`
- 🟨 **[Active Business And Behavioral Language](#active-business-and-behavioral-language)** - 78 violation(s) (EXECUTION_SUCCESS) - [View Details](#active-business-and-behavioral-language-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.active_language_scanner.ActiveLanguageScanner`
- 🟨 **[Small And Testable](#small-and-testable)** - 20 violation(s) (EXECUTION_SUCCESS) - [View Details](#small-and-testable-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.implementation_details_scanner.ImplementationDetailsScanner`
- 🟩 **[Outcome Oriented Language](#outcome-oriented-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.communication_verb_scanner.CommunicationVerbScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Lightweight And Precise](#lightweight-and-precise)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Valuable](#valuable)** - No scanner configured
- <span style="color: gray;">[i]</span> **[User And System Behavior](#user-and-system-behavior)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Story Map Existing Code](#story-map-existing-code)** - No scanner configured

## Validation Rules Checked

### 🟩 Rule: <span id="outcome-oriented-language">Outcome Oriented Language</span> - CLEAN (0 violations)
**Description:** Use outcome-oriented language over mechanism-oriented language. Focus on what is created or achieved, not how it's shown or communicated.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.communication_verb_scanner.CommunicationVerbScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="active-business-and-behavioral-language">Active Business And Behavioral Language</span> - 78 VIOLATION(S) - [View Details](#active-business-and-behavioral-language-violations)
**Description:** Use active business language focused on user/system behavior. Describe what actors do with clear action verbs, not technical implementation or passive constructions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.active_language_scanner.ActiveLanguageScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="lightweight-and-precise">Lightweight And Precise</span> - NO SCANNER
**Description:** Create lightweight but precise documentation during shaping. Focus on structure and scope, not detailed specifications.
**Scanner:** Not configured

### 🟨 Rule: <span id="small-and-testable">Small And Testable</span> - 20 VIOLATION(S) - [View Details](#small-and-testable-violations)
**Description:** Stories must be testable as complete interactions and deliverable independently. Balance testability with maintaining value and behavioral focus - stories should be small enough to test but large enough to matter.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.implementation_details_scanner.ImplementationDetailsScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="story-map-existing-code">Story Map Existing Code</span> - NO SCANNER
**Description:** When creating story maps from code, start with the outermost layer (entry points), analyze operations, create epics from higher-order goals, and lay out the story journey.
**Scanner:** Not configured

### [i] Rule: <span id="user-and-system-behavior">User And System Behavior</span> - NO SCANNER
**Description:** Stories should capture both user and system behavior. User-facing stories show user actions with system responses. System stories capture system-to-system interactions and should be marked with story_type: 'system'. NOTE: This rule only applies when strategy decisions in planning.json specify flow_scope_and_granularity as 'Integration boundary level' or 'Intra-system level', OR drill_down_approach includes 'Dig deep on system interactions' or 'Dig deep on architectural pieces'. Check {project_area}/docs/stories/planning.json for these decisions.
**Scanner:** Not configured

### [i] Rule: <span id="valuable">Valuable</span> - NO SCANNER
**Description:** Stories must deliver independent value as complete functional accomplishments. Balance value with testability - stories should be valuable enough to matter but small enough to deliver quickly. Not just data access or isolated operations.
**Scanner:** Not configured

### 🟨 Rule: <span id="verb-noun-format">Verb Noun Format</span> - 80 VIOLATION(S) - [View Details](#verb-noun-format-violations)
**Description:** Use verb-noun format consistently across all hierarchy levels. Actor --> verb noun [qualifiers]. Actor is documented separately, NOT in the name. Focus on specific actions with context.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

## Violations Found

**Total Violations:** 178
- **File-by-File Violations:** 178
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="verb-noun-format-violations">Verb Noun Format: 80 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].name): Epic name "Build Agile Bots" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[0].story_groups[0].stories[2].name): Story name "Input File Copied To Context Folder" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[0].story_groups[0].stories[3].name): Story name "Store Context Files" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[0].story_groups[0].stories[4].name): Story name "Guards Prevent Writes Without Project" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[0].story_groups[0].stories[5].name): Story name "Stores Activity for Initialize Project Action" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[6].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[0].story_groups[0].stories[6].name): Story name "Bootstrap Workspace" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[1].story_groups[0].stories[1].name): Story name "Load And Merge Behavior Action Instructions" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[1].story_groups[0].stories[2].name): Story name "Forward To Current Behavior and Current Action" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[1].story_groups[0].stories[3].name): Story name "Forward To Current Action" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[1].story_groups[0].stories[4].name): Story name "Track Activity For Workspace" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[2].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[2].story_groups[0].stories[3].name): Story name "Get Help for Command Line Functions" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[3].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].story_groups[0].stories[0].name): Story name "Find Behavior Folder" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[3].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].story_groups[0].stories[5].name): Story name "Close Current Action" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[3].story_groups[0].stories[7].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].story_groups[0].stories[7].name): Story name "Load And Merge Behavior Action Instructions" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[0].name): Story name "Route to Default Behavior Action" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[1].name): Story name "Route to BotLangFlow" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[4].name): Story name "Process Bot Behavor Action Instructions Automatically" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[5].name): Story name "Process Behavor Action Instructions Through AI Chat" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[7].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[7].name): Story name "Return to chat and pause for human-in-the-loop Node" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[8].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[8].name): Story name "Handle Execution Modes" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[9].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[9].name): Story name "Resume BotLangFlow from Checkpoint" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].name): Sub_epic name "Run Interactive REPL" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[0].name): Story name "Launch CLI in Interactive Mode" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[1].name): Story name "Launch CLI in Pipe Mode" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[2].name): Story name "Display Piped Mode Instructions for AI Agents" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[4].name): Story name "Load and Display Workspace Context in CLI" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[5].name): Story name "Load All Registered Bots" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[1].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[1].story_groups[0].stories[2].name): Story name "Exit CLI REPL" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[2].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[2].story_groups[0].stories[1].name): Story name "Advance Action And Persist State" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[2].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[2].story_groups[0].stories[2].name): Story name "Show Remaining Actions After Completion" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[3].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[3].story_groups[0].stories[0].name): Story name "Get Action Instructions Through CLI" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[3].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[3].story_groups[0].stories[3].name): Story name "Re-execute Current Operation Using CLI" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[3].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[3].story_groups[0].stories[4].name): Story name "Handle Operation Errors and Validation in CLI" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[0].name): Story name "Set Scope Through CLI Using String Parameters" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[1].name): Story name "View Current Scope in CLI" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[2].name): Story name "Clear Scope Through CLI" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[3].name): Story name "Pass Scope Parameters When Executing Actions Through CLI" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[5].name): Sub_epic name "Display Bot State Using CLI" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[0].name): Story name "Display CLI Header" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[1].name): Story name "Display Bot Hierarchy Tree with Progress Indicators" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[2].name): Story name "Display CLI Navigation Menu Footer" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[3].name): Story name "Display Available Bot in Tree Hierarchy" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[4].name): Story name "Display CLI Bot Command in Navigation Menu Footer" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[6].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[6].name): Sub_epic name "Get Help Using CLI" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[6].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[6].story_groups[0].stories[0].name): Story name "Request Action Help Through CLI" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[6].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[6].story_groups[0].stories[1].name): Story name "View Parameter Documentation in CLI" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[6].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[6].story_groups[0].stories[2].name): Story name "View Command Examples in CLI" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[0].name): Sub_epic name "Document Headless Mode Requirements" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[0].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[0].story_groups[0].stories[0].name): Story name "Add Headless Mode To Help" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[0].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[0].story_groups[0].stories[1].name): Story name "Add Headless Mode To Status" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[2].name): Sub_epic name "Monitor Session" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[2].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[2].story_groups[0].stories[0].name): Story name "Monitor Execution" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[2].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[2].story_groups[0].stories[1].name): Story name "Surface Block Reason" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[2].story_groups[1].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[2].story_groups[1].stories[0].name): Story name "Report Completion" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].name): Sub_epic name "Gather Context" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].story_groups[0].stories[1].name): Story name "Track Activity for Gather Context Action" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].story_groups[0].stories[2].name): Story name "Store Clarification Data" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].story_groups[0].stories[4].name): Story name "Load Base Action Config" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].story_groups[0].stories[5].name): Story name "Access Actions" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].story_groups[0].stories[7].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].story_groups[0].stories[7].name): Story name "Load Guardrails" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[1].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[1].story_groups[0].stories[1].name): Story name "Track Activity for Planning Action" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[1].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[1].story_groups[0].stories[2].name): Story name "Save Final Assumptions and Decisions" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[1].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[1].story_groups[0].stories[5].name): Story name "Store Strategy Data" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[2].name): Sub_epic name "Build Knowledge" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[2].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[2].story_groups[0].stories[0].name): Story name "Load Story Graph Into Memory" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[2].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[2].story_groups[0].stories[2].name): Story name "Track Activity for Build Knowledge Action" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[2].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[2].story_groups[0].stories[3].name): Story name "Update Existing Knowledge Graph" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[2].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[2].story_groups[0].stories[5].name): Story name "proactively Validate knowledge against rules" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[2].story_groups[0].stories[7].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[2].story_groups[0].stories[7].name): Story name "Filter Knowledge Graph" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].name): Sub_epic name "Render Output" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].story_groups[0].stories[0].name): Story name "Track Activity for Render Output Action" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].story_groups[0].stories[2].name): Story name "Load Render Configurations" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].story_groups[0].stories[6].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].story_groups[0].stories[6].name): Story name "Get Render Instructions" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].story_groups[0].stories[8].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].story_groups[0].stories[8].name): Story name "Render Output Using Synchronizers" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].story_groups[0].stories[10].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].story_groups[0].stories[10].name): Story name "Get Render Instructions" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].story_groups[0].stories[12].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].story_groups[0].stories[12].name): Story name "Render Output Using Synchronizers" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[4].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[4].story_groups[0].stories[1].name): Story name "Track Activity for Validate Rules Action" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[4].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[4].story_groups[0].stories[4].name): Story name "Run Scanners against Knowledge Graph" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[4].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[4].story_groups[0].stories[5].name): Story name "Run AST Scanners against Knowledge Graph (OUT OF SCOPE)" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[4].story_groups[0].stories[8].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[4].story_groups[0].stories[8].name): Story name "Report Validation and Error Handling" contains actor prefix (e.g., "Customer") - use verb-noun format without actor

#### <span id="active-business-and-behavioral-language-violations">Active Business And Behavioral Language: 78 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].name): Epic name "Build Agile Bots" has actor "Build" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Agile Bots"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[0].story_groups[0].stories[2].name): Story name "Input File Copied To Context Folder" has actor "Input" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "File Copied To Context Folder"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[0].story_groups[0].stories[3].name): Story name "Store Context Files" has actor "Store" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Context Files"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[0].story_groups[0].stories[4].name): Story name "Guards Prevent Writes Without Project" has actor "Guards" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Prevent Writes Without Project"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[0].story_groups[0].stories[5].name): Story name "Stores Activity for Initialize Project Action" has actor "Stores" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Activity for Initialize Project Action"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[6].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[0].story_groups[0].stories[6].name): Story name "Bootstrap Workspace" has actor "Bootstrap" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Workspace"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[1].story_groups[0].stories[1].name): Story name "Load And Merge Behavior Action Instructions" has actor "Load" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "And Merge Behavior Action Instructions"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[1].story_groups[0].stories[2].name): Story name "Forward To Current Behavior and Current Action" has actor "Forward" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "To Current Behavior and Current Action"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[1].story_groups[0].stories[3].name): Story name "Forward To Current Action" has actor "Forward" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "To Current Action"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[1].story_groups[0].stories[4].name): Story name "Track Activity For Workspace" has actor "Track" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Activity For Workspace"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[2].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[2].story_groups[0].stories[3].name): Story name "Get Help for Command Line Functions" has actor "Get" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Help for Command Line Functions"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[3].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].story_groups[0].stories[0].name): Story name "Find Behavior Folder" has actor "Find" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Behavior Folder"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[3].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].story_groups[0].stories[5].name): Story name "Close Current Action" has actor "Close" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Current Action"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[3].story_groups[0].stories[7].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].story_groups[0].stories[7].name): Story name "Load And Merge Behavior Action Instructions" has actor "Load" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "And Merge Behavior Action Instructions"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[0].name): Story name "Route to Default Behavior Action" has actor "Route" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "To Default Behavior Action"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[1].name): Story name "Route to BotLangFlow" has actor "Route" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "To BotLangFlow"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[4].name): Story name "Process Bot Behavor Action Instructions Automatically" has actor "Process" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Bot Behavor Action Instructions Automatically"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[5].name): Story name "Process Behavor Action Instructions Through AI Chat" has actor "Process" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Behavor Action Instructions Through AI Chat"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[7].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[7].name): Story name "Return to chat and pause for human-in-the-loop Node" has actor "Return" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "To chat and pause for human-in-the-loop Node"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[8].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[8].name): Story name "Handle Execution Modes" has actor "Handle" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Execution Modes"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[4].story_groups[0].stories[9].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[9].name): Story name "Resume BotLangFlow from Checkpoint" has actor "Resume" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "BotLangFlow from Checkpoint"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].name): Sub_epic name "Run Interactive REPL" has actor "Run" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Interactive REPL"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[0].name): Story name "Launch CLI in Interactive Mode" has actor "Launch" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "CLI in Interactive Mode"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[1].name): Story name "Launch CLI in Pipe Mode" has actor "Launch" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "CLI in Pipe Mode"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[2].name): Story name "Display Piped Mode Instructions for AI Agents" has actor "Display" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Piped Mode Instructions for AI Agents"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[4].name): Story name "Load and Display Workspace Context in CLI" has actor "Load" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "And Display Workspace Context in CLI"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[0].story_groups[0].stories[5].name): Story name "Load All Registered Bots" has actor "Load" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "All Registered Bots"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[1].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[1].story_groups[0].stories[2].name): Story name "Exit CLI REPL" has actor "Exit" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "CLI REPL"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[2].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[2].story_groups[0].stories[1].name): Story name "Advance Action And Persist State" has actor "Advance" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Action And Persist State"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[2].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[2].story_groups[0].stories[2].name): Story name "Show Remaining Actions After Completion" has actor "Show" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Remaining Actions After Completion"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[3].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[3].story_groups[0].stories[0].name): Story name "Get Action Instructions Through CLI" has actor "Get" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Action Instructions Through CLI"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[3].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[3].story_groups[0].stories[4].name): Story name "Handle Operation Errors and Validation in CLI" has actor "Handle" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Operation Errors and Validation in CLI"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[0].name): Story name "Set Scope Through CLI Using String Parameters" has actor "Set" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Scope Through CLI Using String Parameters"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[1].name): Story name "View Current Scope in CLI" has actor "View" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Current Scope in CLI"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[2].name): Story name "Clear Scope Through CLI" has actor "Clear" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Scope Through CLI"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[4].story_groups[0].stories[3].name): Story name "Pass Scope Parameters When Executing Actions Through CLI" has actor "Pass" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Scope Parameters When Executing Actions Through CLI"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[5].name): Sub_epic name "Display Bot State Using CLI" has actor "Display" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Bot State Using CLI"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[0].name): Story name "Display CLI Header" has actor "Display" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "CLI Header"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[1].name): Story name "Display Bot Hierarchy Tree with Progress Indicators" has actor "Display" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Bot Hierarchy Tree with Progress Indicators"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[2].name): Story name "Display CLI Navigation Menu Footer" has actor "Display" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "CLI Navigation Menu Footer"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[3].name): Story name "Display Available Bot in Tree Hierarchy" has actor "Display" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Available Bot in Tree Hierarchy"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[5].story_groups[0].stories[4].name): Story name "Display CLI Bot Command in Navigation Menu Footer" has actor "Display" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "CLI Bot Command in Navigation Menu Footer"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[6].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[6].name): Sub_epic name "Get Help Using CLI" has actor "Get" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Help Using CLI"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[6].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[6].story_groups[0].stories[0].name): Story name "Request Action Help Through CLI" has actor "Request" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Action Help Through CLI"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[6].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[6].story_groups[0].stories[1].name): Story name "View Parameter Documentation in CLI" has actor "View" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Parameter Documentation in CLI"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[6].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[6].story_groups[0].stories[2].name): Story name "View Command Examples in CLI" has actor "View" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Command Examples in CLI"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[0].name): Sub_epic name "Document Headless Mode Requirements" has actor "Document" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Headless Mode Requirements"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[0].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[0].story_groups[0].stories[0].name): Story name "Add Headless Mode To Help" has actor "Add" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Headless Mode To Help"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[0].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[0].story_groups[0].stories[1].name): Story name "Add Headless Mode To Status" has actor "Add" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Headless Mode To Status"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[2].name): Sub_epic name "Monitor Session" has actor "Monitor" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Session"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[2].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[2].story_groups[0].stories[0].name): Story name "Monitor Execution" has actor "Monitor" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Execution"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[2].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[2].story_groups[0].stories[1].name): Story name "Surface Block Reason" has actor "Surface" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Block Reason"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[6].sub_epics[2].story_groups[1].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[6].sub_epics[2].story_groups[1].stories[0].name): Story name "Report Completion" has actor "Report" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Completion"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].name): Sub_epic name "Gather Context" has actor "Gather" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Context"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].story_groups[0].stories[1].name): Story name "Track Activity for Gather Context Action" has actor "Track" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Activity for Gather Context Action"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].story_groups[0].stories[2].name): Story name "Store Clarification Data" has actor "Store" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Clarification Data"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].story_groups[0].stories[4].name): Story name "Load Base Action Config" has actor "Load" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Base Action Config"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].story_groups[0].stories[5].name): Story name "Access Actions" has actor "Access" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Actions"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].story_groups[0].stories[7].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].story_groups[0].stories[7].name): Story name "Load Guardrails" has actor "Load" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Guardrails"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[1].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[1].story_groups[0].stories[1].name): Story name "Track Activity for Planning Action" has actor "Track" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Activity for Planning Action"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[1].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[1].story_groups[0].stories[2].name): Story name "Save Final Assumptions and Decisions" has actor "Save" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Final Assumptions and Decisions"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[1].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[1].story_groups[0].stories[5].name): Story name "Store Strategy Data" has actor "Store" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Strategy Data"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[2].name): Sub_epic name "Build Knowledge" has actor "Build" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Knowledge"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[2].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[2].story_groups[0].stories[0].name): Story name "Load Story Graph Into Memory" has actor "Load" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Story Graph Into Memory"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[2].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[2].story_groups[0].stories[2].name): Story name "Track Activity for Build Knowledge Action" has actor "Track" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Activity for Build Knowledge Action"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[2].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[2].story_groups[0].stories[3].name): Story name "Update Existing Knowledge Graph" has actor "Update" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Existing Knowledge Graph"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[2].story_groups[0].stories[7].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[2].story_groups[0].stories[7].name): Story name "Filter Knowledge Graph" has actor "Filter" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Knowledge Graph"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].name): Sub_epic name "Render Output" has actor "Render" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Output"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].story_groups[0].stories[0].name): Story name "Track Activity for Render Output Action" has actor "Track" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Activity for Render Output Action"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].story_groups[0].stories[2].name): Story name "Load Render Configurations" has actor "Load" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Render Configurations"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].story_groups[0].stories[6].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].story_groups[0].stories[6].name): Story name "Get Render Instructions" has actor "Get" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Render Instructions"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].story_groups[0].stories[8].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].story_groups[0].stories[8].name): Story name "Render Output Using Synchronizers" has actor "Render" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Output Using Synchronizers"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].story_groups[0].stories[10].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].story_groups[0].stories[10].name): Story name "Get Render Instructions" has actor "Get" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Render Instructions"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].story_groups[0].stories[12].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[3].story_groups[0].stories[12].name): Story name "Render Output Using Synchronizers" has actor "Render" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Output Using Synchronizers"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[4].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[4].story_groups[0].stories[1].name): Story name "Track Activity for Validate Rules Action" has actor "Track" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Activity for Validate Rules Action"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[4].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[4].story_groups[0].stories[4].name): Story name "Run Scanners against Knowledge Graph" has actor "Run" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Scanners against Knowledge Graph"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[4].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[4].story_groups[0].stories[5].name): Story name "Run AST Scanners against Knowledge Graph (OUT OF SCOPE)" has actor "Run" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "AST Scanners against Knowledge Graph (OUT OF SCOPE)"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[4].story_groups[0].stories[8].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[4].story_groups[0].stories[8].name): Story name "Report Validation and Error Handling" has actor "Report" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Validation and Error Handling"

#### <span id="small-and-testable-violations">Small And Testable: 20 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`Generate Bot Tools`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Bot Tools): Story "Generate Bot Tools" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Behavior Tools`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Behavior Tools): Story "Generate Behavior Tools" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate MCP Bot Server`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate MCP Bot Server): Story "Generate MCP Bot Server" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Behavior Action Tools`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Behavior Action Tools): Story "Generate Behavior Action Tools" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate BOT CLI code`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate BOT CLI code): Story "Generate BOT CLI code" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Cursor Command Files`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Cursor Command Files): Story "Generate Cursor Command Files" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Help`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Help): Story "Generate Help" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Cursor Awareness Files`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Cursor Awareness Files): Story "Generate Cursor Awareness Files" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Help Parameters From Action Context Classes`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Help Parameters From Action Context Classes): Story "Generate Help Parameters From Action Context Classes" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate REPL Command Definitions`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate REPL Command Definitions): Story "Generate REPL Command Definitions" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate CLI Entry Point`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate CLI Entry Point): Story "Generate CLI Entry Point" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Cursor Commands`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Cursor Commands): Story "Generate Cursor Commands" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Help Documentation`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Help Documentation): Story "Generate Help Documentation" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Store Context Files`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Store Context Files): Story "Store Context Files" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Set Scope Through CLI Using String Parameters`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Set Scope Through CLI Using String Parameters): Story "Set Scope Through CLI Using String Parameters" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Store Clarification Data`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Store Clarification Data): Story "Store Clarification Data" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Save Final Assumptions and Decisions`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Save Final Assumptions and Decisions): Story "Save Final Assumptions and Decisions" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Store Strategy Data`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Store Strategy Data): Story "Store Strategy Data" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Create Build Scope`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Create Build Scope): Story "Create Build Scope" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Violation Report`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Violation Report): Story "Generate Violation Report" appears to be an implementation operation - should be a step within a story that describes user/system outcome

## Validation Instructions

The following validation steps were performed:

1. ## Step 1: Scanner Violation Review
2. 
3. {{scanner_output}}
4. 
5. Carefully review all scanner-reported violations as follows:
6. 1. For each violation message, locate the corresponding element in the knowledge graph.
7. 2. Open the relevant rule file and read all DO and DON'T examples thoroughly.
8. 3. Decide if the violation is **Valid** (truly a rule breach per examples) or a **False Positive** (explain why if so).
9. 4. Determine the **Root Cause** (e.g., 'incorrect concept naming', 'missing actor', etc.).
10. 5. Assign a **Theme** grouping based on the type of issue (e.g., 'noun-only naming', 'incomplete acceptance criteria').
*... and 54 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\shape-validation-report-2025-12-30_14-01-20.md`

