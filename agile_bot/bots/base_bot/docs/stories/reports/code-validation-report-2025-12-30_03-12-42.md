# Validation Report - Code

**Generated:** 2025-12-30 03:13:41
**Project:** base_bot
**Behavior:** code
**Action:** validate

## Summary

Validated story map and domain model and 275 code file(s) against **32 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `story-graph.json`
- **Code Files Scanned:**
  - `src/actions/action.py`
  - `src/actions/action_context.py`
  - `src/actions/action_factory.py`
  - `src/actions/action_scope.py`
  - `src/actions/action_state_manager.py`
  - `src/actions/actions.py`
  - `src/actions/activity_tracker.py`
  - `src/actions/build/build_action.py`
  - `src/actions/build/build_scope.py`
  - `src/actions/build/knowledge.py`
  - `src/actions/build/knowledge_graph_spec.py`
  - `src/actions/build/knowledge_graph_template.py`
  - `src/actions/clarify/clarify_action.py`
  - `src/actions/clarify/evidence.py`
  - `src/actions/clarify/key_questions.py`
  - `src/actions/clarify/required_context.py`
  - `src/actions/clarify/requirements_clarifications.py`
  - `src/actions/content.py`
  - `src/actions/context_data_injector.py`
  - `src/actions/guardrails.py`
  - `src/actions/help_action.py`
  - `src/actions/instructions.py`
  - `src/actions/render/evidence.py`
  - `src/actions/render/render_action.py`
  - `src/actions/render/render_config_loader.py`
  - `src/actions/render/render_instruction_builder.py`
  - `src/actions/render/render_spec.py`
  - `src/actions/render/synchronizer.py`
  - `src/actions/render/template.py`
  - `src/actions/rules/rule.py`
  - `src/actions/rules/rule_filter.py`
  - `src/actions/rules/rule_loader.py`
  - `src/actions/rules/rules.py`
  - `src/actions/rules/rules_action.py`
  - `src/actions/rules/rules_digest_guidance.py`
  - `src/actions/scoping_parameter.py`
  - `src/actions/strategy/assumptions.py`
  - `src/actions/strategy/json_persistent.py`
  - `src/actions/strategy/strategy.py`
  - `src/actions/strategy/strategy_action.py`
  - `src/actions/strategy/strategy_criteria.py`
  - `src/actions/strategy/strategy_criterias.py`
  - `src/actions/strategy/strategy_decision.py`
  - `src/actions/validate/background_validation_handler.py`
  - `src/actions/validate/file_discovery.py`
  - `src/actions/validate/file_link_builder.py`
  - `src/actions/validate/knowledge_graph.py`
  - `src/actions/validate/path_resolver.py`
  - `src/actions/validate/story_graph.py`
  - `src/actions/validate/validate_action.py`
  - `src/actions/validate/validation_executor.py`
  - `src/actions/validate/validation_report_builder.py`
  - `src/actions/validate/validation_report_formatter.py`
  - `src/actions/validate/validation_report_writer.py`
  - `src/actions/validate/validation_scope.py`
  - `src/actions/validate/validation_stats.py`
  - `src/actions/validate/validation_violations_builder.py`
  - `src/actions/validate/violation_formatter.py`
  - `src/actions/workflow_status_builder.py`
  - `src/base_bot_cli.py`
  - `src/bot/behavior.py`
  - `src/bot/behaviors.py`
  - `src/bot/bot.py`
  - `src/bot/bot_paths.py`
  - `src/bot/merged_instructions.py`
  - `src/bot/reminders.py`
  - `src/bot/workspace.py`
  - `src/cli/action_data_collector.py`
  - `src/cli/base_bot_cli.py`
  - `src/cli/cli_action_parsers.py`
  - `src/cli/cli_code_visitor.py`
  - `src/cli/cli_command_router.py`
  - `src/cli/cli_context_builder.py`
  - `src/cli/cli_executor.py`
  - `src/cli/cli_generator.py`
  - `src/cli/cli_help_generator.py`
  - `src/cli/cli_help_renderer_visitor.py`
  - `src/cli/cli_parameter_parser.py`
  - `src/cli/cli_parser_generator.py`
  - `src/cli/cli_parser_generator_visitor.py`
  - `src/cli/cli_script_generator.py`
  - `src/cli/cursor/command_file_visitor.py`
  - `src/cli/cursor/command_generator.py`
  - `src/cli/cursor/command_renderer_visitor.py`
  - `src/cli/cursor/help_renderer_visitor.py`
  - `src/cli/cursor_command_file_visitor.py`
  - `src/cli/cursor_command_generator.py`
  - `src/cli/cursor_command_renderer_visitor.py`
  - `src/cli/cursor_help_renderer_visitor.py`
  - `src/cli/description_extractor.py`
  - `src/cli/formatter.py`
  - `src/cli/help_renderer.py`
  - `src/cli/mcp_code_visitor.py`
  - `src/cli/parameter_info_builder.py`
  - `src/cli/type_hint_converter.py`
  - `src/ext/behavior_matcher.py`
  - `src/ext/bot_matcher.py`
  - `src/ext/trigger_domain.py`
  - `src/ext/trigger_router.py`
  - `src/ext/trigger_router_entry.py`
  - `src/ext/trigger_words.py`
  - `src/generator/action_data_collector.py`
  - `src/generator/help_context.py`
  - `src/generator/orchestrator.py`
  - `src/generator/visitor.py`
  - `src/mcp/mcp_code_generator.py`
  - `src/mcp/mcp_code_visitor.py`
  - `src/mcp/mcp_config_generator.py`
  - `src/mcp/mcp_server.py`
  - `src/mcp/mcp_server_generator.py`
  - `src/mcp/server_deployer.py`
  - `src/mcp/server_restart.py`
  - `src/repl_cli/cli_base.py`
  - `src/repl_cli/cli_bot/cli_actions/build_cli_action.py`
  - `src/repl_cli/cli_bot/cli_actions/clarify_cli_action.py`
  - `src/repl_cli/cli_bot/cli_actions/cli_action.py`
  - `src/repl_cli/cli_bot/cli_actions/cli_action_factory.py`
  - `src/repl_cli/cli_bot/cli_actions/cli_actions.py`
  - `src/repl_cli/cli_bot/cli_actions/render_cli_action.py`
  - `src/repl_cli/cli_bot/cli_actions/strategy_cli_action.py`
  - `src/repl_cli/cli_bot/cli_actions/validate_cli_action.py`
  - `src/repl_cli/cli_bot/cli_behavior.py`
  - `src/repl_cli/cli_bot/cli_behaviors.py`
  - `src/repl_cli/cli_bot/cli_bot.py`
  - `src/repl_cli/cli_scope.py`
  - `src/repl_cli/command_parser.py`
  - `src/repl_cli/formatters/formatter_factory.py`
  - `src/repl_cli/formatters/markdown_formatter.py`
  - `src/repl_cli/formatters/output_formatter.py`
  - `src/repl_cli/formatters/terminal_formatter.py`
  - `src/repl_cli/headless/cursor_api.py`
  - `src/repl_cli/headless/error_recovery.py`
  - `src/repl_cli/headless/execution_context.py`
  - `src/repl_cli/headless/execution_result.py`
  - `src/repl_cli/headless/headless_config.py`
  - `src/repl_cli/headless/headless_session.py`
  - `src/repl_cli/headless/non_recoverable_error.py`
  - `src/repl_cli/headless/recoverable_error.py`
  - `src/repl_cli/headless/session_log.py`
  - `src/repl_cli/repl_help.py`
  - `src/repl_cli/repl_main.py`
  - `src/repl_cli/repl_results.py`
  - `src/repl_cli/repl_session.py`
  - `src/repl_cli/repl_status.py`
  - `src/repl_cli/status_display.py`
  - `src/scanners/abstraction_levels_scanner.py`
  - `src/scanners/ac_consolidation_scanner.py`
  - `src/scanners/active_language_scanner.py`
  - `src/scanners/arrange_act_assert_scanner.py`
  - `src/scanners/ascii_only_scanner.py`
  - `src/scanners/background_common_setup_scanner.py`
  - `src/scanners/bad_comments_scanner.py`
  - `src/scanners/behavioral_ac_scanner.py`
  - `src/scanners/business_readable_test_names_scanner.py`
  - `src/scanners/calculation_timing_code_scanner.py`
  - `src/scanners/calculation_timing_scanner.py`
  - `src/scanners/class_based_organization_scanner.py`
  - `src/scanners/class_size_scanner.py`
  - `src/scanners/clear_parameters_scanner.py`
  - `src/scanners/code_representation_code_scanner.py`
  - `src/scanners/code_representation_scanner.py`
  - `src/scanners/code_scanner.py`
  - `src/scanners/communication_verb_scanner.py`
  - `src/scanners/complete_refactoring_scanner.py`
  - `src/scanners/complexity_metrics.py`
  - `src/scanners/consistent_indentation_scanner.py`
  - `src/scanners/consistent_naming_scanner.py`
  - `src/scanners/consistent_vocabulary_scanner.py`
  - `src/scanners/cover_all_paths_scanner.py`
  - `src/scanners/delegation_code_scanner.py`
  - `src/scanners/delegation_scanner.py`
  - `src/scanners/dependency_chaining_code_scanner.py`
  - `src/scanners/dependency_chaining_scanner.py`
  - `src/scanners/descriptive_function_names_scanner.py`
  - `src/scanners/domain_concept_node.py`
  - `src/scanners/domain_grouping_code_scanner.py`
  - `src/scanners/domain_grouping_scanner.py`
  - `src/scanners/domain_language_code_scanner.py`
  - `src/scanners/domain_language_scanner.py`
  - `src/scanners/domain_scanner.py`
  - `src/scanners/duplication_scanner.py`
  - `src/scanners/encapsulation_scanner.py`
  - `src/scanners/enumerate_ac_permutations_scanner.py`
  - `src/scanners/enumerate_stories_scanner.py`
  - `src/scanners/error_handling_isolation_scanner.py`
  - `src/scanners/exact_variable_names_scanner.py`
  - `src/scanners/exception_classification_scanner.py`
  - `src/scanners/exception_handling_scanner.py`
  - `src/scanners/excessive_guards_scanner.py`
  - `src/scanners/exhaustive_decomposition_scanner.py`
  - `src/scanners/explicit_dependencies_scanner.py`
  - `src/scanners/fixture_placement_scanner.py`
  - `src/scanners/function_size_scanner.py`
  - `src/scanners/generic_capability_scanner.py`
  - `src/scanners/given_precondition_scanner.py`
  - `src/scanners/given_state_not_actions_scanner.py`
  - `src/scanners/given_when_then_helpers_scanner.py`
  - `src/scanners/implementation_details_scanner.py`
  - `src/scanners/import_placement_scanner.py`
  - `src/scanners/increment_folder_structure_scanner.py`
  - `src/scanners/intention_revealing_names_scanner.py`
  - `src/scanners/invest_principles_scanner.py`
  - `src/scanners/meaningful_context_scanner.py`
  - `src/scanners/minimize_mutable_state_scanner.py`
  - `src/scanners/mock_boundaries_scanner.py`
  - `src/scanners/natural_english_code_scanner.py`
  - `src/scanners/natural_english_scanner.py`
  - `src/scanners/no_fallbacks_scanner.py`
  - `src/scanners/no_guard_clauses_scanner.py`
  - `src/scanners/noun_redundancy_scanner.py`
  - `src/scanners/observable_behavior_scanner.py`
  - `src/scanners/one_concept_per_test_scanner.py`
  - `src/scanners/open_closed_principle_scanner.py`
  - `src/scanners/parameterized_tests_scanner.py`
  - `src/scanners/plain_english_scenarios_scanner.py`
  - `src/scanners/prefer_object_model_over_config_scanner.py`
  - `src/scanners/present_ac_consolidation_scanner.py`
  - `src/scanners/primitive_vs_object_scanner.py`
  - `src/scanners/property_encapsulation_code_scanner.py`
  - `src/scanners/property_encapsulation_scanner.py`
  - `src/scanners/real_implementations_scanner.py`
  - `src/scanners/resource_oriented_code_scanner.py`
  - `src/scanners/resource_oriented_design_scanner.py`
  - `src/scanners/resources/ast_elements.py`
  - `src/scanners/resources/block.py`
  - `src/scanners/resources/block_extractor.py`
  - `src/scanners/resources/file.py`
  - `src/scanners/resources/line.py`
  - `src/scanners/resources/scan.py`
  - `src/scanners/resources/scope.py`
  - `src/scanners/resources/violation.py`
  - `src/scanners/scanner.py`
  - `src/scanners/scanner_execution_error.py`
  - `src/scanners/scanner_loader.py`
  - `src/scanners/scanner_orchestrator.py`
  - `src/scanners/scanner_registry.py`
  - `src/scanners/scanner_status_formatter.py`
  - `src/scanners/scenario_outline_scanner.py`
  - `src/scanners/scenario_specific_given_scanner.py`
  - `src/scanners/scenarios_cover_all_cases_scanner.py`
  - `src/scanners/scenarios_on_story_docs_scanner.py`
  - `src/scanners/separate_concerns_scanner.py`
  - `src/scanners/simplify_control_flow_scanner.py`
  - `src/scanners/single_responsibility_scanner.py`
  - `src/scanners/specification_match_scanner.py`
  - `src/scanners/specificity_scanner.py`
  - `src/scanners/spine_optional_scanner.py`
  - `src/scanners/story_enumeration_scanner.py`
  - `src/scanners/story_filename_scanner.py`
  - `src/scanners/story_graph_match_scanner.py`
  - `src/scanners/story_map.py`
  - `src/scanners/story_scanner.py`
  - `src/scanners/story_sizing_scanner.py`
  - `src/scanners/swallowed_exceptions_scanner.py`
  - `src/scanners/technical_abstraction_code_scanner.py`
  - `src/scanners/technical_abstraction_scanner.py`
  - `src/scanners/technical_language_scanner.py`
  - `src/scanners/test_boundary_behavior_scanner.py`
  - `src/scanners/test_file_naming_scanner.py`
  - `src/scanners/test_quality_scanner.py`
  - `src/scanners/test_scanner.py`
  - `src/scanners/third_party_isolation_scanner.py`
  - `src/scanners/type_safety_scanner.py`
  - `src/scanners/ubiquitous_language_scanner.py`
  - `src/scanners/unnecessary_parameter_passing_scanner.py`
  - `src/scanners/useless_comments_scanner.py`
  - `src/scanners/validation_scanner_status_builder.py`
  - `src/scanners/verb_noun_scanner.py`
  - `src/scanners/vertical_density_scanner.py`
  - `src/scanners/vertical_slice_scanner.py`
  - `src/scanners/violation.py`
  - `src/scanners/vocabulary_helper.py`
  - `src/story_graph/domain.py`
  - `src/story_graph/nodes.py`
  - `src/utils.py`
  - **Total:** 275 src file(s)

