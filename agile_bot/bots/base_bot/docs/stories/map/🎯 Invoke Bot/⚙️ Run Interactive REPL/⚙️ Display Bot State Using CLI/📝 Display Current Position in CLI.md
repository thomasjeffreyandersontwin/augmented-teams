# 📝 Display Current Position in CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L104)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Display Bot State Using CLI](.)  
**Sequential Order:** 3
**Story Type:** system

## Story Description

Display Current Position in CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user views status
  **then** CLI displays current behavior, action, and operation

- **When** user navigates to different action
  **then** CLI updates current position display

- **When** displaying position
  **then** CLI shows behavior.action.operation format

- **When** position is at first action
  **then** CLI indicates start of workflow

## Scenarios

### Scenario: CLI displays progress section with current position (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L107)

**Steps:**
```gherkin
Given: CLI is at shape.clarify.instructions
When: user enters 'status'
Then: CLI displays Progress section header with position icon
AND: CLI shows 'Current Position:' label
AND: CLI shows current position in code block format: 'shape.clarify.instructions'
AND: CLI displays hierarchical status tree with behaviors and actions
AND: CLI shows current behavior marked with current marker (âž¤)
AND: CLI shows current action marked with current marker (âž¤)
AND: CLI shows current operation marked with current marker (âž¤)
AND: CLI shows completed actions with completed marker (â˜‘)
AND: CLI shows pending actions with pending marker (â˜)
AND: CLI shows behavior descriptions for current behavior and action
AND: CLI shows operations (instructions, submit, confirm) under current action
AND: CLI shows 'Run:' section with command examples
AND: CLI shows 'Args:' section with parameter examples
AND: CLI applies subsection separator after progress section
```


### Scenario: Current position updates after navigation (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.clarify.instructions
WHEN: user navigates to discovery behavior
AND: user views status
THEN: REPLSession updates behavior action state
AND: CLI updates current position display to show 'discovery' behavior
AND: CLI updates progress tree to highlight discovery behavior as current
```


### Scenario: CLI displays Progress section with current position (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L137)

**Steps:**
```gherkin
Given: CLI is at exploration.validate.instructions
When: CLI renders status display
Then: CLI displays '## ðŸ“ **Progress**' section header
AND: CLI shows '**Current Position:**' label
AND: CLI shows current position in code block: 'exploration.validate.instructions'
AND: CLI displays hierarchical status tree with behaviors and actions
```


### Scenario: CLI displays hierarchical status tree with progress indicators (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L166)

**Steps:**
```gherkin
Given: CLI is at exploration.validate.instructions
When: CLI renders hierarchical status
Then: CLI displays behaviors with status markers (â˜‘ completed, âž¤ current, â˜ pending)
AND: CLI displays current behavior 'exploration' with âž¤ marker
AND: CLI displays completed behaviors (shape, prioritization, discovery) with â˜‘ marker
AND: CLI displays pending behaviors (scenarios, tests, code) with â˜ marker
AND: CLI displays actions under current behavior with proper indentation
AND: CLI displays operations (instructions, confirm) under current action
AND: CLI shows current operation 'instructions' with âž¤ marker
```


### Scenario: CLI displays Run instructions and Args sections (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L196)

**Steps:**
```gherkin
Given: CLI is at exploration.validate.instructions
When: CLI renders hierarchical status
Then: CLI displays 'Run:' section
AND: CLI shows command examples: 'echo 'behavior.action' | python repl_main.py'
AND: CLI shows '**Args:**' section
AND: CLI shows scope parameter examples
AND: CLI shows headless parameter example
AND: CLI shows action-specific parameters (e.g., validate-specific: --skip-cross-file, --max-cross-file-comparisons, --all-files, --background)
```

