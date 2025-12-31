# 📝 proactively Validate knowledge against rules

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Build Knowledge](.)  
**Sequential Order:** 1
**Story Type:** user

## Story Description

proactively Validate knowledge against rules functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** BuildKnowledgeAction it's the initial pass of building the knowledge graphTHEN Build Knowledge Action invokes the Validate Rules action to understand if what is generated violates any rules

- **When** Validate Rules action is finsihed generateing the validation report
  **then** the BuildKnowledgeAction goes through all of the violations to determine if any corrective action needs to be taken
  **and** the system updates the knowledge graph based on the recommendations.

- **When** BuildKnowledgeAction Is finished making corrections.
  **then** BuildKnowledgeAction tells AI to notify the user of what corrections it made as part of presenting the fact that it's done building knowledge.

## Scenarios

### Scenario: Build knowledge forwards to validate action bot and receives enhanced instructions (happy_path)

**Steps:**
```gherkin
Given Agent is initialized with agent_name='test_story_bot'
And Project has finished generating knowledge graph
And Behavior is '{behavior_name}'
And Common rules directory exists at 'agile_bot/bots/test_story_bot/rules/'
And Behavior rules directory exists at 'agile_bot/bots/test_story_bot/behaviors/{behavior_number}_{behavior_name}/3_rules/'
And Action is 'build_knowledge'
And Knowledge graph exists at 'agile_bot/bots/test_story_bot/docs/stories/story-graph.json'
And Behavior has validation rules '{validation_rules}'
And Validation rules have code scanners '{code_scanners}'
And Code scanners are stubbed to return '{code_scanner_output}'
When Build knowledge action forwards to validate_action_bot with knowledge graph at 'agile_bot/bots/test_story_bot/docs/stories/story-graph.json'
Then Validate action bot runs stubbed code scanners '{code_scanners}' against knowledge graph
And Stubbed scanners return '{code_scanner_output}'
And Validation report is generated with '{code_scanner_output}'
And Enhanced instructions are returned to build_knowledge action
And Enhanced instructions contain '{enhanced_instructions}'
```

