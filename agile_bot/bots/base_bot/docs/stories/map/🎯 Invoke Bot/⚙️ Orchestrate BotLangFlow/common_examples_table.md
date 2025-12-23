# Common Examples for BotLangFlow Testing

This document contains test data for all behavior-action combinations in story_bot, following proper Given/When/Then structure with exact domain variable names.

## Test Data Structure

Each behavior-action combination includes:
- **Given**: Initial state with exact domain variables (agent_name, workspace_root, behavior_name, action_name, etc.)
- **When**: Action execution with exact method calls
- **Then**: Expected outcomes with exact assertions
- **Example Variables**: Concrete test data values

## Scenario Outline: Execute behavior-action through BotLangFlow

**Given** Agent is initialized with agent_name="<agent_name>"  
**And** workspace_root="<workspace_root>"  
**And** behavior_name="<behavior_name>"  
**And** action_name="<action_name>"  
**And** BotLangFlow is created with one BotLangActionNode  
**And** BotLangState is initialized with behavior="<behavior_name>" and action="<action_name>"  

**When** BotLangFlow executes the single node  

**Then** BotLangActionNode is created successfully  
**And** get_instructions() returns instructions containing "<expected_instruction_snippet>"  
**And** action.execute() completes  
**And** BotLangState is updated with action results  

### Examples:

| agent_name | workspace_root | behavior_name | action_name | expected_instruction_snippet |
|------------|----------------|---------------|-------------|------------------------------|
| test_story_bot | C:/test/workspace | shape | clarify | Gather context for both story mapping and domain modeling |
| test_story_bot | C:/test/workspace | shape | strategy | Include domain modeling planning criteria alongside story mapping criteria |
| test_story_bot | C:/test/workspace | shape | build | shape: build story map structure AND domain model |
| test_story_bot | C:/test/workspace | shape | validate | shape: validate hierarchy, story structure, AND domain model |
| test_story_bot | C:/test/workspace | shape | render | shape: render story map documents AND domain model documents |
| test_story_bot | C:/test/workspace | shape | rules | Display digested rules for this behavior as AI context |
| test_story_bot | C:/test/workspace | prioritization | clarify | Gather context for prioritization |
| test_story_bot | C:/test/workspace | prioritization | strategy | Determine prioritization approach |
| test_story_bot | C:/test/workspace | prioritization | build | Build increment prioritization |
| test_story_bot | C:/test/workspace | prioritization | validate | Validate prioritization structure |
| test_story_bot | C:/test/workspace | prioritization | render | Render prioritization documents |
| test_story_bot | C:/test/workspace | prioritization | rules | Display digested rules for this behavior as AI context |
| test_story_bot | C:/test/workspace | discovery | clarify | Gather context for story discovery |
| test_story_bot | C:/test/workspace | discovery | strategy | Determine discovery approach |
| test_story_bot | C:/test/workspace | discovery | build | Build detailed story flows |
| test_story_bot | C:/test/workspace | discovery | validate | Validate story flows and domain rules |
| test_story_bot | C:/test/workspace | discovery | render | Render discovery documents |
| test_story_bot | C:/test/workspace | discovery | rules | Display digested rules for this behavior as AI context |
| test_story_bot | C:/test/workspace | exploration | clarify | Gather context for acceptance criteria |
| test_story_bot | C:/test/workspace | exploration | strategy | Determine exploration approach |
| test_story_bot | C:/test/workspace | exploration | build | Build acceptance criteria |
| test_story_bot | C:/test/workspace | exploration | validate | Validate acceptance criteria |
| test_story_bot | C:/test/workspace | exploration | render | Render exploration documents |
| test_story_bot | C:/test/workspace | exploration | rules | Display digested rules for this behavior as AI context |
| test_story_bot | C:/test/workspace | scenarios | clarify | Gather context for scenario specification |
| test_story_bot | C:/test/workspace | scenarios | strategy | Determine scenario approach |
| test_story_bot | C:/test/workspace | scenarios | build | specification_scenarios: build scenarios AND refine domain model based on scenario details |
| test_story_bot | C:/test/workspace | scenarios | validate | specification_scenarios: validate scenario structure AND domain model refinements |
| test_story_bot | C:/test/workspace | scenarios | render | specification_scenarios: render story documents with scenarios |
| test_story_bot | C:/test/workspace | scenarios | rules | Display digested rules for this behavior as AI context |
| test_story_bot | C:/test/workspace | tests | clarify | Gather context for test generation |
| test_story_bot | C:/test/workspace | tests | strategy | Determine test approach |
| test_story_bot | C:/test/workspace | tests | build | Build test code from scenarios |
| test_story_bot | C:/test/workspace | tests | validate | Validate test code |
| test_story_bot | C:/test/workspace | tests | render | Render test files |
| test_story_bot | C:/test/workspace | tests | rules | Display digested rules for this behavior as AI context |
| test_story_bot | C:/test/workspace | code | clarify | Gather context for code review |
| test_story_bot | C:/test/workspace | code | strategy | Determine code review approach |
| test_story_bot | C:/test/workspace | code | build | Analyze code against stories |
| test_story_bot | C:/test/workspace | code | validate | Validate code quality |
| test_story_bot | C:/test/workspace | code | render | Render code review reports |
| test_story_bot | C:/test/workspace | code | rules | Display digested rules for this behavior as AI context |

## Notes

- All variable names follow domain terminology from story_bot
- agent_name, workspace_root, behavior_name, action_name are exact domain variables
- expected_instruction_snippet is the key text that MUST appear in get_instructions() output
- This scenario outline can be used to create parameterized tests using @pytest.mark.parametrize
- Tests should use exact variable names from this table (rule: use_exact_variable_names)
- Test methods should match scenario names (rule: match_specification_scenarios)
