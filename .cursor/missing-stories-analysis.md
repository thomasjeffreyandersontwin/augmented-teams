# Missing Stories & Scenarios Analysis

## Overview
This document analyzes what functionality was IMPLEMENTED/FIXED during this conversation and identifies what is MISSING from the story graph documentation (stories, scenarios, tests).

---

## Bugs Fixed & Features Built in This Conversation

### 1. **Assumptions Always Editable Bug**
**What was fixed:**
- Assumptions textarea was rendering as read-only when it had values
- Fixed to always show editable textarea, pre-filled with saved values
- File: `instructions_view.js`

**Story Graph Status:**
- ✅ **Story exists**: "Display Strategy Instructions" mentions assumptions textarea
- ❌ **Bug scenario MISSING**: No scenario for "Assumptions become read-only after being saved"
- ❌ **Test MISSING**: No test for ensuring assumptions remain editable regardless of saved state

**Missing Scenario:**
```
Story: Display Strategy Instructions
Scenario: "Assumptions textarea remains editable after being saved"
- Given Bot is at shape.strategy
- And User has previously saved assumptions
- When Panel displays strategy instructions
- Then Assumptions textarea is displayed as editable input
- And Textarea is pre-filled with saved assumptions
- And User can edit and update assumptions
```

---

### 2. **Strategy Criteria Visible Across All Actions**
**What was fixed:**
- Strategy criteria (questions/options) and saved decisions were only visible in strategy action
- Fixed to load and display strategy data in ALL actions (clarify, build, validate, render)
- Files: `action.py` (_load_all_saved_guardrails), `clarify_action.py`

**Story Graph Status:**
- ✅ **Story exists**: "Display Strategy Instructions" (but only for strategy action)
- ✅ **Story exists**: "Display Clarify Instructions"  
- ❌ **Cross-action visibility scenario MISSING**: No scenario for strategy being visible in clarify action
- ❌ **Test MISSING**: No test for strategy criteria appearing in non-strategy actions

**Missing Story/Scenarios:**
```
Story: "Display All Guardrails Across All Actions"
Acceptance Criteria:
- WHEN User is on clarify action
- THEN System displays saved strategy decisions and criteria
- WHEN User is on build action
- THEN System displays saved strategy decisions and criteria
- WHEN User is on validate action
- THEN System displays saved strategy decisions and criteria

Scenario: "User views strategy guardrails in clarify action"
- Given Bot is at shape.clarify
- And User has previously made strategy decisions
- When Panel displays clarify instructions
- Then Panel displays Strategy section
- And Strategy section shows all decision criteria with selected options
- And Strategy section shows saved assumptions
- And Strategy data is read-only (not editable in clarify action)

Scenario: "User views clarify answers in strategy action"
- Given Bot is at shape.strategy
- And User has previously answered clarify questions
- When Panel displays strategy instructions
- Then Panel displays Clarify section
- And Clarify section shows answered questions
- And Clarify data is read-only (not editable in strategy action)
```

---

### 3. **Strategy Criteria Data Structure Fix**
**What was fixed:**
- `instructions_view.js` was trying to access `instructions.strategy_criteria` directly
- Fixed to access `instructions.strategy_criteria.criteria` (nested structure)
- File: `instructions_view.js`

**Story Graph Status:**
- ❌ **Bug scenario MISSING**: No scenario for incorrect data structure causing display issues
- ❌ **Test MISSING**: No test validating strategy_criteria data structure format

**Missing Test Scenario:**
```
Story: Display Strategy Instructions
Scenario: "Panel correctly extracts strategy criteria from nested structure"
- Given Strategy data has nested structure with criteria template
- And Structure is { strategy_criteria: { criteria: {...}, decisions_made: {...} } }
- When Panel renders strategy instructions
- Then Panel extracts criteria from nested path
- And All decision criteria are displayed with options
```

---

### 4. **Permanent Story-Graph and Story-Map Links**
**What was fixed:**
- story-graph.json and story-map.md links were not always visible
- Added permanent links that are always displayed regardless of scope state
- File: `scope_view.js`

**Story Graph Status:**
- ✅ **Story exists**: "Open Story Files"
- ❌ **"Always visible" requirement MISSING**: Story doesn't specify links should always be present
- ❌ **Test MISSING**: No test for links being visible when scope is empty or filtered