## Scanner Execution Status

### 🟨 Overall Status: NEEDS ATTENTION

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 29 | Scanners ran without errors |
| 🟩 Clean Rules | 16 | No violations found |
| 🟨 Rules with Warnings | 8 | Found 25 warning violation(s) |
| 🟥 Rules with Errors | 3 | Found 591 error violation(s) |
| 🟥 Load Failed | 1 | Scanner could not be loaded |
| [i] No Scanner | 2 | Rule has no scanner configured |

**Total Rules:** 32
- **Rules with Scanners:** 30
  - 🟩 **Executed Successfully:** 29
  - 🟥 **Load Failed:** 1
- [i] **Rules without Scanners:** 2

### 🟩 Successfully Executed Scanners

- 🟥 **[Eliminate Duplication](#eliminate-duplication)** - 551 violation(s) (EXECUTION_SUCCESS) - [View Details](#eliminate-duplication-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.duplication_scanner.DuplicationScanner`
- 🟨 **[Use Domain Language](#use-domain-language)** - 108 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-domain-language-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
- 🟥 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 36 violation(s) (EXECUTION_SUCCESS) - [View Details](#stop-writing-useless-comments-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟨 **[Maintain Vertical Density](#maintain-vertical-density)** - 13 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-vertical-density-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟨 **[Simplify Control Flow](#simplify-control-flow)** - 7 violation(s) (EXECUTION_SUCCESS) - [View Details](#simplify-control-flow-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟨 **[Avoid Unnecessary Parameter Passing](#avoid-unnecessary-parameter-passing)** - 4 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-unnecessary-parameter-passing-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
- 🟨 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 4 violation(s) (EXECUTION_SUCCESS) - [View Details](#chain-dependencies-properly-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟥 **[Never Swallow Exceptions](#never-swallow-exceptions)** - 4 violation(s) (EXECUTION_SUCCESS) - [View Details](#never-swallow-exceptions-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
- 🟨 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#refactor-completely-not-partially-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
- 🟨 **[Enforce Encapsulation](#enforce-encapsulation)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#enforce-encapsulation-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.encapsulation_scanner.EncapsulationScanner`
- 🟨 **[Keep Classes Small With Single Responsibility](#keep-classes-small-with-single-responsibility)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-classes-small-with-single-responsibility-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.class_size_scanner.ClassSizeScanner`
- 🟨 **[Keep Functions Small Focused](#keep-functions-small-focused)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-functions-small-focused-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.function_size_scanner.FunctionSizeScanner`
- 🟨 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-excessive-guards-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🟩 **[Classify Exceptions By Caller Needs](#classify-exceptions-by-caller-needs)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.exception_classification_scanner.ExceptionClassificationScanner`
- 🟩 **[Delegate To Lowest Level](#delegate-to-lowest-level)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.delegation_code_scanner.DelegationCodeScanner`
- 🟩 **[Favor Code Representation](#favor-code-representation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
- 🟩 **[Group By Domain](#group-by-domain)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
- 🟩 **[Hide Business Logic Behind Properties](#hide-business-logic-behind-properties)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟩 **[Hide Calculation Timing](#hide-calculation-timing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟩 **[Keep Functions Single Responsibility](#keep-functions-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟩 **[Place Imports At Top](#place-imports-at-top)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟩 **[Prefer Object Model Over Config](#prefer-object-model-over-config)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.prefer_object_model_over_config_scanner.PreferObjectModelOverConfigScanner`
- 🟩 **[Provide Meaningful Context](#provide-meaningful-context)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.meaningful_context_scanner.MeaningfulContextScanner`
- 🟩 **[Use Clear Function Parameters](#use-clear-function-parameters)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.clear_parameters_scanner.ClearParametersScanner`
- 🟩 **[Use Consistent Indentation](#use-consistent-indentation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.consistent_indentation_scanner.ConsistentIndentationScanner`
- 🟩 **[Use Consistent Naming](#use-consistent-naming)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.consistent_naming_scanner.ConsistentNamingScanner`
- 🟩 **[Use Exceptions Properly](#use-exceptions-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.exception_handling_scanner.ExceptionHandlingScanner`
- 🟩 **[Use Explicit Dependencies](#use-explicit-dependencies)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
- 🟩 **[Use Natural English](#use-natural-english)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.natural_english_code_scanner.NaturalEnglishCodeScanner`

### 🟥 Scanner Load Failures

- 🟥 **[Use Resource Oriented Design](#use-resource-oriented-design)** - LOAD FAILED
  - Scanner Path: `agile_bot.bots.base_bot.src.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`
  - Error: `Scanner class not found: agile_bot.bots.base_bot.src.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Detect Legacy Unused Code](#detect-legacy-unused-code)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Refactor Tests With Production Code](#refactor-tests-with-production-code)** - No scanner configured

## Validation Rules Checked

### 🟥 Rule: <span id="use-resource-oriented-design">Use Resource Oriented Design</span> - FAILED
**Description:** CRITICAL: Code must use resource-oriented, object-oriented design. Use object-oriented classes (singular or collection) with responsibilities that encapsulate logic over manager/doer/loader patterns. Maximize encapsulation through collaborator relationships.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`
**Error:** `Scanner class not found: agile_bot.bots.base_bot.src.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`

### 🟥 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - 551 ERROR(S) - [View Details](#eliminate-duplication-violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="stop-writing-useless-comments">Stop Writing Useless Comments</span> - 36 ERROR(S) - [View Details](#stop-writing-useless-comments-violations)
**Description:** CRITICAL: DO NOT WRITE COMMENTS. Delete all comments written by the AI chat. Code must be self-explanatory through clear naming and structure. ONLY exception: legal/license requirements. If you think a comment is needed, the code is wrong - fix the code instead.
**Scanner:** `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="never-swallow-exceptions">Never Swallow Exceptions</span> - 4 ERROR(S) - [View Details](#never-swallow-exceptions-violations)
**Description:** CRITICAL: Never swallow exceptions silently. Empty catch blocks hide failures and make debugging impossible. Always log, handle, or rethrow exceptions with context.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="simplify-control-flow">Simplify Control Flow</span> - 7 WARNING(S) - [View Details](#simplify-control-flow-violations)
**Description:** Keep nesting minimal and control flow straightforward. Use guard clauses to reduce nesting and extract nested blocks into separate functions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="avoid-unnecessary-parameter-passing">Avoid Unnecessary Parameter Passing</span> - 4 WARNING(S) - [View Details](#avoid-unnecessary-parameter-passing-violations)
**Description:** Don't pass parameters to internal methods when the value is already accessible through instance variables. Access instance properties directly instead of passing them around unnecessarily.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="chain-dependencies-properly">Chain Dependencies Properly</span> - 4 WARNING(S) - [View Details](#chain-dependencies-properly-violations)
**Description:** CRITICAL: Code must chain dependencies properly with constructor injection. Map dependencies in a chain: highest-level object → collaborator → sub-collaborator. Inject collaborators at construction time so methods can use them without passing them as parameters. Access sub-collaborators through their owning objects.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="refactor-completely-not-partially">Refactor Completely Not Partially</span> - 3 WARNING(S) - [View Details](#refactor-completely-not-partially-violations)
**Description:** CRITICAL: When refactoring, replace old code completely - don't try to support both legacy and new patterns. Write new code, delete old code, fix tests. Clean breaks are better than compatibility bridges that create technical debt.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="enforce-encapsulation">Enforce Encapsulation</span> - 2 WARNING(S) - [View Details](#enforce-encapsulation-violations)
**Description:** CRITICAL: Hide implementation details and expose minimal interface. Make fields private by default, expose behavior not data. NEVER pass raw dicts/lists that expose internal structure - use typed objects that encapsulate the data. Follow Law of Demeter (principle of least knowledge).
**Scanner:** `agile_bot.bots.base_bot.src.scanners.encapsulation_scanner.EncapsulationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-classes-small-with-single-responsibility">Keep Classes Small With Single Responsibility</span> - 2 WARNING(S) - [View Details](#keep-classes-small-with-single-responsibility-violations)
**Description:** CRITICAL: Classes should be small (under 200-300 lines) with a single responsibility. Keep classes cohesive (methods/data interdependent), eliminate dead code, and favor many small focused classes over few large ones.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.class_size_scanner.ClassSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-functions-small-focused">Keep Functions Small Focused</span> - 2 WARNING(S) - [View Details](#keep-functions-small-focused-violations)
**Description:** Functions should be small enough to understand at a glance. Keep functions under 20 lines when possible and extract complex logic into named helper functions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.function_size_scanner.FunctionSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="avoid-excessive-guards">Avoid Excessive Guards</span> - 1 WARNING(S) - [View Details](#avoid-excessive-guards-violations)
**Description:** Excessive guard clauses add to cyclomatic complexity and make code harder to read. Centralize error handling in one place rather than scattering defensive checks throughout the code. Let code fail fast with clear errors rather than silently handling missing components.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="classify-exceptions-by-caller-needs">Classify Exceptions By Caller Needs</span> - CLEAN (0 violations)
**Description:** Design exceptions based on how callers will handle them. Create exception types based on caller's needs, use special case objects for predictable failures, and wrap third-party exceptions at boundaries.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.exception_classification_scanner.ExceptionClassificationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="delegate-to-lowest-level">Delegate To Lowest Level</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must delegate responsibilities to the lowest-level object that can handle them. If a collection class can do something, delegate to it rather than implementing it in the parent.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.delegation_code_scanner.DelegationCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="favor-code-representation">Favor Code Representation</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code should represent domain concepts directly. Domain models should match code. If code doesn't match domain concepts, refactor the code rather than creating abstract domain models.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="group-by-domain">Group By Domain</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must be organized by domain area and relationships, not by technical layers, object types, or architectural concerns.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="hide-business-logic-behind-properties">Hide Business Logic Behind Properties</span> - CLEAN (0 violations)
**Description:** CRITICAL: Hide business logic behind properties. Properties hide logic that occurs—it may be computed on-demand, cached, pre-computed, or loaded from storage. The caller shouldn't know or care when the values are calculated / determined.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="hide-calculation-timing">Hide Calculation Timing</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must hide calculations. Properties hide logic that occurs—it may be computed on-demand, cached, pre-computed, or loaded from storage. The caller shouldn't know or care when the values are calculated / determined.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="keep-functions-single-responsibility">Keep Functions Single Responsibility</span> - CLEAN (0 violations)
**Description:** CRITICAL: Functions should do one thing and do it well, with no hidden side effects. Each function must have a single, well-defined responsibility.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="place-imports-at-top">Place Imports At Top</span> - CLEAN (0 violations)
**Description:** Place all import statements at the top of the file, after module docstrings and comments, but before any executable code. This improves readability and makes dependencies clear.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.import_placement_scanner.ImportPlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

*... and 12 more rules*

## Violations Found

**Total Violations:** 737
- **File-by-File Violations:** 188
- **Cross-File Violations:** 549

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="avoid-excessive-guards-violations">Avoid Excessive Guards: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1459): Line 1459: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

    ```python
        def parse_command_parameters(self, args: str) -> Dict[str, Any]:
            params = {}
            if not args:
                return params
            
    ```

#### <span id="avoid-unnecessary-parameter-passing-violations">Avoid Unnecessary Parameter Passing: 4 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:129): Internal method "_run_with_streaming" receives parameter "timeout" that matches instance attribute. Consider accessing via self.timeout instead.
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:267): Internal method "_run_cursor_agent" receives parameter "timeout" that matches instance attribute. Consider accessing via self.timeout instead.
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:283): Internal method "_run_via_wsl" receives parameter "timeout" that matches instance attribute. Consider accessing via self.timeout instead.
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:356): Internal method "_run_directly" receives parameter "timeout" that matches instance attribute. Consider accessing via self.timeout instead.

#### <span id="chain-dependencies-properly-violations">Chain Dependencies Properly: 4 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:129): Method "_run_with_streaming" in Test class [CursorHeadlessAPI](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:129) takes parameter "timeout" that is already injected in __init__. Use self.timeout instead.

```python
            raise RecoverableError('cursor-agent timed out')
    
    def _run_with_streaming(self, cmd: List[str], timeout: int) -> subprocess.CompletedProcess:
        """Run command with real-time streaming output."""
        import time
    # ... (truncated)
```
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:267): Method "_run_cursor_agent" in Test class [CursorHeadlessAPI](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:267) takes parameter "timeout" that is already injected in __init__. Use self.timeout instead.

```python
                sys.stdout.flush()
    
    def _run_cursor_agent(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        """Run cursor-agent CLI command.
        
    # ... (truncated)
```
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:283): Method "_run_via_wsl" in Test class [CursorHeadlessAPI](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:283) takes parameter "timeout" that is already injected in __init__. Use self.timeout instead.

```python
            return self._run_directly(prompt, timeout, resume_chat_id)
    
    def _run_via_wsl(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        import tempfile
        
    # ... (truncated)
```
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:356): Method "_run_directly" in Test class [CursorHeadlessAPI](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:356) takes parameter "timeout" that is already injected in __init__. Use self.timeout instead.

```python
                    pass
    
    def _run_directly(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
        if self.stream:
            cmd = ['cursor-agent', '--print', '--output-format', 'stream-json', '--stream-partial-output', '--force']
    # ... (truncated)
```

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 2 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (display_current_state:191-202):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion             ...
    ```

  Location (display_current_state:226-234):
    ```python
    lines.append(formatter.subsection_separator())
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:469): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_handle_next_command:469-488):
    ```python
    if not self.has_current_action:
        return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
    behavior = self.current_behavior
    if not behavior:...
    ```

  Location (_handle_back_command:505-524):
    ```python
    if not self.has_current_action:
        return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
    behavior = self.current_behavior
    if not behavior:...
    ```

#### <span id="enforce-encapsulation-violations">Enforce Encapsulation: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:722): Method "_handle_scope_command" in Test class [REPLSession](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:722) has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:333): Method "_run_via_wsl" in Test class [CursorHeadlessAPI](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:333) has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

#### <span id="keep-classes-small-with-single-responsibility-violations">Keep Classes Small With Single Responsibility: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:17): Class "REPLSession" is 1578 lines - should be under 300 lines (extract related methods into separate classes)

```python


class REPLSession:
    def __init__(self, bot, workspace_directory: Path):
        self.cli_bot = CLIBot(bot, self)
        self.workspace_directory = Path(workspace_directory)
        tty_result = self.detect_tty()
        self.formatter = FormatterFactory.create_formatter(tty_detected=tty_result.tty_detected)
    
    @property
    # ... (truncated)
```
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:30): Class "CursorHeadlessAPI" is 418 lines - should be under 300 lines (extract related methods into separate classes)

```python


class CursorHeadlessAPI:
    """Executes instructions via cursor-agent CLI command.
    
    Uses --print flag for non-interactive/headless execution.
    On Windows, runs cursor-agent through WSL Ubuntu.
    """
    
    def __init__(self, api_key: str = None, model: str = None, timeout: int = 600, workspace_path: Optional[Path] = None, stream: bool = True):
    # ... (truncated)
```

#### <span id="keep-functions-small-focused-violations">Keep Functions Small Focused: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:144): Function "display_current_state" is 83 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return True
        
        def display_current_state(self, full=False) -> REPLStateDisplay:
            """Single source of truth for displaying current bot state.
            
            Returns REPLStateDisplay with formatted status output showing:
            - Bot name and paths
            - Current position header
            - Scope filter (if set)
            - Progress in workflow
            - Hierarchical behavior/action/operation tree
            """
            if not self.has_current_action:
                if not self._initialize_to_first_behavior_action():
                    return REPLStateDisplay(
                        output="No behaviors available\n\n  help          - Show detailed help\n  exit          - Exit REPL",
                        state_loaded=False
                    )
                return self.display_current_state(full=full)
            
            lines = []
            formatter = self.formatter
            
            # Get bot name from bot_directory
            if self.bot and hasattr(self.bot, 'bot_paths'):
                bot_name = self.bot.bot_paths.bot_directory.name
            else:
                bot_name = 'UNKNOWN'
            
            # THICK LINE at top
            lines.append(formatter.section_separator())
            lines.append("")
            
            # Bot section header
            lines.append(f"## {formatter.bot_icon()} Bot: {bot_name}")
            
            if self.bot:
                bot_path = self.bot.bot_paths.bot_directory if hasattr(self.bot, 'bot_paths') else 'Unknown'
                lines.append(f"**Bot Path:**")
                lines.append("```")
                lines.append(str(bot_path))
                lines.append("```")
            
            lines.append("")
            
            # Workspace section
            workspace_name = self.workspace_directory.name if hasattr(self.workspace_directory, 'name') else 'base_bot'
            lines.append(f"{formatter.workspace_icon()} **Workspace:** {workspace_name}")
            lines.append(f"**Path:**")
            lines.append("```")
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:57): Function "starts_session" is 38 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return self._chat_id
        
        def starts_session(self, instructions: str) -> APIResponse:
            """Start a headless session by running cursor-agent with the instructions."""
            import uuid
            self._session_id = str(uuid.uuid4())[:8]
            
            print(f"[DEBUG] starts_session called, about to run cursor-agent")
            sys.stdout.flush()
            
            try:
                result = self._run_cursor_agent(instructions, timeout=self.timeout)
                
                print(f"[DEBUG] cursor-agent finished with returncode: {result.returncode}")
                sys.stdout.flush()
                
                if result.returncode != 0:
                    error_msg = result.stderr.strip() if result.stderr else result.stdout.strip() or 'Unknown error'
                    
                    # Check for common errors
                    if 'not found' in error_msg.lower() or 'not recognized' in error_msg.lower():
                        raise NonRecoverableError(
                            'cursor-agent not found. On Windows, install via WSL: '
                            'wsl -d Ubuntu -e bash -c "curl https://cursor.com/install -fsS | bash"'
                        )
                    if 'unauthorized' in error_msg.lower() or 'authentication' in error_msg.lower():
                        raise NonRecoverableError(f'Authentication failed: {error_msg}')
                    if 'rate limit' in error_msg.lower():
                        raise RecoverableError(f'Rate limited: {error_msg}')
                        
                    raise RecoverableError(f'cursor-agent failed (exit {result.returncode}): {error_msg}')
                
                self._last_output = result.stdout
                response = self._parse_cursor_output(result.stdout)
                
                print(f"[DEBUG] _parse_cursor_output returned done={response.done}")
                sys.stdout.flush()
                
                # Extract chatId from response for session resumption
                # cursor-agent should return chatId in the response
                if response.session_id:
                    self._chat_id = response.session_id
                
                return response
                
            except FileNotFoundError as e:
                raise NonRecoverableError(
                    f'cursor-agent command not found: {e}. '
                    'On Windows, install via WSL: wsl -d Ubuntu -e bash -c "curl https://cursor.com/install -fsS | bash"'
                )
        # ... (truncated)
    ```

#### <span id="maintain-vertical-density-violations">Maintain Vertical Density: 13 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:144): Function "display_current_state" is 114 lines - consider improving vertical density by declaring variables near usage

    ```python
            return True
        
        def display_current_state(self, full=False) -> REPLStateDisplay:
            """Single source of truth for displaying current bot state.
            
            Returns REPLStateDisplay with formatted status output showing:
            - Bot name and paths
            - Current position header
            - Scope filter (if set)
            - Progress in workflow
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:268): Function "_convert_domain_result_to_repl_response" is 57 lines - consider improving vertical density by declaring variables near usage

    ```python
            return state_display.output
        
        def _convert_domain_result_to_repl_response(self, result: Dict[str, Any], command: str) -> REPLCommandResponse:
            """Convert a domain method result to a REPL response.
            
            Args:
                result: Dict returned from domain method
                command: The command that was executed
            
            Returns:
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:339): Function "_handle_simple_command" is 59 lines - consider improving vertical density by declaring variables near usage

    ```python
            return self._handle_simple_command(command)
        
        def _handle_simple_command(self, command: str) -> REPLCommandResponse:
            parts = command.split(maxsplit=1)
            command_verb = parts[0].lower()
            command_args = parts[1] if len(parts) > 1 else ""
            
            # Meta commands
            if command_verb == 'help':
                return self._handle_help_command(command_args)
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:549): Function "_handle_instructions_command" is 53 lines - consider improving vertical density by declaring variables near usage

    ```python
            )
        
        def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
            """Handle instructions command"""
            if not self.has_current_action:
                return REPLCommandResponse(
                    output="ERROR: No current action to get instructions for",
                    response="ERROR: No current action",
                    status="error"
                )
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:624): Function "_handle_confirm_command" is 54 lines - consider improving vertical density by declaring variables near usage

    ```python
                )
        
        def _handle_confirm_command(self) -> REPLCommandResponse:
            """Handle confirm command"""
            if not self.has_current_action:
                return REPLCommandResponse(
                    output="ERROR: No current action to confirm",
                    response="ERROR: No current action",
                    status="error"
                )
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:698): Function "_handle_scope_command" is 65 lines - consider improving vertical density by declaring variables near usage

    ```python
            )
        
        def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
            """Handle scope command"""
            if not args:
                # Show current scope
                output = self.cli_bot.get_scope_display()
                return REPLCommandResponse(
                    output=output,
                    response=output,
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:839): Function "_execute_operation_locally" is 60 lines - consider improving vertical density by declaring variables near usage

    ```python
                return None, args.strip().strip('"').strip("'")
        
        def _execute_operation_locally(self, target: str, cli_args: str = "") -> str:
            """Execute a CLI operation locally and return its output.
            
            Args:
                target: CLI target (e.g., 'tests.build', 'tests.build.instructions', 'tests.build.submit')
                cli_args: CLI arguments like '--scope "X"'
            
            Returns:
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1129): Function "_handle_dot_notation" is 127 lines - consider improving vertical density by declaring variables near usage

    ```python
                pass
        
        def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
            """Handle dot notation commands (behavior.action.operation)"""
            # Parse dot notation: behavior.action.operation or action.operation or .operation
            parts = command.split()
            dot_path = parts[0]
            args = ' '.join(parts[1:]) if len(parts) > 1 else ""
            
            path_parts = dot_path.split('.')
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1257): Function "_handle_action_shortcut" is 60 lines - consider improving vertical density by declaring variables near usage

    ```python
                )
        
        def _handle_action_shortcut(self, action_name: str, args_str: str) -> REPLCommandResponse:
            args_str = args_str.strip()
            
            # Parse CLI-style arguments (--message, --scope, etc.)
            cli_args = []
            subcommand = None
            
            if args_str:
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1362): Function "_execute_action_with_args" is 73 lines - consider improving vertical density by declaring variables near usage

    ```python
            return converted_args
        
        def _execute_action_with_args(self, action_name: str, cli_args: list, operation: str = None) -> REPLCommandResponse:
            if not self.has_current_behavior:
                return REPLCommandResponse(
                    output="ERROR: No current behavior set. Please select a behavior first.",
                    response="ERROR: No current behavior set",
                    status="error"
                )
            
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:129): Function "_run_with_streaming" is 61 lines - consider improving vertical density by declaring variables near usage

    ```python
                raise RecoverableError('cursor-agent timed out')
        
        def _run_with_streaming(self, cmd: List[str], timeout: int) -> subprocess.CompletedProcess:
            """Run command with real-time streaming output."""
            import time
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:191): Function "_print_cleaned_stream_line" is 75 lines - consider improving vertical density by declaring variables near usage

    ```python
                raise e
        
        def _print_cleaned_stream_line(self, line: str):
            """Parse JSON stream line and print only meaningful content."""
            line = line.strip()
            if not line:
                return
            
            try:
                data = json.loads(line)
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:283): Function "_run_via_wsl" is 72 lines - consider improving vertical density by declaring variables near usage

    ```python
                return self._run_directly(prompt, timeout, resume_chat_id)
        
        def _run_via_wsl(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
            import tempfile
            
            temp_prompt_file = None
            temp_script_file = None
            
            try:
                if len(prompt) > 4000:
        # ... (truncated)
    ```

#### <span id="never-swallow-exceptions-violations">Never Swallow Exceptions: 4 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1126): Except block only contains pass at line 1126 - exceptions must be logged or rethrown, never swallowed

    ```python
                state_data['completed_behaviors'] = completed
                state_file.write_text(json.dumps(state_data, indent=2))
            except (json.JSONDecodeError, IOError):
                pass
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:78): Except block only contains pass at line 78 - exceptions must be logged or rethrown, never swallowed

    ```python
                    state_data = json.loads(state_file.read_text())
                    return state_data.get('action_phase', 'not_started')
                except (json.JSONDecodeError, IOError):
                    pass
            return 'not_started'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:348): Except block only contains pass at line 348 - exceptions must be logged or rethrown, never swallowed

    ```python
                    try:
                        os.unlink(temp_prompt_file)
                    except:
                        pass
                if temp_script_file:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:353): Except block only contains pass at line 353 - exceptions must be logged or rethrown, never swallowed

    ```python
                    try:
                        os.unlink(temp_script_file)
                    except:
                        pass
        
    ```

#### <span id="refactor-completely-not-partially-violations">Refactor Completely Not Partially: 3 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:72): Fallback/legacy support code found (comment at line 72, code at line 73) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:239): Fallback/legacy support code found (comment at line 239, code at line 240) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1505): Fallback/legacy support code found (comment at line 1505, code at line 1506) - complete refactoring by removing old pattern support

#### <span id="simplify-control-flow-violations">Simplify Control Flow: 7 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:438): Function "_handle_current_command" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            )
        
        def _handle_current_command(self) -> REPLCommandResponse:
            """Re-execute current operation based on progress state"""
            if not self.has_current_action:
                return REPLCommandResponse(
                    output="ERROR: No current action",
                    response="ERROR: No current action",
                    status="error"
                )
            
            # Extract operation from progress (behavior.action.operation)
            progress = self.get_progress_line()
            if '.' in progress and 'Progress: ' in progress:
                parts = progress.replace('Progress: ', '').split('.')
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:698): Function "_handle_scope_command" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            )
        
        def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
            """Handle scope command"""
            if not args:
                # Show current scope
                output = self.cli_bot.get_scope_display()
                return REPLCommandResponse(
                    output=output,
                    response=output,
                    status="success"
                )
            
            # Handle "all" - clears the scope filter
            if args.lower() == 'all':
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:839): Function "_execute_operation_locally" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                return None, args.strip().strip('"').strip("'")
        
        def _execute_operation_locally(self, target: str, cli_args: str = "") -> str:
            """Execute a CLI operation locally and return its output.
            
            Args:
                target: CLI target (e.g., 'tests.build', 'tests.build.instructions', 'tests.build.submit')
                cli_args: CLI arguments like '--scope "X"'
            
            Returns:
                Output from the operation (instructions, submit result, confirm result, etc.)
            """
            # Parse target
            parts = target.split('.')
            if len(parts) < 2:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1129): Function "_handle_dot_notation" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                pass
        
        def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
            """Handle dot notation commands (behavior.action.operation)"""
            # Parse dot notation: behavior.action.operation or action.operation or .operation
            parts = command.split()
            dot_path = parts[0]
            args = ' '.join(parts[1:]) if len(parts) > 1 else ""
            
            path_parts = dot_path.split('.')
            
            # . alone means current position
            if dot_path == '.':
                return self._handle_current_command()
            
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1325): Function "_convert_repl_scope_to_cli_format" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                return args_str.split()
        
        def _convert_repl_scope_to_cli_format(self, cli_args: list) -> list:
            import json
            converted_args = []
            i = 0
            while i < len(cli_args):
                arg = cli_args[i]
                if arg == '--scope' and i + 1 < len(cli_args):
                    scope_value = cli_args[i + 1]
                    if scope_value.startswith(('file:', 'files:')):
                        prefix = 'file:' if scope_value.startswith('file:') else 'files:'
                        paths = scope_value[len(prefix):].split(',')
                        paths = [p.strip() for p in paths if p.strip()]
                        json_scope = json.dumps({"type": "files", "value": paths})
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:129): Function "_run_with_streaming" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                raise RecoverableError('cursor-agent timed out')
        
        def _run_with_streaming(self, cmd: List[str], timeout: int) -> subprocess.CompletedProcess:
            """Run command with real-time streaming output."""
            import time
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',
                errors='replace',  # Replace invalid characters instead of crashing
                bufsize=1  # Line buffered
            )
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:191): Function "_print_cleaned_stream_line" has nesting depth of 9 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                raise e
        
        def _print_cleaned_stream_line(self, line: str):
            """Parse JSON stream line and print only meaningful content."""
            line = line.strip()
            if not line:
                return
            
            try:
                data = json.loads(line)
                msg_type = data.get('type', '')
                
                # Skip system init and thinking deltas
                if msg_type in ('system', 'user'):
                    return
        # ... (truncated)
    ```

#### <span id="stop-writing-useless-comments-violations">Stop Writing Useless Comments: 36 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:145): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def display_current_state(self, full=False) -> REPLStateDisplay:
            """Single source of truth for displaying current bot state.
            
            Returns REPLStateDisplay with formatted status output showing:
            - Bot name and paths
            - Current position header
            - Scope filter (if set)
            - Progress in workflow
            - Hierarchical behavior/action/operation tree
            """
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:260): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def get_context_header_for_ai(self) -> str:
            """Get status display as a string for AI context headers.
            
            This is a convenience method that extracts just the output string
            from display_current_state().
            """
            state_display = self.display_current_state()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:269): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _convert_domain_result_to_repl_response(self, result: Dict[str, Any], command: str) -> REPLCommandResponse:
            """Convert a domain method result to a REPL response.
            
            Args:
                result: Dict returned from domain method
                command: The command that was executed
            
            Returns:
                REPLCommandResponse with appropriate formatting
            """
            status = result.get('status', 'success')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:400): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_help_command(self, args: str = "") -> REPLCommandResponse:
            """Handle help command using bot.help"""
            if not args:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:430): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_status_command(self) -> REPLCommandResponse:
            """Handle status command using bot.status"""
            state_display = self.display_current_state(full=True)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:439): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_current_command(self) -> REPLCommandResponse:
            """Re-execute current operation based on progress state"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:468): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_next_command(self) -> REPLCommandResponse:
            """Handle next/advance navigation"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:504): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_back_command(self) -> REPLCommandResponse:
            """Handle back/previous navigation"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:550): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
            """Handle instructions command"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:604): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_submit_command(self, args: str = "") -> REPLCommandResponse:
            """Handle submit command"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:625): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_confirm_command(self) -> REPLCommandResponse:
            """Handle confirm command"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:680): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_path_command(self, args: str = "") -> REPLCommandResponse:
            """Handle path/workspace command"""
            if not args:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:699): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
            """Handle scope command"""
            if not args:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:765): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _validate_headless_ready(self, args: str) -> tuple[bool, REPLCommandResponse | None, any]:
            """Validate that headless mode is ready to execute.
            
            Returns:
                Tuple of (is_valid, error_response, config)
                - If is_valid is False, error_response contains the error to return
                - If is_valid is True, config contains the loaded configuration
            """
            from agile_bot.bots.base_bot.src.repl_cli.headless.headless_config import HeadlessConfig
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:806): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _parse_headless_args(self, args: str) -> tuple[str | None, str]:
            """Parse headless command args into target and message.
            
            Args:
                args: Raw argument string (e.g., 'test.build "message" --scope "X"')
            
            Returns:
                Tuple of (target, message) where:
                - target is the CLI target (e.g., 'test.build') or None
                - message is the rest (message + CLI args)
            """
            import shlex
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:840): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _execute_operation_locally(self, target: str, cli_args: str = "") -> str:
            """Execute a CLI operation locally and return its output.
            
            Args:
                target: CLI target (e.g., 'tests.build', 'tests.build.instructions', 'tests.build.submit')
                cli_args: CLI arguments like '--scope "X"'
            
            Returns:
                Output from the operation (instructions, submit result, confirm result, etc.)
            """
            # Parse target
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:948): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _format_headless_result(self, execution_result) -> REPLCommandResponse:
            """Format headless execution result as a REPL response.
            
            Args:
                execution_result: Result from HeadlessSession.invokes()
            
            Returns:
                REPLCommandResponse with formatted output
            """
            output_lines = [
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:975): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_headless_command(self, args: str = "") -> REPLCommandResponse:
            """Handle headless command - execute instruction in headless mode"""
            from agile_bot.bots.base_bot.src.repl_cli.headless.headless_session import HeadlessSession
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1020): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_behavior_command(self, behavior_name: str) -> REPLCommandResponse:
            """Handle behavior navigation"""
            behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1049): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def navigate_to_behavior_action(self, behavior_name: str, action_name: str):
            """Navigate to a specific behavior and action
            
            Raises:
                ValueError: If behavior or action not found
            """
            # Navigate to behavior
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1070): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _wrap_navigation_with_instructions(self) -> REPLCommandResponse:
            """After navigation, auto-execute instructions for new position"""
            return self._handle_instructions_command()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1074): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _wrap_with_context_header(self, content: str, response_msg: str) -> REPLCommandResponse:
            """Wrap content with instructions header and CLI status section"""
            formatter = self.formatter
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1115): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _mark_behavior_complete(self, behavior_name: str) -> None:
            """Mark a behavior as complete in the state file"""
            state_file = self.workspace_directory / 'behavior_action_state.json'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1130): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
            """Handle dot notation commands (behavior.action.operation)"""
            # Parse dot notation: behavior.action.operation or action.operation or .operation
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:210): Useless comment: "# Get scope display" - delete it or improve the code instead

    ```python
            lines.append(formatter.subsection_separator())
            
            # Get scope display
            scope_display = self.cli_bot.get_scope_display()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:754): Useless comment: "# Get the scope display lines" - delete it or improve the code instead

    ```python
            result = self.cli_bot.set_scope(scope)
            
            # Get the scope display lines
            output = self.cli_bot.get_scope_display()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:987): Useless comment: "# Execute in headless mode" - delete it or improve the code instead

    ```python
            target, message = self._parse_headless_args(args)
            
            # Execute in headless mode
            try:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1001): Useless comment: "# Execute in headless mode" - delete it or improve the code instead

    ```python
                    final_message = message
                
                # Execute in headless mode
                execution_result = session.invokes(message=final_message, context_file=None)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1056): Useless comment: "# Get the behavior" - delete it or improve the code instead

    ```python
            # Navigate to behavior
            self.cli_bot.behaviors.domain_behaviors.navigate_to(behavior_name)
            # Get the behavior
            behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:31): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class CursorHeadlessAPI:
        """Executes instructions via cursor-agent CLI command.
        
        Uses --print flag for non-interactive/headless execution.
        On Windows, runs cursor-agent through WSL Ubuntu.
        """
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:54): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @property
        def chat_id(self) -> Optional[str]:
            """Return the cursor-agent chatId for session resumption."""
            return self._chat_id
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:58): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def starts_session(self, instructions: str) -> APIResponse:
            """Start a headless session by running cursor-agent with the instructions."""
            import uuid
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:109): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def resumes_session(self, prompt: str) -> APIResponse:
            """Resume an existing session with a new prompt.
            
            Requires a previous session to have been started with starts_session().
            """
            if not self._chat_id:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:130): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _run_with_streaming(self, cmd: List[str], timeout: int) -> subprocess.CompletedProcess:
            """Run command with real-time streaming output."""
            import time
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:192): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _print_cleaned_stream_line(self, line: str):
            """Parse JSON stream line and print only meaningful content."""
            line = line.strip()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:268): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _run_cursor_agent(self, prompt: str, timeout: int, resume_chat_id: Optional[str] = None) -> subprocess.CompletedProcess:
            """Run cursor-agent CLI command.
            
            On Windows, runs through WSL Ubuntu.
            Uses --print --output-format json for headless execution.
            
            Args:
                prompt: The prompt/message to send
                timeout: Execution timeout in seconds
                resume_chat_id: Optional chatId to resume an existing session
            """
            if self._is_windows:
    ```

