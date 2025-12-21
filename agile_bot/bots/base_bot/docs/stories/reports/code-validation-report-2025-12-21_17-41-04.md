# Validation Report - Code

**Generated:** 2025-12-21 17:41:54
**Project:** base_bot
**Behavior:** code
**Action:** validate

## Summary

Validated story map and domain model and 228 code file(s) against **32 validation rules**.

## Content Validated

- **Rendered Outputs:**
  - `story-graph.json`
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
  - `src\actions\clarify\recommended_activities.py`
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
  - `src\actions\render\render_instruction_formatter.py`
  - `src\actions\render\render_scope.py`
  - `src\actions\render\render_spec.py`
  - `src\actions\render\synchronizer.py`
  - `src\actions\render\template.py`
  - `src\actions\rules\rule.py`
  - `src\actions\rules\rule_filter.py`
  - `src\actions\rules\rule_loader.py`
  - `src\actions\rules\rules.py`
  - `src\actions\rules\rules_action.py`
  - `src\actions\scoping_parameter.py`
  - `src\actions\strategy\assumptions.py`
  - `src\actions\strategy\json_persistent.py`
  - `src\actions\strategy\recommended_activities.py`
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
  - `src\actions\validate\scanner_status_formatter.py`
  - `src\actions\validate\scanners\useless_comments_scanner.py`
  - `src\actions\validate\story_graph.py`
  - `src\actions\validate\validate_action.py`
  - `src\actions\validate\validation_executor.py`
  - `src\actions\validate\validation_report_builder.py`
  - `src\actions\validate\validation_report_formatter.py`
  - `src\actions\validate\validation_report_writer.py`
  - `src\actions\validate\validation_scanner_status_builder.py`
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
  - `src\bot\trigger_words.py`
  - `src\bot\workspace.py`
  - `src\cli\base_bot_cli.py`
  - `src\cli\behavior_matcher.py`
  - `src\cli\bot_matcher.py`
  - `src\cli\cli_command_router.py`
  - `src\cli\cli_context_builder.py`
  - `src\cli\cli_executor.py`
  - `src\cli\cli_generator.py`
  - `src\cli\cli_help_generator.py`
  - `src\cli\cli_help_renderer.py`
  - `src\cli\cli_parameter_parser.py`
  - `src\cli\cli_parser_generator.py`
  - `src\cli\cli_script_generator.py`
  - `src\cli\cursor_command_generator.py`
  - `src\cli\cursor_help_renderer.py`
  - `src\cli\description_extractor.py`
  - `src\cli\help_context.py`
  - `src\cli\help_renderer.py`
  - `src\cli\parameter_info_builder.py`
  - `src\cli\trigger_domain.py`
  - `src\cli\trigger_router.py`
  - `src\cli\trigger_router_entry.py`
  - `src\cli\unified_help_generator.py`
  - `src\mcp\behavior_tool_generator.py`
  - `src\mcp\bot_tool_generator.py`
  - `src\mcp\mcp_code_generator.py`
  - `src\mcp\mcp_config_generator.py`
  - `src\mcp\mcp_server.py`
  - `src\mcp\mcp_server_generator.py`
  - `src\mcp\mcp_tool_registrar.py`
  - `src\mcp\server_deployer.py`
  - `src\mcp\server_restart.py`
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
  - `src\scanners\resources\block.py`
  - `src\scanners\resources\block_extractor.py`
  - `src\scanners\resources\file.py`
  - `src\scanners\resources\line.py`
  - `src\scanners\resources\scan.py`
  - `src\scanners\resources\scope.py`
  - `src\scanners\resources\violation.py`
  - `src\scanners\scanner.py`
  - `src\scanners\scanner_loader.py`
  - `src\scanners\scanner_orchestrator.py`
  - `src\scanners\scanner_registry.py`
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
  - `src\scanners\verb_noun_scanner.py`
  - `src\scanners\vertical_density_scanner.py`
  - `src\scanners\vertical_slice_scanner.py`
  - `src\scanners\violation.py`
  - `src\story_graph\domain.py`
  - `src\story_graph\nodes.py`
  - `src\utils.py`
  - **Total:** 228 src file(s)

## Scanner Execution Status

### 🟨 Overall Status: NEEDS ATTENTION

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 30 | Scanners ran without errors |
| 🟩 Clean Rules | 9 | No violations found |
| 🟨 Rules with Warnings | 13 | Found 437 warning violation(s) |
| 🟥 Rules with Errors | 5 | Found 729 error violation(s) |
| [i] No Scanner | 2 | Rule has no scanner configured |

**Total Rules:** 32
- **Rules with Scanners:** 30
  - 🟩 **Executed Successfully:** 30
- [i] **Rules without Scanners:** 2

### 🟩 Successfully Executed Scanners

