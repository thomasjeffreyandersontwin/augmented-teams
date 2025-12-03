# Scenarios: Generate Cursor Awareness Files

**Story:** Generate Cursor Awareness Files  
**Epic:** Build Agile Bots  
**Feature:** Generate Bot Server And Tools

---

## Scenario 1: Generator creates bot-specific workspace rules file with trigger patterns sectioned by behavior

**Given** MCP Server Generator is initialized with bot_name='test_bot' and behaviors=['shape', 'discovery']  
**When** Generator runs `generate_awareness_files()` method  
**Then** Generator creates file at `.cursor/rules/mcp-test-bot-awareness.mdc` with bot-specific filename  
**And** Filename includes bot name with hyphens: mcp-<bot_name>-awareness.mdc  
**And** File includes bot name in content header  
**And** File sections trigger words by behavior (not flat list)  
**And** Each behavior section includes: behavior name, trigger words for that behavior, tool pattern  
**And** Shape section includes shape trigger words only  
**And** Discovery section includes discovery trigger words only  
**And** Each bot creates separate awareness file for independent management  

---

## Scenario 2: Rules file includes explicit bot-specific instructions with error handling

**Given** Bot has instructions.json with goal and behavior descriptions  
**When** Generator creates `.cursor/rules/mcp-<bot-name>-awareness.mdc` file  
**Then** Critical rule states: "When user is trying to [bot goal], ALWAYS check for and use MCP story_bot tools FIRST" with specific bot name  
**And** Each behavior section follows format: "When user is trying to: [behavior description] as indicated by **Trigger words:** [list], Then check for story_bot_shape_<action>"  
**And** Shape section states: "When user is trying to: Create initial story map outline as indicated by **Trigger words:** shape story, create story map, Then check for story_bot_shape_<action>"  
**And** File includes error handling section: "If registered tool is broken or returns error, do NOT attempt workaround"  
**And** Error handling instructs: "Inform user of exact error details and ask if should attempt repair or proceed manually"  

---

## Scenario 3: Generator creates memory for tool awareness

**Given** MCP Server Generator is initialized  
**When** Generator runs `generate_awareness_files()` method  
**Then** Generator calls `update_memory` API with action='create'  
**And** Memory title is "Always Check MCP Tools First for Workflow Commands"  
**And** Memory content includes trigger word patterns for all bot types  
**And** Memory content includes pattern: "hear trigger word → check if in agent mode → check available tools → invoke tool"  
**And** Memory persists successfully with returned memory ID  

---

## Scenario 4: Rules file maps trigger patterns to tool naming conventions

**Given** MCP Server Generator creates awareness file  
**When** File is written to `.cursor/rules/mcp-tool-awareness.mdc`  
**Then** File includes tool pattern format: `story_bot_<behavior>_<action>`  
**And** File includes example: "explore increment 3" → Check for `story_bot_exploration_*` tools  
**And** File includes example: "shape new feature" → Check for `story_bot_shape_*` tools  
**And** Pattern examples exist for all bot types (story, domain, bdd, code_agent)  

---

## Scenario 5: Memory includes ask mode vs agent mode handling

**Given** Generator creates tool awareness memory  
**When** Memory is persisted via update_memory API  
**Then** Memory content includes: "If in ask mode when MCP tools needed, inform user that MCP tools only available in agent mode"  
**And** Memory explains AI should check mode before attempting tool invocation  

---

## Scenario 6: Generator handles file write errors gracefully

**Given** MCP Server Generator attempts to create awareness files  
**When** `.cursor/rules/` directory does not exist  
**Then** Generator creates directory before writing file  
**And** File write succeeds  

**Given** `.cursor/rules/` directory is write-protected  
**When** Generator attempts to write file  
**Then** Generator raises clear error message indicating permission issue  
**And** Error includes path attempted: `.cursor/rules/mcp-tool-awareness.mdc`  

---

## Source Material

**Based on:** Generate Cursor Awareness Files story  
**Acceptance Criteria:** Transformed into executable BDD scenarios  
**Generated:** 2025-12-03

