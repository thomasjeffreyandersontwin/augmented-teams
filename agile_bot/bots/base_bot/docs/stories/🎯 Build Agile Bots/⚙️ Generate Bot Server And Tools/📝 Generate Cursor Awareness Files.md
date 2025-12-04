# 📝 Generate Cursor Awareness Files

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../Generate%20Bot%20Server%20And%20Tools.md)

**Epic:** Build Agile Bots
**Feature:** Generate Bot Server And Tools

## Story Description

MCP Generator creates workspace rules file and memory to make AI aware of MCP tool trigger patterns.

## Acceptance Criteria

### Behavioral Criteria

- **WHEN** MCP Generator runs for a bot
  - **THEN** Generator creates `.cursor/rules/mcp-<bot-name>-awareness.mdc` file with bot-specific name
  - **AND** File includes bot name in filename (e.g., `mcp-story-bot-awareness.mdc`, `mcp-bdd-bot-awareness.mdc`)
  - **AND** File includes trigger word patterns from that specific bot's behaviors
  - **AND** Each bot has separate awareness file for independent management

- **WHEN** workspace rules file is generated
  - **THEN** Rules include bot's goal and description from instructions.json
  - **AND** Critical rule states: "When user is trying to [bot goal], ALWAYS check for and use MCP [bot_name] tools FIRST"
  - **AND** Trigger words are sectioned by behavior (not flat list)
  - **AND** Each behavior section includes: "When user is trying to [behavior description] as indicated by **Trigger words:** [list], Then check for [bot_name]_[behavior]_<action> tool"
  - **AND** Rules include error handling: "If registered tool is broken or returns error, do NOT attempt workaround. Inform user of exact error details and ask if should attempt repair or proceed manually"

- **WHEN** Generator creates memory about tool awareness
  - **THEN** Memory created via update_memory API
  - **AND** Memory persists pattern for AI to check MCP tools when hearing workflow trigger words
  - **AND** Memory includes handling for ask mode vs agent mode

## Scenarios

### Scenario: Generator creates bot-specific workspace rules file with trigger patterns sectioned by behavior

**Steps:**
```gherkin
Given MCP Server Generator is initialized with bot_name='test_bot' and behaviors=['shape', 'discovery']
When Generator runs generate_awareness_files() method
Then Generator creates file at .cursor/rules/mcp-test-bot-awareness.mdc with bot-specific filename
And Filename includes bot name with hyphens: mcp-<bot_name>-awareness.mdc
And File includes bot name in content header
And File sections trigger words by behavior (not flat list)
And Each behavior section includes: behavior name, trigger words for that behavior, tool pattern
And Shape section includes shape trigger words only
And Discovery section includes discovery trigger words only
And Each bot creates separate awareness file for independent management
```

### Scenario: Rules file includes explicit bot-specific instructions with error handling

**Steps:**
```gherkin
Given Bot has instructions.json with goal and behavior descriptions
When Generator creates .cursor/rules/mcp-<bot-name>-awareness.mdc file
Then Critical rule states: "When user is trying to [bot goal], ALWAYS check for and use MCP story_bot tools FIRST" with specific bot name
And Each behavior section follows format: "When user is trying to: [behavior description] as indicated by **Trigger words:** [list], Then check for story_bot_shape_<action>"
And Shape section states: "When user is trying to: Create initial story map outline as indicated by **Trigger words:** shape story, create story map, Then check for story_bot_shape_<action>"
And File includes error handling section: "If registered tool is broken or returns error, do NOT attempt workaround"
And Error handling instructs: "Inform user of exact error details and ask if should attempt repair or proceed manually"
```

### Scenario: Generator creates memory for tool awareness

**Steps:**
```gherkin
Given MCP Server Generator is initialized
When Generator runs generate_awareness_files() method
Then Generator calls update_memory API with action='create'
And Memory title is "Always Check MCP Tools First for Workflow Commands"
And Memory content includes trigger word patterns for all bot types
And Memory content includes pattern: "hear trigger word → check if in agent mode → check available tools → invoke tool"
And Memory persists successfully with returned memory ID
```

### Scenario: Rules file maps trigger patterns to tool naming conventions

**Steps:**
```gherkin
Given MCP Server Generator creates awareness file
When File is written to .cursor/rules/mcp-tool-awareness.mdc
Then File includes tool pattern format: story_bot_<behavior>_<action>
And File includes example: "explore increment 3" → Check for story_bot_exploration_* tools
And File includes example: "shape new feature" → Check for story_bot_shape_* tools
And Pattern examples exist for all bot types (story, domain, bdd, code_agent)
```

### Scenario: Memory includes ask mode vs agent mode handling

**Steps:**
```gherkin
Given Generator creates tool awareness memory
When Memory is persisted via update_memory API
Then Memory content includes: "If in ask mode when MCP tools needed, inform user that MCP tools only available in agent mode"
And Memory explains AI should check mode before attempting tool invocation
```

### Scenario: Generator handles file write errors gracefully

**Steps:**
```gherkin
Given MCP Server Generator attempts to create awareness files
When .cursor/rules/ directory does not exist
Then Generator creates directory before writing file
And File write succeeds
```

**Steps:**
```gherkin
Given .cursor/rules/ directory is write-protected
When Generator attempts to write file
Then Generator raises clear error message indicating permission issue
And Error includes path attempted: .cursor/rules/mcp-tool-awareness.mdc
```

## Generated Artifacts

### Workspace Rules File
**Generated by:** MCP Server Generator
**Location:** `.cursor/rules/mcp-<bot-name>-awareness.mdc`
**Content:**
- Bot-specific trigger word patterns by behavior
- Tool naming conventions
- Error handling instructions

### Awareness Memory
**Generated by:** MCP Server Generator
**Created via:** update_memory API
**Content:**
- Pattern for checking MCP tools when hearing trigger words
- Ask mode vs agent mode handling

## Notes

Files generated:
1. `.cursor/rules/mcp-tool-awareness.mdc` - trigger patterns
2. Memory via `update_memory` - persistent awareness

---

## Source Material

**Inherited From**: Increment 2 exploration
- Primary source: Conversation about AI not recognizing MCP tool trigger words
- Bug fix session where manual operations were used instead of MCP tools
- Generated: 2025-12-03