**Missing Scenario:**
```
Story: Open Story Files  
Scenario: "Story graph and story map links always visible"
- Given Panel displays scope section
- And Scope may be filtered or showing all stories
- When User views scope header
- Then story-graph.json link is always visible
- And story-map.md link is always visible
- And Links persist regardless of filter state
- And Links are positioned consistently in header
```

---

### 5. **Chat Submission via Python Submit Command**
**What was fixed:**
- Submit was trying to use `cursor.cmd --command` which opened new windows and didn't work
- Changed to delegate to Python `bot.submit()` command
- Matches legacy approach
- Files: `bot.py`, `bot_panel.js`

**Story Graph Status:**
- ✅ **Story exists**: "Submit Instructions To AI Agent"
- ❌ **Scenario MISSING**: No scenario for what happens when submit is clicked

**Missing Scenario:**
```
Story: Submit Instructions To AI Agent
Scenario: "User submits instructions to chat"
- Given Panel displays instructions
- When User clicks submit button
- Then System opens chat panel
- And System sends instructions to chat
- And Chat displays instructions
```

---

### 6. **Complete Scope Included in Submitted Instructions**
**What was fixed:**
- Submitted instructions were missing scope entirely
- Then only included high-level scope type, not full story graph tree
- Fixed to include complete scope with `scope.results` (full story graph hierarchy)
- Files: `markdown_instructions.py`, `action.py`

**Story Graph Status:**
- ✅ **Story exists**: "Submit Instructions To AI Agent"
- ❌ **Scope inclusion requirement MISSING**: No acceptance criteria requiring scope in submitted instructions
- ❌ **Full tree requirement MISSING**: No scenario specifying complete story graph tree must be included
- ❌ **Test MISSING**: No test validating scope.results is serialized

**Missing Acceptance Criteria & Scenarios:**
```
Story: Submit Instructions To AI Agent
Acceptance Criteria:
- WHEN User clicks submit button
- THEN Submitted instructions include scope section
- AND Scope section includes scope type (story/files/all)
- AND Scope section includes scope filter values
- AND Scope section includes complete story graph tree when scope is story-based
- AND Scope section uses MarkdownInstructions adapter for serialization

Scenario: "Submitted instructions include complete scope with story tree"
- Given Bot has scope set to story "Open Panel"
- And Scope.results contains full story graph hierarchy
- When User clicks submit in panel
- Then Submitted instructions contain Scope section at top
- And Scope section shows "Story Scope: Open Panel"
- And Scope section shows complete epic/sub-epic/story hierarchy
- And Story tree is serialized using AdapterFactory with markdown adapter

Scenario: "Submitted instructions include all guardrails"
- Given Bot is at shape.build
- And User has answered clarify questions
- And User has made strategy decisions
- When User clicks submit in panel
- Then Submitted instructions include Clarify section with answers
- And Submitted instructions include Strategy section with decisions and assumptions
- And All saved guardrails are visible in submitted markdown
```

---

### 8. **MarkdownInstructions Adapter for Display Content**
**What was fixed:**
- `action.py` had duplicate manual formatting logic in `_build_display_content`
- Refactored to use existing MarkdownInstructions adapter for serialization
- Avoids duplicate logic and ensures consistency
- File: `action.py`

**Story Graph Status:**
- ✅ **Adapter class exists**: MarkdownInstructionsAdapter is documented
- ❌ **Refactoring story MISSING**: No story for consolidating duplicate formatting logic
- ❌ **Architecture scenario MISSING**: No scenario specifying actions should use adapters for display

**Missing Story:**
```
Story: "Use MarkdownInstructions Adapter for Consistency"
Acceptance Criteria:
- WHEN Action builds display content
- THEN Action uses MarkdownInstructions adapter
- AND Action does not duplicate formatting logic
- AND Display content matches submitted content format

Scenario: "Action delegates display formatting to adapter"
- Given Action needs to build display_content for instructions
- When _build_display_content is called
- Then Method creates MarkdownInstructions adapter instance
- And Method calls adapter.serialize()
- And Serialized output is used for display_content
- And No manual formatting logic is duplicated
```

