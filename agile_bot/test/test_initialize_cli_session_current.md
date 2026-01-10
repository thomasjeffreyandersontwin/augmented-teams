# Test Initialize CLI Session Current

**Status:** Superseded

This test file was originally planned to port `test_initialize_repl_session_current.py`, which tested the "CURRENT" (legacy) REPL implementation behavior before refactoring.

## Resolution

The initialization tests for the new CLI architecture have already been ported in:
- **`agile_bot/test/test_initialize_cli_session.py`**

That file contains all the relevant initialization tests for the new CLISession:
- Launch CLI in Interactive Mode
- Launch CLI in Pipe Mode  
- Display Piped Mode Instructions for AI Agents
- Detect and Configure TTY/Non-TTY Input for CLI
- Load and Display Workspace Context in CLI
- Display CLI Header
- Display Headless Mode Status in CLI

## Original File

The original REPL tests can be found at:
- `agile_bot/test/test_initialize_cli_session.py`

These tests were specific to the old REPL implementation and are not needed for the new CLI architecture.
