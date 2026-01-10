# Validation Report - Shape

**Generated:** 2026-01-09 03:01:10
**Project:** agile_bot
**Behavior:** shape
**Action:** validate

## Summary

Validated story map and domain model and 267 code file(s) and 10 test file(s) against **8 validation rules**.

## Content Validated

- **Rendered Outputs:**
  - `story-graph.json`
- **Test Files Scanned:**
  - `test\test_build_knowledge.py`
  - `test\test_execute_actions_using_cli.py`
  - `test\test_execute_behavior_actions.py`
  - `test\test_get_help_using_cli.py`
  - `test\test_helpers.py`
  - `test\test_initialize_cli_session.py`
  - `test\test_invoke_bot_directly.py`
  - `test\test_invoke_bot_helpers.py`
  - `test\test_manage_scope_using_cli.py`
  - `test\test_navigate_behaviors_using_cli_commands.py`
  - **Total:** 10 test file(s)
- **Code Files Scanned:**
  - `src\actions\action.py`
  - `src\actions\action_context.py`
  - `src\actions\action_factory.py`
  - `src\actions\action_state_manager.py`
  - `src\actions\actions.py`
  - `src\actions\activity_tracker.py`
  - `src\actions\behavior_action_status_builder.py`
  - `src\actions\build\build_action.py`
  - `src\actions\build\build_scope.py`
  - `src\actions\build\json_build_action.py`
  - `src\actions\build\knowledge.py`
  - `src\actions\build\knowledge_graph_spec.py`
  - `src\actions\build\knowledge_graph_template.py`
  - `src\actions\build\markdown_build_action.py`
  - `src\actions\build\tty_build_action.py`
  - `src\actions\clarify\clarify_action.py`
  - `src\actions\clarify\evidence.py`
  - `src\actions\clarify\json_clarify_action.py`
  - `src\actions\clarify\key_questions.py`
  - `src\actions\clarify\markdown_clarify_action.py`
  - `src\actions\clarify\required_context.py`
  - `src\actions\clarify\requirements_clarifications.py`
  - `src\actions\clarify\tty_clarify_action.py`
  - `src\actions\content.py`
  - `src\actions\guardrails.py`
  - `src\actions\guardrails\tty_guardrails.py`
  - `src\actions\guardrails\tty_required_context.py`
  - `src\actions\guardrails\tty_strategy.py`
  - `src\actions\render\evidence.py`
  - `src\actions\render\json_render_action.py`
  - `src\actions\render\markdown_render_action.py`
  - `src\actions\render\render_action.py`
  - `src\actions\render\render_config_loader.py`
  - `src\actions\render\render_instruction_builder.py`
  - `src\actions\render\render_spec.py`
  - `src\actions\render\synchronizer.py`
  - `src\actions\render\template.py`
  - `src\actions\render\tty_render_action.py`
  - `src\actions\strategy\assumptions.py`
  - `src\actions\strategy\json_persistent.py`
  - `src\actions\strategy\json_strategy_action.py`
  - `src\actions\strategy\markdown_strategy_action.py`
  - `src\actions\strategy\strategy.py`
  - `src\actions\strategy\strategy_action.py`
  - `src\actions\strategy\strategy_criteria.py`
  - `src\actions\strategy\strategy_criterias.py`
  - `src\actions\strategy\strategy_decision.py`
  - `src\actions\strategy\tty_strategy_action.py`
  - `src\actions\tty_action.py`
  - `src\actions\tty_actions.py`
  - `src\actions\validate\background_validation_handler.py`
  - `src\actions\validate\file_discovery.py`
  - `src\actions\validate\file_link_builder.py`
  - `src\actions\validate\json_validate_action.py`
  - `src\actions\validate\knowledge_graph.py`
  - `src\actions\validate\markdown_validate_action.py`
  - `src\actions\validate\tty_validate_action.py`
  - `src\actions\validate\validate_action.py`
  - `src\actions\validate\validation_executor.py`
  - `src\actions\validate\validation_report_builder.py`
  - `src\actions\validate\validation_report_formatter.py`
  - `src\actions\validate\validation_report_writer.py`
  - `src\actions\validate\validation_scope.py`
  - `src\actions\validate\validation_stats.py`
  - `src\actions\validate\validation_type.py`
  - `src\actions\validate\validation_violations_builder.py`
  - `src\actions\validate\violation_formatter.py`
  - `src\actions\workflow_status_builder.py`
  - `src\behaviors\behavior.py`
  - `src\behaviors\behaviors.py`
  - `src\behaviors\json_behavior.py`
  - `src\behaviors\markdown_behavior.py`
  - `src\behaviors\tty_behavior.py`
  - `src\bot\behavior.py`
  - `src\bot\behaviors.py`
  - `src\bot\bot.py`
  - `src\bot\bot_paths.py`
  - `src\bot\json_bot.py`
  - `src\bot\markdown_bot.py`
  - `src\bot\tty_bot.py`
  - `src\bot\workspace.py`
  - `src\bot_path\bot_path.py`
  - `src\bot_path\json_bot_path.py`
  - `src\bot_path\markdown_bot_path.py`
  - `src\bot_path\path_resolver.py`
  - `src\bot_path\tty_bot_path.py`
  - `src\cli\adapter_factory.py`
  - `src\cli\adapters.py`
  - `src\cli\cli_main.py`
  - `src\cli\cli_results.py`
  - `src\cli\cli_session.py`
  - `src\exit_result\exit_result.py`
  - `src\exit_result\json_exit_result.py`
  - `src\exit_result\markdown_exit_result.py`
  - `src\exit_result\tty_exit_result.py`
  - `src\ext\behavior_matcher.py`
  - `src\ext\bot_matcher.py`
  - `src\ext\trigger_domain.py`
  - `src\ext\trigger_router.py`
  - `src\ext\trigger_router_entry.py`
  - `src\ext\trigger_words.py`
  - `src\help\help.py`
  - `src\help\help_action.py`
  - `src\help\json_help.py`
  - `src\help\markdown_help.py`
  - `src\help\tty_help.py`
  - `src\instructions\context_data_injector.py`
  - `src\instructions\instructions.py`
  - `src\instructions\json_instructions.py`
  - `src\instructions\markdown_instructions.py`
  - `src\instructions\reminders.py`
  - `src\instructions\tty_instructions.py`
  - `src\navigation\json_navigation.py`
  - `src\navigation\markdown_navigation.py`
  - `src\navigation\navigation.py`
  - `src\navigation\tty_navigation.py`
  - `src\rules\rule.py`
  - `src\rules\rule_filter.py`
  - `src\rules\rule_loader.py`
  - `src\rules\rules.py`
  - `src\rules\rules_action.py`
  - `src\rules\rules_digest_guidance.py`
  - `src\scanners\abstraction_levels_scanner.py`
  - `src\scanners\ac_consolidation_scanner.py`
  - `src\scanners\active_language_scanner.py`
  - `src\scanners\actor_alternation_scanner.py`
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
  - `src\scanners\dead_code_scanner.py`
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
  - `src\scanners\reaction_chaining_scanner.py`
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
  - `src\scope\action_scope.py`
  - `src\scope\json_scope.py`
  - `src\scope\markdown_scope.py`
  - `src\scope\scope.py`
  - `src\scope\scope_action_context.py`
  - `src\scope\scope_matcher.py`
  - `src\scope\scoping_parameter.py`
  - `src\scope\tty_scope.py`
  - `src\story_graph\domain.py`
  - `src\story_graph\json_story_graph.py`
  - `src\story_graph\markdown_story_graph.py`
  - `src\story_graph\nodes.py`
  - `src\story_graph\story_graph.py`
  - `src\story_graph\tty_story_graph.py`
  - `src\utils.py`
  - **Total:** 267 src file(s)