---

### 8. **Scope Serialization in MarkdownInstructions**
**What was fixed:**
- MarkdownInstructions adapter did not serialize scope
- Added scope serialization logic to include scope type, values, and results (story tree)
- Uses AdapterFactory to serialize scope.results
- File: `markdown_instructions.py`

**Story Graph Status:**
- ✅ **Adapter exists**: MarkdownInstructionsAdapter is documented
- ❌ **Scope serialization MISSING**: No scenario for adapter including scope in output
- ❌ **Test MISSING**: No test for MarkdownInstructionsAdapter.serialize() including scope section

**Missing Scenario:**
```
Story: "Serialize Instructions to Markdown" (or add to MarkdownInstructionsAdapter domain concept)
Scenario: "Markdown adapter includes scope section"
- Given Instructions object has scope with type 'story' and value 'Open Panel'
- And Scope.results contains story graph tree
- When MarkdownInstructions.serialize() is called
- Then Output contains "## Scope" section at top
- And Scope section shows scope type and values
- And Scope section includes serialized scope.results using AdapterFactory
- And Scope section is followed by separator line
```

---

### 9. **Show All Scope Functionality**
**What was fixed:**
- Added "Show All" button in scope section to call `scope showall` command
- Files: `bot_panel.js`, `scope_view.js`

**Story Graph Status:**
- ✅ **Backend functionality exists**: "Clear scope with show_all parameter" scenario exists (domain story)
- ❌ **Panel UI story MISSING**: No panel story for "Show All" button
- ❌ **Test MISSING**: No panel test for clicking show all button

**Missing Story:**
```
Story: "Show All Scope Through Panel"
Sequential Order: Insert after "Filter Story Scope"
Acceptance Criteria:
- WHEN User has filtered scope
- THEN System displays "Show All" button
- WHEN User clicks "Show All" button
- THEN System calls 'scope showall' command via CLI
- AND System clears scope filter
- AND Panel displays complete unfiltered story hierarchy

Scenario: "User clicks show all to clear filter"
- Given Panel displays filtered scope showing only "Open Panel" story
- And Show All button is visible
- When User clicks Show All button
- Then Panel calls 'scope showall' via CLI
- And Scope filter is cleared
- And Panel displays all epics, sub-epics, and stories
- And Filter input is empty

Scenario: "Show all button is visible when scope is filtered"
- Given Panel has no scope filter applied
- When User views scope section
- Then Show All button is not visible
- When User applies filter to scope
- Then Show All button becomes visible
```

---

### 10. **Bot Switching Backend (bots property, active_bot setter)**
**What was fixed:**
- Added `bots` property to Bot class to return list of available bots
- Added `active_bot` property and setter for switching between bots
- Discovers bots by scanning parent directory for bot_config.json files
- File: `bot.py`

**Story Graph Status:**
- ✅ **Story exists**: "Switch Bot" (in Panel epic)
- ❌ **Backend implementation MISSING**: No domain story for Bot class bot switching capability
- ❌ **Discovery logic MISSING**: No scenario for scanning directory to find bots
- ❌ **Test MISSING**: No domain test for Bot.bots property or Bot.active_bot setter

**Missing Domain Story:**
```
Epic: "Build Agile Bots" or "Invoke Bot Directly"
Story: "Discover And Switch Between Bots"
Sequential Order: TBD
Test Class: TestDiscoverAndSwitchBots

Acceptance Criteria:
- WHEN Bot.bots property is accessed
- THEN System scans parent bots directory for subdirectories with bot_config.json
- AND System returns sorted list of bot names
- WHEN Bot.active_bot setter is called with valid bot name
- THEN System validates bot exists
- AND System creates new Bot instance for target bot
- AND System updates class-level registry
- WHEN Bot.active_bot is accessed
- THEN System returns currently active bot instance

Scenario: "Bot discovers available bots in parent directory"
Test Method: test_bot_discovers_available_bots_in_parent_directory
- Given Parent bots directory contains story_bot and crc_bot subdirectories
- And Each subdirectory has bot_config.json
- When Bot.bots property is accessed
- Then Property returns ['crc_bot', 'story_bot'] (sorted)

Scenario: "Bot switches to different bot"
Test Method: test_bot_switches_to_different_bot
- Given Current bot is story_bot
- And crc_bot exists in parent directory
- When Bot.active_bot = 'crc_bot'
- Then New Bot instance is created for crc_bot
- And Bot._active_bot_instance is updated
- And Bot._active_bot_name is 'crc_bot'

Scenario: "Bot switch fails for non-existent bot"
Test Method: test_bot_switch_fails_for_nonexistent_bot
- Given Current bot is story_bot
- When Bot.active_bot = 'fake_bot'
- Then ValueError is raised
- And Error message lists available bots
```

