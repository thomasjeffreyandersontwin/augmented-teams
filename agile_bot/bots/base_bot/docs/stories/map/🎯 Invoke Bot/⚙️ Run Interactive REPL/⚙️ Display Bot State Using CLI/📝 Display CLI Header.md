# 📝 Display CLI Header

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L261)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Display Bot State Using CLI](.)  
**Sequential Order:** 1
**Story Type:** system

## Story Description

Display CLI Header functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** CLI displays status
  **then** CLI shows header with bot name
  **and** workspace path

- **When** displaying header in terminal mode
  **then** CLI uses plain text formatting

- **When** displaying header in piped mode
  **then** CLI uses markdown formatting

- **When** header is displayed
  **then** CLI includes separator line after header

## Scenarios

### Scenario: CLI displays CLI STATUS section header when status command is run (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L264)

**Steps:**
```gherkin
Given: CLI is initialized
When: user enters 'status' command
Then: CLI displays CLI STATUS section header
AND: CLI shows section separator line
AND: CLI shows '*** CLI STATUS section ***' header text
AND: CLI shows description text explaining what the section contains
AND: CLI shows warning text: 'You MUST DISPLAY this entire section in your response to the user exactly as you see it'
AND: CLI shows subsection separator
AND: CLI shows section separator after header
```


### Scenario: CLI displays bot name with robot emoji in header (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L294)

**Steps:**
```gherkin
Given CLI is initialized with story_bot
And CLI is in piped mode
When CLI renders the dashboard header
Then output contains heading with robot emoji and bot name
And output shows Bot: story_bot
```


### Scenario: CLI displays bot path in code block (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L325)

**Steps:**
```gherkin
Given CLI is initialized with story_bot at path C:/dev/augmented-teams/agile_bot/bots/story_bot
When CLI renders the dashboard header
Then output contains '**Bot Path:**' label
And output shows code block with three backticks
And output shows the full bot directory path: 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
And output closes code block with three backticks
```


### Scenario: CLI displays workspace name and path (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L355)

**Steps:**
```gherkin
Given CLI is initialized with workspace base_bot
And workspace path is C:/dev/augmented-teams/agile_bot/bots/base_bot
When CLI renders the dashboard header
Then output contains 'Ã°Å¸â€œâ€š **Workspace:** base_bot' with folder emoji
And output shows code block with three backticks
And output shows full workspace path: 'C:\dev\augmented-teams\agile_bot\bots\base_bot'
And output closes code block with three backticks
```


### Scenario: CLI displays path change instructions (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L388)

**Steps:**
```gherkin
Given CLI is in piped mode
When CLI renders the dashboard header
Then output contains 'To change path:' label
And output shows code block with three backticks
And output shows path command example: 'path demo/mob_minion              # Change to specific project'
And output shows path command example: 'path ../another_bot               # Change to relative path'
And output closes code block with three backticks
```


### Scenario: CLI applies separator after header section (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L418)

**Steps:**
```gherkin
Given CLI is in piped mode
When CLI renders the dashboard header
Then output ends with horizontal separator line (subsection separator)
```


### Scenario: CLI displays headless mode section when configured (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L447)

**Steps:**
```gherkin
Given: Headless mode is configured with API key
When: CLI renders status display
Then: CLI displays 'Headless Mode:' label
AND: CLI shows 'Status: Available (configured)'
AND: CLI shows API key prefix
AND: CLI shows Usage section with headless command format
AND: CLI shows Examples section with headless command examples
AND: CLI applies subsection separator after headless section
```


### Scenario: CLI displays active headless session when running (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L476)

**Steps:**
```gherkin
Given: Headless mode is configured
AND: Active headless session is running
When: CLI renders status display
Then: CLI displays 'Active Session:' section
AND: CLI shows Session ID
AND: CLI shows session Status (running)
AND: CLI shows Log file path
```


### Scenario: CLI displays headless mode unavailable when not configured (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L512)

**Steps:**
```gherkin
Given: Headless mode is not configured
When: CLI renders status display
Then: CLI displays 'Headless Mode:' label
AND: CLI shows 'Status: Unavailable (not configured)'
AND: CLI shows configuration instructions
```

