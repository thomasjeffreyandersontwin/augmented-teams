# 📝 Provide File Scope Context For Instructions

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Execute Workflow Operations (Mock)
**User:** REPLSession
**Sequential Order:** 9
**Story Type:** system

## Story Description

Provide File Scope Context For Instructions functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user runs instructions command with file scope parameter
  **then** REPLSession gathers file scope parameters from command
  **and** REPLSession parses file paths and validates it against File Scope schema
  **and** REPLSession creates a new File Scope from the parameters
  **and** REPLSession adds the new File Scope to the Action Context
  **and** passes the Action Context with Scope to the instruction operation

- **When** validation fails
  **then** REPLSession displays file scope validation errors to user

## Scenarios

### Scenario: File scope filters workspace files and passes matching files to action (happy_path)

**Steps:**
```gherkin
Given workspace contains directory src/repl_cli/ with files: repl_session.py, repl_commands.py, repl_help.py
And workspace contains directory src/bot/ with files: bot.py, behavior.py, action.py
And REPLSession is active with Bot at behavior "code" action "validate"
And user enters command: "instructions --scope '{"type": "files", "value": ["<include_path>"]}'"
When REPLSession processes the command with scope
Then Bot scans workspace for files matching "<include_path>"
And Bot returns <matched_count> matching files: <matched_files>
And Bot passes filtered files to validate action
And Action receives ActionContext with <matched_count> files in scope
```

**Examples:**
| include_path | matched_count | matched_files |
| --- | --- | --- |
| src/repl_cli/ | 3 | repl_session.py, repl_commands.py, repl_help.py |
| src/bot/ | 3 | bot.py, behavior.py, action.py |
| src/bot/bot.py | 1 | bot.py |


### Scenario: File scope with exclude pattern filters out matching files (happy_path)

**Steps:**
```gherkin
Given workspace contains directory src/ with files: bot.py, action.py, utils.py, config.json
And workspace contains directory src/__pycache__/ with files: bot.cpython-311.pyc, action.cpython-311.pyc
And REPLSession is active with Bot at behavior "code" action "validate"
And user enters command: "instructions --scope '{"type": "files", "value": ["src/"], "exclude": ["<exclude_pattern>"]}'"
When REPLSession processes the command with scope
Then Bot scans workspace for files in src/
And Bot excludes files matching "<exclude_pattern>"
And Bot returns <matched_count> matching files: <matched_files>
```

**Examples:**
| exclude_pattern | matched_count | matched_files |
| --- | --- | --- |
| __pycache__ | 4 | bot.py, action.py, utils.py, config.json |
| *.pyc | 4 | bot.py, action.py, utils.py, config.json |
| *.json | 3 | bot.py, action.py, utils.py |
| utils.py | 3 | bot.py, action.py, config.json |


### Scenario: File scope with non-existent path returns empty result (happy_path)

**Steps:**
```gherkin
Given workspace contains directory src/repl_cli/ with files: repl_session.py
And REPLSession is active with Bot at behavior "code" action "validate"
And user enters command: "instructions --scope '{"type": "files", "value": ["src/nonexistent/"]}'"
When REPLSession processes the command with scope
Then Bot scans workspace for files matching src/nonexistent/
And Bot returns 0 matching files
And Bot displays warning: "No files found matching scope: src/nonexistent/"
```


### Scenario: REPLSession displays validation error for invalid file scope (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And user enters command: "instructions --scope '{"type": "files", "value": []}'"
When REPLSession processes the command
Then REPLSession validates empty value array against File Scope schema
And validation fails with error: "File scope requires at least one file path"
And REPLSession displays file scope validation errors to user
```

