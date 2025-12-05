# 📝 Restart MCP Server

**Navigation:** [📋 Story Map](../../story-map.txt) | [Story Graph](../../story-graph.json)

**Epic:** Invoke MCP Bot Server  
**Feature:** Invoke Bot Tool

**User:** Developer  
**Sequential Order:** 6  
**Story Type:** system

## Story Description

Developer invokes Restart MCP Server tool so that code changes and configuration updates are loaded without manual process management or cache clearing.

## Acceptance Criteria

### AC 1: Terminate All Python MCP Processes

- **WHEN** developer invokes `{bot_name}_restart_server` tool
- **THEN** system identifies all running Python MCP server processes
- **AND** all identified processes are terminated gracefully (SIGTERM)
- **AND** system waits up to 5 seconds for graceful shutdown
- **AND** remaining processes are force killed (SIGKILL)
- **AND** system verifies all processes terminated successfully
- **Technical Constraint:** Must handle multiple orphaned processes from failed restarts

### AC 2: Clear Python Bytecode Caches

- **WHEN** process termination completes
- **THEN** system recursively finds all `__pycache__` directories in `agile_bot/` path
- **AND** all `.pyc` files are deleted from found directories
- **AND** all `.pyo` files are deleted from found directories
- **AND** all `__pycache__` directories are removed
- **AND** Python will generate fresh bytecode on server restart
- **Technical Constraint:** Cross-platform path handling using `pathlib`

### AC 3: Restart Server with Fresh State

- **WHEN** bytecode cache clearing completes
- **THEN** MCP server starts in new Python subprocess
- **AND** server reloads all bot configurations from disk
- **AND** server preloads updated bot instances with new code
- **AND** server registers all tools with MCP protocol
- **AND** system waits for successful server initialization (max 10 seconds)
- **AND** AI Chat reconnects to restarted server automatically

### AC 4: Return Restart Status

- **WHEN** server restart completes successfully
- **THEN** tool returns status object with:
  - `status`: "restarted" or "started" (if no previous processes)
  - `previous_pids`: list of terminated process IDs
  - `new_pid`: process ID of new server
  - `cache_cleared`: true/false
  - `behaviors_loaded`: list of behavior names loaded

### AC 5: Handle Edge Cases

- **WHEN** no MCP processes are running
- **THEN** tool still clears bytecode cache
- **AND** tool starts server fresh
- **AND** status indicates "started" not "restarted"

- **WHEN** restart fails (port conflict, missing file, etc.)
- **THEN** tool returns error with specific message
- **AND** tool does NOT leave system in broken state
- **AND** response includes troubleshooting guidance

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given developer is working on bot code or configurations
And Python MCP server is deployed and running
And developer has made changes requiring server reload
```

## Scenarios

### Scenario: Restart server to load code changes

**Steps:**
```gherkin
Given MCP server process with PID 12345 is running
And developer modified file 'agile_bot/bots/test_bot/src/bot/bot.py'
And Python bytecode cache exists at 'agile_bot/bots/test_bot/src/bot/__pycache__/'
When developer invokes 'test_bot_restart_server' tool with parameters: {}
Then system finds process 12345 running 'mcp_server.py'
And system sends SIGTERM to process 12345
And process 12345 terminates within 3 seconds
And system deletes all files in '__pycache__' recursively under 'agile_bot/'
And system removes all '__pycache__' directories
And system starts new server process with PID 67890
And server loads 'test_bot' configuration from disk
And server preloads updated Bot instance with modified code
And system verifies server responds within 10 seconds
And tool returns: {"status": "restarted", "previous_pids": [12345], "new_pid": 67890, "cache_cleared": true}
```

### Scenario: Kill multiple orphaned processes before restart

**Steps:**
```gherkin
Given MCP server processes with PIDs [12345, 12346, 12347] are running
And processes are orphaned from failed previous restarts
When developer invokes 'test_bot_restart_server' tool
Then system identifies all three processes
And system terminates all processes: [12345, 12346, 12347]
And system verifies all three processes terminated
And system clears bytecode cache
And system starts single new server process with PID 67890
And tool returns: {"status": "restarted", "previous_pids": [12345, 12346, 12347], "new_pid": 67890}
```

### Scenario: Start server when none running

**Steps:**
```gherkin
Given no MCP server processes are running
And bytecode cache exists from previous session
When developer invokes 'test_bot_restart_server' tool
Then system detects no running processes (skips termination)
And system still clears bytecode cache
And system starts server process with PID 67890
And tool returns: {"status": "started", "previous_pids": [], "new_pid": 67890, "cache_cleared": true}
```

### Scenario: Restart picks up new behavior

**Steps:**
```gherkin
Given server is running with behaviors: ['shape', 'discovery', 'exploration']
And developer added new behavior folder 'agile_bot/bots/test_bot/behaviors/scenarios/'
And current server does not know about 'scenarios' behavior
When developer invokes 'test_bot_restart_server' tool
Then system terminates current server process
And system clears bytecode cache
And system starts new server process
And server reloads bot configuration from 'agile_bot/bots/test_bot/config/bot_config.json'
And server loads behaviors: ['shape', 'discovery', 'exploration', 'scenarios']
And server registers new tools: ['test_bot_scenarios_*']
And tool returns: {"behaviors_loaded": ["shape", "discovery", "exploration", "scenarios"], "new_pid": 67890}
```

### Scenario: Handle graceful shutdown timeout

**Steps:**
```gherkin
Given MCP server process 12345 is running and unresponsive
When developer invokes 'test_bot_restart_server' tool
Then system sends SIGTERM to process 12345
And system waits 5 seconds for graceful shutdown
And process 12345 does NOT terminate after 5 seconds
And system sends SIGKILL to process 12345
And process 12345 terminates immediately
And restart continues normally
And tool returns successful restart status
```

### Scenario: Handle restart failure

**Steps:**
```gherkin
Given MCP server process 12345 is running
When developer invokes 'test_bot_restart_server' tool
And process termination succeeds
And bytecode cache clearing succeeds
And server restart fails with error: "Port 5000 already in use"
Then tool returns error response: {"error": "Server restart failed", "message": "Port 5000 already in use", "troubleshooting": "Check for other processes using port 5000"}
And previous server remains stopped (not in broken state)
And bytecode cache remains cleared
```

## Implementation Notes

- Tool name pattern: `{bot_name}_restart_server`
- Use `psutil` library for cross-platform process management
- Search for Python processes containing "mcp_server" or bot-specific script name
- Clear cache before starting to ensure clean state
- Optional `force` parameter for immediate SIGKILL (default: false)
- Return structured JSON with PIDs, status, and loaded behaviors

## Out of Scope

- Auto-restart on file changes (file watching)
- Zero-downtime rolling restarts
- Restarting AI Chat client
- Managing non-Python MCP servers
- Preserving in-memory workflow state (state persists to disk)

---

## Source Material

**Primary Source**: Backlog item "auto refresh MCP server cache on update of code"  
**Phase**: Specification - New feature for developer experience  
**Date Generated**: 2025-12-04  
**Context**: Streamline development workflow by automating server restart and cache clearing
