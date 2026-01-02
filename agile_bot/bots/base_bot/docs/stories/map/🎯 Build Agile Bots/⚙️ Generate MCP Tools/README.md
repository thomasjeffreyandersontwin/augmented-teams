# ⚙️ Generate MCP Tools

**Navigation:** [📋 Story Map](../../../story-map.drawio)

**Path:** [🎯 Build Agile Bots](..)  
**Type:** sub-epic
**Test File:** test_generate_mcp_tools.py
**Test Location:** agile_bot/bots/base_bot/test/test_generate_mcp_tools.py

## Description

Generate MCP (Model Context Protocol) tools for bot behaviors, including bot tools, behavior tools, behavior-action tools, server generation, deployment, and restart functionality.

## Stories

This sub-epic contains the following stories:

1. **📝 Generate Bot Tools** - TestGenerateBotTools
2. **📝 Generate Behavior Tools** - TestGenerateBehaviorTools
3. **📝 Generate MCP Bot Server** - TestGenerateMCPBotServer
4. **📝 Generate Behavior Action Tools** - (Covered by TestGenerateBehaviorTools and TestGenerateMCPBotServer)
5. **📝 Deploy MCP BOT Server** - TestDeployMCPBotServer
6. **📝 Restart MCP Server To Load Code Changes** - TestRestartMCPServerToLoadCodeChanges

## Test Coverage

All stories in this sub-epic are tested in `test_generate_mcp_tools.py` with dedicated test classes for each major story.

**Total Test Classes:** 5  
**Total Test Methods:** 9  
**Coverage:** Complete for all implemented functionality