---

## Summary

### Stories That Need To Be Added: 4
1. **Display All Guardrails Across All Actions** - Cross-action guardrail visibility
2. **Use MarkdownInstructions Adapter for Consistency** - Refactoring/architecture story
3. **Show All Scope Through Panel** - Panel UI for scope showall command
4. **Discover And Switch Between Bots** - Domain story for bot switching backend

### Scenarios That Need To Be Added: 13
1. Assumptions textarea remains editable after being saved
2. User views strategy guardrails in clarify action
3. User views clarify answers in strategy action  
4. Panel correctly extracts strategy criteria from nested structure
5. Story graph and story map links always visible
6. User submits instructions to chat
7. Submitted instructions include complete scope with story tree
8. Submitted instructions include all guardrails
9. Action delegates display formatting to adapter
10. Markdown adapter includes scope section
11. User clicks show all to clear filter
12. Show all button visibility changes based on filter state
13. Bot discovers available bots in parent directory
14. Bot switches to different bot
15. Bot switch fails for non-existent bot

### Tests That Need To Be Added: 15
1. Test assumptions textarea is editable regardless of saved state
2. Test strategy criteria visible in clarify action
3. Test clarify answers visible in strategy action
4. Test strategy_criteria data structure extraction
5. Test story links always visible
6. Test user can submit instructions to chat
7. Test submitted instructions include scope.results
8. Test submitted instructions include all guardrails
9. Test _build_display_content uses MarkdownInstructions adapter
10. Test MarkdownInstructions.serialize includes scope
11. Test show all button calls scope showall
12. Test show all button visibility
13. Test Bot.bots property returns sorted list
14. Test Bot.active_bot setter switches bots
15. Test Bot.active_bot setter validates bot exists

---

## Acceptance Criteria That Need Enhancement

### Story: Submit Instructions To AI Agent
**Current:** Basic acceptance criteria for sending to chat
**Missing:**
- Scope inclusion requirement
- Guardrails inclusion requirement

### Story: Display Strategy Instructions  
**Current:** Shows strategy for strategy action only
**Missing:**
- Strategy visible in other actions
- Assumptions always editable requirement

### Story: Filter Story Scope
**Current:** Filter and clear functionality
**Missing:**
- Show All button functionality
- Always-visible links requirement

---

## Files That Need Test Coverage

### Python Backend
1. `agile_bot/src/bot/bot.py`
   - `Bot.bots` property
   - `Bot.active_bot` property and setter

2. `agile_bot/src/actions/action.py`
   - `_build_display_content` using MarkdownInstructions
   - `_load_all_saved_guardrails` loading strategy for all actions

3. `agile_bot/src/instructions/markdown_instructions.py`
   - Scope serialization in `serialize()` method

### JavaScript Frontend
4. `agile_bot/src/panel/bot_panel.js`
   - `sendToChat` delegating to bot.submit()
   - `showAllScope` message handler

5. `agile_bot/src/panel/instructions_view.js`
   - Assumptions always rendered as editable textarea
   - Strategy criteria extraction from nested structure

6. `agile_bot/src/panel/scope_view.js`
   - Permanent story-graph.json and story-map.md links
   - Show all button functionality

---

## Conclusion

While the functionality has been **successfully implemented and is working**, the **documentation is significantly behind**. This creates risk for:
- Future developers not understanding expected behavior
- Regression bugs when behavior isn't documented
- Difficulty maintaining consistency across the codebase
- Missing test coverage for critical bugs that were fixed

**Recommendation:** Prioritize adding the missing scenarios and tests to the story graph, especially for the cross-action guardrail visibility and keyboard automation behavior, as these were significant architectural decisions.