#### <span id="use-domain-language-violations">Use Domain Language: 108 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:17): Class "REPLSession" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:18): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:82): Function "set_action_phase" uses parameter name "phase" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:96): Function "stage_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:120): Function "detect_tty" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:127): Function "get_progress_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:144): Function "display_current_state" uses parameter name "full" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:259): Function "get_context_header_for_ai" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:268): Function "_convert_domain_result_to_repl_response" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:268): Function "_convert_domain_result_to_repl_response" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:326): Function "read_and_execute_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:326): Function "read_and_execute_command" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:339): Function "_handle_simple_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:339): Function "_handle_simple_command" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:399): Function "_handle_help_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:399): Function "_handle_help_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:429): Function "_handle_status_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:438): Function "_handle_current_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:467): Function "_handle_next_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:503): Function "_handle_back_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:549): Function "_handle_instructions_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:549): Function "_handle_instructions_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:603): Function "_handle_submit_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:603): Function "_handle_submit_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:624): Function "_handle_confirm_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:679): Function "_handle_path_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:698): Function "_handle_scope_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:698): Function "_handle_scope_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:764): Function "_validate_headless_ready" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:805): Function "_parse_headless_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:805): Function "_parse_headless_args" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:839): Function "_execute_operation_locally" uses parameter name "target" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:839): Function "_execute_operation_locally" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:900): Function "_prepare_headless_message" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:900): Function "_prepare_headless_message" uses parameter name "target" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:900): Function "_prepare_headless_message" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:947): Function "_format_headless_result" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:947): Function "_format_headless_result" uses parameter name "execution_result" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:974): Function "_handle_headless_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:974): Function "_handle_headless_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1069): Function "_wrap_navigation_with_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1073): Function "_wrap_with_context_header" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1073): Function "_wrap_with_context_header" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1073): Function "_wrap_with_context_header" uses parameter name "response_msg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1129): Function "_handle_dot_notation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1129): Function "_handle_dot_notation" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1257): Function "_handle_action_shortcut" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1318): Function "_tokenize_cli_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1318): Function "_tokenize_cli_args" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1325): Function "_convert_repl_scope_to_cli_format" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1325): Function "_convert_repl_scope_to_cli_format" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1362): Function "_execute_action_with_args" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1362): Function "_execute_action_with_args" uses parameter name "operation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1436): Function "display_confirm_prompt" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1461): Function "parse_command_parameters" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1475): Function "parse_scope_from_string" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1475): Function "parse_scope_from_string" uses parameter name "scope_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1484): Function "get_stored_scope" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1494): Function "_get_scope_display_lines" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1518): Function "_find_scope_matches" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1518): Function "_find_scope_matches" uses parameter name "scope_values" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1531): Function "_search_for_scope_match" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1531): Function "_search_for_scope_match" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1542): Function "_search_sub_epics" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1553): Function "_search_stories" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1553): Function "_search_stories" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1565): Function "_matches_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1565): Function "_matches_name" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1565): Function "_matches_name" uses parameter name "pattern" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1568): Function "_format_node_with_children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1568): Function "_format_node_with_children" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1568): Function "_format_node_with_children" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1568): Function "_format_node_with_children" uses parameter name "indent" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:19): Class "APIResponse" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:30): Class "CursorHeadlessAPI" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:37): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:37): Function "__init__" uses parameter name "api_key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:37): Function "__init__" uses parameter name "model" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:37): Function "__init__" uses parameter name "timeout" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:37): Function "__init__" uses parameter name "stream" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:49): Function "session_id" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:53): Function "chat_id" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:57): Function "starts_session" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:57): Function "starts_session" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:108): Function "resumes_session" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:108): Function "resumes_session" uses parameter name "prompt" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:129): Function "_run_with_streaming" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:129): Function "_run_with_streaming" uses parameter name "cmd" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:129): Function "_run_with_streaming" uses parameter name "timeout" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:191): Function "_print_cleaned_stream_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:191): Function "_print_cleaned_stream_line" uses parameter name "line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:267): Function "_run_cursor_agent" uses parameter name "prompt" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:267): Function "_run_cursor_agent" uses parameter name "timeout" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:267): Function "_run_cursor_agent" uses parameter name "resume_chat_id" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:283): Function "_run_via_wsl" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:283): Function "_run_via_wsl" uses parameter name "prompt" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:283): Function "_run_via_wsl" uses parameter name "timeout" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:283): Function "_run_via_wsl" uses parameter name "resume_chat_id" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:356): Function "_run_directly" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:356): Function "_run_directly" uses parameter name "prompt" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:356): Function "_run_directly" uses parameter name "timeout" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:356): Function "_run_directly" uses parameter name "resume_chat_id" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:391): Function "sends_instruction" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:391): Function "sends_instruction" uses parameter name "instruction" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:408): Function "polls_session_status" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:424): Function "terminates_session" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:428): Function "_parse_cursor_output" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src/repl_cli/headless/cursor_api.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:428): Function "_parse_cursor_output" uses parameter name "output" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

