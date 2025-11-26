# 📝 Create, Select, or Remove Mob from Dialog

**Navigation:** [📋 Story Map](../../mob-rule-story-map.md) | [⚙️ Feature Overview](../⚙️ Create Mobs from Canvas Tokens)

**Epic:** Group Minions into Mobs
**Feature:** Create Mobs from Canvas Tokens

## Story Description

GM opens Mob dialog box and creates, selects, or removes a mob, then updates mob membership

## Scenarios

### Background
Given GM has access to Foundry VTT canvas
And canvas has tokens available

### Scenario: GM opens dialog and creates new mob
When GM presses hotkey to initiate minion selection mode
Then a dialog box appears with a plus button to create a new mob
And if mobs already exist, they appear in a list showing only their names
When GM clicks the plus button
Then a new mob is created with a default mob name field (which can be edited) and empty list of members
When GM edits the mob name in the dialog box and saves changes
Then the updated mob name is stored by the Mob Manager
And the new mob becomes the active mob for editing

### Scenario: GM selects existing mob from dialog
Given one or more mobs have been created
When GM presses hotkey to initiate minion selection mode
Then a dialog box appears with a plus button to create a new mob
And each existing mob appears in the list showing only its name
When GM clicks on an existing mob in the dialog box
Then the dialog displays the member tokens of the selected mob
And the selected mob becomes the active mob for editing, selecting, and unselecting members
And Mob Manager selects all member tokens of the selected mob on the canvas
And Canvas System displays all member tokens as selected
When GM closes the dialog box
Then no mob is active for editing

### Scenario: GM deletes an existing mob
Given one or more mobs have been created
When GM presses hotkey to initiate minion selection mode
And GM selects an existing mob from the dialog list
Then the dialog displays the member tokens of the selected mob
When GM clicks delete button for the selected mob
Then Mob Manager removes the mob
And all member tokens are removed from the mob
And the mob is removed from the dialog list
And if the mob leader was in combat tracker, it is removed from combat tracker

### Scenario: Dialog shows no mobs when none exist
When GM presses hotkey to initiate minion selection mode
And no mobs have been created
Then a dialog box appears with a plus button to create a new mob
And no mobs appear in the list

## Notes

- Mob dialog provides interface for managing mobs (create, select, delete)
- Active mob is the one currently being edited
- Closing dialog deactivates the current mob

---

## Source Material

**Inherited From**: Story Map
- See story map "Source Material" section for primary source
- Acceptance criteria from Exploration phase: Technical Proof of Concept and Drill-Down Stories - Increment Exploration
