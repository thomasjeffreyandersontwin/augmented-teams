# 📝 Display Active Scope in CLI Status

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L226)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Display Bot State Using CLI](.)  
**Sequential Order:** 4
**Story Type:** system

## Story Description

Display Active Scope in CLI Status functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user views status with active scope
  **then** CLI displays active scope section

- **When** no scope is active
  **then** CLI displays no active scope filters message

- **When** multiple scope filters are active
  **then** CLI displays all active filters

- **When** scope is cleared
  **then** CLI updates status to show no active scope

## Scenarios

### Scenario: CLI displays all scope when no filter is set (happy_path)

**Steps:**
```gherkin
Given: CLI is at shape.build.instructions
And: no scope filters are active
When: user enters 'status'
Then: CLI displays scope section with scope icon
AND: CLI shows 'Current Scope: all (entire project)'
AND: CLI shows scope change instructions with three options
AND: CLI shows 'scope all' command example
AND: CLI shows 'scope "Story Name"' command example
AND: CLI shows 'scope "file:C:/path/to/**/*.py"' command example
```


### Scenario: CLI displays story scope with story names listed (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L229)

**Steps:**
```gherkin
Given: CLI is at shape.build.instructions
And: active scope filter is story scope with stories 'Generate Bot Tools' and 'Generate BOT CLI code'
When: user enters 'status'
Then: CLI displays scope section with scope icon and 'Scope' header
AND: CLI shows 'Filter:' label followed by story names
AND: CLI lists each story with story emoji and story name
AND: CLI shows warning text: 'Work ONLY on this scope'
AND: CLI shows warning text: 'DO NOT work on all files or the entire story graph'
AND: CLI shows warning text: 'Focus EXCLUSIVELY on the items listed above'
AND: CLI shows scope change instructions
```


### Scenario: CLI displays file scope with file paths (happy_path)

**Steps:**
```gherkin
Given: CLI is at code.validate.instructions
And: active scope filter is file scope with path 'agile_bot/bots/base_bot/src/repl_cli/**/*.py'
When: user enters 'status'
Then: CLI displays scope section with scope icon and 'Scope' header
AND: CLI shows 'Filter:' label followed by file path pattern
AND: CLI shows '(no files found)' if no files match
AND: CLI shows warning text: 'Work ONLY on this scope'
AND: CLI shows warning text: 'DO NOT work on all files or the entire story graph'
AND: CLI shows warning text: 'Focus EXCLUSIVELY on the items listed above'
AND: CLI shows scope change instructions
```