- 🟥 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 690 violation(s) (EXECUTION_SUCCESS) - [View Details](#stop-writing-useless-comments-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟨 **[Simplify Control Flow](#simplify-control-flow)** - 158 violation(s) (EXECUTION_SUCCESS) - [View Details](#simplify-control-flow-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟨 **[Provide Meaningful Context](#provide-meaningful-context)** - 106 violation(s) (EXECUTION_SUCCESS) - [View Details](#provide-meaningful-context-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
- 🟨 **[Maintain Vertical Density](#maintain-vertical-density)** - 59 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-vertical-density-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟨 **[Use Clear Function Parameters](#use-clear-function-parameters)** - 59 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-clear-function-parameters-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
- 🟨 **[Keep Functions Small Focused](#keep-functions-small-focused)** - 54 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-functions-small-focused-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
- 🟨 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 18 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-excessive-guards-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🟥 **[Never Swallow Exceptions](#never-swallow-exceptions)** - 16 violation(s) (EXECUTION_SUCCESS) - [View Details](#never-swallow-exceptions-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
- 🟥 **[Prefer Object Model Over Config](#prefer-object-model-over-config)** - 14 violation(s) (EXECUTION_SUCCESS) - [View Details](#prefer-object-model-over-config-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.prefer_object_model_over_config_scanner.PreferObjectModelOverConfigScanner`
- 🟨 **[Use Natural English](#use-natural-english)** - 14 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-natural-english-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.natural_english_code_scanner.NaturalEnglishCodeScanner`
- 🟨 **[Keep Classes Small With Single Responsibility](#keep-classes-small-with-single-responsibility)** - 13 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-classes-small-with-single-responsibility-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
- 🟨 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 10 violation(s) (EXECUTION_SUCCESS) - [View Details](#refactor-completely-not-partially-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
- 🟥 **[Place Imports At Top](#place-imports-at-top)** - 7 violation(s) (EXECUTION_SUCCESS) - [View Details](#place-imports-at-top-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟨 **[Enforce Encapsulation](#enforce-encapsulation)** - 6 violation(s) (EXECUTION_SUCCESS) - [View Details](#enforce-encapsulation-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.encapsulation_scanner.EncapsulationScanner`
- 🟨 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 5 violation(s) (EXECUTION_SUCCESS) - [View Details](#chain-dependencies-properly-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟨 **[Delegate To Lowest Level](#delegate-to-lowest-level)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#delegate-to-lowest-level-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.delegation_code_scanner.DelegationCodeScanner`
- 🟨 **[Use Domain Language](#use-domain-language)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-domain-language-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
- 🟥 **[Eliminate Duplication](#eliminate-duplication)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#eliminate-duplication-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
- 🟨 **[Hide Business Logic Behind Properties](#hide-business-logic-behind-properties)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#hide-business-logic-behind-properties-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟨 **[Hide Calculation Timing](#hide-calculation-timing)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#hide-calculation-timing-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟨 **[Use Explicit Dependencies](#use-explicit-dependencies)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-explicit-dependencies-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
- 🟩 **[Avoid Unnecessary Parameter Passing](#avoid-unnecessary-parameter-passing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
- 🟩 **[Classify Exceptions By Caller Needs](#classify-exceptions-by-caller-needs)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
- 🟩 **[Favor Code Representation](#favor-code-representation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
- 🟩 **[Group By Domain](#group-by-domain)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
- 🟩 **[Keep Functions Single Responsibility](#keep-functions-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟩 **[Use Consistent Indentation](#use-consistent-indentation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_indentation_scanner.ConsistentIndentationScanner`
- 🟩 **[Use Consistent Naming](#use-consistent-naming)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_naming_scanner.ConsistentNamingScanner`
- 🟩 **[Use Exceptions Properly](#use-exceptions-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_handling_scanner.ExceptionHandlingScanner`
- 🟩 **[Use Resource Oriented Design](#use-resource-oriented-design)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Detect Legacy Unused Code](#detect-legacy-unused-code)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Refactor Tests With Production Code](#refactor-tests-with-production-code)** - No scanner configured

## Validation Rules Checked

### 🟥 Rule: <span id="stop-writing-useless-comments">Stop Writing Useless Comments</span> - 690 ERROR(S) - [View Details](#stop-writing-useless-comments-violations)
**Description:** CRITICAL: DO NOT WRITE COMMENTS. Delete all comments written by the AI chat. Code must be self-explanatory through clear naming and structure. ONLY exception: legal/license requirements. If you think a comment is needed, the code is wrong - fix the code instead.
**Scanner:** `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="never-swallow-exceptions">Never Swallow Exceptions</span> - 16 ERROR(S) - [View Details](#never-swallow-exceptions-violations)
**Description:** CRITICAL: Never swallow exceptions silently. Empty catch blocks hide failures and make debugging impossible. Always log, handle, or rethrow exceptions with context.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="prefer-object-model-over-config">Prefer Object Model Over Config</span> - 14 ERROR(S) - [View Details](#prefer-object-model-over-config-violations)
**Description:** Use existing object model to access information instead of directly accessing configuration files
**Scanner:** `agile_bot.bots.base_bot.src.scanners.prefer_object_model_over_config_scanner.PreferObjectModelOverConfigScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="place-imports-at-top">Place Imports At Top</span> - 7 ERROR(S) - [View Details](#place-imports-at-top-violations)
**Description:** Place all import statements at the top of the file, after module docstrings and comments, but before any executable code. This improves readability and makes dependencies clear.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - 2 ERROR(S) - [View Details](#eliminate-duplication-violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="simplify-control-flow">Simplify Control Flow</span> - 158 WARNING(S) - [View Details](#simplify-control-flow-violations)
**Description:** Keep nesting minimal and control flow straightforward. Use guard clauses to reduce nesting and extract nested blocks into separate functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="provide-meaningful-context">Provide Meaningful Context</span> - 106 WARNING(S) - [View Details](#provide-meaningful-context-violations)
**Description:** Names should provide appropriate context without redundancy. Use longer names for longer scopes and replace magic numbers with named constants.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="use-clear-function-parameters">Use Clear Function Parameters</span> - 59 WARNING(S) - [View Details](#use-clear-function-parameters-violations)
**Description:** CRITICAL: Function signatures must be simple and intention-revealing. Prefer 0-2 parameters. NEVER pass Dict[str, Any] or List[str] for complex data - create typed objects instead. Examples: parameters dict → ParametersObject, files dict → FilesCollection, exclude list → ExcludePatterns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-functions-small-focused">Keep Functions Small Focused</span> - 54 WARNING(S) - [View Details](#keep-functions-small-focused-violations)
**Description:** Functions should be small enough to understand at a glance. Keep functions under 20 lines when possible and extract complex logic into named helper functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="avoid-excessive-guards">Avoid Excessive Guards</span> - 18 WARNING(S) - [View Details](#avoid-excessive-guards-violations)
**Description:** Excessive guard clauses add to cyclomatic complexity and make code harder to read. Centralize error handling in one place rather than scattering defensive checks throughout the code. Let code fail fast with clear errors rather than silently handling missing components.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-classes-small-with-single-responsibility">Keep Classes Small With Single Responsibility</span> - 13 WARNING(S) - [View Details](#keep-classes-small-with-single-responsibility-violations)
**Description:** CRITICAL: Classes should be small (under 200-300 lines) with a single responsibility. Keep classes cohesive (methods/data interdependent), eliminate dead code, and favor many small focused classes over few large ones.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="refactor-completely-not-partially">Refactor Completely Not Partially</span> - 10 WARNING(S) - [View Details](#refactor-completely-not-partially-violations)
**Description:** CRITICAL: When refactoring, replace old code completely - don't try to support both legacy and new patterns. Write new code, delete old code, fix tests. Clean breaks are better than compatibility bridges that create technical debt.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="enforce-encapsulation">Enforce Encapsulation</span> - 6 WARNING(S) - [View Details](#enforce-encapsulation-violations)
**Description:** CRITICAL: Hide implementation details and expose minimal interface. Make fields private by default, expose behavior not data. NEVER pass raw dicts/lists that expose internal structure - use typed objects that encapsulate the data. Follow Law of Demeter (principle of least knowledge).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.encapsulation_scanner.EncapsulationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="chain-dependencies-properly">Chain Dependencies Properly</span> - 5 WARNING(S) - [View Details](#chain-dependencies-properly-violations)
**Description:** CRITICAL: Code must chain dependencies properly with constructor injection. Map dependencies in a chain: highest-level object → collaborator → sub-collaborator. Inject collaborators at construction time so methods can use them without passing them as parameters. Access sub-collaborators through their owning objects.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="use-domain-language">Use Domain Language</span> - 3 WARNING(S) - [View Details](#use-domain-language-violations)
**Description:** CRITICAL: Code must use domain-specific language, not generic terms. NEVER use Dict[str, Any], List[str], or generic 'data'/'config'/'parameters' - use typed domain objects. Objects should expose properties representing what they contain (e.g., recommended_trades), not methods that 'generate' or 'calculate' things.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="hide-business-logic-behind-properties">Hide Business Logic Behind Properties</span> - 2 WARNING(S) - [View Details](#hide-business-logic-behind-properties-violations)
**Description:** CRITICAL: Hide business logic behind properties. Properties hide logic that occurs—it may be computed on-demand, cached, pre-computed, or loaded from storage. The caller shouldn't know or care when the values are calculated / determined.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="hide-calculation-timing">Hide Calculation Timing</span> - 2 WARNING(S) - [View Details](#hide-calculation-timing-violations)
**Description:** CRITICAL: Code must hide calculations. Properties hide logic that occurs—it may be computed on-demand, cached, pre-computed, or loaded from storage. The caller shouldn't know or care when the values are calculated / determined.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="use-explicit-dependencies">Use Explicit Dependencies</span> - 1 WARNING(S) - [View Details](#use-explicit-dependencies-violations)
**Description:** CRITICAL: Make dependencies visible through constructor injection. Pass dependencies through constructors, make all dependencies explicit and visible, and use dependency injection for flexibility.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="avoid-unnecessary-parameter-passing">Avoid Unnecessary Parameter Passing</span> - CLEAN (0 violations)
**Description:** Don't pass parameters to internal methods when the value is already accessible through instance variables. Access instance properties directly instead of passing them around unnecessarily.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="classify-exceptions-by-caller-needs">Classify Exceptions By Caller Needs</span> - CLEAN (0 violations)
**Description:** Design exceptions based on how callers will handle them. Create exception types based on caller's needs, use special case objects for predictable failures, and wrap third-party exceptions at boundaries.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
**Execution Status:** EXECUTION_SUCCESS

*... and 12 more rules*

## Violations Found

**Total Violations:** 1242
- **File-by-File Violations:** 1242
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="avoid-excessive-guards-violations">Avoid Excessive Guards: 18 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:171): Line 171: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:184): Line 184: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:38): Line 38: Variable truthiness check detected (if not data:). Assume variable exists - let code fail fast if missing.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:247): Line 247: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:251): Line 251: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:75): Line 75: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\cover_all_paths_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/cover_all_paths_scanner.py:43): Line 43: Variable truthiness check detected (if has_code:). Assume variable exists - let code fail fast if missing.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scanner_orchestrator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_orchestrator.py:75): Line 75: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/violation.py:82): Line 82: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:45): Line 45: Variable truthiness check detected (if has_scope_in_params:). Assume variable exists - let code fail fast if missing.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:142): Line 142: Variable truthiness check detected (if changed:). Assume variable exists - let code fail fast if missing.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:27): Line 27: Variable truthiness check detected (if not is_absolute:). Assume variable exists - let code fail fast if missing.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:52): Line 52: Variable truthiness check detected (if line_number:). Assume variable exists - let code fail fast if missing.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:96): Line 96: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:109): Line 109: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:122): Line 122: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:136): Line 136: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:150): Line 150: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

#### <span id="chain-dependencies-properly-violations">Chain Dependencies Properly: 5 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:13): Method "render_header" in Test class [CursorHelpRenderer](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:13) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\prefer_object_model_over_config_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/prefer_object_model_over_config_scanner.py:36): Method "scan_file" in Test class [PreferObjectModelOverConfigScanner](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/prefer_object_model_over_config_scanner.py:36) takes parameter "rule_obj" that is already injected in __init__. Use self.rule_obj instead.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scanner_orchestrator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_orchestrator.py:35): Method "selects_scanner_helpers_by_rule" in Test class [ScannerOrchestrator](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_orchestrator.py:35) takes parameter "scanner_registry" that is already injected in __init__. Use self.scanner_registry instead.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rule_loader.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rule_loader.py:22): Method "_load_rules_from_glob" in Test class [RuleLoader](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rule_loader.py:22) takes parameter "behavior" that is already injected in __init__. Use self.behavior instead.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:42): Method "_extract_skiprule_from_scope" in Test class [ValidationScope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:42) takes parameter "parameters" that is already injected in __init__. Use self.parameters instead.

#### <span id="delegate-to-lowest-level-violations">Delegate To Lowest Level: 3 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\file_discovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_discovery.py:24): Method "_matches_any_exclude_pattern" in Test class [FileDiscovery](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_discovery.py:24) iterates through "exclude_patterns" instead of delegating to collection class. Delegate to collection class instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resources\scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scope.py:40): Method "_collect_blocks_from_files" in Test class [Scope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scope.py:40) iterates through "files" instead of delegating to collection class. Delegate to collection class instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resources\scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scope.py:46): Method "_create_files_from_paths" in Test class [Scope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scope.py:46) iterates through "_file_paths" instead of delegating to collection class. Delegate to collection class instead.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 2 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\rules\rules_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules_action.py:44): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_add_rules_context:44-53):
    ```python
    instructions.add('')
    instructions.add(rules_digest)
    instructions.add('')
    instructions.add('CRITICAL: The rules digest above contains everything you need to get started.')
    instructions.add('')
    instruct...
    ```

  Location (_add_rules_context:54-59):
    ```python
    instructions.add('   - The full rule has detailed examples and detection patterns')
    instructions.add('4. Cite rule names when making decisions')
    instructions.add('')
    instructions.add('The digest gives...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:150): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_get_status_path:150-154):
    ```python
    docs_path = self.bot_paths.documentation_path
    docs_dir = self.workspace_directory / docs_path / 'reports'
    docs_dir.mkdir(parents=True, exist_ok=True)
    status_file = docs_dir / f'{self.behavior_name}-va...
    ```

  Location (get_report_path:241-245):
    ```python
    docs_path = self.bot_paths.documentation_path
    docs_dir = self.workspace_directory / docs_path / 'reports'
    docs_dir.mkdir(parents=True, exist_ok=True)
    report_file = docs_dir / f'{self.behavior_name}-va...
    ```

#### <span id="enforce-encapsulation-violations">Enforce Encapsulation: 6 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:70): Method "update_workspace_directory" in Test class [BotPaths](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:70) has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:105): Method "_output_result" in Test class [CliExecutor](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:105) has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\ac_consolidation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/ac_consolidation_scanner.py:32): Method "_check_duplicate_ac" in Test class [ACConsolidationScanner](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/ac_consolidation_scanner.py:32) has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:187): Method "_find_src_locations" in Test class [RealImplementationsScanner](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:187) has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scanner_loader.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_loader.py:30): Method "_load_scanner_class" in Test class [ScannerLoader](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_loader.py:30) has Law of Demeter violation (method chain depth 4) - encapsulate access to related objects
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scanner_registry.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_registry.py:72): Method "loads_scanner_class_with_error" in Test class [ScannerRegistry](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_registry.py:72) has Law of Demeter violation (method chain depth 4) - encapsulate access to related objects

#### <span id="hide-business-logic-behind-properties-violations">Hide Business Logic Behind Properties: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:241): Function "calculate_lcom" exposes calculation timing. Use property with "get_" or no prefix instead (e.g., "total_value" not "calculate_total_value").
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:113): Function "calculate_complexity" exposes calculation timing. Use property with "get_" or no prefix instead (e.g., "total_value" not "calculate_total_value").

#### <span id="hide-calculation-timing-violations">Hide Calculation Timing: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:241): Function "calculate_lcom" exposes calculation timing. Use property with "get_" or no prefix instead (e.g., "total_value" not "calculate_total_value").
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:113): Function "calculate_complexity" exposes calculation timing. Use property with "get_" or no prefix instead (e.g., "total_value" not "calculate_total_value").

#### <span id="keep-classes-small-with-single-responsibility-violations">Keep Classes Small With Single Responsibility: 13 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:13): Class "BadCommentsScanner" is 301 lines - should be under 300 lines (extract related methods into separate classes)
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:12): Class "ClassBasedOrganizationScanner" is 610 lines - should be under 300 lines (extract related methods into separate classes)
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:11): Class "CodeScanner" is 471 lines - should be under 300 lines (extract related methods into separate classes)
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:7): Class "ComplexityMetrics" is 438 lines - should be under 300 lines (extract related methods into separate classes)
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:40): Class "DuplicationScanner" is 2036 lines - should be under 300 lines (extract related methods into separate classes)
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:14): Class "ExcessiveGuardsScanner" is 327 lines - should be under 300 lines (extract related methods into separate classes)
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:11): Class "GivenWhenThenHelpersScanner" is 392 lines - should be under 300 lines (extract related methods into separate classes)
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\import_placement_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/import_placement_scanner.py:14): Class "ImportPlacementScanner" is 372 lines - should be under 300 lines (extract related methods into separate classes)
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:14): Class "IntentionRevealingNamesScanner" is 396 lines - should be under 300 lines (extract related methods into separate classes)
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:14): Class "RealImplementationsScanner" is 576 lines - should be under 300 lines (extract related methods into separate classes)
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner.py:16): Class "Scanner" is 314 lines - should be under 300 lines (extract related methods into separate classes)
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:14): Class "SpecificationMatchScanner" is 539 lines - should be under 300 lines (extract related methods into separate classes)
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:27): Class "VerbNounScanner" is 453 lines - should be under 300 lines (extract related methods into separate classes)

#### <span id="keep-functions-small-focused-violations">Keep Functions Small Focused: 54 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:108): Function "instructions" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
        @property
        def instructions(self) -> Instructions:
            base_instructions = self._base_config.get('instructions', [])
            inst = Instructions(base_instructions if isinstance(base_instructions, list) else [], bot_paths=self.behavior.bot_paths)
            
            # Add context instructions (clarification, strategy, context files) at the beginning
            context_instructions = []
            # Use shared dict to capture injected data
            injected_data = {}
            try:
                context_instructions.extend(self._inject_clarification_data(injected_data))
                context_instructions.extend(self._inject_strategy_data(injected_data))
            except FileNotFoundError as e:
                logger.debug(f'Clarification or strategy data files not found: {e}')
                raise
            context_instructions.extend(self._inject_context_files(injected_data))
            
            # Add injected data (clarification, strategy) to instructions
            for key, value in injected_data.items():
                inst._data[key] = value
            
            # Add context instructions to the beginning
            for line in reversed(context_instructions):
                inst._data['base_instructions'].insert(0, line)
            
            # Add workflow status breadcrumbs to display_content (for deterministic display)
            breadcrumbs = self._inject_status_update_breadcrumbs({})
            for line in breadcrumbs:
                inst.add_display(line)
            
            return inst
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:15): Function "__init__" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    class Actions:
    
        def __init__(self, behavior: 'Behavior'):
            self.behavior = behavior
            actions_list = behavior.actions_workflow
            
            # Separate workflow actions (have order) from non-workflow actions (no order)
            workflow_actions = [a for a in actions_list if a.get('order') is not None]
            non_workflow_actions = [a for a in actions_list if a.get('order') is None]
            
            # Sort workflow actions by order
            workflow_actions = sorted(workflow_actions, key=lambda x: x.get('order', 0))
            
            self._factory = ActionFactory(behavior)
            self._state_manager = ActionStateManager(behavior)
            
            # _actions contains only workflow actions (for sequencing)
            self._actions: List[Action] = []
            for action_dict in workflow_actions:
                action_name = action_dict.get('name', '')
                if action_name:
                    action_instance = self._factory.create_action_instance(action_name=action_name, action_config=action_dict)
                    self._actions.append(action_instance)
            
            # _non_workflow_actions contains actions that can be invoked but don't participate in workflow
            self._non_workflow_actions: List[Action] = []
            for action_dict in non_workflow_actions:
                action_name = action_dict.get('name', '')
                if action_name:
                    action_instance = self._factory.create_action_instance(action_name=action_name, action_config=action_dict)
                    self._non_workflow_actions.append(action_instance)
            
            self._current_index: Optional[int] = None
            self.load_state()
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:110): Function "navigate_to" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return self._state_manager.filter_completed_actions_after_target(completed_actions, target_index, self._actions)
    
        def navigate_to(self, action_name: str, out_of_order: bool=False):
            action = self.find_by_name(action_name)
            if action is None:
                raise ValueError(f"Action '{action_name}' not found")
            
            # Check if this is a non-workflow action (no order)
            is_non_workflow = action in self._non_workflow_actions
            if is_non_workflow:
                # Non-workflow actions don't affect workflow state
                return
            
            target_index = None
            for i, a in enumerate(self._actions):
                if a.action_name == action_name:
                    target_index = i
                    self._current_index = i
                    break
            if not out_of_order or not self.behavior.bot_paths:
                self.save_state()
                return
            state_file = self._state_manager.get_state_file_path()
            state_data = json.loads(state_file.read_text(encoding='utf-8'))
            completed_actions = state_data.get('completed_actions', [])
            if completed_actions:
                state_data['completed_actions'] = self._filter_completed_actions_after_target(completed_actions, target_index)
                state_file.write_text(json.dumps(state_data, indent=2), encoding='utf-8')
            self.save_state()
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:166): Function "help_cursor_commands" is 28 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
                self._handle_error(e)
    
        def help_cursor_commands(self):
            """Route help to the help action."""
            try:
                # Create help action directly (doesn't need a behavior workflow)
                from agile_bot.bots.base_bot.src.actions.help_action import HelpAction
                from agile_bot.bots.base_bot.src.utils import read_json_file
                from agile_bot.bots.base_bot.src.bot.workspace import get_base_actions_directory
                
                # Load help action config from base_actions
                base_actions_dir = get_base_actions_directory()
                help_config_path = base_actions_dir / 'help' / 'action_config.json'
                help_config = read_json_file(help_config_path)
                
                # Create a minimal behavior wrapper for the help action
                # Help action needs access to bot_name and bot_paths
                class HelpBehaviorWrapper:
                    def __init__(self, bot, bot_name, bot_paths):
                        self.bot = bot
                        self.bot_name = bot_name
                        self.name = 'help'
                        self.bot_paths = bot_paths
                        self.actions = None  # Help action doesn't participate in workflow
                
                behavior_wrapper = HelpBehaviorWrapper(self.bot, self.bot_name, self.bot.bot_paths)
                help_action = HelpAction(behavior_wrapper, help_config, 'help')
                
                # Execute the help action with empty context
                result = help_action.execute()
                
                # Output the result
                self.executor._output_result(result)
                return result
            except Exception as e:
                self._handle_error(e)
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:36): Function "generate_parsers_for_bot" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            self._generated_lines: List[str] = []
        
        def generate_parsers_for_bot(self, bot) -> str:
            """Generate parser code for all actions in a bot."""
            self._generated_lines = []
            self._add_header()
            self._add_imports()
            
            # Collect all unique context classes
            context_classes_seen = set()
            action_mappings = []
            
            for behavior in bot.behaviors:
                for action in behavior.actions:
                    context_class = action.context_class
                    action_name = action.action_name
                    
                    # Generate parser for this context class if not seen
                    if context_class not in context_classes_seen:
                        context_classes_seen.add(context_class)
                        self._generate_parser_function(context_class)
                    
                    # Record mapping
                    action_mappings.append((behavior.name, action_name, context_class.__name__))
            
            self._add_blank_line()
            self._generate_context_builder_functions()
            self._add_blank_line()
            self._generate_action_parser_mapping(action_mappings)
            
            return '\n'.join(self._generated_lines)
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\background_common_setup_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/background_common_setup_scanner.py:16): Function "scan_story_node" has high cognitive complexity (17) - should be under 15. Reduce nesting and extract complex logic.

    ```python
        """
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            if isinstance(node, Story):
                story_data = node.data
                scenarios = story_data.get('scenarios', [])
                background = story_data.get('background', [])
                
                if background:
                    # Check if background has When/Then (should only have Given/And)
                    violation = self._check_background_has_when_then(background, node, rule_obj)
                    if violation:
                        violations.append(violation)
                    
                    # Check if background is used for scenario-specific setup
                    violation = self._check_background_scenario_specific(background, scenarios, node, rule_obj)
                    if violation:
                        violations.append(violation)
                
                # Check if scenarios have 3+ but no background (might need one)
                if len(scenarios) >= 3 and not background:
                    # Check if scenarios share common setup that should be in background
                    violation = self._check_missing_background(scenarios, node, rule_obj)
                    if violation:
                        violations.append(violation)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:25): Function "scan_file" is 33 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return []  # Test scanning happens in scan_test_file, not scan_story_node
        
        def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
            violations = []
            
            if not file_path.exists():
                return violations
            
            # Check file naming matches sub-epic
            sub_epic_names = self._extract_sub_epic_names(knowledge_graph)
            file_name = file_path.stem  # Without .py extension
            violation = self._check_file_name_matches_sub_epic(file_name, sub_epic_names, file_path, rule_obj, knowledge_graph)
            if violation:
                violations.append(violation)
            
            parsed = self._read_and_parse_file(file_path)
            if not parsed:
                return violations
            
            content, lines, tree = parsed
            
            # Extract story names from knowledge graph
            story_names = self._extract_story_names(knowledge_graph)
            
            # Find test classes
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    if node.name.startswith('Test'):
                        # Check if class name matches a story name
                        violation = self._check_class_name_matches_story(node.name, story_names, file_path, rule_obj)
                        if violation:
                            violations.append(violation)
                        
                        # Check test methods in this class
                        for item in node.body:
                            if isinstance(item, ast.FunctionDef):
                                if item.name.startswith('test_'):
                                    # Check method name matches scenario
                                    violation = self._check_method_name_matches_scenario(
                                        item.name, node.name, story_names, knowledge_graph, file_path, rule_obj
                                    )
                                    if violation:
                                        violations.append(violation)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\clear_parameters_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/clear_parameters_scanner.py:37): Function "scan_file" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        }
        
        def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
            violations = []
            
            if not file_path.exists():
                return violations
            
            # Skip test files - they may use different parameter naming conventions
            if self._is_test_file(file_path):
                return violations
            
            # Extract domain terms from knowledge graph
            domain_terms = set()
            if self.knowledge_graph:
                domain_terms = self._extract_domain_terms(self.knowledge_graph)
            
            parsed = self._read_and_parse_file(file_path)
            if not parsed:
                return violations
            
            content, lines, tree = parsed
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    violation = self._check_parameters(node, file_path, rule_obj, domain_terms)
                    if violation:
                        violations.append(violation)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_representation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_representation_scanner.py:24): Function "scan_domain_concept" is 35 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return []
        
        def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            # Check node name for abstract patterns
            node_name_lower = node.name.lower()
            for pattern in self.ABSTRACT_PATTERNS:
                if pattern in node_name_lower:
                    violations.append(
                        Violation(
                            rule=rule_obj,
                            violation_message=f'Domain concept "{node.name}" uses abstract terminology. Domain models should represent code closely - refactor code if needed.',
                            location=node.map_location('name'),
                            line_number=None,
                            severity='info'
                        ).to_dict()
                    )
                    break
            
            # Check responsibilities for abstract collaborators
            for i, responsibility_data in enumerate(node.responsibilities):
                responsibility_name = responsibility_data.get('name', '')
                collaborators = responsibility_data.get('collaborators', [])
                
                for collab in collaborators:
                    collab_lower = collab.strip().lower()
                    for pattern in self.ABSTRACT_PATTERNS:
                        if pattern in collab_lower:
                            violations.append(
                                Violation(
                                    rule=rule_obj,
                                    violation_message=f'Responsibility "{responsibility_name}" uses abstract collaborator "{collab.strip()}". Use concrete domain concepts that exist in code.',
                                    location=node.map_location(f'responsibilities[{i}].collaborators'),
                                    line_number=None,
                                    severity='info'
                                ).to_dict()
                            )
                            break
            
            return violations
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:32): Function "cognitive_complexity" is 28 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        
        @staticmethod
        def cognitive_complexity(func_node: ast.FunctionDef) -> int:
            """Calculate cognitive complexity (nested structures weighted more).
            
            Similar to cyclomatic but penalizes nesting more heavily.
            """
            complexity = 0
            nesting_level = 0
            
            def visit_node(node: ast.AST, level: int):
                nonlocal complexity
                
                # Increment complexity for decision points
                if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                    complexity += 1 + level  # Nesting adds to complexity
                    # Visit children with increased nesting
                    for child in ast.iter_child_nodes(node):
                        visit_node(child, level + 1)
                elif isinstance(node, ast.With):
                    complexity += 1 + level
                    for child in ast.iter_child_nodes(node):
                        visit_node(child, level + 1)
                elif isinstance(node, ast.BoolOp):
                    complexity += len(node.values) - 1 + level
                    for child in ast.iter_child_nodes(node):
                        visit_node(child, level)
                elif isinstance(node, ast.Assert):
                    complexity += 1 + level
                else:
                    # Visit children at same nesting level
                    for child in ast.iter_child_nodes(node):
                        visit_node(child, level)
            
            for stmt in func_node.body:
                visit_node(stmt, 0)
            
            return complexity
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:102): Function "detect_responsibilities_with_examples" is 35 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        
        @staticmethod
        def detect_responsibilities_with_examples(func_node: ast.FunctionDef) -> Dict[str, List[Dict[str, Any]]]:
            """Detect multiple responsibilities with code examples.
            
            Returns dict mapping responsibility type to list of examples:
            {
                'I/O': [{'line': 26, 'code': 'read_json_file(path)'}],
                'Transformation': [{'line': 19, 'code': 'result = process(data)'}],
                ...
            }
            """
            responsibilities: Dict[str, List[Dict[str, Any]]] = {}
            
            def add_example(resp_type: str, node: ast.AST):
                if resp_type not in responsibilities:
                    responsibilities[resp_type] = []
                # Only keep first 2 examples per type to avoid verbose output
                if len(responsibilities[resp_type]) < 2:
                    line = getattr(node, 'lineno', None)
                    try:
                        code = ast.unparse(node) if hasattr(ast, 'unparse') else str(node)
                        # Truncate long code
                        if len(code) > 80:
                            code = code[:77] + '...'
                    except:
                        code = '<code unavailable>'
                    responsibilities[resp_type].append({'line': line, 'code': code})
            
            for node in ast.walk(func_node):
                # I/O operations - must be actual file/network operations, not dict methods
                if isinstance(node, ast.Call):
                    func_name = ComplexityMetrics._get_call_name(node)
                    if func_name and ComplexityMetrics._is_io_operation(func_name, node):
                        add_example('I/O', node)
                
                # Validation (assertions, checks, validations)
                if isinstance(node, ast.Assert):
                    add_example('Validation', node)
                
                # Transformation (assignments with meaningful operations, not simple accessors)
                if isinstance(node, ast.Assign):
                    if ComplexityMetrics._has_transformation(node):
                        add_example('Transformation', node)
                
                # Computation (math operations - but not simple comparisons or string ops)
                if isinstance(node, ast.BinOp):
                    # Only count actual math, not string concatenation or list operations
                    if isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow, ast.FloorDiv)):
                        add_example('Computation', node)
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:241): Function "calculate_lcom" is 26 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        
        @staticmethod
        def calculate_lcom(class_node: ast.ClassDef) -> float:
            """Calculate Lack of Cohesion of Methods (LCOM) metric.
            
            LCOM measures how related methods are. Lower is better (more cohesive).
            Returns value between 0 and 1, where 0 = perfect cohesion.
            
            Improvements over naive LCOM:
            - Excludes simple property getters (just return self._x)
            - Follows delegation chains (self.x.y counts as accessing x)
            - Normalizes attribute names (self._x and self.x are same attribute)
            """
            methods = [node for node in class_node.body if isinstance(node, ast.FunctionDef)]
            
            # Filter out simple property getters - they're data accessors, not real methods
            meaningful_methods = []
            for method in methods:
                if not ComplexityMetrics._is_simple_property_getter(method):
                    meaningful_methods.append(method)
            
            if len(meaningful_methods) < 2:
                return 0.0  # Single method or no methods = perfect cohesion
            
            # Get attributes accessed by each method (with delegation awareness)
            method_attributes = []
            for method in meaningful_methods:
                attrs = ComplexityMetrics._get_accessed_attributes(method, class_node)
                method_attributes.append(attrs)
            
            # Count pairs of methods that don't share attributes
            non_shared_pairs = 0
            total_pairs = 0
            
            for i in range(len(method_attributes)):
                for j in range(i + 1, len(method_attributes)):
                    total_pairs += 1
                    if not (method_attributes[i] & method_attributes[j]):
                        non_shared_pairs += 1
            
            if total_pairs == 0:
                return 0.0
            
            # LCOM = ratio of non-shared pairs to total pairs
            return non_shared_pairs / total_pairs
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:400): Function "detect_class_responsibilities_with_examples" is 23 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        
        @staticmethod
        def detect_class_responsibilities_with_examples(class_node: ast.ClassDef) -> Dict[str, List[Dict[str, Any]]]:
            """Detect multiple responsibilities in class with method examples.
            
            Returns dict mapping responsibility type to methods that exhibit it:
            {
                'I/O': [{'method': '_load_config', 'line': 21, 'code': 'read_json_file(path)'}],
                ...
            }
            """
            methods = [node for node in class_node.body if isinstance(node, ast.FunctionDef)]
            
            if len(methods) == 0:
                return {}
            
            # Group methods by responsibility type with examples
            responsibility_groups: Dict[str, List[Dict[str, Any]]] = {}
            
            for method in methods:
                responsibilities_detailed = ComplexityMetrics.detect_responsibilities_with_examples(method)
                if not responsibilities_detailed:
                    # Method has no detected responsibility - classify as General
                    if 'General' not in responsibility_groups:
                        responsibility_groups['General'] = []
                    if len(responsibility_groups['General']) < 2:
                        # Get actual code from the method body (first non-docstring statement)
                        code_sample = ComplexityMetrics._get_method_code_sample(method)
                        responsibility_groups['General'].append({
                            'method': method.name,
                            'line': method.lineno,
                            'code': code_sample
                        })
                else:
                    for resp_type, examples in responsibilities_detailed.items():
                        if resp_type not in responsibility_groups:
                            responsibility_groups[resp_type] = []
                        # Add method name and first example
                        if len(responsibility_groups[resp_type]) < 2 and examples:
                            first_example = examples[0]
                            responsibility_groups[resp_type].append({
                                'method': method.name,
                                'line': first_example.get('line'),
                                'code': first_example.get('code', '')
                            })
            
            return responsibility_groups
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:40): Function "visit_node" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            nesting_level = 0
            
            def visit_node(node: ast.AST, level: int):
                nonlocal complexity
                
                # Increment complexity for decision points
                if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                    complexity += 1 + level  # Nesting adds to complexity
                    # Visit children with increased nesting
                    for child in ast.iter_child_nodes(node):
                        visit_node(child, level + 1)
                elif isinstance(node, ast.With):
                    complexity += 1 + level
                    for child in ast.iter_child_nodes(node):
                        visit_node(child, level + 1)
                elif isinstance(node, ast.BoolOp):
                    complexity += len(node.values) - 1 + level
                    for child in ast.iter_child_nodes(node):
                        visit_node(child, level)
                elif isinstance(node, ast.Assert):
                    complexity += 1 + level
                else:
                    # Visit children at same nesting level
                    for child in ast.iter_child_nodes(node):
                        visit_node(child, level)
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\cover_all_paths_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/cover_all_paths_scanner.py:13): Function "scan_file" is 34 lines - should be under 20 lines (extract complex logic to helper functions)

```python
    """Validates all behavior paths are tested."""
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        # Find all test methods
        test_methods = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                test_methods.append(node)
        
        # Check if test methods have actual code (not just pass/TODO)
        for test_method in test_methods:
            has_code = False
            for stmt in test_method.body:
                if isinstance(stmt, ast.Pass):
                    continue
                elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, (ast.Constant, ast.Str)):
                    # Skip docstrings
                    continue
                else:
                    # Check for actual executable code
                    for node in ast.walk(stmt):
                        if isinstance(node, (ast.Call, ast.Assign, ast.Assert, ast.Return, ast.Raise)):
                            has_code = True
                            break
                    if has_code:
                        break
            
            if not has_code:
                violations.append(Violation(
                    rule=rule_obj,
                    violation_message=f'Test method [{test_method.name}](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/cover_all_paths_scanner.py:13) has no actual test code - tests must exercise behavior paths, not just contain pass statements',
                    location=str(file_path),
                    line_number=test_method.lineno,
                    severity='error'
                ).to_dict())
        
        return violations

```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\delegation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/delegation_scanner.py:16): Function "scan_domain_concept" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return []
        
        def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            # Check for patterns where parent objects might be doing child's work
            for i, responsibility_data in enumerate(node.responsibilities):
                responsibility_name = responsibility_data.get('name', '')
                collaborators = responsibility_data.get('collaborators', [])
                resp_lower = responsibility_name.lower()
                
                # Check for patterns like "Find X by Y" where X should be found by collection class
                if 'find' in resp_lower and 'by' in resp_lower:
                    # If this is not a collection class, it might be doing child's work
                    if not self._is_collection_class(node.name):
                        violations.append(
                            Violation(
                                rule=rule_obj,
                                violation_message=f'Responsibility "{responsibility_name}" may be doing what a collection class should do. Consider delegating to collection class.',
                                location=node.map_location(f'responsibilities[{i}].name'),
                                line_number=None,
                                severity='info'
                            ).to_dict()
                        )
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\dependency_chaining_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/dependency_chaining_scanner.py:16): Function "scan_domain_concept" is 35 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return []
        
        def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            # Check if "Instantiated with" is present (constructor injection)
            has_instantiation = False
            instantiation_collaborators = []
            
            for i, responsibility_data in enumerate(node.responsibilities):
                responsibility_name = responsibility_data.get('name', '')
                resp_lower = responsibility_name.lower()
                
                if 'instantiated with' in resp_lower:
                    has_instantiation = True
                    collaborators = responsibility_data.get('collaborators', [])
                    instantiation_collaborators = [c.strip() for c in collaborators]
                    break
            
            # Check if methods use collaborators that weren't in instantiation
            # This is a simplified check - full implementation would track dependency chain
            if has_instantiation:
                for i, responsibility_data in enumerate(node.responsibilities):
                    responsibility_name = responsibility_data.get('name', '')
                    if 'instantiated with' in responsibility_name.lower():
                        continue
                    
                    collaborators = responsibility_data.get('collaborators', [])
                    
                    # Check if method uses collaborators that should come through owning objects
                    for collab in collaborators:
                        collab = collab.strip()
                        if collab and collab not in instantiation_collaborators:
                            # Check if it's a sub-collaborator that should be accessed through owner
                            if self._might_be_sub_collaborator(collab, instantiation_collaborators):
                                violations.append(
                                    Violation(
                                        rule=rule_obj,
                                        violation_message=f'Responsibility "{responsibility_name}" may be accessing sub-collaborator "{collab}" directly. Access through owning object instead.',
                                        location=node.map_location(f'responsibilities[{i}].collaborators'),
                                        line_number=None,
                                        severity='info'
                                    ).to_dict()
                                )
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\domain_grouping_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_grouping_code_scanner.py:22): Function "scan_file" is 28 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        ]
        
        def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
            violations = []
            
            if not file_path.exists():
                return violations
            
            # Check file path for technical layer patterns
            file_path_str = str(file_path)
            for pattern in self.TECHNICAL_LAYER_PATTERNS:
                if re.search(pattern, file_path_str, re.IGNORECASE):
                    violations.append(
                        Violation(
                            rule=rule_obj,
                            violation_message=f'File path "{file_path}" uses technical layer terminology. Organize by domain area instead.',
                            location=str(file_path),
                            line_number=None,
                            severity='info'
                        ).to_dict()
                    )
                    break
            
            parsed = self._read_and_parse_file(file_path)
            if not parsed:
                return violations
            
            content, lines, tree = parsed
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    violation = self._check_class_name(node, file_path, rule_obj)
                    if violation:
                        violations.append(violation)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\domain_language_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_code_scanner.py:61): Function "scan_file" is 36 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return super().scan(knowledge_graph, rule_obj, test_files=test_files, code_files=code_files, on_file_scanned=on_file_scanned)
        
        def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
            violations = []
            
            if not file_path.exists():
                return violations
            
            # Extract domain terms from knowledge graph
            domain_terms = set()
            if self.knowledge_graph:
                domain_terms = self._extract_domain_terms(self.knowledge_graph)
            
            # Generic names that are acceptable in specific contexts
            generic_names = {'self', 'result', 'value', 'data', 'item', 'obj', 'workspace', 'root', 'path', 'config'}
            
            parsed = self._read_and_parse_file(file_path)
            if not parsed:
                return violations
            
            content, lines, tree = parsed
            
            # Process classes and their methods with context
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_violations = self._check_domain_language(node, file_path, rule_obj, domain_terms, generic_names)
                    violations.extend(class_violations)
                    
                    # Check methods within this class, passing class context
                    for child in node.body:
                        if isinstance(child, ast.FunctionDef):
                            func_violations = self._check_function_domain_language(
                                child, file_path, rule_obj, domain_terms, generic_names,
                                enclosing_class=node.name
                            )
                            violations.extend(func_violations)
            
            # Check module-level functions (no enclosing class)
            for node in ast.iter_child_nodes(tree):
                if isinstance(node, ast.FunctionDef):
                    func_violations = self._check_function_domain_language(
                        node, file_path, rule_obj, domain_terms, generic_names,
                        enclosing_class=None
                    )
                    violations.extend(func_violations)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\domain_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_scanner.py:27): Function "scan_story_node" is 50 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        ]
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            # Only scan DomainConceptNodes, skip Story/Epic/SubEpic nodes
            if not isinstance(node, DomainConceptNode):
                return violations
            
            # Check node name for generic terms
            node_name_lower = node.name.lower()
            for term in ['data', 'config', 'parameter', 'result']:
                if term in node_name_lower and not self._is_domain_specific(node.name):
                    violations.append(
                        Violation(
                            rule=rule_obj,
                            violation_message=f'Domain concept "{node.name}" uses generic term "{term}". Use domain-specific language instead (e.g., "PortfolioData" → "Portfolio", "TargetConfig" → "TargetAllocation").',
                            location=node.map_location('name'),
                            line_number=None,
                            severity='warning'
                        ).to_dict()
                    )
            
            # Check responsibilities for generic terms and generate/calculate patterns
            for i, responsibility_data in enumerate(node.responsibilities):
                responsibility_name = responsibility_data.get('name', '')
                collaborators = responsibility_data.get('collaborators', [])
                resp_lower = responsibility_name.lower()
                
                # Check for generic terms in collaborators
                for collab in collaborators:
                    collab_lower = collab.lower()
                    for term in self.GENERIC_TERMS:
                        if term in collab_lower and not self._is_domain_specific(collab):
                            violations.append(
                                Violation(
                                    rule=rule_obj,
                                    violation_message=f'Responsibility "{responsibility_name}" uses generic collaborator "{collab}". Use domain-specific language instead.',
                                    location=node.map_location(f'responsibilities[{i}].collaborators'),
                                    line_number=None,
                                    severity='warning'
                                ).to_dict()
                            )
                            break
                
                # Check for generate/calculate patterns
                for pattern in self.GENERATE_PATTERNS:
                    if re.search(pattern, resp_lower):
                        violations.append(
                            Violation(
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:52): Function "scan_file" is 67 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        """
        
        def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
            violations = []
            
            _safe_print(f"[DuplicationScanner.scan_code_file] Called for: {file_path}")
            
            if not file_path.exists():
                _safe_print(f"[DuplicationScanner.scan_code_file] File does not exist: {file_path}")
                return violations
            
            # Track time for timeout detection
            file_start_time = datetime.now()
            
            # Check file size - skip very large files that might cause issues
            try:
                file_size = file_path.stat().st_size
                if file_size > 500_000:  # Skip files larger than 500KB
                    _safe_print(f"Skipping large file ({file_size/1024:.1f}KB): {file_path}")
                    return violations
            except Exception as e:
                _safe_print(f"Could not check file size for {file_path}: {e}")
            
            try:
                content = file_path.read_text(encoding='utf-8')
                tree = ast.parse(content, filename=str(file_path))
                lines = content.split('\n')
                
                # Extract function bodies for comparison
                functions = []
                
                def extract_functions_from_node(node: ast.AST, parent_class: str = None):
                    """Recursively extract functions, tracking parent class context."""
                    if isinstance(node, ast.ClassDef):
                        # Found a class - extract its methods
                        for child in node.body:
                            extract_functions_from_node(child, node.name)
                    elif isinstance(node, ast.FunctionDef):
                        # Found a function - extract it with class context
                        func_body = ast.unparse(node.body) if hasattr(ast, 'unparse') else str(node.body)
                        functions.append((node.name, func_body, node.lineno, node, parent_class))
                
                # Extract functions from top-level nodes
                for node in tree.body:
                    extract_functions_from_node(node, None)
                
                # Check for duplicate function bodies
                func_violations = self._check_duplicate_functions(functions, file_path, rule_obj, lines)
                violations.extend(func_violations)
                
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1821): Function "scan_cross_file" is 220 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            _safe_print("")  # Blank line after violations
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
            test_files: Optional[List[Path]] = None,
            code_files: Optional[List[Path]] = None,
            all_test_files: Optional[List[Path]] = None,
            all_code_files: Optional[List[Path]] = None,
            status_writer: Optional[Any] = None
        ) -> List[Dict[str, Any]]:
            violations = []
            
            # If all_* not provided, fall back to regular behavior
            if all_test_files is None:
                all_test_files = test_files
            if all_code_files is None:
                all_code_files = code_files
            
            # Combine changed files (to scan)
            changed_files = []
            if code_files:
                changed_files.extend(code_files)
            if test_files:
                changed_files.extend(test_files)
            
            # Combine all files (for reference)
            all_files = []
            if all_code_files:
                all_files.extend(all_code_files)
            if all_test_files:
                all_files.extend(all_test_files)
            
            if not changed_files or not all_files:
                return violations
            
            if len(changed_files) < len(all_files):
                _safe_print(f"\n[CROSS-FILE] Incremental scan: Checking {len(changed_files)} changed file(s) against {len(all_files)} total files...")
            else:
                _safe_print(f"\n[CROSS-FILE] Full scan: Scanning {len(all_files)} files for cross-file duplication...")
            import sys
            
            def write_status(msg: str):
                """Write progress to status file using the status writer."""
                if status_writer and hasattr(status_writer, 'write_cross_file_progress'):
                    try:
                        status_writer.write_cross_file_progress(msg)
                    except Exception as e:
                        logger.debug(f'Could not write to status file: {type(e).__name__}: {e}')
            
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:797): Function "extract_from_node" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
                                 ast.AsyncFor, ast.AsyncWith)
            
            def extract_from_node(node):
                """Recursively extract control structures from a node."""
                if isinstance(node, control_structures):
                    # Count nodes in this subtree
                    num_nodes = len(list(ast.walk(node)))
                    if min_nodes <= num_nodes <= max_nodes:
                        subtrees.append(node)
                
                # Recursively process children
                if hasattr(node, 'body') and isinstance(node.body, list):
                    for child in node.body:
                        extract_from_node(child)
                
                # Process orelse blocks (for if/for/while)
                if hasattr(node, 'orelse') and isinstance(node.orelse, list):
                    for child in node.orelse:
                        extract_from_node(child)
                
                # Process handlers (for try)
                if hasattr(node, 'handlers') and isinstance(node.handlers, list):
                    for handler in node.handlers:
                        if hasattr(handler, 'body') and isinstance(handler.body, list):
                            for child in handler.body:
                                extract_from_node(child)
                
                # Process finalbody (for try)
                if hasattr(node, 'finalbody') and isinstance(node.finalbody, list):
                    for child in node.finalbody:
                        extract_from_node(child)
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\enumerate_stories_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/enumerate_stories_scanner.py:13): Function "scan_story_node" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        """Validates all stories are explicitly enumerated (no "~X stories" notation)."""
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            if isinstance(node, Epic):
                epic_data = node.data
                
                # Check for "~X stories" notation
                description = epic_data.get('description', '')
                if '~' in description and re.search(r'~\d+\s+stories?', description, re.IGNORECASE):
                    location = node.map_location('description')
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Epic "{node.name}" uses "~X stories" notation - all stories must be explicitly enumerated',
                        location=location,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
                
                # Check sub-epics
                sub_epics = epic_data.get('sub_epics', [])
                for sub_epic_idx, sub_epic_data in enumerate(sub_epics):
                    violation = self._check_sub_epic_enumeration(sub_epic_data, node, sub_epic_idx, rule_obj)
                    if violation:
                        violations.append(violation)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:172): Function "visit_statement" is 35 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            multi_line_lines = set()
            
            def visit_statement(stmt_node):
                """Visit a statement node and find multi-line expressions within it."""
                # Check if this statement itself spans multiple lines
                if hasattr(stmt_node, 'end_lineno') and hasattr(stmt_node, 'lineno') and stmt_node.end_lineno and stmt_node.lineno:
                    if stmt_node.end_lineno > stmt_node.lineno:
                        # This statement spans multiple lines
                        # Check what type of statement it is
                        if isinstance(stmt_node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
                            # Assignment statement - check if the value/expression is multi-line
                            if hasattr(stmt_node, 'value') and stmt_node.value:
                                value = stmt_node.value
                                if hasattr(value, 'end_lineno') and hasattr(value, 'lineno') and value.end_lineno and value.lineno:
                                    if value.end_lineno > value.lineno:
                                        # Multi-line expression in assignment
                                        # Exclude continuation lines (all except first)
                                        for line_num in range(value.lineno + 1, value.end_lineno + 1):
                                            multi_line_lines.add(line_num)
                        
                        elif isinstance(stmt_node, ast.Expr):
                            # Expression statement (e.g., function call)
                            if hasattr(stmt_node, 'value') and stmt_node.value:
                                value = stmt_node.value
                                if isinstance(value, ast.Call):
                                    # Function call - check if it spans multiple lines
                                    if hasattr(value, 'end_lineno') and hasattr(value, 'lineno') and value.end_lineno and value.lineno:
                                        if value.end_lineno > value.lineno:
                                            # Multi-line function call - exclude continuation lines
                                            for line_num in range(value.lineno + 1, value.end_lineno + 1):
                                                multi_line_lines.add(line_num)
                        
                        elif isinstance(stmt_node, ast.Return):
                            # Return statement - check if return value is multi-line
                            if stmt_node.value:
                                if hasattr(stmt_node.value, 'end_lineno') and hasattr(stmt_node.value, 'lineno') and stmt_node.value.end_lineno and stmt_node.value.lineno:
                                    if stmt_node.value.end_lineno > stmt_node.value.lineno:
                                        # Multi-line return expression
                                        for line_num in range(stmt_node.value.lineno + 1, stmt_node.value.end_lineno + 1):
                                            multi_line_lines.add(line_num)
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_precondition_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_precondition_scanner.py:13): Function "scan_story_node" has high cognitive complexity (20) - should be under 15. Reduce nesting and extract complex logic.

    ```python
        """Validates Given describes preconditions, not functionality."""
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            if isinstance(node, Story):
                story_data = node.data
                scenarios = story_data.get('scenarios', [])
                
                for scenario_idx, scenario in enumerate(scenarios):
                    scenario_steps = self._get_scenario_steps(scenario)
                    
                    # Check each Given step
                    for step_idx, step in enumerate(scenario_steps):
                        if step.startswith('Given') or step.startswith('And'):
                            violation = self._check_given_is_functionality(step, node, scenario_idx, step_idx, rule_obj)
                            if violation:
                                violations.append(violation)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_state_not_actions_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_state_not_actions_scanner.py:16): Function "scan_story_node" has high cognitive complexity (20) - should be under 15. Reduce nesting and extract complex logic.

    ```python
        """
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            if isinstance(node, Story):
                story_data = node.data
                scenarios = story_data.get('scenarios', [])
                
                for scenario_idx, scenario in enumerate(scenarios):
                    scenario_steps = self._get_scenario_steps(scenario)
                    
                    # Check each Given step for action verbs
                    for step_idx, step in enumerate(scenario_steps):
                        if step.startswith('Given') or step.startswith('And'):
                            violation = self._check_given_is_action(step, node, scenario_idx, step_idx, rule_obj)
                            if violation:
                                violations.append(violation)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:332): Function "scan_cross_file" is 43 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return None, [], False, 0
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
            test_files: Optional[List[Path]] = None,
            code_files: Optional[List[Path]] = None,
            all_test_files: Optional[List[Path]] = None,
            all_code_files: Optional[List[Path]] = None,
            status_writer: Optional[Any] = None
        ) -> List[Dict[str, Any]]:
            """Scan across all test files for cross-file violations.
            
            Detects:
            1. Duplicate helper functions across files (should be consolidated)
            
            NOTE: Only reports ERRORS for duplicate definitions. Does NOT generate warnings
            about functions used in multiple files - that's not a problem.
            
            Args:
                rule_obj: Rule object reference
                test_files: List of all test file paths to analyze together
                code_files: Not used by TestScanner
                
            Returns:
                List of violation dictionaries for cross-file issues (only duplicates)
            """
            violations = []
            
            if not test_files or len(test_files) < 2:
                # Need at least 2 files to detect cross-file issues
                return violations
            
            # Reuse base class method to parse all test files
            parsed_files = self._get_all_test_files_parsed(test_files)
            
            # Extract helper function definitions using existing method
            helper_definitions = {}  # func_name -> list of (file_path, line_number)
            
            for file_path, content, tree in parsed_files:
                # Reuse existing method to get defined helpers
                defined_helpers = self._get_defined_helper_functions(tree)
                
                for func_name, line_number in defined_helpers.items():
                    if func_name not in helper_definitions:
                        helper_definitions[func_name] = []
                    helper_definitions[func_name].append((
                        str(file_path),
                        line_number
                    ))
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\implementation_details_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/implementation_details_scanner.py:21): Function "scan_story_node" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        ]
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            if not hasattr(node, 'name') or not node.name:
                return violations
            
            name_lower = node.name.lower()
            
            # Check for implementation operation verbs
            for verb in self.IMPLEMENTATION_VERBS:
                # Check if verb appears as main action (start of name or after "to")
                pattern = rf'\b{verb}\b'
                if re.search(pattern, name_lower):
                    # Check if it's describing an outcome vs implementation
                    # If it's just "Verb Noun" without user context, it's likely implementation
                    words = name_lower.split()
                    # Check if verb is at the start (most common pattern for implementation operations)
                    if verb in words[0] or (len(words) > 1 and verb in words[0:2]):
                        violation = Violation(
                            rule=rule_obj,
                            violation_message=f'Story "{node.name}" appears to be an implementation operation - should be a step within a story that describes user/system outcome',
                            location=node.name,
                            severity='error'
                        ).to_dict()
                        violations.append(violation)
                        break
            
            return violations
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:45): Function "scan_file" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        }
        
        def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
            violations = []
            
            if not file_path.exists():
                return violations
            
            # Extract domain terms from knowledge graph (using enhanced extraction from CodeScanner base class)
            domain_terms = set()
            if self.knowledge_graph:
                domain_terms = self._extract_domain_terms(self.knowledge_graph)
            
            parsed = self._read_and_parse_file(file_path)
            if not parsed:
                return violations
            
            content, lines, tree = parsed
            
            # Build docstring line ranges to exclude from scanning
            docstring_ranges = self._get_docstring_ranges(tree)
            
            # Check variable names
            violations.extend(self._check_variable_names(tree, file_path, rule_obj, content, domain_terms, docstring_ranges))
            
            # Check function names
            violations.extend(self._check_function_names(tree, file_path, rule_obj, domain_terms))
            
            # Check class names
            violations.extend(self._check_class_names(tree, file_path, rule_obj, domain_terms))
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:344): Function "visit_node" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            docstring_ranges = []
            
            def visit_node(node):
                """Recursively visit nodes to find docstrings."""
                # Check if this node has a body (function, class, module)
                if hasattr(node, 'body') and isinstance(node.body, list) and len(node.body) > 0:
                    # Check if first statement is a docstring
                    first_stmt = node.body[0]
                    if isinstance(first_stmt, ast.Expr):
                        # Docstring is an expression with a constant string
                        if isinstance(first_stmt.value, (ast.Constant, ast.Str)):
                            # Get the string value
                            if isinstance(first_stmt.value, ast.Constant):
                                docstring_value = first_stmt.value.value
                            else:  # ast.Str (Python < 3.8)
                                docstring_value = first_stmt.value.s
                            
                            if isinstance(docstring_value, str):
                                # Get line numbers
                                start_line = first_stmt.lineno if hasattr(first_stmt, 'lineno') else None
                                if start_line:
                                    # Count lines in docstring content
                                    docstring_lines = docstring_value.count('\n')
                                    # Add 1 for the content itself, and account for triple quotes (2 lines)
                                    end_line = start_line + docstring_lines + 2
                                    docstring_ranges.append((start_line, end_line))
                
                # Recursively visit child nodes
                for child in ast.iter_child_nodes(node):
                    visit_node(child)
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\invest_principles_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/invest_principles_scanner.py:12): Function "scan_story_node" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        """Validates stories follow INVEST principles (Independent, Negotiable, Valuable, Estimable, Small, Testable)."""
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            # Only check Story nodes (not epics/sub-epics)
            if not isinstance(node, Story):
                return violations
            
            if not hasattr(node, 'name') or not node.name:
                return violations
            
            # Check Testable: Story should have scenarios/scenario_outlines OR acceptance criteria in JSON
            story_data = node.data if hasattr(node, 'data') else {}
            scenarios = story_data.get('scenarios', [])
            scenario_outlines = story_data.get('scenario_outlines', [])
            acceptance_criteria = story_data.get('acceptance_criteria', [])
            
            # Story is testable if it has scenarios OR scenario_outlines OR acceptance criteria
            # Stories can have EITHER scenarios OR scenario_outlines (not requiring both)
            has_scenarios = (scenarios and len(scenarios) > 0) or (scenario_outlines and len(scenario_outlines) > 0)
            has_acceptance_criteria = acceptance_criteria and len(acceptance_criteria) > 0
            
            if not has_scenarios and not has_acceptance_criteria:
                violation = Violation(
                    rule=rule_obj,
                    violation_message=f'Story "{node.name}" lacks scenarios/scenario_outlines or acceptance criteria in story-graph.json - INVEST principle "Testable" requires clear testable outcomes',
                    location=node.name,
                    severity='warning'
                ).to_dict()
                violations.append(violation)
            
            # Small: Check sizing (already handled by StorySizingScanner, but we can add a reminder)
            # Independent: Hard to validate programmatically (requires dependency analysis)
            # Negotiable: Hard to validate programmatically
            # Valuable: Hard to validate programmatically
            # Estimable: Hard to validate programmatically (related to clarity)
            
            return violations
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\noun_redundancy_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/noun_redundancy_scanner.py:13): Function "scan_story_node" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        """Detects redundant nouns in story element names (e.g., 'Animation System', 'Animation Component')."""
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            if not hasattr(node, 'name') or not node.name:
                return violations
            
            name = node.name
            
            # Extract nouns (words that are capitalized or common nouns)
            words = re.findall(r'\b[A-Z][a-z]+\b|\b[a-z]+\b', name)
            
            # Check for repeated nouns across sibling nodes
            # This is a simplified check - full implementation would need parent context
            # For now, check if name has redundant patterns like "X Animation", "Y Animation"
            if len(words) >= 2:
                # Check for pattern: "Noun1 Noun2" where Noun2 appears in other names
                # This is a heuristic - full check needs sibling context
                pass
            
            # Check for numbered/generic qualifiers that suggest redundancy
            if re.search(r'\d+|System|Component|Module|Manager|Handler', name, re.IGNORECASE):
                # Check if removing qualifier would make it ambiguous
                base_name = re.sub(r'\s+(System|Component|Module|Manager|Handler|\d+)$', '', name, flags=re.IGNORECASE)
                if base_name and base_name != name:
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Story element "{name}" may have redundant noun - consider integrating with related concepts instead of using qualifiers',
                        location=node.name,
                        severity='warning'
                    ).to_dict()
                    violations.append(violation)
            
            return violations
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\parameterized_tests_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/parameterized_tests_scanner.py:9): Function "scan" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    class ParameterizedTestsScanner(Scanner):
        
        def scan(
            self, 
            knowledge_graph: Dict[str, Any], 
            rule_obj: Any = None,
            test_files: Optional[List['Path']] = None,
            code_files: Optional[List['Path']] = None,
            on_file_scanned: Optional[Any] = None
        ) -> List[Dict[str, Any]]:
            if not rule_obj:
                raise ValueError("rule_obj parameter is required for ParameterizedTestsScanner")
            
            violations = []
            story_map = StoryMap(knowledge_graph)
            
            for epic in story_map.epics():
                for node in story_map.walk(epic):
                    if isinstance(node, Story):
                        for scenario_outline in node.scenario_outlines:
                            if scenario_outline.examples_rows and len(scenario_outline.examples_rows) > 1:
                                location = scenario_outline.map_location()
                                violations.append(Violation(
                                    rule=rule_obj,
                                    violation_message=f"Scenario outline '{scenario_outline.name}' has {len(scenario_outline.examples_rows)} examples but may not use @pytest.mark.parametrize",
                                    location=location,
                                    severity='warning'
                                ).to_dict())
            
            return violations
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\prefer_object_model_over_config_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/prefer_object_model_over_config_scanner.py:36): Function "scan_file" is 41 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            ]
        
        def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Dict[str, Any] = None) -> List[Violation]:
            """Scan a file for direct config access violations."""
            violations = []
            
            # Need rule_obj to create violations
            effective_rule_obj = rule_obj if rule_obj is not None else self.rule_obj
            if not effective_rule_obj:
                return violations
            
            # Store rule_obj for creating violations
            self.rule_obj = effective_rule_obj
            
            # Read the file content
            if not file_path.exists():
                return violations
            
            try:
                content = file_path.read_text(encoding='utf-8')
            except Exception:
                return violations
            
            lines = content.split('\n')
            
            # Check if file is in an exception location
            if self._is_exception_file(file_path):
                return violations
            
            for line_num, line in enumerate(lines, start=1):
                # Skip if line has explicit ignore comment
                if '# scanner ignore' in line or '# noqa' in line:
                    continue
                
                # Check if we're in an exception context (like __init__)
                if self._is_in_exception_context(lines, line_num):
                    continue
                
                # Check for direct config access patterns
                for pattern, description in self.config_access_patterns:
                    if re.search(pattern, line):
                        violations.append(self._create_violation(
                            line_num,
                            f"{description}. Use object properties instead of accessing _config directly."
                        ))
                
                # Check for config file reading
                if re.search(self.config_file_pattern, line):
                    # Only flag if it looks like we're reading config when an object might exist
                    if self._looks_like_object_exists_context(lines, line_num):
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\property_encapsulation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/property_encapsulation_scanner.py:35): Function "scan_domain_concept" is 33 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return []
        
        def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            # Check responsibilities for exposed state patterns
            for i, responsibility_data in enumerate(node.responsibilities):
                responsibility_name = responsibility_data.get('name', '')
                resp_lower = responsibility_name.lower()
                
                # Check for exposed internal structure
                for pattern in self.EXPOSED_STATE_PATTERNS:
                    if re.search(pattern, resp_lower):
                        violations.append(
                            Violation(
                                rule=rule_obj,
                                violation_message=f'Responsibility "{responsibility_name}" exposes internal structure. Use property encapsulation instead (e.g., "Get holdings: Holdings" not "Get holdings list: List").',
                                location=node.map_location(f'responsibilities[{i}].name'),
                                line_number=None,
                                severity='warning'
                            ).to_dict()
                        )
                        break
                
                # Check for calculate/compute methods instead of properties
                for pattern in self.CALCULATE_PATTERNS:
                    if re.search(pattern, resp_lower):
                        violations.append(
                            Violation(
                                rule=rule_obj,
                                violation_message=f'Responsibility "{responsibility_name}" uses calculate/compute instead of property. Use "Get X" instead of "Calculate X" to hide calculation timing.',
                                location=node.map_location(f'responsibilities[{i}].name'),
                                line_number=None,
                                severity='warning'
                            ).to_dict()
                        )
                        break
            
            return violations
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:33): Function "scan_cross_file" is 48 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return []
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
            test_files: Optional[List[Path]] = None,
            code_files: Optional[List[Path]] = None,
            all_test_files: Optional[List[Path]] = None,
            all_code_files: Optional[List[Path]] = None,
            status_writer: Optional[Any] = None
        ) -> List[Dict[str, Any]]:
            """Scan across all files to check if loader/manager classes are owned by domain objects."""
            violations = []
            
            # Combine all files
            all_files = []
            if code_files:
                all_files.extend(code_files)
            if test_files:
                all_files.extend(test_files)
            
            if not all_files:
                return violations
            
            # First pass: collect all loader/manager classes and all classes
            loader_classes = {}  # class_name -> (file_path, class_node, pattern)
            all_classes = {}  # (file_path, class_name) -> class_node
            
            for file_path in all_files:
                if not file_path.exists():
                    continue
                
                try:
                    content = file_path.read_text(encoding='utf-8')
                    tree = ast.parse(content, filename=str(file_path))
                    
                    for node in ast.walk(tree):
                        if isinstance(node, ast.ClassDef):
                            all_classes[(file_path, node.name)] = node
                            
                            # Check if it's a loader/manager pattern
                            for pattern in self.MANAGER_PATTERNS:
                                if node.name.endswith(pattern):
                                    loader_classes[node.name] = (file_path, node, pattern)
                                    break
                except (SyntaxError, UnicodeDecodeError) as e:
                    logger.debug(f'Skipping file {file_path} due to {type(e).__name__}: {e}')
                    continue
            
            # Second pass: check if each loader class is owned by a domain object
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner.py:28): Function "scan" is 26 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        """
        
        def scan(
            self, 
            knowledge_graph: Dict[str, Any], 
            rule_obj: Any = None,
            test_files: Optional[List['Path']] = None,
            code_files: Optional[List['Path']] = None,
            on_file_scanned: Optional[Any] = None
        ) -> List[Dict[str, Any]]:
            """Scan knowledge graph for rule violations (file-by-file pass).
            
            This is the first pass where each file is scanned individually.
            
            Default implementation combines test_files and code_files, then calls scan_file()
            for each file. Subclasses can override to customize behavior.
            
            Args:
                knowledge_graph: The knowledge graph to validate (typically story-graph.json structure)
                rule_obj: Optional Rule object reference (for creating Violations with rule reference)
                test_files: Optional list of test file paths
                code_files: Optional list of code file paths
                on_file_scanned: Optional callback(file_path, violations) called after each file is scanned
                
            Returns:
                List of violation dictionaries or Violation objects, each containing:
                - rule: Rule object reference or rule name string
                - line_number: Line number where violation occurs (if applicable)
                - location: Location in knowledge graph (e.g., 'epics[0].name')
                - violation_message: Description of the violation
                - severity: Severity level ('error', 'warning', 'info')
                
            Raises:
                Exception: If scanner execution fails (exceptions should not be swallowed)
            """
            violations = []
            
            # Combine all files - unified architecture
            all_files = []
            if test_files:
                all_files.extend(test_files)
            if code_files:
                all_files.extend(code_files)
            
            # Scan each file using unified scan_file() method
            for file_path in all_files:
                if file_path and file_path.exists() and file_path.is_file():
                    file_violations = self.scan_file(file_path, rule_obj, knowledge_graph)
                    file_violations_list = file_violations if isinstance(file_violations, list) else [file_violations] if file_violations else []
                    
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scanner_registry.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_registry.py:56): Function "loads_scanner_class_with_error" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return scanner_class
        
        def loads_scanner_class_with_error(self, scanner_module_path: str) -> tuple[Optional[Type[Scanner]], Optional[str]]:
            """Load scanner class from module path with error information.
            
            Args:
                scanner_module_path: Module path to scanner class (e.g., 'scanners.import_placement_scanner.ImportPlacementScanner')
                
            Returns:
                Tuple of (scanner class if found, error message if not found)
            """
            if not scanner_module_path:
                return None, None
            
            try:
                module_path, class_name = scanner_module_path.rsplit('.', 1)
                
                # Extract scanner name from class name (handle camelCase)
                scanner_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower().replace('_scanner', '').replace('scanner', '')
                
                # Build paths to try
                paths_to_try = [
                    module_path,  # Exact path from config
                    f'agile_bot.bots.base_bot.src.scanners.{scanner_name}_scanner'
                ]
                
                # Add bot-specific path if not base_bot
                if self._bot_name and self._bot_name != 'base_bot':
                    paths_to_try.append(f'agile_bot.bots.{self._bot_name}.src.scanners.{scanner_name}_scanner')
                
                for path in paths_to_try:
                    try:
                        module = importlib.import_module(path)
                        if hasattr(module, class_name):
                            scanner_class = getattr(module, class_name)
                            
                            if isinstance(scanner_class, type) and hasattr(scanner_class, 'scan'):
                                if issubclass(scanner_class, Scanner):
                                    return scanner_class, None
                    except (ImportError, AttributeError):
                        continue
                
                return None, f"Scanner class not found: {scanner_module_path}"
            except Exception as e:
                return None, f"Error loading scanner {scanner_module_path}: {e}"
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scenarios_cover_all_cases_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_cover_all_cases_scanner.py:13): Function "scan_story_node" is 43 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        """Validates scenarios cover happy path, edge cases, and error cases."""
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            if isinstance(node, Story):
                story_data = node.data
                scenarios = story_data.get('scenarios', [])
                
                if len(scenarios) > 0:
                    # Check scenario coverage
                    has_happy_path = False
                    has_edge_case = False
                    has_error_case = False
                    
                    for scenario_idx, scenario in enumerate(scenarios):
                        scenario_text = self._get_scenario_text(scenario)
                        
                        if self._is_happy_path(scenario_text):
                            has_happy_path = True
                        if self._is_edge_case(scenario_text):
                            has_edge_case = True
                        if self._is_error_case(scenario_text):
                            has_error_case = True
                    
                    # Report missing coverage
                    if not has_happy_path:
                        violation = Violation(
                            rule=rule_obj,
                            violation_message='Story has no happy path scenario - add a scenario covering the normal success case',
                            location=node.map_location(),
                            severity='error'
                        ).to_dict()
                        violations.append(violation)
                    
                    if not has_edge_case and len(scenarios) > 1:
                        violation = Violation(
                            rule=rule_obj,
                            violation_message='Story has no edge case scenario - add scenarios covering boundary values and edge conditions',
                            location=node.map_location(),
                            severity='warning'
                        ).to_dict()
                        violations.append(violation)
                    
                    if not has_error_case and len(scenarios) > 1:
                        violation = Violation(
                            rule=rule_obj,
                            violation_message='Story has no error case scenario - add scenarios covering invalid inputs and error conditions',
                            location=node.map_location(),
                            severity='warning'
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scenarios_on_story_docs_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_on_story_docs_scanner.py:182): Function "scan_story_node" is 25 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return super().scan(knowledge_graph, rule_obj, test_files=test_files, code_files=code_files)
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            if isinstance(node, Story):
                # Skip stories not in scope (if scope is defined)
                if self._in_scope_story_names is not None:
                    if node.name not in self._in_scope_story_names:
                        # Story is out of scope, skip validation
                        return violations
                
                story_data = node.data
                scenarios = story_data.get('scenarios', [])
                scenario_outlines = story_data.get('scenario_outlines', [])
                
                # Check if story has scenarios OR scenario_outlines in JSON
                # Story is valid if it has EITHER scenarios OR scenario_outlines (not requiring both)
                has_scenarios = scenarios and len(scenarios) > 0
                has_scenario_outlines = scenario_outlines and len(scenario_outlines) > 0
                
                if not has_scenarios and not has_scenario_outlines:
                    location = node.map_location()
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Story "{node.name}" has no scenarios or scenario_outlines in story-graph.json - scenarios should be in JSON (scenarios or scenario_outlines fields)',
                        location=location,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
            
            return violations
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scenario_outline_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenario_outline_scanner.py:13): Function "scan_story_node" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        """Validates Scenario Outlines are used for multiple similar scenarios."""
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            if isinstance(node, Story):
                story_data = node.data
                scenarios = story_data.get('scenarios', [])
                
                # Check for Scenario Outline usage
                for scenario_idx, scenario in enumerate(scenarios):
                    scenario_text = self._get_scenario_text(scenario)
                    
                    # Check if scenario uses Scenario Outline
                    if 'Scenario Outline' in scenario_text:
                        # Check if it has Examples table
                        has_examples = 'Examples:' in scenario_text or 'examples' in str(scenario).lower()
                        
                        if not has_examples:
                            location = f"{node.map_location()}.scenarios[{scenario_idx}]"
                            violation = Violation(
                                rule=rule_obj,
                                violation_message='Scenario Outline used but no Examples table found - Scenario Outlines require Examples table',
                                location=location,
                                severity='error'
                            ).to_dict()
                            violations.append(violation)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scenario_specific_given_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenario_specific_given_scanner.py:15): Function "scan_story_node" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        """
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            if isinstance(node, Story):
                story_data = node.data
                scenarios = story_data.get('scenarios', [])
                background = story_data.get('background', [])
                
                for scenario_idx, scenario in enumerate(scenarios):
                    scenario_steps = self._get_scenario_steps(scenario)
                    
                    # Check if scenario starts with Given (should have scenario-specific Given)
                    if scenario_steps:
                        first_step = scenario_steps[0]
                        if not first_step.startswith('Given'):
                            location = f"{node.map_location()}.scenarios[{scenario_idx}]"
                            violation = Violation(
                                rule=rule_obj,
                                violation_message=f'Scenario does not start with Given step - scenario-specific setup should start with Given, not When',
                                location=location,
                                severity='error'
                            ).to_dict()
                            violations.append(violation)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\story_enumeration_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_enumeration_scanner.py:17): Function "scan_story_node" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        """
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            if isinstance(node, Epic):
                epic_data = node.data
                
                # Check for "~X stories" notation in epic description or estimated_stories
                estimated_stories = epic_data.get('estimated_stories')
                if estimated_stories:
                    if isinstance(estimated_stories, str) and '~' in str(estimated_stories):
                        location = node.map_location('estimated_stories')
                        violation = Violation(
                            rule=rule_obj,
                            violation_message=f'Epic "{node.name}" uses "~{estimated_stories}" notation - all stories must be explicitly enumerated, not estimated',
                            location=location,
                            severity='error'
                        ).to_dict()
                        violations.append(violation)
                
                # Check sub-epics for story enumeration
                sub_epics = epic_data.get('sub_epics', [])
                for sub_epic_idx, sub_epic_data in enumerate(sub_epics):
                    violation = self._check_sub_epic_stories(sub_epic_data, node, sub_epic_idx, rule_obj)
                    if violation:
                        violations.append(violation)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:40): Function "map_location" has high cognitive complexity (22) - should be under 15. Reduce nesting and extract complex logic.

    ```python
            return self.data.get('name', '')
        
        def map_location(self, field: str = 'name') -> str:
            if isinstance(self, Epic):
                return f"epics[{self.epic_idx}].{field}"
            elif isinstance(self, SubEpic):
                if self.sub_epic_path:
                    path_str = "".join([f".sub_epics[{idx}]" for idx in self.sub_epic_path])
                    return f"epics[{self.epic_idx}]{path_str}.{field}"
                else:
                    return f"epics[{self.epic_idx}].{field}"
            elif isinstance(self, Story):
                path_parts = [f"epics[{self.epic_idx}]"]
                if self.sub_epic_path:
                    for idx in self.sub_epic_path:
                        path_parts.append(f"sub_epics[{idx}]")
                if self.story_group_idx is not None:
                    path_parts.append(f"story_groups[{self.story_group_idx}]")
                path_parts.append(f"stories[{self.story_idx}]")
                path_parts.append(field)
                return ".".join(path_parts)
            return ""
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\story_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_scanner.py:10): Function "scan" is 34 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    class StoryScanner(Scanner):
        
        def scan(
            self, 
            knowledge_graph: Dict[str, Any], 
            rule_obj: Any = None,
            test_files: Optional[List['Path']] = None,
            code_files: Optional[List['Path']] = None,
            on_file_scanned: Optional[Any] = None
        ) -> List[Dict[str, Any]]:
            if not rule_obj:
                raise ValueError("rule_obj parameter is required for StoryScanner")
            
            violations = []
            # Extract story_graph from knowledge_graph if nested
            story_graph_data = knowledge_graph.get('story_graph', knowledge_graph)
            story_map = StoryMap(story_graph_data)
            
            # Scan domain concepts from epics and sub_epics
            for epic in story_map.epics():
                # Scan domain concepts at epic level
                epic_violations = self._scan_domain_concepts(
                    epic.data.get('domain_concepts', []),
                    epic.epic_idx,
                    None,
                    rule_obj
                )
                violations.extend(epic_violations)
                
                # Walk through all nodes (including sub_epics)
                for node in story_map.walk(epic):
                    # Scan domain concepts at sub_epic level
                    if hasattr(node, 'data') and 'domain_concepts' in node.data:
                        sub_epic_violations = self._scan_domain_concepts(
                            node.data.get('domain_concepts', []),
                            epic.epic_idx,
                            getattr(node, 'sub_epic_path', None),
                            rule_obj
                        )
                        violations.extend(sub_epic_violations)
                    
                    # Also scan story nodes if needed (for other validations)
                    if not isinstance(node, StoryGroup):
                        node_violations = self.scan_story_node(node, rule_obj)
                        violations.extend(node_violations)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\technical_abstraction_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/technical_abstraction_scanner.py:26): Function "scan_domain_concept" is 33 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return []
        
        def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            # Check node name for technical abstraction patterns
            node_name_lower = node.name.lower()
            for pattern in [r'\bsaver\b', r'\bloader\b', r'\bstorage\b']:
                if re.search(pattern, node_name_lower):
                    violations.append(
                        Violation(
                            rule=rule_obj,
                            violation_message=f'Domain concept "{node.name}" separates technical abstraction. Keep technical details (saving, loading) as part of domain concepts instead.',
                            location=node.map_location('name'),
                            line_number=None,
                            severity='warning'
                        ).to_dict()
                    )
                    break
            
            # Check responsibilities for technical abstraction patterns
            for i, responsibility_data in enumerate(node.responsibilities):
                responsibility_name = responsibility_data.get('name', '')
                resp_lower = responsibility_name.lower()
                for pattern in self.TECHNICAL_ABSTRACTION_PATTERNS:
                    if re.search(pattern, resp_lower):
                        violations.append(
                            Violation(
                                rule=rule_obj,
                                violation_message=f'Responsibility "{responsibility_name}" exposes technical abstraction. Stay at domain level (e.g., "Save portfolio" not "Save portfolio to file").',
                                location=node.map_location(f'responsibilities[{i}].name'),
                                line_number=None,
                                severity='warning'
                            ).to_dict()
                        )
                        break
            
            return violations
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\technical_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/technical_language_scanner.py:26): Function "scan_story_node" is 28 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        ]
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            if not hasattr(node, 'name') or not node.name:
                return violations
            
            name_lower = node.name.lower()
            
            # Check for technical verbs
            for verb in self.TECHNICAL_VERBS:
                if verb in name_lower:
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Story element "{node.name}" uses technical implementation verb "{verb}" - use business language focusing on user experience',
                        location=node.name,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
                    break
            
            # Check for technical phrases
            for phrase in self.TECHNICAL_PHRASES:
                if phrase in name_lower:
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Story element "{node.name}" uses technical implementation phrase "{phrase}" - focus on what user experiences, not how it\'s implemented',
                        location=node.name,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
                    break
            
            return violations
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:33): Function "scan_story_node" is 28 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return []
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            name = node.name
            
            if not name:
                return violations
            
            node_type = self._get_node_type(node)
            
            violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            violation = self._check_gerund_ending(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            violation = self._check_actor_prefix(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            violation = self._check_noun_only(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            violation = self._check_third_person_singular(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\vertical_slice_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vertical_slice_scanner.py:22): Function "scan" is 26 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return violations
        
        def scan(
            self, 
            knowledge_graph: Dict[str, Any], 
            rule_obj: Any = None,
            test_files: Optional[List['Path']] = None,
            code_files: Optional[List['Path']] = None,
            on_file_scanned: Optional[Any] = None
        ) -> List[Dict[str, Any]]:
            """Scan increments for vertical slice violations."""
            violations = []
            
            if not rule_obj:
                raise ValueError("rule_obj parameter is required")
            
            # Check increments
            increments = knowledge_graph.get('increments', [])
            
            for increment_idx, increment in enumerate(increments):
                increment_epics = increment.get('epics', [])
                
                # Check if increment spans only one epic (horizontal layer violation)
                if len(increment_epics) == 1:
                    location = f"increments[{increment_idx}]"
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Increment "{increment.get("name", f"Increment {increment_idx+1}")}" spans only 1 epic - increments should be vertical slices spanning multiple epics',
                        location=location,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
            
            return violations
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\build\build_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_action.py:74): Function "inject_rules" is 33 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return behavior_to_content.get(self.behavior.name, [])
    
        def inject_rules(self, instructions) -> None:
            validate_action = self.rules
            rules_obj = validate_action.rules
            rules_text = rules_obj.formatted_rules()
            rules_data = validate_action.inject_behavior_specific_and_bot_rules()
            all_rules = rules_data.get('validation_rules', [])
            
            # Get existing base_instructions (these are the CUSTOM INSTRUCTIONS - keep them FIRST)
            existing_instructions = instructions.get('base_instructions', [])
            new_instructions = []
            rules_section = []
            
            # Process each instruction, removing {{rules}} placeholder if present
            # Keep ALL other instructions as-is (they are the custom instructions)
            for line in existing_instructions:
                if isinstance(line, str) and '{{rules}}' in line:
                    # Remove the placeholder line - we'll add rules at the very end
                    pass  # Don't add this line
                else:
                    # Keep all custom instructions
                    new_instructions.append(line)
            
            # Prepare rules section to append at the END
            if rules_text != 'No validation rules found.':
                rules_lines = rules_text.split('\n')
                rules_section.extend(rules_lines)
            
            # CRITICAL: Append rules section at the VERY END (after ALL custom instructions)
            # This ensures: CUSTOM INSTRUCTIONS FIRST, RULES LAST
            if rules_section:
                new_instructions.append('')  # Blank line separator
                new_instructions.append('**VALIDATION RULES:**')  # Section header
                new_instructions.append('')  # Blank line
                new_instructions.extend(rules_section)
            
            # Replace base_instructions with: [custom instructions] + [rules at end]
            instructions._data['base_instructions'] = new_instructions
            instructions.set('rules', all_rules)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\render\render_config_loader.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_config_loader.py:57): Function "verify_synchronizer_class" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return config_entry
    
        def verify_synchronizer_class(self, synchronizer_class_path: str) -> None:
            module_path, class_name = synchronizer_class_path.rsplit('.', 1)
            possible_paths = [module_path, f'agile_bot.bots.{self.behavior.bot_name}.src.{module_path}', f'agile_bot.bots.{self.behavior.bot_name}.src.synchronizers.{module_path}']
            module = None
            for path in possible_paths:
                try:
                    module = importlib.import_module(path)
                    if hasattr(module, class_name):
                        break
                    module = None
                except ImportError:
                    continue
            
            # If module not found, skip verification (may be in test environment)
            if module is None:
                return
            
            synchronizer_class = getattr(module, class_name, None)
            if synchronizer_class is None:
                return
                
            has_render = hasattr(synchronizer_class, 'render')
            has_sync_methods = any((hasattr(synchronizer_class, method) for method in ['synchronize_outline', 'synchronize_increments', 'synchronize_exploration']))
            if not (has_render or has_sync_methods):
                raise ValueError(f'Synchronizer class {synchronizer_class_path} does not have required methods')
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:103): Function "get_last_report_timestamp" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return rules_instance._rule_filter.filter_files(self.files, self.exclude)
    
        def get_last_report_timestamp(self) -> float:
            logger = logging.getLogger(__name__)
            docs_path = self.bot_paths.documentation_path
            reports_dir = self.bot_paths.workspace_directory / docs_path / 'reports'
            logger.info(f'Looking for previous reports in: {reports_dir}')
            if not reports_dir.exists():
                logger.info('Reports directory does not exist - returning 0.0')
                return 0.0
            
            report_files = list(reports_dir.glob(f'{self.behavior.name}-validation-status-*.md'))
            logger.info(f'Found {len(report_files)} report files')
            if not report_files:
                logger.info('No report files found - returning 0.0')
                return 0.0
            
            current_time = time.time()
            previous_run_files = [f for f in report_files if (current_time - f.stat().st_mtime) > 10]
            logger.info(f'Found {len(previous_run_files)} previous run files (excluding files < 10 seconds old)')
            
            if not previous_run_files:
                logger.info('No previous run files found - returning 0.0')
                return 0.0
            
            most_recent = max(previous_run_files, key=lambda p: p.stat().st_mtime)
            logger.info(f'Most recent previous report: {most_recent.name} (timestamp: {most_recent.stat().st_mtime})')
            return most_recent.stat().st_mtime
    
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:29): Function "categorize_scanner_rules" has deep nesting (depth=5) - should be under 4 levels. Extract nested logic to helper functions.

    ```python
            return lines
    
        def categorize_scanner_rules(self, validation_rules: List[Dict[str, Any]]) -> Dict:
            """Categorize rules by execution status."""
            executed_rules = []
            load_failed_rules = []
            execution_failed_rules = []
            no_scanner_rules = []
            for rule_dict in validation_rules:
                category = self._get_rule_category(rule_dict)
                if category == 'executed':
                    executed_rules.append(self._build_executed_rule_entry(rule_dict))
                elif category == 'load_failed':
                    load_failed_rules.append(self._build_failed_rule_entry(rule_dict))
                elif category == 'execution_failed':
                    execution_failed_rules.append(self._build_failed_rule_entry(rule_dict))
                elif category == 'no_scanner':
                    no_scanner_rules.append(self._get_rule_file(rule_dict))
            return {'executed': executed_rules, 'load_failed': load_failed_rules, 'execution_failed': execution_failed_rules, 'no_scanner': no_scanner_rules}
    
    ```

#### <span id="maintain-vertical-density-violations">Maintain Vertical Density: 59 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cursor_command_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_command_generator.py:92): Function "_build_behavior_command_with_actions" is 65 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cursor_command_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_command_generator.py:158): Function "_build_rules_command" is 55 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:97): Function "_is_actual_commented_code" is 89 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:221): Function "_extract_comment_text" is 66 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\business_readable_test_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/business_readable_test_names_scanner.py:43): Function "_extract_domain_language" is 58 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\business_readable_test_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/business_readable_test_names_scanner.py:111): Function "_check_business_readable" is 84 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:147): Function "_find_expected_scenario_name" is 139 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:392): Function "_check_file_name_matches_sub_epic" is 59 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:484): Function "_find_sub_epic_for_method" is 75 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\class_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_size_scanner.py:37): Function "_check_class_size" is 55 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\clear_parameters_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/clear_parameters_scanner.py:85): Function "_check_parameters" is 55 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:81): Function "_extract_domain_terms" is 123 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:362): Function "_extract_code_snippet" is 56 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:419): Function "_create_violation_with_snippet" is 63 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\delegation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/delegation_code_scanner.py:32): Function "_check_delegation" is 55 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\dependency_chaining_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/dependency_chaining_code_scanner.py:38): Function "_check_dependency_chaining" is 57 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\descriptive_function_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/descriptive_function_names_scanner.py:33): Function "_check_descriptive_name" is 85 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\domain_language_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_code_scanner.py:136): Function "_check_function_domain_language" is 67 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\domain_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_scanner.py:27): Function "scan_story_node" is 58 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:52): Function "scan_file" is 86 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:318): Function "_check_duplicate_code_blocks" is 302 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:621): Function "_extract_code_blocks" is 163 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:928): Function "_is_mostly_helper_calls" is 55 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1758): Function "_log_violation_details" is 62 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1821): Function "scan_cross_file" is 255 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:149): Function "_is_optional_config_check" is 69 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:276): Function "_check_guard_pattern" is 59 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:40): Function "_check_function_size" is 120 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:161): Function "_get_multi_line_expression_line_numbers" is 55 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:257): Function "_get_comment_and_docstring_line_numbers" is 52 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\generic_capability_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/generic_capability_scanner.py:119): Function "_check_generic_technical_verbs" is 51 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:220): Function "_find_inline_code_blocks" is 79 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:332): Function "scan_cross_file" is 71 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\import_placement_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/import_placement_scanner.py:165): Function "_skip_try_import_error_block" is 67 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\import_placement_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/import_placement_scanner.py:255): Function "_check_import_placement" is 84 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:76): Function "_check_variable_names" is 66 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\meaningful_context_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/meaningful_context_scanner.py:64): Function "_check_numbered_variables" is 82 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\no_guard_clauses_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/no_guard_clauses_scanner.py:44): Function "_check_guard_clause_patterns" is 60 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\one_concept_per_test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/one_concept_per_test_scanner.py:35): Function "_check_one_concept" is 72 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\prefer_object_model_over_config_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/prefer_object_model_over_config_scanner.py:36): Function "scan_file" is 54 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\property_encapsulation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/property_encapsulation_code_scanner.py:30): Function "_check_encapsulation" is 61 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:42): Function "_check_test_methods_call_production_code" is 117 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:246): Function "_is_production_module" is 56 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:316): Function "_is_empty_or_todo_only" is 59 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:376): Function "_has_production_code_calls" is 52 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:429): Function "_helper_calls_production_code" is 56 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:33): Function "scan_cross_file" is 60 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:117): Function "_class_uses_as_attribute" is 64 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner.py:28): Function "scan" is 56 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\scenarios_cover_all_cases_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_cover_all_cases_scanner.py:13): Function "scan_story_node" is 52 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\scenarios_on_story_docs_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_on_story_docs_scanner.py:9): Function "_get_story_names_from_scope" is 68 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\separate_concerns_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/separate_concerns_scanner.py:33): Function "_check_mixed_concerns" is 56 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:254): Function "_extract_domain_terms" is 105 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:433): Function "_check_variable_matches" is 51 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:485): Function "_check_assertion_matches" is 64 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\test_file_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_file_naming_scanner.py:167): Function "_find_sub_epic_for_method" is 74 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\unnecessary_parameter_passing_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/unnecessary_parameter_passing_scanner.py:151): Function "_check_property_extraction" is 53 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:281): Function "_check_noun_verb_pattern" is 64 lines - consider improving vertical density by declaring variables near usage
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:365): Function "_check_noun_only" is 115 lines - consider improving vertical density by declaring variables near usage

#### <span id="never-swallow-exceptions-violations">Never Swallow Exceptions: 16 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\behavior_matcher.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/behavior_matcher.py:80): Except block only contains pass at line 80 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:92): Except block only contains pass at line 92 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:89): Except block only contains pass at line 89 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:478): Except block only contains pass at line 478 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\communication_verb_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/communication_verb_scanner.py:79): Except block only contains pass at line 79 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\communication_verb_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/communication_verb_scanner.py:114): Except block only contains pass at line 114 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\generic_capability_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/generic_capability_scanner.py:81): Except block only contains pass at line 81 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\generic_capability_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/generic_capability_scanner.py:114): Except block only contains pass at line 114 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\generic_capability_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/generic_capability_scanner.py:166): Except block only contains pass at line 166 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:517): Except block only contains pass at line 517 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\specificity_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specificity_scanner.py:70): Except block only contains pass at line 70 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:143): Except block only contains pass at line 143 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:164): Except block only contains pass at line 164 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:195): Except block only contains pass at line 195 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:276): Except block only contains pass at line 276 - exceptions must be logged or rethrown, never swallowed
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:475): Except block only contains pass at line 475 - exceptions must be logged or rethrown, never swallowed

#### <span id="place-imports-at-top-violations">Place Imports At Top: 7 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\base_bot_cli.py:20`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/base_bot_cli.py:20:20): Import statement found at line 20 after non-import code. Move all imports to the top of the file.
- <span style="color: red;">[X]</span> **ERROR** - [`src\base_bot_cli.py:21`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/base_bot_cli.py:21:21): Import statement found at line 21 after non-import code. Move all imports to the top of the file.
- <span style="color: red;">[X]</span> **ERROR** - [`src\base_bot_cli.py:22`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/base_bot_cli.py:22:22): Import statement found at line 22 after non-import code. Move all imports to the top of the file.
- <span style="color: red;">[X]</span> **ERROR** - [`src\base_bot_cli.py:23`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/base_bot_cli.py:23:23): Import statement found at line 23 after non-import code. Move all imports to the top of the file.
- <span style="color: red;">[X]</span> **ERROR** - [`src\base_bot_cli.py:45`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/base_bot_cli.py:45:45): Import statement found at line 45 after non-import code. Move all imports to the top of the file.
- <span style="color: red;">[X]</span> **ERROR** - [`src\base_bot_cli.py:46`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/base_bot_cli.py:46:46): Import statement found at line 46 after non-import code. Move all imports to the top of the file.
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py:21`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:21:21): Import statement found at line 21 after non-import code. Move all imports to the top of the file.

#### <span id="prefer-object-model-over-config-violations">Prefer Object Model Over Config: 14 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.
- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.
- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.
- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.
- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.
- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.
- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.
- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.
- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.
- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.
- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.
- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.
- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.
- <span style="color: red;">[X]</span> **ERROR** - `unknown`: Using .get() on _config attribute. Use object properties instead of accessing _config directly.

#### <span id="provide-meaningful-context-violations">Provide Meaningful Context: 106 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:237): Line 237 uses numbered variable "s1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:296): Line 296 uses numbered variable "name1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:296): Line 296 uses numbered variable "name2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:299): Line 299 uses numbered variable "n1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:300): Line 300 uses numbered variable "n2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_size_scanner.py:17): Line 17 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:385): Line 385 uses numbered variable "start_line_0" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:389): Line 389 uses numbered variable "end_line_0" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:392): Line 392 uses numbered variable "end_line_0" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:398): Line 398 uses numbered variable "start_line_0" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:400): Line 400 uses numbered variable "end_line_0" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:402): Line 402 uses numbered variable "end_line_0" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:395): Line 395 uses numbered variable "end_line_0" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:16): Line 16 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:68): Line 68 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:394): Line 394 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:598): Line 598 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:929): Line 929 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:932): Line 932 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:981): Line 981 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1138): Line 1138 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1896): Line 1896 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1898): Line 1898 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1345): Line 1345 uses numbered variable "block1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1345): Line 1345 uses numbered variable "block2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1505): Line 1505 uses numbered variable "block1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1505): Line 1505 uses numbered variable "block2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1528): Line 1528 uses numbered variable "block1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1528): Line 1528 uses numbered variable "block2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1589): Line 1589 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1589): Line 1589 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1629): Line 1629 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1629): Line 1629 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1639): Line 1639 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1639): Line 1639 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1645): Line 1645 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1645): Line 1645 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1666): Line 1666 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1666): Line 1666 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1671): Line 1671 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1671): Line 1671 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1679): Line 1679 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1679): Line 1679 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1686): Line 1686 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1686): Line 1686 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1692): Line 1692 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1692): Line 1692 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1698): Line 1698 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1698): Line 1698 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1705): Line 1705 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1705): Line 1705 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1713): Line 1713 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1713): Line 1713 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1721): Line 1721 uses numbered variable "expr1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1721): Line 1721 uses numbered variable "expr2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:344): Line 344 uses numbered variable "block1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1353): Line 1353 uses numbered variable "domain_patterns1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1354): Line 1354 uses numbered variable "domain_patterns2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1390): Line 1390 uses numbered variable "calls1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1391): Line 1391 uses numbered variable "calls2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1522): Line 1522 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1522): Line 1522 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1535): Line 1535 uses numbered variable "node1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1648): Line 1648 uses numbered variable "arg_count1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1649): Line 1649 uses numbered variable "arg_count2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1659): Line 1659 uses numbered variable "a1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1659): Line 1659 uses numbered variable "a2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1982): Line 1982 uses numbered variable "block1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:345): Line 345 uses numbered variable "block2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1400): Line 1400 uses numbered variable "method_names1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1401): Line 1401 uses numbered variable "method_names2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1537): Line 1537 uses numbered variable "node2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1983): Line 1983 uses numbered variable "block2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1362): Line 1362 uses numbered variable "func1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1363): Line 1363 uses numbered variable "func2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:509): Line 509 uses numbered variable "block1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2029): Line 2029 uses numbered variable "file1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2030): Line 2030 uses numbered variable "file2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2031): Line 2031 uses numbered variable "func1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2032): Line 2032 uses numbered variable "func2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2033): Line 2033 uses numbered variable "start1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2034): Line 2034 uses numbered variable "end1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2035): Line 2035 uses numbered variable "start2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2036): Line 2036 uses numbered variable "end2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2039): Line 2039 uses numbered variable "preview1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2040): Line 2040 uses numbered variable "preview2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2049): Line 2049 uses numbered variable "location1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2050): Line 2050 uses numbered variable "location2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:510): Line 510 uses numbered variable "block2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2044): Line 2044 uses numbered variable "preview1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2046): Line 2046 uses numbered variable "preview2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\meaningful_context_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/meaningful_context_scanner.py:40): Line 40 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\meaningful_context_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/meaningful_context_scanner.py:41): Line 41 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\meaningful_context_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/meaningful_context_scanner.py:42): Line 42 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\separate_concerns_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/separate_concerns_scanner.py:56): Line 56 uses numbered variable "resp1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\separate_concerns_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/separate_concerns_scanner.py:56): Line 56 uses numbered variable "resp2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\single_responsibility_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/single_responsibility_scanner.py:108): Line 108 uses numbered variable "verb1" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\single_responsibility_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/single_responsibility_scanner.py:109): Line 109 uses numbered variable "verb2" - use meaningful descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\useless_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/useless_comments_scanner.py:91): Line 91 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\useless_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/useless_comments_scanner.py:146): Line 146 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\useless_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/useless_comments_scanner.py:148): Line 148 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:6): Line 6 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validation_scanner_status_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scanner_status_builder.py:8): Line 8 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\scanners\useless_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanners/useless_comments_scanner.py:89): Line 89 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\scanners\useless_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanners/useless_comments_scanner.py:126): Line 126 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\scanners\useless_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanners/useless_comments_scanner.py:128): Line 128 contains magic number - replace with named constant

#### <span id="refactor-completely-not-partially-violations">Refactor Completely Not Partially: 10 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:95): Fallback/legacy support code found (comment at line 95, code at line 96) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:152): Fallback/legacy support code found (comment at line 152, code at line 153) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1791): Fallback/legacy support code found (comment at line 1791, code at line 1792) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:47): Fallback/legacy support code found (comment at line 47, code at line 48) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:206): Fallback/legacy support code found (comment at line 206, code at line 208) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\import_placement_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/import_placement_scanner.py:369): Fallback/legacy support code found (comment at line 369, code at line 370) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:66): Fallback/legacy support code found (comment at line 66, code at line 67) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:423): Fallback/legacy support code found (comment at line 423, code at line 424) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resources\block_extractor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block_extractor.py:68): Fallback/legacy support code found (comment at line 68, code at line 69) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resources\block_extractor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block_extractor.py:93): Fallback/legacy support code found (comment at line 93, code at line 94) - complete refactoring by removing old pattern support

#### <span id="simplify-control-flow-violations">Simplify Control Flow: 158 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:14): Function "_handle_scope_parameter" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\scoping_parameter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/scoping_parameter.py:252): Function "_extract_story_names_from_increment" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\behavior_matcher.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/behavior_matcher.py:70): Function "_load_action_triggers_for_behavior" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_context_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_context_builder.py:73): Function "_add_argument_for_field" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:65): Function "_output_result" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:214): Function "_parse_json_parameters" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:129): Function "_add_argument_for_field" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\arrange_act_assert_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/arrange_act_assert_scanner.py:16): Function "scan_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\arrange_act_assert_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/arrange_act_assert_scanner.py:68): Function "_detect_aaa_sections_ast" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\arrange_act_assert_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/arrange_act_assert_scanner.py:105): Function "_classify_statement" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\arrange_act_assert_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/arrange_act_assert_scanner.py:148): Function "_validate_aaa_structure" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\arrange_act_assert_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/arrange_act_assert_scanner.py:236): Function "_has_actual_code" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\background_common_setup_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/background_common_setup_scanner.py:110): Function "_get_scenario_steps" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:40): Function "_check_commented_code" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:97): Function "_is_actual_commented_code" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:187): Function "_check_html_in_comments" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:221): Function "_extract_comment_text" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:288): Function "_check_misleading_todos" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\business_readable_test_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/business_readable_test_names_scanner.py:21): Function "scan_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\business_readable_test_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/business_readable_test_names_scanner.py:43): Function "_extract_domain_language" has nesting depth of 11 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:25): Function "scan_file" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:69): Function "_extract_story_names" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:147): Function "_find_expected_scenario_name" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:452): Function "_get_sub_epics_spanned_by_test_methods" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:484): Function "_find_sub_epic_for_method" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:560): Function "_find_closest_sub_epic_names" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:598): Function "_is_helper_file_only" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_representation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_representation_scanner.py:24): Function "scan_domain_concept" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:81): Function "_extract_domain_terms" has nesting depth of 12 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:362): Function "_extract_code_snippet" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\communication_verb_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/communication_verb_scanner.py:49): Function "_check_communication_verbs" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\communication_verb_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/communication_verb_scanner.py:84): Function "_check_enablement_verbs" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complete_refactoring_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complete_refactoring_scanner.py:30): Function "_check_fallback_legacy_support" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:11): Function "cyclomatic_complexity" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:32): Function "cognitive_complexity" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:320): Function "_get_accessed_attributes" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:400): Function "detect_class_responsibilities_with_examples" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:40): Function "visit_node" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\consistent_vocabulary_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/consistent_vocabulary_scanner.py:48): Function "_check_vocabulary_consistency" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\cover_all_paths_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/cover_all_paths_scanner.py:13): Function "scan_file" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\delegation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/delegation_code_scanner.py:32): Function "_check_delegation" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\delegation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/delegation_code_scanner.py:94): Function "_is_plain_collection" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\delegation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/delegation_code_scanner.py:137): Function "_is_class_constant" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\dependency_chaining_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/dependency_chaining_code_scanner.py:38): Function "_check_dependency_chaining" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\dependency_chaining_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/dependency_chaining_code_scanner.py:96): Function "_collect_instance_attributes" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\dependency_chaining_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/dependency_chaining_code_scanner.py:121): Function "_check_method_calls_for_instance_attrs" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\dependency_chaining_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/dependency_chaining_scanner.py:16): Function "scan_domain_concept" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\descriptive_function_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/descriptive_function_names_scanner.py:14): Function "scan_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\domain_language_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_code_scanner.py:61): Function "scan_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\domain_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_scanner.py:27): Function "scan_story_node" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:227): Function "_is_simple_delegation" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:272): Function "_is_simple_property_getter" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:318): Function "_check_duplicate_code_blocks" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:785): Function "_extract_subtrees_from_function" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:851): Function "_get_statement_end_line" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:928): Function "_is_mostly_helper_calls" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:984): Function "_is_only_helper_calls" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1089): Function "_count_actual_code_statements" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1158): Function "_is_test_pattern" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1201): Function "_is_list_building_pattern" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1244): Function "_is_simple_property" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1277): Function "_is_simple_constructor" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1345): Function "_operates_on_different_domains" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1378): Function "_calls_different_methods" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1416): Function "_extract_method_calls" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1445): Function "_normalize_block" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1487): Function "_get_block_preview" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1559): Function "_get_node_signature" has nesting depth of 11 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1589): Function "_compare_ast_nodes_deep" has nesting depth of 11 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1721): Function "_compare_expr_structure" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1758): Function "_log_violation_details" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1821): Function "scan_cross_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:797): Function "extract_from_node" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\exact_variable_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/exact_variable_names_scanner.py:34): Function "_extract_domain_concepts" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\exact_variable_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/exact_variable_names_scanner.py:47): Function "_check_variable_names" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\exception_handling_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/exception_handling_scanner.py:27): Function "_check_exception_misuse" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:55): Function "_check_function_guards" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:89): Function "_is_guard_pattern" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:149): Function "_is_optional_config_check" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:228): Function "_is_followed_by_creation_logic" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:266): Function "_contains_creation_call" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:276): Function "_check_guard_pattern" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:161): Function "_get_multi_line_expression_line_numbers" has nesting depth of 9 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:217): Function "_get_data_structure_line_numbers" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:257): Function "_get_comment_and_docstring_line_numbers" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:172): Function "visit_statement" has nesting depth of 9 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\generic_capability_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/generic_capability_scanner.py:119): Function "_check_generic_technical_verbs" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_precondition_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_precondition_scanner.py:13): Function "scan_story_node" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_precondition_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_precondition_scanner.py:32): Function "_get_scenario_steps" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_state_not_actions_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_state_not_actions_scanner.py:16): Function "scan_story_node" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_state_not_actions_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_state_not_actions_scanner.py:35): Function "_get_scenario_steps" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:58): Function "_get_helper_functions" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:82): Function "_get_defined_helper_functions" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:101): Function "_get_helper_calls_in_file" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:180): Function "_get_docstring_line_range" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:220): Function "_find_inline_code_blocks" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\import_placement_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/import_placement_scanner.py:43): Function "_find_import_section_end" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\import_placement_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/import_placement_scanner.py:165): Function "_skip_try_import_error_block" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:76): Function "_check_variable_names" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:186): Function "_collect_loop_and_comprehension_var_names" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:248): Function "_check_function_names" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:283): Function "_check_class_names" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:322): Function "_is_in_small_loop" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:337): Function "_get_docstring_ranges" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:344): Function "visit_node" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\meaningful_context_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/meaningful_context_scanner.py:34): Function "_check_magic_numbers" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\meaningful_context_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/meaningful_context_scanner.py:64): Function "_check_numbered_variables" has nesting depth of 13 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\minimize_mutable_state_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/minimize_mutable_state_scanner.py:28): Function "_check_mutable_patterns" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\natural_english_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/natural_english_code_scanner.py:22): Function "scan_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\no_guard_clauses_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/no_guard_clauses_scanner.py:44): Function "_check_guard_clause_patterns" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\no_guard_clauses_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/no_guard_clauses_scanner.py:122): Function "_check_function_guard_clauses" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\one_concept_per_test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/one_concept_per_test_scanner.py:17): Function "scan_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\one_concept_per_test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/one_concept_per_test_scanner.py:108): Function "_detect_multiple_concepts" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\parameterized_tests_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/parameterized_tests_scanner.py:9): Function "scan" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\prefer_object_model_over_config_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/prefer_object_model_over_config_scanner.py:105): Function "_is_in_exception_context" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\primitive_vs_object_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/primitive_vs_object_scanner.py:78): Function "_check_function_parameters" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\property_encapsulation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/property_encapsulation_code_scanner.py:30): Function "_check_encapsulation" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\property_encapsulation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/property_encapsulation_code_scanner.py:92): Function "_get_parent_function" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:225): Function "_has_production_code_imports" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:303): Function "_is_test_infrastructure_import" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:316): Function "_is_empty_or_todo_only" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:376): Function "_has_production_code_calls" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:429): Function "_helper_calls_production_code" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:501): Function "_file_has_production_code_calls" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:521): Function "_is_production_function" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:33): Function "scan_cross_file" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:117): Function "_class_uses_as_attribute" has nesting depth of 10 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scanner_loader.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_loader.py:23): Function "_load_scanner_class" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scanner_registry.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_registry.py:56): Function "loads_scanner_class_with_error" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scenarios_cover_all_cases_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_cover_all_cases_scanner.py:13): Function "scan_story_node" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scenarios_on_story_docs_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_on_story_docs_scanner.py:129): Function "_extract_story_names_from_epic" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scenario_outline_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenario_outline_scanner.py:13): Function "scan_story_node" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scenario_specific_given_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenario_specific_given_scanner.py:15): Function "scan_story_node" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scenario_specific_given_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenario_specific_given_scanner.py:41): Function "_get_scenario_steps" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:41): Function "_check_test_method_names" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:117): Function "_check_variable_names" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:152): Function "_is_in_helper_call" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:168): Function "_check_assertions" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:254): Function "_extract_domain_terms" has nesting depth of 12 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:383): Function "_find_matching_story" has nesting depth of 12 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:433): Function "_check_variable_matches" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:485): Function "_check_assertion_matches" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specificity_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specificity_scanner.py:50): Function "_check_too_generic" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\story_graph_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_graph_match_scanner.py:36): Function "_extract_story_names" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\story_graph_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_graph_match_scanner.py:52): Function "_check_test_classes_match_stories" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:40): Function "map_location" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\swallowed_exceptions_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/swallowed_exceptions_scanner.py:30): Function "_check_swallowed_exceptions" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\test_file_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_file_naming_scanner.py:136): Function "_get_sub_epics_spanned_by_test_methods" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\test_file_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_file_naming_scanner.py:167): Function "_find_sub_epic_for_method" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\test_file_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_file_naming_scanner.py:242): Function "_find_closest_sub_epic_names" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\type_safety_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/type_safety_scanner.py:168): Function "_check_parameters_get_pattern" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\type_safety_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/type_safety_scanner.py:200): Function "_is_dict_any_annotation" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\ubiquitous_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/ubiquitous_language_scanner.py:32): Function "_extract_domain_terms" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\unnecessary_parameter_passing_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/unnecessary_parameter_passing_scanner.py:69): Function "_collect_instance_attributes" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\unnecessary_parameter_passing_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/unnecessary_parameter_passing_scanner.py:132): Function "_parameter_used_like_instance_attr" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\unnecessary_parameter_passing_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/unnecessary_parameter_passing_scanner.py:151): Function "_check_property_extraction" has nesting depth of 11 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:365): Function "_check_noun_only" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:29): Function "categorize_scanner_rules" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

#### <span id="stop-writing-useless-comments-violations">Stop Writing Useless Comments: 690 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/base_bot_cli.py:50): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:164): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:253): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:16): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:26): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:37): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:55): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:66): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:76): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:85): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:95): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:105): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:116): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\activity_tracker.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/activity_tracker.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:63): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:94): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:112): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:167): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:169): Useless comment: "# Create help action directly (doesn't need a behavior workf" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:179): Useless comment: "# Create a minimal behavior wrapper for the help action" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:192): Useless comment: "# Execute the help action with empty context" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_command_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_command_router.py:18): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_command_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_command_router.py:33): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_context_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_context_builder.py:23): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_context_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_context_builder.py:26): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_context_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_context_builder.py:56): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_context_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_context_builder.py:74): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_context_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_context_builder.py:99): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_context_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_context_builder.py:120): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_context_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_context_builder.py:128): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_context_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_context_builder.py:134): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_context_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_context_builder.py:123): Useless comment: "# Handle Python dict syntax (single quotes) by replacing wit" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:6): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:13): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:23): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:27): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:25): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:115): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:143): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:178): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:198): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:215): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:244): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:71): Useless comment: "# Process unrecognized flags from argparse (things it couldn" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:74): Useless comment: "# Process positional context arguments separately" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:31): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:37): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:67): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:106): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:124): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:130): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:170): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:210): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:235): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:242): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:114): Useless comment: "# Get all fields including inherited ones" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_command_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_command_generator.py:53): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_command_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_command_generator.py:93): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_command_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_command_generator.py:159): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:7): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:22): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:27): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:32): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_context.py:6): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_context.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:7): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:16): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:21): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:26): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:30): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:42): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:47): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:60): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:64): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:74): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:79): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\parameter_info_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/parameter_info_builder.py:6): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\parameter_info_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/parameter_info_builder.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\parameter_info_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/parameter_info_builder.py:25): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\parameter_info_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/parameter_info_builder.py:39): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\parameter_info_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/parameter_info_builder.py:43): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\parameter_info_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/parameter_info_builder.py:51): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\parameter_info_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/parameter_info_builder.py:59): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\parameter_info_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/parameter_info_builder.py:63): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\parameter_info_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/parameter_info_builder.py:73): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\parameter_info_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/parameter_info_builder.py:87): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\parameter_info_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/parameter_info_builder.py:99): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:104): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:117): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:127): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\abstraction_levels_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/abstraction_levels_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\abstraction_levels_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/abstraction_levels_scanner.py:34): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:61): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:89): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:99): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:123): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:136): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:146): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:156): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:219): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:242): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\ac_consolidation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/ac_consolidation_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\ac_consolidation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/ac_consolidation_scanner.py:26): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\ac_consolidation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/ac_consolidation_scanner.py:54): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\arrange_act_assert_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/arrange_act_assert_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\arrange_act_assert_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/arrange_act_assert_scanner.py:35): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\arrange_act_assert_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/arrange_act_assert_scanner.py:69): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\arrange_act_assert_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/arrange_act_assert_scanner.py:106): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\arrange_act_assert_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/arrange_act_assert_scanner.py:141): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\arrange_act_assert_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/arrange_act_assert_scanner.py:237): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\arrange_act_assert_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/arrange_act_assert_scanner.py:65): Useless comment: "# Return first violation" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\arrange_act_assert_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/arrange_act_assert_scanner.py:200): Useless comment: "# Get line numbers for each section" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\ascii_only_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/ascii_only_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\ascii_only_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/ascii_only_scanner.py:35): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\background_common_setup_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/background_common_setup_scanner.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\background_common_setup_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/background_common_setup_scanner.py:45): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\background_common_setup_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/background_common_setup_scanner.py:59): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\background_common_setup_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/background_common_setup_scanner.py:77): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\background_common_setup_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/background_common_setup_scanner.py:99): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\background_common_setup_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/background_common_setup_scanner.py:111): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:41): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:88): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:98): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:188): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:222): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\bad_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/bad_comments_scanner.py:143): Useless comment: "# Return statements with values" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\behavioral_ac_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/behavioral_ac_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\behavioral_ac_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/behavioral_ac_scanner.py:37): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\behavioral_ac_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/behavioral_ac_scanner.py:43): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\business_readable_test_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/business_readable_test_names_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\business_readable_test_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/business_readable_test_names_scanner.py:44): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\business_readable_test_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/business_readable_test_names_scanner.py:103): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\business_readable_test_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/business_readable_test_names_scanner.py:112): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\business_readable_test_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/business_readable_test_names_scanner.py:197): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\calculation_timing_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/calculation_timing_code_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\calculation_timing_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/calculation_timing_code_scanner.py:42): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\calculation_timing_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/calculation_timing_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:13): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:22): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:70): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:88): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:148): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:288): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:292): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:297): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:304): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:320): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:325): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:337): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:345): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:363): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:393): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:453): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:485): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:561): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:599): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_size_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\class_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_size_scanner.py:38): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\clear_parameters_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/clear_parameters_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\clear_parameters_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/clear_parameters_scanner.py:67): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\clear_parameters_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/clear_parameters_scanner.py:86): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\clear_parameters_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/clear_parameters_scanner.py:142): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\code_representation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_representation_code_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\code_representation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_representation_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:82): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:206): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:219): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:283): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:304): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complete_refactoring_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complete_refactoring_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complete_refactoring_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complete_refactoring_scanner.py:31): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:8): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:33): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:71): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:93): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:103): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:155): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:194): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:203): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:242): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:287): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:321): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:358): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:368): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:393): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:401): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:263): Useless comment: "# Get attributes accessed by each method (with delegation aw" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:379): Useless comment: "# Get first statement" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:424): Useless comment: "# Get actual code from the method body (first non-docstring " - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\consistent_indentation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/consistent_indentation_scanner.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\consistent_indentation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/consistent_indentation_scanner.py:27): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\consistent_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/consistent_naming_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\consistent_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/consistent_naming_scanner.py:45): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\consistent_vocabulary_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/consistent_vocabulary_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\consistent_vocabulary_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/consistent_vocabulary_scanner.py:31): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\consistent_vocabulary_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/consistent_vocabulary_scanner.py:49): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\cover_all_paths_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/cover_all_paths_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\delegation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/delegation_code_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\delegation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/delegation_code_scanner.py:33): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\delegation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/delegation_code_scanner.py:89): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\delegation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/delegation_code_scanner.py:95): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\delegation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/delegation_code_scanner.py:138): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\delegation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/delegation_code_scanner.py:176): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\delegation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/delegation_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\delegation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/delegation_scanner.py:42): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\dependency_chaining_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/dependency_chaining_code_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\dependency_chaining_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/dependency_chaining_code_scanner.py:39): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\dependency_chaining_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/dependency_chaining_code_scanner.py:97): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\dependency_chaining_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/dependency_chaining_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\dependency_chaining_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/dependency_chaining_scanner.py:62): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\descriptive_function_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/descriptive_function_names_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\descriptive_function_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/descriptive_function_names_scanner.py:34): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\domain_concept_node.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_concept_node.py:7): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\domain_concept_node.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_concept_node.py:30): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\domain_grouping_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_grouping_code_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\domain_grouping_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_grouping_code_scanner.py:58): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\domain_grouping_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_grouping_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\domain_language_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_code_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\domain_language_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_code_scanner.py:40): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\domain_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\domain_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_scanner.py:87): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\domain_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_scanner.py:93): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:20): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:41): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:82): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:140): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:188): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:228): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:273): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:319): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:622): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:786): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:798): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:834): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:852): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:894): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:904): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:929): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:985): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1035): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1039): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1048): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1059): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1090): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1138): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1159): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1202): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1245): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1278): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1323): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1346): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1379): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1417): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1446): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:488): Useless comment: "# Get function pairs for this group" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:551): Useless comment: "# Get all blocks in this group" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:594): Useless comment: "# Create violation message showing all duplicate locations" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:659): Useless comment: "# Get line numbers" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:712): Useless comment: "# Get preview text" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:756): Useless comment: "# Get line numbers" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2038): Useless comment: "# Get code snippets for both locations" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:2048): Useless comment: "# Create violation message with code boxes for each location" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\encapsulation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/encapsulation_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\encapsulation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/encapsulation_scanner.py:34): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\encapsulation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/encapsulation_scanner.py:47): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\encapsulation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/encapsulation_scanner.py:70): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\encapsulation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/encapsulation_scanner.py:43): Useless comment: "# Return first violation found" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\enumerate_ac_permutations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/enumerate_ac_permutations_scanner.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\enumerate_stories_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/enumerate_stories_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\enumerate_stories_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/enumerate_stories_scanner.py:41): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\error_handling_isolation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/error_handling_isolation_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\error_handling_isolation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/error_handling_isolation_scanner.py:28): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\exact_variable_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/exact_variable_names_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\exact_variable_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/exact_variable_names_scanner.py:35): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\exact_variable_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/exact_variable_names_scanner.py:48): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\exception_classification_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/exception_classification_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\exception_classification_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/exception_classification_scanner.py:29): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\exception_handling_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/exception_handling_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\exception_handling_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/exception_handling_scanner.py:28): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:56): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:70): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:90): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:132): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:150): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:220): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:229): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:267): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:277): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\excessive_guards_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/excessive_guards_scanner.py:337): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\explicit_dependencies_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/explicit_dependencies_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\explicit_dependencies_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/explicit_dependencies_scanner.py:28): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\fixture_placement_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/fixture_placement_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\fixture_placement_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/fixture_placement_scanner.py:28): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:41): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:162): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:173): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:218): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:230): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:258): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\generic_capability_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/generic_capability_scanner.py:120): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_precondition_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_precondition_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_precondition_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_precondition_scanner.py:33): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_precondition_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_precondition_scanner.py:45): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_state_not_actions_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_state_not_actions_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_state_not_actions_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_state_not_actions_scanner.py:36): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_state_not_actions_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_state_not_actions_scanner.py:70): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:59): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:83): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:102): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:127): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:181): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:301): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:325): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:329): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:44): Useless comment: "# Get all helper function names defined in the file and impo" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:62): Useless comment: "# Get functions defined in this file" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:147): Useless comment: "# Get test method source lines" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:160): Useless comment: "# Create violation for this block" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:227): Useless comment: "# Get the actual starting line number of the test method bod" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:231): Useless comment: "# Get docstring line range to skip" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\implementation_details_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/implementation_details_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\import_placement_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/import_placement_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\import_placement_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/import_placement_scanner.py:18): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\import_placement_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/import_placement_scanner.py:44): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\import_placement_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/import_placement_scanner.py:178): Useless comment: "# Get the indentation level of the 'try:' line" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\increment_folder_structure_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/increment_folder_structure_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\increment_folder_structure_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/increment_folder_structure_scanner.py:39): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\increment_folder_structure_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/increment_folder_structure_scanner.py:49): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:77): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:187): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:231): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:239): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:249): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:284): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:323): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:338): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:345): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:377): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:360): Useless comment: "# Get line numbers" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\invest_principles_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/invest_principles_scanner.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\meaningful_context_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/meaningful_context_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\meaningful_context_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/meaningful_context_scanner.py:35): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\meaningful_context_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/meaningful_context_scanner.py:65): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\meaningful_context_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/meaningful_context_scanner.py:75): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\meaningful_context_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/meaningful_context_scanner.py:94): Useless comment: "# Handle tuple unpacking: a, b = ..." - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\minimize_mutable_state_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/minimize_mutable_state_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\minimize_mutable_state_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/minimize_mutable_state_scanner.py:29): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\mock_boundaries_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/mock_boundaries_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\mock_boundaries_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/mock_boundaries_scanner.py:33): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\natural_english_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/natural_english_code_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\natural_english_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/natural_english_code_scanner.py:44): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\natural_english_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/natural_english_code_scanner.py:60): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\natural_english_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/natural_english_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\noun_redundancy_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/noun_redundancy_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\no_fallbacks_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/no_fallbacks_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\no_fallbacks_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/no_fallbacks_scanner.py:32): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\no_guard_clauses_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/no_guard_clauses_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\no_guard_clauses_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/no_guard_clauses_scanner.py:45): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\observable_behavior_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/observable_behavior_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\observable_behavior_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/observable_behavior_scanner.py:29): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\one_concept_per_test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/one_concept_per_test_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\one_concept_per_test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/one_concept_per_test_scanner.py:36): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\one_concept_per_test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/one_concept_per_test_scanner.py:109): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\one_concept_per_test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/one_concept_per_test_scanner.py:147): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\one_concept_per_test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/one_concept_per_test_scanner.py:155): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\one_concept_per_test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/one_concept_per_test_scanner.py:169): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\one_concept_per_test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/one_concept_per_test_scanner.py:177): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\one_concept_per_test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/one_concept_per_test_scanner.py:105): Useless comment: "# Return first violation" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\open_closed_principle_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/open_closed_principle_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\open_closed_principle_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/open_closed_principle_scanner.py:29): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\plain_english_scenarios_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/plain_english_scenarios_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\plain_english_scenarios_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/plain_english_scenarios_scanner.py:44): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\plain_english_scenarios_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/plain_english_scenarios_scanner.py:51): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\plain_english_scenarios_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/plain_english_scenarios_scanner.py:75): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\plain_english_scenarios_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/plain_english_scenarios_scanner.py:88): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\prefer_object_model_over_config_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/prefer_object_model_over_config_scanner.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\prefer_object_model_over_config_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/prefer_object_model_over_config_scanner.py:37): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\prefer_object_model_over_config_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/prefer_object_model_over_config_scanner.py:92): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\prefer_object_model_over_config_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/prefer_object_model_over_config_scanner.py:106): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\prefer_object_model_over_config_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/prefer_object_model_over_config_scanner.py:128): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\prefer_object_model_over_config_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/prefer_object_model_over_config_scanner.py:148): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\present_ac_consolidation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/present_ac_consolidation_scanner.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\primitive_vs_object_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/primitive_vs_object_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\primitive_vs_object_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/primitive_vs_object_scanner.py:62): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\primitive_vs_object_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/primitive_vs_object_scanner.py:79): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\primitive_vs_object_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/primitive_vs_object_scanner.py:119): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\primitive_vs_object_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/primitive_vs_object_scanner.py:143): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\primitive_vs_object_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/primitive_vs_object_scanner.py:157): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\primitive_vs_object_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/primitive_vs_object_scanner.py:151): Useless comment: "# Handle typing.Dict, typing.List, etc." - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\property_encapsulation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/property_encapsulation_code_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\property_encapsulation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/property_encapsulation_code_scanner.py:31): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\property_encapsulation_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/property_encapsulation_code_scanner.py:93): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\property_encapsulation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/property_encapsulation_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:161): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:194): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:205): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:216): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:247): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:304): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:317): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:487): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:502): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:551): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:173): Useless comment: "# Get relative path from project root" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:321): Useless comment: "# Get method source lines for comment checking" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:26): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:118): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resource_oriented_design_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_design_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner.py:17): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner.py:138): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner.py:225): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner.py:239): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner.py:251): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner.py:263): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner_orchestrator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_orchestrator.py:19): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner_orchestrator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_orchestrator.py:22): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner_orchestrator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_orchestrator.py:32): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner_orchestrator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_orchestrator.py:78): Useless comment: "# Perform the scan" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner_registry.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_registry.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner_registry.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_registry.py:13): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner_registry.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_registry.py:22): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner_registry.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_registry.py:45): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner_registry.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_registry.py:57): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scanner_registry.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_registry.py:101): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenarios_cover_all_cases_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_cover_all_cases_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenarios_cover_all_cases_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_cover_all_cases_scanner.py:67): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenarios_cover_all_cases_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_cover_all_cases_scanner.py:73): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenarios_cover_all_cases_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_cover_all_cases_scanner.py:80): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenarios_cover_all_cases_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_cover_all_cases_scanner.py:87): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenarios_on_story_docs_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_on_story_docs_scanner.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenarios_on_story_docs_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_on_story_docs_scanner.py:80): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenarios_on_story_docs_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_on_story_docs_scanner.py:101): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenarios_on_story_docs_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_on_story_docs_scanner.py:116): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenarios_on_story_docs_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_on_story_docs_scanner.py:130): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenarios_on_story_docs_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_on_story_docs_scanner.py:152): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenario_outline_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenario_outline_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenario_outline_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenario_outline_scanner.py:42): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenario_specific_given_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenario_specific_given_scanner.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\scenario_specific_given_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenario_specific_given_scanner.py:42): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\separate_concerns_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/separate_concerns_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\separate_concerns_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/separate_concerns_scanner.py:34): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\simplify_control_flow_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/simplify_control_flow_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\simplify_control_flow_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/simplify_control_flow_scanner.py:31): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\simplify_control_flow_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/simplify_control_flow_scanner.py:47): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\single_responsibility_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/single_responsibility_scanner.py:16): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\single_responsibility_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/single_responsibility_scanner.py:44): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\single_responsibility_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/single_responsibility_scanner.py:80): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\single_responsibility_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/single_responsibility_scanner.py:123): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\single_responsibility_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/single_responsibility_scanner.py:166): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\single_responsibility_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/single_responsibility_scanner.py:177): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:42): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:77): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:118): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:153): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:169): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:209): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:255): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:361): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:369): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:384): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:551): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_enumeration_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_enumeration_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_enumeration_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_enumeration_scanner.py:46): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_filename_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_filename_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_filename_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_filename_scanner.py:37): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_graph_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_graph_match_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_graph_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_graph_match_scanner.py:37): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_graph_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_graph_match_scanner.py:53): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:17): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:63): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:83): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:104): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:119): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:123): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:131): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:141): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:170): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:211): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:260): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:270): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:295): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:300): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:29): Useless comment: "# Create new node for internal use" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_scanner.py:89): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\swallowed_exceptions_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/swallowed_exceptions_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\swallowed_exceptions_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/swallowed_exceptions_scanner.py:31): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\technical_abstraction_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/technical_abstraction_code_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\technical_abstraction_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/technical_abstraction_code_scanner.py:34): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\technical_abstraction_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/technical_abstraction_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\technical_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/technical_language_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_boundary_behavior_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_boundary_behavior_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_boundary_behavior_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_boundary_behavior_scanner.py:32): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_file_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_file_naming_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_file_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_file_naming_scanner.py:40): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_file_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_file_naming_scanner.py:48): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_file_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_file_naming_scanner.py:64): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_file_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_file_naming_scanner.py:89): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_file_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_file_naming_scanner.py:137): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_file_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_file_naming_scanner.py:168): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_file_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_file_naming_scanner.py:243): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_file_naming_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_file_naming_scanner.py:27): Useless comment: "# Get expected file name from sub-epic" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_quality_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_quality_scanner.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_quality_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_quality_scanner.py:44): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_quality_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_quality_scanner.py:73): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_quality_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_quality_scanner.py:92): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_quality_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_quality_scanner.py:117): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_scanner.py:104): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\test_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/test_scanner.py:125): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\third_party_isolation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/third_party_isolation_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\third_party_isolation_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/third_party_isolation_scanner.py:29): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\type_safety_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/type_safety_scanner.py:20): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\type_safety_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/type_safety_scanner.py:73): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\type_safety_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/type_safety_scanner.py:103): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\type_safety_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/type_safety_scanner.py:140): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\type_safety_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/type_safety_scanner.py:169): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\type_safety_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/type_safety_scanner.py:201): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\type_safety_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/type_safety_scanner.py:235): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\ubiquitous_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/ubiquitous_language_scanner.py:13): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\ubiquitous_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/ubiquitous_language_scanner.py:33): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\ubiquitous_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/ubiquitous_language_scanner.py:52): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\unnecessary_parameter_passing_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/unnecessary_parameter_passing_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\unnecessary_parameter_passing_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/unnecessary_parameter_passing_scanner.py:49): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\unnecessary_parameter_passing_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/unnecessary_parameter_passing_scanner.py:70): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\unnecessary_parameter_passing_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/unnecessary_parameter_passing_scanner.py:133): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\unnecessary_parameter_passing_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/unnecessary_parameter_passing_scanner.py:206): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\useless_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/useless_comments_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\useless_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/useless_comments_scanner.py:39): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\useless_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/useless_comments_scanner.py:64): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\useless_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/useless_comments_scanner.py:102): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\useless_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/useless_comments_scanner.py:140): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:30): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:82): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:93): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:98): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:103): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:108): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:170): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:201): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:282): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:366): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:215): Useless comment: "# Handle truly irregular verbs that don't follow regular pat" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:235): Useless comment: "# Handle verbs ending in -es (e.g., "fixes" -> "fix", "watch" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:239): Useless comment: "# Handle verbs ending in -s (e.g., "selects" -> "select", "g" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vertical_density_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vertical_density_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vertical_density_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vertical_density_scanner.py:31): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vertical_slice_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vertical_slice_scanner.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/violation.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/violation.py:44): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/violation.py:49): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/violation.py:54): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/violation.py:59): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/violation.py:64): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/violation.py:68): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\story_graph\nodes.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/story_graph/nodes.py:45): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\story_graph\nodes.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/story_graph/nodes.py:53): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\build\build_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_scope.py:17): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\rules\rules_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules_action.py:23): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\rules\rules_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules_action.py:27): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:8): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:24): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:35): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:46): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:57): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:68): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:77): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:84): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:91): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:103): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:17): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:30): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:48): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:63): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:67): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:73): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:80): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:84): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:92): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:102): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:113): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:126): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:136): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:143): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:158): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:173): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:181): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:189): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:193): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:204): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:215): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:221): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:226): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:232): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:238): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:247): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_builder.py:26): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_formatter.py:43): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:145): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:321): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_scanner_status_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scanner_status_builder.py:52): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:30): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\violation_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/violation_formatter.py:9): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\violation_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/violation_formatter.py:17): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\violation_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/violation_formatter.py:38): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\violation_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/violation_formatter.py:52): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\violation_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/violation_formatter.py:61): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\violation_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/violation_formatter.py:67): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\violation_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/violation_formatter.py:80): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\violation_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/violation_formatter.py:91): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\scanners\useless_comments_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanners/useless_comments_scanner.py:14): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:13): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:36): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:41): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:46): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:51): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:56): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:61): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:65): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:69): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:73): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:87): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:101): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:114): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:128): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:142): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block_extractor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block_extractor.py:13): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block_extractor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block_extractor.py:16): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block_extractor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block_extractor.py:41): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block_extractor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block_extractor.py:45): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block_extractor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block_extractor.py:63): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block_extractor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block_extractor.py:82): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\block_extractor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block_extractor.py:57): Useless comment: "# Get source code for this node" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\file.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/file.py:18): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\file.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/file.py:21): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\file.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/file.py:37): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\file.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/file.py:42): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\file.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/file.py:47): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\file.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/file.py:58): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\file.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/file.py:65): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\file.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/file.py:71): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\file.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/file.py:93): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\file.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/file.py:103): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\file.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/file.py:122): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\file.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/file.py:134): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\file.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/file.py:143): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\line.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/line.py:7): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\line.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/line.py:10): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\line.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/line.py:23): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\line.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/line.py:28): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\line.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/line.py:33): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\line.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/line.py:37): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\line.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/line.py:48): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\scan.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scan.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\scan.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scan.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\scan.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scan.py:27): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\scan.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scan.py:32): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\scan.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scan.py:37): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\scan.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scan.py:41): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\scan.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scan.py:45): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\scan.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scan.py:49): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scope.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scope.py:15): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scope.py:26): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/scope.py:33): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/violation.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/violation.py:49): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/violation.py:54): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/violation.py:59): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/violation.py:64): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/violation.py:69): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/violation.py:74): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resources\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/violation.py:103): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

#### <span id="use-clear-function-parameters-violations">Use Clear Function Parameters: 59 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\parameter_info_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/parameter_info_builder.py:24): Function "add_param_detail" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:183): Function "_check_gerund_capability_noun" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:199): Function "_check_abstract_noun_suffix" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:241): Function "_create_capability_noun_violation" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\business_readable_test_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/business_readable_test_names_scanner.py:111): Function "_check_business_readable" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:119): Function "_check_method_name_matches_scenario" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\class_based_organization_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/class_based_organization_scanner.py:392): Function "_check_file_name_matches_sub_epic" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\clear_parameters_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/clear_parameters_scanner.py:20): Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:23): Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:253): Function "scan_cross_file" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:362): Function "_extract_code_snippet" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:419): Function "_create_violation_with_snippet" has 12 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\dependency_chaining_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/dependency_chaining_code_scanner.py:121): Function "_check_method_calls_for_instance_attrs" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\dependency_chaining_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/dependency_chaining_code_scanner.py:143): Function "_check_argument" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\domain_language_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_code_scanner.py:56): Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\domain_language_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_code_scanner.py:107): Function "_check_domain_language" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\domain_language_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/domain_language_code_scanner.py:136): Function "_check_function_domain_language" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1821): Function "scan_cross_file" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\function_size_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/function_size_scanner.py:40): Function "_check_function_size" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_precondition_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_precondition_scanner.py:44): Function "_check_given_is_functionality" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_state_not_actions_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_state_not_actions_scanner.py:69): Function "_check_given_is_action" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:142): Function "_check_test_method" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:332): Function "scan_cross_file" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:24): Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:76): Function "_check_variable_names" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\intention_revealing_names_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/intention_revealing_names_scanner.py:143): Function "_create_generic_name_violation" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\parameterized_tests_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/parameterized_tests_scanner.py:9): Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\primitive_vs_object_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/primitive_vs_object_scanner.py:167): Function "_create_primitive_violation" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:42): Function "_check_test_methods_call_production_code" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:376): Function "_has_production_code_calls" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\real_implementations_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/real_implementations_scanner.py:429): Function "_helper_calls_production_code" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:33): Function "scan_cross_file" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner.py:28): Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner.py:109): Function "scan_cross_file" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\scenarios_on_story_docs_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scenarios_on_story_docs_scanner.py:167): Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:88): Function "_create_violation_with_line_number" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:215): Function "_check_specification_matches" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\specification_match_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/specification_match_scanner.py:433): Function "_check_variable_matches" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\spine_optional_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/spine_optional_scanner.py:9): Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\spine_optional_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/spine_optional_scanner.py:103): Function "_check_all_stories_mandatory" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\story_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_scanner.py:10): Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\unnecessary_parameter_passing_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/unnecessary_parameter_passing_scanner.py:48): Function "_check_class" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\unnecessary_parameter_passing_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/unnecessary_parameter_passing_scanner.py:96): Function "_check_method_parameters" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\unnecessary_parameter_passing_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/unnecessary_parameter_passing_scanner.py:151): Function "_check_property_extraction" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\vertical_slice_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vertical_slice_scanner.py:22): Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\render\render_instruction_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_instruction_formatter.py:33): Function "_update_instructions_dict" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rule.py:113): Function "scan" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rule.py:146): Function "_execute_file_by_file_scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rule.py:158): Function "_execute_cross_file_scan" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:291): Function "_process_scanner_result" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:307): Function "_execute_scanner" has 9 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:327): Function "_process_rule" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:339): Function "validate" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:344): Function "_create_legacy_context" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validation_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_executor.py:86): Function "_process_scanner_status" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validation_scanner_status_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scanner_status_builder.py:38): Function "_categorize_rule_by_status" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validation_scanner_status_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scanner_status_builder.py:241): Function "_get_rule_status_display" has vague parameter name "info" - use descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validation_scanner_status_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scanner_status_builder.py:255): Function "_format_rule_scanner_info" has vague parameter name "info" - use descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resources\violation.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/violation.py:78): Function "create_from_rule_and_context" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

#### <span id="use-domain-language-violations">Use Domain Language: 3 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:241): Function "generate_parsers_for_story_bot" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\complexity_metrics.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/complexity_metrics.py:241): Function "calculate_lcom" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resources\block.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resources/block.py:113): Function "calculate_complexity" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

#### <span id="use-explicit-dependencies-violations">Use Explicit Dependencies: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:79): Global variable usage detected - dependencies should be explicit (passed as parameters)

#### <span id="use-natural-english-violations">Use Natural English: 14 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:385): Variable "start_line_0" uses technical notation. Use natural English instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:389): Variable "end_line_0" uses technical notation. Use natural English instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:392): Variable "end_line_0" uses technical notation. Use natural English instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:398): Variable "start_line_0" uses technical notation. Use natural English instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:408): Variable "start_line_0" uses technical notation. Use natural English instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:409): Variable "end_line_0" uses technical notation. Use natural English instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:392): Variable "start_line_0" uses technical notation. Use natural English instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:400): Variable "end_line_0" uses technical notation. Use natural English instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:402): Variable "end_line_0" uses technical notation. Use natural English instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:395): Variable "end_line_0" uses technical notation. Use natural English instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:402): Variable "start_line_0" uses technical notation. Use natural English instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/code_scanner.py:395): Variable "end_line_0" uses technical notation. Use natural English instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\spine_optional_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/spine_optional_scanner.py:89): Variable "is_optional" uses technical notation. Use natural English instead.
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\spine_optional_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/spine_optional_scanner.py:92): Variable "is_optional" uses technical notation. Use natural English instead.

## Validation Instructions

The following validation steps were performed:

1. **MANDATORY: Before validating any content, you MUST load and review the project's context files:**
2. 1. Load `{project_area}/docs/stories/clarification.json` - Contains key questions and evidence (generated file)
3. 2. Load `{project_area}/docs/stories/planning.json` - Contains assumptions and decisions (generated file)
4. 3. Load `{project_area}/docs/context/input.txt` (or similar) - Original input/source material if needed for validation (original context)
5. 
6. **CRITICAL: File locations:**
7. - **Generated files:** `{project_area}/docs/stories/clarification.json`, `{project_area}/docs/stories/planning.json`
8. - **Original input:** `{project_area}/docs/context/input.txt` and other original context files
9. 
10. These files contain critical requirements, decisions, and context that MUST be checked against during validation.
*... and 267 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\code-validation-report-2025-12-21_17-41-04.md`

