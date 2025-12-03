# 📝 AI Chat Triggers MCP Tool

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../Invoke%20Bot%20Tool.md)

**Epic:** Invoke MCP Bot Server
**Feature:** Invoke Bot Tool

## Story Description

AI Chat recognizes trigger words from workspace rules and memory, then invokes the appropriate MCP bot tool instead of doing manual file operations.

## Acceptance Criteria

### Behavioral Criteria

- **WHEN** AI receives command with workflow trigger words (explore, shape, discover, arrange, validate)
  - **THEN** AI reads workspace rules and memory to identify matching MCP tool
  - **AND** AI invokes the appropriate MCP tool (e.g., `story_bot_exploration_gather_context`)

- **WHEN** AI is in ask mode and recognizes need for MCP tool
  - **THEN** AI informs user to switch to agent mode
  - **AND** AI explains that MCP tools are only available in agent mode

## Notes

This story describes the AI behavior AFTER awareness files exist. The generation of those files is handled in "Generate Cursor Awareness Files" story (in Generate Bot Server And Tools feature).

Problem being solved: AI heard "explore increment 3" and did manual file operations instead of invoking MCP tool.

---

## Source Material

**Inherited From**: Increment 2 exploration
- Primary source: Conversation about AI not recognizing MCP tool trigger words
- Bug fix session where AI used manual file operations instead of MCP tools
- Generated: 2025-12-03

