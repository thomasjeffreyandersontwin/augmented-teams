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

## Notes
ature).

Files generated:
1. `.cursor/rules/mcp-tool-awareness.mdc` - trigger patterns
2. Memory via `update_memory` - persistent awareness

---

## Source Material

**Inherited From**: Increment 2 exploration
- Primary source: Conversation about AI not recognizing MCP tool trigger words
- Bug fix session where manual operations were used instead of MCP tools
- Generated: 2025-12-03

