# 📝 Launch CLI in Interactive Mode

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_initialize_repl_session.py#L102)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Initialize REPL Session](.)  
**Sequential Order:** 1
**Story Type:** user

## Story Description

Launch CLI in Interactive Mode functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: CLI launches in interactive mode (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_initialize_repl_session.py#L105)

**Steps:**
```gherkin
GIVEN: REPLSession is configured for interactive mode
WHEN: user runs 'python repl_main.py --stdio'
THEN: REPLSession creates CLIBot wrapping Bot
```


### Scenario: CLI loads existing behavior action state on launch (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_initialize_repl_session.py#L137)

**Steps:**
```gherkin
GIVEN: REPLSession is configured for interactive mode
AND: behavior action state file exists
WHEN: user runs 'python repl_main.py --stdio'
THEN: REPLSession loads stored behavior action state
```

