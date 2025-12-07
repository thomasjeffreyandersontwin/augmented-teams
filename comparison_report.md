# Comparison: story-graph.json vs map folder
## Only showing: Missing, Different Place, or Different Name

## Epic Name Difference
- **JSON:** "Invoke MCP Bot Server"
- **Map:** "Invoke Bot"   cdhange name and hierarch in json to match map
- ⚠️ **Different name**

---

## Epic: Build Agile Bots

### Sub-Epic: Generate MCP Tools

**In map but NOT in JSON (main epics section):**
- ❌ Create Bot Scaffolding delete 
- ❌ Generate Cursor Awareness Files   keep

*Note: These may exist in JSON under different increments/epics*

### Sub-Epic: Init Project

**Missing in map (in JSON but not in map):**
- ❌ Shares Context and Project Location delete
- ❌ Drops Behavior Folder in Chat w/ relevant Bot Config delete
- ❌ Intercepts Tool Call With Project Check  delete
- ❌ Move to Project delete


- ❌ Stores Activity for Initialize Project Action  keep



**Different name:**
- **JSON:** (no equivalent)
- **Map:** Context Folder Management
- ⚠️ *May be related to "Store Context Files" but has different name* i deleted in map 

### Sub-Epic: Perform Behavior Action

**Missing in map (in JSON but not in map):**
- ❌ Inject Behavior Action Instructions  I SEE THIS IN MAP KEEP
- ❌ Workflow Determines Next Action From Current Action RENAME TO 📝 Workflow Determines Next Action From Current Action LIKE IN MAP

---

## Epic: Execute Behavior Actions

### Sub-Epic: Gather Context

**Missing in map (in JSON but not in map):**
- ❌ Injects Gather Context Instructions
- ❌ Inject Questions and Evidence
- ❌ Answers Questions and Evidence
- ❌ Load + inject Questions and Evidence
- ❌ Track Activity for Gather Context Action
- ❌ Proceeds to follow planning
- ❌ Correct, Feedback, Proceed
- ❌ Saves Answers and Evidencein Context
- ❌ Pause based on context
- ❌ Pauses
- ❌ Submit Answers and Evidence to Tools for Saving
- ❌ Answers Questions and Evidence from Context
- ❌ Presents Answers and Evidence to User
KILL ALL

### Sub-Epic: Decide Planning Criteria

**Missing in map (in JSON but not in map):**
- ❌ Track Activity for Planning Action
- ❌ Make Assumptions and Decisions from Context
- ❌ Make Assumptions and Decisions
- ❌ Correct, Feedback, Proceed
- ❌ Submit Final Assumptions and Decisions to Tools for Saving
- ❌ Inject Decision Criteria and Assumptions Loading Instructions
- ❌ Read Answers and Evidence from Context
- ❌ Load + Inject Answers + Evidence
- ❌ Read Injected Answers and Evidence

KILL ALL

### Sub-Epic: Render Output

**Missing in map (in JSON but not in map):**
- ❌ Track Activity for Render Output Action
ADD TO MAP 
### Sub-Epic: Validate Knowledge & Content Against Rules

**Missing in map (in JSON but not in map):**
- ❌ Complete Validate Rules Action
- ❌ FInd Content in Context
- ❌ Find Rules in Context and validate against Rules
- ❌ Validate Content vs Injected Diagnostics and Rules
- ❌ Validate Content Using Injected Diagnostics + Rules
- ❌ Pause
- ❌ Read report and make changes
- ❌ Save Content through Context
- ❌ Submit Content to Tool for Saving
- ❌ Save Content
- ❌ Load + Inject Diagnostics Results, Knowledge, Content Instructions
- ❌ Proceed to Correct-Bot trough context
KILL

---

## Summary

### Missing Stories (in JSON but NOT in map):
- **Init Project:** 5 stories
- **Perform Behavior Action:** 2 stories
- **Gather Context:** 13 stories
- **Decide Planning Criteria:** 9 stories
- **Render Output:** 1 story
- **Validate Rules:** 12 stories

### Stories in map but NOT in JSON (main epics):
- **Generate MCP Tools:** Create Bot Scaffolding, Generate Cursor Awareness Files
  - *May exist in JSON under different increments*

### Different Names:
- **Epic:** "Invoke MCP Bot Server" (JSON) vs "Invoke Bot" (map)
- **Init Project:** "Context Folder Management" (map) - no exact match in JSON


ASLO AL LSTOREIS IN SUB EPICS nUILD kNOWLKEDGE IN MAP MISSING IN JSON PLS ADD