## Scanner Execution Status

### 🟩 Overall Status: HEALTHY

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 4 | Scanners ran without errors |
| 🟩 Clean Rules | 3 | No violations found |
| [i] No Scanner | 4 | Rule has no scanner configured |

**Total Rules:** 8
- **Rules with Scanners:** 4
  - 🟩 **Executed Successfully:** 4
- [i] **Rules without Scanners:** 4

### 🟩 Successfully Executed Scanners

- 🟨 **[Small And Testable](#small-and-testable)** - 13 violation(s) (EXECUTION_SUCCESS) - [View Details](#small-and-testable-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.implementation_details_scanner.ImplementationDetailsScanner`
- 🟩 **[Active Business And Behavioral Language](#active-business-and-behavioral-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.active_language_scanner.ActiveLanguageScanner`
- 🟩 **[Outcome Oriented Language](#outcome-oriented-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.communication_verb_scanner.CommunicationVerbScanner`
- 🟩 **[Verb Noun Format](#verb-noun-format)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.verb_noun_scanner.VerbNounScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Lightweight And Precise](#lightweight-and-precise)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Valuable](#valuable)** - No scanner configured
- <span style="color: gray;">[i]</span> **[User And System Behavior](#user-and-system-behavior)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Story Map Existing Code](#story-map-existing-code)** - No scanner configured

## Validation Rules Checked

### 🟩 Rule: <span id="active-business-and-behavioral-language">Active Business And Behavioral Language</span> - CLEAN (0 violations)
**Description:** Use active business language focused on user/system behavior. Describe what actors do with clear action verbs, not technical implementation or passive constructions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.active_language_scanner.ActiveLanguageScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="outcome-oriented-language">Outcome Oriented Language</span> - CLEAN (0 violations)
**Description:** Use outcome-oriented language over mechanism-oriented language. Focus on what is created or achieved, not how it's shown or communicated.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.communication_verb_scanner.CommunicationVerbScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="verb-noun-format">Verb Noun Format</span> - CLEAN (0 violations)
**Description:** Use verb-noun format consistently across all hierarchy levels. Actor --> verb noun [qualifiers]. Actor is documented separately, NOT in the name. Focus on specific actions with context.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="lightweight-and-precise">Lightweight And Precise</span> - NO SCANNER
**Description:** Create lightweight but precise documentation during shaping. Focus on structure and scope, not detailed specifications.
**Scanner:** Not configured

### 🟨 Rule: <span id="small-and-testable">Small And Testable</span> - 13 VIOLATION(S) - [View Details](#small-and-testable-violations)
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

## Violations Found

**Total Violations:** 13
- **File-by-File Violations:** 13
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="small-and-testable-violations">Small And Testable: 13 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`Generate Bot Tools`](vscode://file/C:/dev/augmented-teams/agile_bot/Generate%20Bot%20Tools): Story "Generate Bot Tools" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Behavior Tools`](vscode://file/C:/dev/augmented-teams/agile_bot/Generate%20Behavior%20Tools): Story "Generate Behavior Tools" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate MCP Bot Server`](vscode://file/C:/dev/augmented-teams/agile_bot/Generate%20MCP%20Bot%20Server): Story "Generate MCP Bot Server" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Behavior Action Tools`](vscode://file/C:/dev/augmented-teams/agile_bot/Generate%20Behavior%20Action%20Tools): Story "Generate Behavior Action Tools" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate REPL Command Definitions`](vscode://file/C:/dev/augmented-teams/agile_bot/Generate%20REPL%20Command%20Definitions): Story "Generate REPL Command Definitions" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate CLI Entry Point`](vscode://file/C:/dev/augmented-teams/agile_bot/Generate%20CLI%20Entry%20Point): Story "Generate CLI Entry Point" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Cursor Commands`](vscode://file/C:/dev/augmented-teams/agile_bot/Generate%20Cursor%20Commands): Story "Generate Cursor Commands" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Help Documentation`](vscode://file/C:/dev/augmented-teams/agile_bot/Generate%20Help%20Documentation): Story "Generate Help Documentation" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Set Scope Through Bot API`](vscode://file/C:/dev/augmented-teams/agile_bot/Set%20Scope%20Through%20Bot%20API): Story "Set Scope Through Bot API" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Store Clarification Data`](vscode://file/C:/dev/augmented-teams/agile_bot/Store%20Clarification%20Data): Story "Store Clarification Data" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Store Strategy Data`](vscode://file/C:/dev/augmented-teams/agile_bot/Store%20Strategy%20Data): Story "Store Strategy Data" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Create Build Scope`](vscode://file/C:/dev/augmented-teams/agile_bot/Create%20Build%20Scope): Story "Create Build Scope" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Violation Report`](vscode://file/C:/dev/augmented-teams/agile_bot/Generate%20Violation%20Report): Story "Generate Violation Report" appears to be an implementation operation - should be a step within a story that describes user/system outcome

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
*... and 52 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\docs\stories\reports\shape-validation-report-2026-01-09_03-00-51.md`

