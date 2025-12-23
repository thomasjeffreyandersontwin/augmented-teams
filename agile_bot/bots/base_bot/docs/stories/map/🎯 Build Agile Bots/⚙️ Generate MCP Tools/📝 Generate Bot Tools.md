# 📝 Generate Bot Tools

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Build Agile Bots
**Feature:** Generate MCP Tools
**User:** MCP Server Generator
**Sequential Order:** 0.5
**Story Type:** user

## Story Description

MCP Server Generator generates Bot Tools so that AI assistants can invoke bot behaviors through MCP protocol

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Generator processes Bot Config
  **then** Generator creates 1 bot tool instance

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given MCP Server Generator is initialized
And Base bot directory exists at agile_bot/bots/base_bot
And Bot directory structure follows bot_architecture_pattern
```

## Scenarios

### Scenario Outline: Generator creates bot tool for various bot configurations

**Note:** This scenario outline parameterizes across different bot configurations to validate that the generator creates exactly 1 bot tool regardless of the number of behaviors or their configuration.

**Steps:**
```gherkin
Given Bot configuration file specifies bot_name="<bot_name>"
And Bot configuration file specifies behaviors=<behaviors>
And Bot has been initialized from configuration file
When Generator processes Bot Config
Then Generator creates 1 bot tool instance
And Bot tool is named "<expected_tool_name>"
And Bot tool includes <behavior_count> behavior references
```

**Examples:**
| bot_name | behaviors | expected_tool_name | behavior_count |
|----------|-----------|-------------------|----------------|
| story_bot | ["shape", "prioritization", "discovery"] | story_bot | 3 |
| domain_bot | ["event_storming"] | domain_bot | 1 |
| test_bot | ["shape", "prioritization", "discovery", "exploration", "scenarios", "tests", "code"] | test_bot | 7 |
| minimal_bot | ["single_behavior"] | minimal_bot | 1 |
| base_bot | [] | base_bot | 0 |

### Scenario Outline: Generator creates behavior tools for each behavior in configuration

**Note:** This scenario outline verifies that each behavior specified in bot config results in a corresponding behavior tool being generated with proper MCP tool registration.

**Steps:**
```gherkin
Given Bot configuration file specifies bot_name="<bot_name>"
And Bot configuration file specifies behaviors=<behaviors>
And Behavior "<behavior>" has trigger_patterns=<trigger_patterns>
And Bot has been initialized from configuration file
When Generator processes Bot Config
Then Generator creates behavior tool named "<expected_behavior_tool>"
And Behavior tool accepts action parameter
And Behavior tool accepts parameters dict
And Behavior tool description includes trigger patterns: <trigger_patterns_display>
```

**Examples:**
| bot_name | behaviors | behavior | trigger_patterns | expected_behavior_tool | trigger_patterns_display |
|----------|-----------|----------|------------------|------------------------|--------------------------|
| story_bot | ["shape"] | shape | ["shape domain", "create story map", "build map"] | shape_tool | "shape domain, create story map, build map" |
| story_bot | ["prioritization"] | prioritization | ["prioritize stories", "create increments", "plan releases"] | prioritization_tool | "prioritize stories, create increments, plan releases" |
| story_bot | ["discovery"] | discovery | ["discover requirements", "elaborate stories", "refine acceptance criteria"] | discovery_tool | "discover requirements, elaborate stories, refine acceptance criteria" |
| story_bot | ["scenarios"] | scenarios | ["write scenarios", "specify behavior", "create examples"] | scenarios_tool | "write scenarios, specify behavior, create examples" |
| domain_bot | ["event_storming"] | event_storming | ["map domain events", "identify aggregates", "define bounded contexts"] | event_storming_tool | "map domain events, identify aggregates, define bounded contexts" |

### Scenario Outline: Generator creates tool with behavior actions routing

**Note:** This scenario validates that behavior tools properly route to action execution based on action parameter presence.

**Steps:**
```gherkin
Given Bot configuration file specifies bot_name="<bot_name>"
And Bot configuration file specifies behaviors=["<behavior>"]
And Behavior "<behavior>" has actions=<actions>
And Bot has been initialized from configuration file
When Generator processes Bot Config
Then Generator creates behavior tool for "<behavior>"
And Behavior tool routes to action when action parameter is provided
And Behavior tool routes to current action when action parameter is None
And Behavior tool returns status='completed' with behavior, action, and data fields
```

**Examples:**
| bot_name | behavior | actions |
|----------|----------|---------|
| story_bot | shape | ["clarify", "strategy", "build", "validate", "render"] |
| story_bot | discovery | ["clarify", "strategy", "build", "validate", "render"] |
| test_bot | test_behavior | ["clarify", "strategy", "build"] |

### Scenario: Generator handles bot configuration with no behaviors

**Steps:**
```gherkin
Given Bot configuration file specifies bot_name="empty_bot"
And Bot configuration file specifies behaviors=[]
And Bot has been initialized from configuration file
When Generator processes Bot Config
Then Generator creates 1 bot tool instance
And Bot tool includes 0 behavior references
And No behavior tools are created
```

### Scenario: Generator handles bot configuration file with working directory path

**Steps:**
```gherkin
Given Bot configuration file specifies bot_name="workspace_bot"
And Bot configuration file specifies behaviors=["shape"]
And Bot configuration file specifies mcp.env.WORKING_AREA="C:\dev\augmented-teams"
And Bot has been initialized from configuration file
When Generator processes Bot Config
Then Generator creates 1 bot tool instance
And Bot tool configuration includes working directory path
And Working directory path is accessible from bot tool context
```

### Scenario Outline: Generator handles invalid bot configurations

**Note:** This scenario outline covers error cases where bot configuration is malformed or missing required fields.

**Steps:**
```gherkin
Given Bot configuration file has <config_issue>
When Generator attempts to process Bot Config
Then Generator reports error: "<expected_error>"
And No bot tools are created
```

**Examples:**
| config_issue | expected_error |
|--------------|----------------|
| missing_name_field | "Bot configuration must specify 'name' field" |
| name_is_empty_string | "Bot name cannot be empty" |
| behaviors_is_not_array | "Bot configuration 'behaviors' must be an array" |
| behaviors_contains_non_string | "All behavior names must be strings" |
| file_does_not_exist | "Bot configuration file not found" |
| invalid_json_syntax | "Bot configuration file contains invalid JSON" |

### Scenario Outline: Generator creates tools with proper MCP FastMCP registration

**Note:** This validates that generated tools follow MCP protocol requirements with proper decorator syntax and async function signatures.

**Steps:**
```gherkin
Given Bot configuration file specifies bot_name="<bot_name>"
And Bot configuration file specifies behaviors=<behaviors>
And Bot has been initialized from configuration file
When Generator processes Bot Config
Then Generated MCP server file includes @mcp_server.tool decorator for each behavior
And Each behavior tool function signature is "async def <behavior>_tool(action: str=None, parameters: dict=None)"
And Each behavior tool returns dict with keys: status, behavior, action, data
And MCP server file imports are: "from pathlib import Path, sys, os, json, datetime, logging"
And MCP server file creates bot instance with Bot(bot_name, bot_directory, config_path)
```

**Examples:**
| bot_name | behaviors |
|----------|-----------|
| story_bot | ["shape", "discovery"] |
| domain_bot | ["event_storming"] |
| test_bot | ["test_behavior"] |

---

## Source Material

Generated from `story-graph.json` and `bot_architecture_pattern.md`

**Domain Model References:**
- Bot configuration structure: `bot_config.json` format with name and behaviors array
- Behavior structure: trigger_words, description, actions
- MCP tool generation: `MCPCodeVisitor`, `MCPCodeGenerator`
- Bot initialization: `Bot` class from `bot.py`