### Cross-File Violations (Pass 2)

These violations were detected by analyzing all files together to find patterns that span multiple files.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 549 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-194)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-151)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-86)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-87)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-88)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-89)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-90)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-91)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-92)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 89-93)):
    ```python
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file scope)')
    lines.append('scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-143)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-144)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-145)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-146)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-152)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-154)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-155)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-156)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-157)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-195)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 154-158)):
    ```python
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-86)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-87)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-88)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-89)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-90)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-91)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-92)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 89-93)):
    ```python
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file scope)')
    lines.append('scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-143)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-144)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-145)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-146)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-153)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-154)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-155)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-156)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-157)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-196)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 154-158)):
    ```python
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-86)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-87)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-88)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-89)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-90)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-91)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-92)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 89-93)):
    ```python
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file scope)')
    lines.append('scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-143)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-144)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-145)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-146)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-147)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-150)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-151)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-152)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-153)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-154)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-155)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-156)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-157)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 154-158)):
    ```python
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-197)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 155-159)):
    ```python
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-86)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-87)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-88)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-89)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-90)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-91)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-92)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 89-93)):
    ```python
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file scope)')
    lines.append('scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-143)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-144)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-145)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-146)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-147)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-150)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-151)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-152)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-153)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-154)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-155)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-156)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-157)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 154-158)):
    ```python
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-198)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 155-159)):
    ```python
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-86)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-87)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-88)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-89)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-90)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-91)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-92)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 89-93)):
    ```python
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file scope)')
    lines.append('scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-143)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-144)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-145)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-146)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-147)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-150)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-151)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-152)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-153)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-154)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-155)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-156)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-157)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 154-158)):
    ```python
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-199)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 155-159)):
    ```python
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-86)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-87)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-88)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-89)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-90)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-91)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-92)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 89-93)):
    ```python
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file scope)')
    lines.append('scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-143)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-144)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-145)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-146)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-147)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-154)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-155)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-156)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-157)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 154-158)):
    ```python
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:196): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 196-202)):
    ```python
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 155-159)):
    ```python
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-86)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-87)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-88)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-89)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-90)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-91)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-92)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 89-93)):
    ```python
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file scope)')
    lines.append('scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-143)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-144)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-145)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-146)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-151)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-154)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-155)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-156)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-157)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-234)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 154-158)):
    ```python
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-87)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-88)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-89)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-90)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-91)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-92)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-93)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-144)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-145)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-146)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-152)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-154)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-155)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-156)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-157)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-195)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-158)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-87)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-88)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-89)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-90)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-91)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-92)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-93)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-144)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-145)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-146)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-147)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-150)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-151)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-152)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-153)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-154)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-155)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-156)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-157)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-158)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-196)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 154-159)):
    ```python
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-87)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-88)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-89)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-90)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-91)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-92)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-93)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-144)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-145)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-146)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-147)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-150)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-151)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-152)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-153)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-154)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-155)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-156)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-157)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-158)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-197)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 154-159)):
    ```python
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-87)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-88)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-89)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-90)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-91)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-92)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-93)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-144)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-145)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-146)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-147)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-150)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-151)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-152)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-153)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-154)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-155)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-156)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-157)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-158)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-198)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 154-159)):
    ```python
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-87)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-88)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-89)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-90)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-91)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-92)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-93)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-144)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-145)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-146)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-147)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-150)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-151)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-152)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-153)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-154)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-155)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-156)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-157)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-158)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-199)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 154-159)):
    ```python
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-87)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-88)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-89)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-90)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-91)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-92)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-93)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-144)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-145)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-146)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-147)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-150)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-151)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-152)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-153)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-154)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-155)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-156)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-157)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-158)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:195): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 195-202)):
    ```python
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 154-159)):
    ```python
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:226): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 226-233)):
    ```python
    lines.append(formatter.subsection_separator())
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-154)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-87)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-88)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-89)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-90)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-91)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-92)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-93)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-144)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-145)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-146)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-151)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-154)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-155)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-156)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-157)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:229): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 229-234)):
    ```python
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-158)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-87)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-88)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-89)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-90)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-91)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-92)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 88-93)):
    ```python
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (replaces any file sco...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-144)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-145)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-146)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-147)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-152)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-155)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-156)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-157)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-158)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 230-237)):
    ```python
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    lines.append(self.cli_bot.status.hierarchical_status)
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 154-159)):
    ```python
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-195)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-152)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-196)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-88)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-196)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-89)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-196)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-90)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-196)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-91)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-196)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-92)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-196)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-93)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-196)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-145)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-196)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-146)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-196)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-153)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-196)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-155)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-196)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-156)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-196)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-157)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-196)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-158)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-88)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-89)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-90)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-91)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-92)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-93)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-145)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-146)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-147)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-150)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-151)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-152)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-153)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-154)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-155)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-156)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-157)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-158)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-197)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-159)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-88)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-89)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-90)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-91)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-92)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-93)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-145)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-146)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-147)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-150)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-151)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-152)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-153)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-154)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-155)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-156)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-157)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-158)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-198)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-159)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-88)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-89)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-90)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-91)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-92)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-93)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-145)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-146)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-147)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-150)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-151)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-152)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-153)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-154)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-155)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-156)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-157)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-158)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-199)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-159)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-88)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-89)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-90)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-91)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-92)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 87-93)):
    ```python
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                            # Clear scope, work on entire project')
    lines.append('scope "Story Name"                   # Filter by story (repl...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-145)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-146)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-147)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-150)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-151)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-152)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-153)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-154)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-155)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-156)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-157)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-158)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:194): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 194-202)):
    ```python
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_separator())
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 153-159)):
    ```python
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:226): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 226-234)):
    ```python
    lines.append(formatter.subsection_separator())
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path}.{self.stage_name}')
    lines.append('```')
    lines.append('')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-155)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-196)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-153)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-197)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-89)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-197)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-90)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-197)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-91)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-197)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-92)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-197)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-93)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-197)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-146)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-197)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-154)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-197)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-156)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-197)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-157)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-197)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-158)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append(''...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-89)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-90)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-91)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-92)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-93)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-146)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-147)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-150)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-151)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-152)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-153)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-154)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-155)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-156)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-157)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-158)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append(''...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-198)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-159)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-89)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-90)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-91)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-92)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-93)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-146)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-147)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-150)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-151)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-152)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-153)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-154)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-155)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-156)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-157)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-158)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append(''...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-199)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-159)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-89)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-90)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-91)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-92)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 86-93)):
    ```python
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.append('```powershell')
    lines.append('scope all                         ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-146)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-147)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-150)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-151)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-152)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-153)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-154)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-155)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-156)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-157)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-158)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append(''...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:193): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 193-202)):
    ```python
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append('```')
    lines.append(formatter.subsection_se...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 152-159)):
    ```python
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append('')
    lines.append(self.formatter.section_separator())
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-197)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-90)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-197)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-91)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-197)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-92)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-197)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-93)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-197)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-154)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-197)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-156)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-197)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-157)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-197)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-158)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-90)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-91)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-92)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-93)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-147)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-150)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-151)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-152)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-153)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-154)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-155)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-156)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-157)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-158)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-198)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-159)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append(''...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-90)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-91)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-92)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-93)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-147)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-150)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-151)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-152)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-153)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-154)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-155)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-156)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-157)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-158)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-199)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-159)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append(''...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-90)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-91)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-92)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 85-93)):
    ```python
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a new scope replaces the previous):')
    lines.app...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-147)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-150)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-151)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-152)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-153)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-154)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-155)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-156)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-157)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-158)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 192-202)):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative path')
    lines.append...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 151-159)):
    ```python
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    lines.append('```')
    lines.append(''...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-198)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-91)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-198)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-92)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-198)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-93)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-198)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-155)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-198)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-157)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 189-198)):
    ```python
    lines.append(f'{formatter.workspace_icon()} **Workspace:** {workspace_name}')
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-158)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-199)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-91)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-199)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-92)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-199)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-93)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-199)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-150)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-199)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-151)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-199)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-152)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-199)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-153)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-199)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-154)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-199)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-155)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-199)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-156)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-199)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-157)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-199)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-158)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:190): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 190-199)):
    ```python
    lines.append(f'**Path:**')
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot        ...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-159)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-202)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 82-91)):
    ```python
    lines.append('')
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To cha...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-202)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 83-92)):
    ```python
    lines.append('')
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick O...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-202)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (cli_scope.py:to_formatted_display (lines 84-93)):
    ```python
    lines.append('- Work ONLY on this scope:')
    lines.append('- DO NOT work on all files or the entire story graph')
    lines.append('- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system')
    lines.append('')
    lines.append('To change scope (pick ONE - setting a ne...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-202)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 139-150)):
    ```python
    lines.append('')
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operatio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-202)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 140-151)):
    ```python
    lines.append('Run:')
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-202)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 141-152)):
    ```python
    lines.append('```')
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate a...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-202)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 142-153)):
    ```python
    lines.append("echo '[behavior]' | python repl_main.py           - navigate to behavior")
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-202)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 143-154)):
    ```python
    lines.append("echo '[behavior][.action]' | python repl_main.py           - navigate to behavior/action")
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-202)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 144-155)):
    ```python
    lines.append("echo '[behavior.][action.]operation' | python repl_main.py  - navigate and perform operation")
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lin...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-202)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 145-156)):
    ```python
    lines.append('python repl_main.py headless [behavior.action]              - execute in headless mode (unattended)')
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-202)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 146-157)):
    ```python
    lines.append('```')
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-202)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 147-158)):
    ```python
    lines.append(self.formatter.subsection_separator())
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python r...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:display_current_state (lines 191-202)):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specific project')
    lines.append('path ../another_bot               # Change to relative...
    ```

  Location 2 (repl_status.py:hierarchical_status (lines 150-159)):
    ```python
    lines.append('## 💻 **Commands:**')
    lines.append('**status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit**')
    lines.append('')
    lines.append('```')
    lines.append('// Run')
    lines.append("echo '[command]' | python repl_main.py")
    lines.append('// to invoke commands')
    ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:911): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_prepare_headless_message (lines 911-917)):
    ```python
    if parsed[i].startswith('--'):
        cli_args_parts = parsed[i:]
        break
    else:
        message_parts.append(parsed[i])
        i += 1
    ```

  Location 2 (repl_main.py:_execute_headless_with_context (lines 168-175)):
    ```python
    if parsed[i].startswith('--'):
        cli_args_parts = parsed[i:]
        break
    else:
        message_parts.append(parsed[i])
        i += 1
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1522): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_find_scope_matches (lines 1522-1527)):
    ```python
    match_lines = self._search_for_scope_match(epics, scope_val)
    if match_lines:
        lines.extend(match_lines)
    else:
        lines.append(f'  - {scope_val} (no match)')
    ```

  Location 2 (action_context.py:_find_scope_matches_in_graph (lines 357-362)):
    ```python
    match_lines = self._search_for_scope_match(epics, scope_val)
    if match_lines:
        lines.extend(match_lines)
    else:
        lines.append(f'  - {scope_val} (no match)')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1532): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_search_for_scope_match (lines 1532-1538)):
    ```python
    if self._matches_name(epic.get('name', ''), scope_val):
        return self._format_node_with_children(epic, 'epic', 0)
    match_lines = self._search_sub_epics(epic.get('sub_epics', []), scope_val)
    if match_lines:
        return match_lines
    ```

  Location 2 (action_context.py:_search_for_scope_match (lines 368-374)):
    ```python
    if self._matches_name(epic.get('name', ''), scope_val):
        return self._format_node_with_children(epic, 'epic', 0)
    match_lines = self._search_sub_epics(epic.get('sub_epics', []), scope_val)
    if match_lines:
        return match_lines
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1543): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_search_sub_epics (lines 1543-1549)):
    ```python
    if self._matches_name(sub_epic.get('name', ''), scope_val):
        return self._format_node_with_children(sub_epic, 'sub epic', 0)
    match_lines = self._search_stories(sub_epic, scope_val)
    if match_lines:
        return match_lines
    ```

  Location 2 (action_context.py:_search_sub_epics (lines 380-386)):
    ```python
    if self._matches_name(sub_epic.get('name', ''), scope_val):
        return self._format_node_with_children(sub_epic, 'sub epic', 0)
    match_lines = self._search_stories(sub_epic, scope_val)
    if match_lines:
        return match_lines
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1571): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1571-1585)):
    ```python
    name = node.get('name', 'Unknown')
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
     ...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 419-433)):
    ```python
    emoji = emoji_map.get(node_type, '•')
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1572): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1572-1589)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 420-437)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1572): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1572-1589)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 420-439)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1575): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1575-1591)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 423-439)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1575): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1575-1591)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 420-439)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1571): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1571-1589)):
    ```python
    name = node.get('name', 'Unknown')
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
     ...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 419-437)):
    ```python
    emoji = emoji_map.get(node_type, '•')
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1572): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1572-1591)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 420-437)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1572): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1572-1591)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 423-439)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src/repl_cli/repl_session.py`](vscode://file//mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1572): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1572-1591)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 420-439)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```

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
*... and 65 more instructions*

## Report Location

This report was automatically generated and saved to:
`/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/reports/code-validation-report-2025-12-30_03-12-42.md`

