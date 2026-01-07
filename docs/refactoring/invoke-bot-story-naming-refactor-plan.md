# Invoke Bot Story Naming Refactoring Plan

**Date Created:** 2025-01-06  
**Epic:** 🎯 Invoke Bot  
**Status:** Planning  
**Estimated Effort:** Large (3-5 days)

---

## 🎯 TARGET STATE

### Goals
1. **Consistency:** All three invocation methods (Direct, Panel, REPL) use identical terminology for parallel functionality
2. **Clarity:** User-centric, descriptive story names that clearly indicate what is being tested
3. **Simplicity:** Eliminate duplication - generic stories appear once, sub-epics contain only unique functionality
4. **Maintainability:** Flatter feature hierarchy, clear separation between stories and scenarios

### Success Criteria
- ✅ Feature structure aligned: Direct (6 features), Panel (5 features), REPL (6 features)
- ✅ 98%+ naming consistency across all three invocation methods
- ✅ 0% story duplication across behavior action sub-epics (currently 80%)
- ✅ All tests pass after refactoring
- ✅ story-graph.json validates correctly
- ✅ Git history preserved for all renamed files

### Scope
**IN SCOPE:**
- 3 sub-epic renames (Perform Behavior Action → Invoke Bot Directly, Run Interactive REPL → Invoke Bot Through REPL)
- 47+ story renames across Direct, Panel, and REPL
- Reorganize "Invoke Bot Directly" from 7 flat stories → 6 feature groups (33 stories)
- Consolidate ~110+ duplicate stories from 5 behavior action sub-epics → ~20 generic stories
- 10+ test file renames
- 20+ test class renames
- Update story-graph.json with all changes

**OUT OF SCOPE:**
- Changing actual test implementation (only renaming)
- Modifying behavior action logic
- Adding new functionality
- Changing sub-epic structure for Gather Context, Decide Planning, Build Knowledge, Render Output, Validate Rules

---

## 📊 CURRENT STATE & REQUIRED CHANGES

### Change Category 1: Sub-Epic Renames

| Current Name | New Name | Reason |
|-------------|----------|--------|
| Perform Behavior Action | Invoke Bot Directly | Aligns with "Invoke Bot Through Panel/REPL" naming pattern |
| Run Interactive REPL | Invoke Bot Through REPL | Matches pattern, removes redundant "Interactive" |

### Change Category 2: Reorganize "Invoke Bot Directly" (MAJOR)

**CURRENT:** 7 flat stories in "Perform Behavior Action" sub-epic:
```
1. Execute End-to-End Workflow (test: test_perform_behavior_action.py)
2. Execute Behavior Action (test: test_perform_behavior_action.py)
3. Insert Context Into Instructions (test: test_perform_behavior_action.py)
4. Inject Next Behavior Reminder (test: test_perform_behavior_action.py)
5. Confirm Current Action (test: test_perform_behavior_action.py)
6. Determine Action Order From State (test: test_invoke_behavior_in_action_order.py)
7. Inject Status Update Breadcrumbs Into Instructions (test: test_perform_behavior_action.py)
```

**TARGET:** 6 feature groups (33 stories) in "Invoke Bot Directly" sub-epic:
```
1. Navigate And Execute Behaviors (3 stories)
   - Navigate To Behavior Action And Execute
   - Navigate Sequentially
   - Execute End-to-End Workflow

2. Manage Scope (5 stories)
   - Set Story Scope
   - Set File Scope
   - Filter Knowledge Graph By Scope
   - Pass Scope Parameters To Actions
   - Clear Scope

3. Generate Action Instructions (6 stories)
   - Load Base Action Configuration
   - Load And Merge Behavior-Specific Instructions
   - Load Guardrails From Behavior Folder
   - Inject Guardrails Into Instructions
   - Inject Context Into Instructions (SCENARIOS: Inject Next Behavior Reminder, Inject Status Breadcrumbs)
   - Get Action Instructions

4. View Action-Specific Instructions (8 stories)
   - View Base Instructions
   - View Clarify Instructions
   - View Strategy Instructions
   - View Build Instructions
   - View Validate Instructions
   - View Render Instructions
   - View Instructions In Raw Format
   - Submit Instructions To AI Agent

5. Track Workflow State (6 stories)
   - Save Workflow State
   - Load Workflow State
   - Determine Resume Point After Interruption
   - Confirm Current Action
   - Inject Next Action Instructions
   - Transition To Next Action

6. Track Activity (3 stories)
   - Track Action Start
   - Track Action Completion
   - Record Activity Metrics And Paths
```

**TEST FILE CHANGES:**
- Rename: `test_perform_behavior_action.py` → `test_invoke_bot_directly.py`
- Rename: `test_invoke_behavior_in_action_order.py` → `test_navigate_sequentially.py`
- Create new test files for extracted generic stories (or consolidate into test_invoke_bot_directly.py)

### Change Category 3: Consolidate Duplicate Stories Across Behavior Action Sub-Epics (MAJOR)

**PROBLEM:** 5 behavior action sub-epics each contain ~30-40 stories, with 80% duplication:
- Gather Context (Clarify)
- Decide Planning Criteria (Strategy)
- Build Knowledge
- Render Output
- Validate Knowledge & Content Against Rules

**DUPLICATE STORIES (appear 4-5x each):**
- Track Activity for [X] Action (5x)
- Proceed To [Next Action] (4x)
- Load Base Action Config (5x)
- Initialize Action (5x - REMOVE, not needed)
- Access Actions (5x - REMOVE, not needed)
- Load Guardrails (5x)
- Inject [X] Into Instructions (5x with slight variations)

**SOLUTION:** Move generic stories to "Invoke Bot Directly", keep only unique stories in each sub-epic:

| Duplicate Story Pattern | Target Location | Sub-Epics to Remove From |
|------------------------|-----------------|-------------------------|
| Track Activity for [X] Action → Track Action Start/Completion | Track Activity feature | All 5 sub-epics |
| Proceed To [Next Action] → Inject Next Action Instructions, Transition To Next Action | Track Workflow State feature | All 5 sub-epics |
| Load Base Action Config → Load Base Action Configuration | Generate Action Instructions feature | All 5 sub-epics |
| Load Guardrails → Load Guardrails From Behavior Folder | Generate Action Instructions feature | All 5 sub-epics |
| Initialize Action | REMOVE - not needed as standalone story | All 5 sub-epics |
| Access Actions | REMOVE - not needed as standalone story | All 5 sub-epics |

**KEEP IN EACH SUB-EPIC (UNIQUE ONLY):**

**Gather Context:**
- Inject Guardrails As Part Of Clarify Requirements (UNIQUE: questions/evidence)
- Store Clarification Data (UNIQUE: clarification.json)

**Decide Planning Criteria:**
- Inject Strategy Into Instructions (UNIQUE: criteria/assumptions)
- Store Strategy Data (UNIQUE: strategy.json)

**Build Knowledge:**
- Load Story Graph Into Memory
- Inject Knowledge Graph Template and Builder Instructions
- Update Existing Knowledge Graph
- Proactively Validate knowledge against rules
- Create Build Scope
- Filter Knowledge Graph

**Render Output:**
- Load Render Configurations
- Inject Template Instructions
- Inject Synchronizer Instructions
- Inject Render Instructions And Configs
- Get Render Instructions
- Merge Base And Render Instructions
- Render Output Using Synchronizers

**Validate Rules:**
- Inject Validation Rules for Validate Rules Action
- Invoke Complete Validation Workflow
- Discovers Scanners
- Run Scanners against Knowledge Graph
- Validate Rules According To Scope
- Generate Violation Report
- Report Validation and Error Handling

### Change Category 4: Panel Story Renames & Reorganization

**CURRENT STRUCTURE:** 4 features, inconsistent naming
**TARGET STRUCTURE:** 5 features, aligned with REPL

| Current Name | New Name | Reason |
|-------------|----------|--------|
| **Feature:** Manage Bot Information | **Feature:** Manage Panel Session | Matches REPL pattern "Manage REPL Session" |
| Refresh Panel | Display Session Status | Parallels REPL's `status` command |
| **Feature:** Navigate Behavior Action Status | **Feature:** Navigate And Execute Behaviors | Matches REPL/Direct |
| View Behavior Hierarchy | Display Behavior Hierarchy | Consistency with REPL |
| **Feature:** Filter And Navigate Scope | **Feature:** Manage Scope | Matches REPL/Direct |
| **Feature:** Display Instructions | **Feature:** View Action-Specific Instructions | Matches Direct |
| View Clarify Instructions | Display Clarify Instructions | More accurate |
| View Strategy Instructions | Display Strategy Instructions | More accurate |
| (etc. for Build, Validate, Render) | (same pattern) | Consistency |
| Submit Instructions To Chat | Submit Instructions To AI Agent | More accurate terminology |

**NEW STORIES TO ADD (not yet implemented):**
- View Current Scope (placeholder - NOT IMPL)
- Clear Scope (placeholder - NOT IMPL)
- Display Action Help Using Panel (placeholder - NOT IMPL)
- Display Parameter Help Using Panel (placeholder - NOT IMPL)
- Display Command Examples Using Panel (placeholder - NOT IMPL)

### Change Category 5: REPL Story Renames & Reorganization

**CURRENT STRUCTURE:** 7 features with redundant "Through CLI", "Using CLI", "In CLI" phrases
**TARGET STRUCTURE:** 6 features, cleaner names

| Current Name | New Name | Reason |
|-------------|----------|--------|
| **Feature:** Navigate Behaviors Using REPL Commands | **Feature:** Navigate And Execute Behaviors Using REPL Commands | Matches Panel/Direct |
| **Feature:** Navigate Behaviors Using Domain Model | Keep as is | Unique to REPL |
| Navigate To Behavior Action | Navigate To Behavior Action And Execute | More complete description |
| **Feature:** Execute Actions Using REPL | **Feature:** View Action-Specific Instructions | Aligns with Panel/Direct (execution is in Navigate) |
| Request Action Help Through CLI | Display Action Help Using CLI | Remove "Through", consistent with Panel |
| View Parameter Documentation in CLI | Display Parameter Help Using CLI | Parallel to Panel |
| View Command Examples in CLI | Display Command Examples Using CLI | Parallel to Panel |

**REMOVE OBSOLETE STORIES:**
- View Headless Mode Status (no longer used)
- Format Output For AI (no longer used)
- Confirm And Advance Action (replaced by Navigate To Behavior Action And Execute)

---

## 📋 IMPLEMENTATION STEPS

### Phase 1: Preparation & Validation (Est: 2 hours)

**Step 1.1: Create Backup**
```bash
# Create a backup branch
git checkout -b backup-before-story-refactor
git push origin backup-before-story-refactor

# Return to working branch
git checkout -b refactor-invoke-bot-stories
```

**Step 1.2: Run All Tests - Baseline**
```bash
cd agile_bot/bots/base_bot
pytest test/ -v > test-results-before.txt
```
- ✅ All tests must pass before starting
- Save results for comparison

**Step 1.3: Validate story-graph.json**
```bash
# Ensure it's valid JSON
python -m json.tool agile_bot/bots/base_bot/docs/stories/story-graph.json > /dev/null
```

---

### Phase 2: Rename Sub-Epics (Est: 30 minutes)

**Step 2.1: Rename in story-graph.json**
- Open: `agile_bot/bots/base_bot/docs/stories/story-graph.json`
- Find: `"name": "Perform Behavior Action"`
- Replace: `"name": "Invoke Bot Directly"`
- Find: `"name": "Run Interactive REPL"`
- Replace: `"name": "Invoke Bot Through REPL"`

**Step 2.2: Rename Story Folders**
```bash
cd agile_bot/bots/base_bot/docs/stories/map/🎯\ Invoke\ Bot/

# Rename sub-epic folders
git mv "⚙️ Perform Behavior Action" "⚙️ Invoke Bot Directly"
git mv "⚙️ Run Interactive REPL" "⚙️ Invoke Bot Through REPL"
```

**Step 2.3: Update Test Files - Test Class Names**
- Search for: `TestPerformBehaviorAction` → Replace: `TestInvokeBotDirectly`
- Search for: `TestRunInteractiveREPL` → Replace: `TestInvokeBotThroughREPL`
- Files affected: `test_perform_behavior_action.py`, `test_initialize_repl_session.py`, etc.

**Step 2.4: Commit**
```bash
git add .
git commit -m "refactor: rename sub-epics - Perform Behavior Action → Invoke Bot Directly, Run Interactive REPL → Invoke Bot Through REPL"
```

---

### Phase 3: Reorganize "Invoke Bot Directly" Sub-Epic (Est: 4 hours)

**Step 3.1: Update story-graph.json Structure**

In story-graph.json, find the "Invoke Bot Directly" sub-epic and restructure it:

**REMOVE these stories (will be reorganized into features):**
- Execute End-to-End Workflow (keep, but move)
- Execute Behavior Action (remove - merge into Navigate)
- Insert Context Into Instructions (rename and reorganize)
- Inject Next Behavior Reminder (move to scenarios)
- Confirm Current Action (move to Track Workflow State)
- Determine Action Order From State (rename to Navigate Sequentially)
- Inject Status Update Breadcrumbs Into Instructions (move to scenarios)

**ADD these features with stories:**
```json
{
  "name": "Invoke Bot Directly",
  "sub_epics": [],
  "features": [
    {
      "name": "Navigate And Execute Behaviors",
      "stories": [
        {"name": "Navigate To Behavior Action And Execute", ...},
        {"name": "Navigate Sequentially", ...},
        {"name": "Execute End-to-End Workflow", ...}
      ]
    },
    {
      "name": "Manage Scope",
      "stories": [
        {"name": "Set Story Scope", ...},
        {"name": "Set File Scope", ...},
        {"name": "Filter Knowledge Graph By Scope", ...},
        {"name": "Pass Scope Parameters To Actions", ...},
        {"name": "Clear Scope", ...}
      ]
    },
    {
      "name": "Generate Action Instructions",
      "stories": [
        {"name": "Load Base Action Configuration", ...},
        {"name": "Load And Merge Behavior-Specific Instructions", ...},
        {"name": "Load Guardrails From Behavior Folder", ...},
        {"name": "Inject Guardrails Into Instructions", ...},
        {"name": "Inject Context Into Instructions", ...},
        {"name": "Get Action Instructions", ...}
      ]
    },
    {
      "name": "View Action-Specific Instructions",
      "stories": [
        {"name": "View Base Instructions", ...},
        {"name": "View Clarify Instructions", ...},
        {"name": "View Strategy Instructions", ...},
        {"name": "View Build Instructions", ...},
        {"name": "View Validate Instructions", ...},
        {"name": "View Render Instructions", ...},
        {"name": "View Instructions In Raw Format", ...},
        {"name": "Submit Instructions To AI Agent", ...}
      ]
    },
    {
      "name": "Track Workflow State",
      "stories": [
        {"name": "Save Workflow State", ...},
        {"name": "Load Workflow State", ...},
        {"name": "Determine Resume Point After Interruption", ...},
        {"name": "Confirm Current Action", ...},
        {"name": "Inject Next Action Instructions", ...},
        {"name": "Transition To Next Action", ...}
      ]
    },
    {
      "name": "Track Activity",
      "stories": [
        {"name": "Track Action Start", ...},
        {"name": "Track Action Completion", ...},
        {"name": "Record Activity Metrics And Paths", ...}
      ]
    }
  ]
}
```

**Step 3.2: Rename Test Files**
```bash
cd agile_bot/bots/base_bot/test/

# Rename main test file
git mv test_perform_behavior_action.py test_invoke_bot_directly.py

# Rename specific test file
git mv test_invoke_behavior_in_action_order.py test_navigate_sequentially.py
```

**Step 3.3: Update Test Class Names**
- In `test_invoke_bot_directly.py`:
  - `TestInvokeBehaviorActionsInWorkflowOrder` → `TestExecuteEndToEndWorkflow`
  - `TestExecuteBehavior` → `TestNavigateToBehaviorActionAndExecute`
  - `TestInsertContextIntoInstructions` → `TestInjectContextIntoInstructions`
  - `TestInjectNextBehaviorReminder` → (move to scenarios in TestInjectContextIntoInstructions)
  - `TestConfirmCurrentAction` → keep name, move to Track Workflow State tests
  - `TestInjectStatusUpdateBreadcrumbs` → (move to scenarios in TestInjectContextIntoInstructions)

- In `test_navigate_sequentially.py`:
  - `TestInvokeBehaviorInActionOrder` → `TestNavigateSequentially`
  - `TestDetermineActionOrderFromState` → `TestLoadAndSequenceActions`

**Step 3.4: Update story-graph.json test_file and test_class References**
- Update all `"test_file"` references from old names to new names
- Update all `"test_class"` references from old names to new names

**Step 3.5: Commit**
```bash
git add .
git commit -m "refactor: reorganize Invoke Bot Directly from 7 flat stories to 6 feature groups (33 stories)"
```

---

### Phase 4: Consolidate Duplicate Stories from Behavior Action Sub-Epics (Est: 6 hours)

**Step 4.1: Extract Generic Stories - Track Activity**

For each of the 5 sub-epics (Gather Context, Decide Planning, Build Knowledge, Render Output, Validate Rules):

1. **Locate "Track Activity for [X] Action" story**
2. **Remove from sub-epic** in story-graph.json
3. **Verify** these stories now exist in "Invoke Bot Directly" → "Track Activity" feature:
   - Track Action Start
   - Track Action Completion
   - Record Activity Metrics And Paths

**Files to modify:**
- `agile_bot/bots/base_bot/docs/stories/story-graph.json` (remove duplicate stories)
- Each test file for the action (remove duplicate tests or consolidate)

**Step 4.2: Extract Generic Stories - Workflow State Transitions**

For each of the 4 sub-epics that have "Proceed To [Next Action]":

1. **Locate "Proceed To [X]" story**
2. **Remove from sub-epic** in story-graph.json
3. **Verify** these stories now exist in "Invoke Bot Directly" → "Track Workflow State":
   - Inject Next Action Instructions
   - Transition To Next Action

**Step 4.3: Extract Generic Stories - Configuration Loading**

For each sub-epic that has "Load Base Action Config":

1. **Locate and remove** from story-graph.json
2. **Verify** "Load Base Action Configuration" exists in "Generate Action Instructions" feature

**Step 4.4: Extract Generic Stories - Guardrails**

For each sub-epic that has "Load Guardrails":

1. **Locate and remove** from story-graph.json
2. **Verify** "Load Guardrails From Behavior Folder" exists in "Generate Action Instructions" feature

**Step 4.5: Remove Unnecessary Generic Stories**

Remove these from ALL sub-epics:
- "Initialize Action" (not needed as standalone story)
- "Access Actions" (not needed as standalone story)

**Step 4.6: Verify Unique Stories Remain**

After consolidation, each sub-epic should contain ONLY unique stories:

**Gather Context - KEEP:**
- Inject Guardrails As Part Of Clarify Requirements
- Store Clarification Data
- (any other unique clarify stories)

**Decide Planning Criteria - KEEP:**
- Inject Strategy Into Instructions
- Store Strategy Data
- (any other unique strategy stories)

**Build Knowledge - KEEP:**
- Load Story Graph Into Memory
- Inject Knowledge Graph Template and Builder Instructions
- Update Existing Knowledge Graph
- Proactively Validate knowledge against rules
- Create Build Scope
- Filter Knowledge Graph

**Render Output - KEEP:**
- Load Render Configurations
- Inject Template Instructions
- Inject Synchronizer Instructions
- Inject Render Instructions And Configs
- Get Render Instructions
- Merge Base And Render Instructions
- Render Output Using Synchronizers

**Validate Rules - KEEP:**
- Inject Validation Rules for Validate Rules Action
- Invoke Complete Validation Workflow
- Discovers Scanners
- Run Scanners against Knowledge Graph
- Validate Rules According To Scope
- Generate Violation Report
- Report Validation and Error Handling

**Step 4.7: Update Test Files**

For each consolidated story:
- Move tests from action-specific test files to `test_invoke_bot_directly.py`
- OR: Keep action-specific tests but update them to import generic functionality
- Update test class names to reflect new story names

**Step 4.8: Commit**
```bash
git add .
git commit -m "refactor: consolidate ~110+ duplicate stories from behavior actions into ~20 generic stories in Invoke Bot Directly"
```

---

### Phase 5: Update Panel Stories (Est: 2 hours)

**Step 5.1: Rename Panel Features in story-graph.json**

```json
// BEFORE
{"name": "Manage Bot Information", ...}
// AFTER
{"name": "Manage Panel Session", ...}

// BEFORE
{"name": "Navigate Behavior Action Status", ...}
// AFTER
{"name": "Navigate And Execute Behaviors", ...}

// BEFORE
{"name": "Filter And Navigate Scope", ...}
// AFTER
{"name": "Manage Scope", ...}

// BEFORE
{"name": "Display Instructions", ...}
// AFTER
{"name": "View Action-Specific Instructions", ...}
```

**Step 5.2: Rename Panel Stories**

| Old | New |
|-----|-----|
| Refresh Panel | Display Session Status |
| View Behavior Hierarchy | Display Behavior Hierarchy |
| View Clarify Instructions | Display Clarify Instructions |
| View Strategy Instructions | Display Strategy Instructions |
| View Build Instructions | Display Build Instructions |
| View Validate Instructions | Display Validate Instructions |
| View Render Instructions | Display Render Instructions |
| Submit Instructions To Chat | Submit Instructions To AI Agent |

**Step 5.3: Add Placeholder Stories (NOT IMPL)**

Add these to story-graph.json with `"status": "not_implemented"`:
- View Current Scope
- Clear Scope
- Display Action Help Using Panel
- Display Parameter Help Using Panel
- Display Command Examples Using Panel

**Step 5.4: Update Test Files**
- Rename test classes to match new story names
- Files: `test_invoke_bot_through_panel.py`, etc.

**Step 5.5: Commit**
```bash
git add .
git commit -m "refactor: rename Panel features and stories for consistency with REPL and Direct"
```

---

### Phase 6: Update REPL Stories (Est: 2 hours)

**Step 6.1: Rename REPL Features in story-graph.json**

```json
// BEFORE
{"name": "Navigate Behaviors Using REPL Commands", ...}
// AFTER
{"name": "Navigate And Execute Behaviors Using REPL Commands", ...}

// BEFORE
{"name": "Execute Actions Using REPL", ...}
// AFTER
{"name": "View Action-Specific Instructions", ...}
```

**Step 6.2: Rename REPL Stories**

| Old | New |
|-----|-----|
| Navigate To Behavior Action | Navigate To Behavior Action And Execute |
| Request Action Help Through CLI | Display Action Help Using CLI |
| View Parameter Documentation in CLI | Display Parameter Help Using CLI |
| View Command Examples in CLI | Display Command Examples Using CLI |

**Step 6.3: Remove Obsolete Stories**

Remove from story-graph.json:
- View Headless Mode Status
- Format Output For AI
- Confirm And Advance Action

**Step 6.4: Update Test Files**
- Rename test classes to match new story names
- Remove tests for obsolete stories
- Files: `test_navigate_bot_behaviors_and_actions_with_cli.py`, `test_initialize_repl_session.py`

**Step 6.5: Commit**
```bash
git add .
git commit -m "refactor: rename REPL features and stories, remove obsolete stories"
```

---

### Phase 7: Validation & Testing (Est: 2 hours)

**Step 7.1: Validate story-graph.json**
```bash
# Ensure it's still valid JSON
python -m json.tool agile_bot/bots/base_bot/docs/stories/story-graph.json > /dev/null

# Check for any broken references
# (run any validation scripts you have)
```

**Step 7.2: Run All Tests**
```bash
cd agile_bot/bots/base_bot
pytest test/ -v > test-results-after.txt
```

**Step 7.3: Compare Test Results**
```bash
# Compare before and after
diff test-results-before.txt test-results-after.txt
```
- ✅ Same number of tests should pass
- ✅ Only test names should have changed

**Step 7.4: Manual Verification**
- Open story-graph.json and spot-check changes
- Verify folder structure matches new names
- Check that git history is preserved (use `git log --follow`)

**Step 7.5: Create Summary Document**
```bash
# Generate change summary
git log backup-before-story-refactor..HEAD --oneline > REFACTORING-SUMMARY.txt
```

---

### Phase 8: Final Review & Merge (Est: 1 hour)

**Step 8.1: Create Pull Request**
- Title: "Refactor: Standardize Invoke Bot story naming and eliminate duplication"
- Description: Link to this plan document
- Include REFACTORING-SUMMARY.txt

**Step 8.2: Code Review**
- Review all renamed files
- Verify test coverage hasn't decreased
- Check story-graph.json for consistency

**Step 8.3: Merge**
```bash
git checkout main
git merge refactor-invoke-bot-stories
git push origin main
```

**Step 8.4: Clean Up**
```bash
# Delete backup branch (after confirming everything works)
git branch -d backup-before-story-refactor
git push origin --delete backup-before-story-refactor
```

---

## ✅ VERIFICATION CHECKLIST

Before considering this refactoring complete, verify:

- [ ] All tests pass (same count as before)
- [ ] story-graph.json is valid JSON
- [ ] Git history preserved for all renamed files (`git log --follow` works)
- [ ] No broken references in story-graph.json (test_file, test_class all point to existing files/classes)
- [ ] Feature counts match target: Direct (6), Panel (5), REPL (6)
- [ ] Story duplication eliminated: ~110+ duplicates → ~20 generics
- [ ] All commits have clear, descriptive messages
- [ ] Documentation updated (if any docs reference old story names)
- [ ] No merge conflicts
- [ ] Backup branch created and preserved until confident in changes

---

## 📝 ROLLBACK PLAN

If issues are discovered after merge:

**Option 1: Revert the merge**
```bash
git revert -m 1 <merge-commit-hash>
git push origin main
```

**Option 2: Restore from backup branch**
```bash
git checkout backup-before-story-refactor
git checkout -b main-restored
git push origin main-restored --force
```

**Option 3: Fix forward**
- Identify specific issue
- Create hotfix branch
- Fix and test
- Merge hotfix

---

## 📚 APPENDIX: Detailed Analysis & Reference

This appendix contains detailed analysis, historical context, and reference materials that informed the plan above.

### A. Deep Dive: Structural Inconsistencies Between Panel and REPL (Historical Analysis)

### Problem Statement

After initial naming cleanup, significant structural differences remain between Panel and REPL features that address the same user needs. These differences make the system harder to understand and maintain.

### Current State Analysis

#### Panel Features:
```
Manage Bot Information
├─ Open Panel
├─ Refresh Panel
├─ Change Workspace Path
├─ Switch Bot
└─ Toggle Panel Section

Navigate Behavior Action Status
├─ View Behavior Hierarchy
├─ Navigate Sequentially
└─ Execute Behavior Action

Filter And Navigate Scope
├─ Set Story Scope
├─ View Story Scope Hierarchy
├─ Set File Scope
└─ Open Story Files

Display Instructions
├─ View Base Instructions
├─ View Clarify Instructions
├─ View Strategy Instructions
├─ View Build Instructions
├─ View Validate Instructions
├─ View Render Instructions
├─ View Instructions In Raw Format
└─ Submit Instructions To Chat
```

#### REPL Features:
```
Initialize REPL Session
├─ Start REPL Session
├─ Start REPL in Pipe Mode
├─ Display Piped Mode Instructions
├─ Detect and Configure TTY/Non-TTY Input
├─ Load Workspace Context
└─ Load All Registered Bots

Navigate Behaviors Using REPL Commands
├─ Navigate To Behavior Action And Execute
├─ Navigate Sequentially
└─ Exit REPL

Navigate Behaviors Using Domain Model
├─ Navigate To Behavior Action And Execute
└─ Show Remaining Actions After Completion

Execute Actions Using REPL
├─ View Instructions
├─ Confirm With Parameters
├─ Confirm Action Completion
├─ Auto-Confirm Action
├─ Re-execute Current Action
├─ Handle Errors and Validation
└─ Execute Behavior Action

Manage Scope Using REPL
├─ Set Scope
├─ Set Story Scope
├─ Set File Scope
├─ Validate Scope Against Story Graph
├─ Pass Scope Parameters When Executing Actions
├─ View Current Scope
├─ Clear Scope
└─ Enforce Mutually Exclusive Scope Types

Display State Using REPL
├─ View Session Header
├─ View Behavior Hierarchy
├─ View Current Position
├─ View Active Scope
├─ View Navigation Commands
├─ View Headless Mode Status
├─ View Available Bots
├─ Display CLI Bot Command in Navigation Menu Footer
└─ Format Output For AI

Get Help Using REPL
├─ Request Action Help
├─ View Command Examples
└─ View Parameter Documentation
```

---

### Inconsistency #1: Navigation Features Are Split Differently

**Panel has ONE navigation feature:**
- Navigate Behavior Action Status (3 stories)
  - Viewing hierarchy
  - Sequential navigation
  - Execution

**REPL has TWO navigation features:**
- Navigate Behaviors Using REPL Commands (3 stories)
  - Dot notation navigation
  - Sequential navigation  
  - Exit
- Navigate Behaviors Using Domain Model (3 stories)
  - Navigate to behavior
  - Confirm and advance
  - Show remaining actions

**Analysis:**
- Panel groups by **user action patterns** (all navigation together)
- REPL splits by **implementation method** (command-based vs domain-based)
- The split makes sense for REPL because they use fundamentally different mechanisms
- But "Navigate Behavior Action Status" in Panel is too broad - it mixes viewing, navigating, and executing

**Recommendation:**
Split Panel's "Navigate Behavior Action Status" into two features to match REPL's conceptual clarity:

```
Panel SHOULD HAVE:
├─ View Bot State
│  └─ View Behavior Hierarchy
└─ Navigate And Execute Behaviors
   ├─ Navigate Sequentially
   └─ Execute Behavior Action
```

---

### Inconsistency #2: "Display State" vs "View Behavior Hierarchy"

**Panel:**
- "View Behavior Hierarchy" is a story under "Navigate Behavior Action Status"
- No dedicated "Display State" or "View State" feature

**REPL:**
- "Display State Using REPL" is a FEATURE with 9 stories
- "View Behavior Hierarchy" is one story among many

**Analysis:**
- REPL correctly recognizes that viewing state is a major feature area
- Panel bundles state viewing with navigation, which obscures the distinction
- Both need to display: hierarchy, current position, paths, scope, instructions

**Recommendation:**
Panel should have a dedicated "View Bot State" feature parallel to REPL's "Display State Using REPL":

```
Panel:
View Bot State
├─ View Session Information (bot name, workspace path)
├─ View Behavior Hierarchy
├─ View Current Position
└─ View Active Scope

REPL:
Display State Using REPL
├─ View Session Header
├─ View Behavior Hierarchy
├─ View Current Position
├─ View Active Scope
├─ View Navigation Commands
├─ View Headless Mode Status
├─ View Available Bots
└─ Format Output For AI
```

---

### Inconsistency #3: Scope Management Granularity

**Panel:**
- "Filter And Navigate Scope" (4 stories)
  - Set Story Scope
  - View Story Scope Hierarchy
  - Set File Scope
  - Open Story Files

**REPL:**
- "Manage Scope Using REPL" (8 stories)
  - Set Scope
  - Set Story Scope
  - Set File Scope
  - Validate Scope
  - Pass Scope Parameters
  - View Current Scope
  - Clear Scope
  - Enforce Mutually Exclusive Scope Types

**Analysis:**
- REPL has more granular scope management (8 stories vs 4)
- Panel is missing: View Current Scope, Clear Scope, Validate Scope
- Panel has "Open Story Files" which is more about navigation than scope
- Both set story scope and file scope

**Recommendation:**
Panel should have complete scope management parallel to REPL:

```
Panel:
Manage Scope
├─ Set Story Scope
├─ Set File Scope
├─ View Current Scope
├─ Clear Scope
└─ View Story Scope Hierarchy (keep - GUI-specific tree view)

Move "Open Story Files" to a different feature (it's about file navigation, not scope)
```

---

### Inconsistency #4: Instructions Handling

**Panel:**
- "Display Instructions" (8 stories)
  - View [Type] Instructions (7 stories for different action types)
  - Submit Instructions To Chat

**REPL:**
- Instructions are part of "Execute Actions Using REPL" (7 stories total)
  - View Instructions (1 story, generic)
  - Confirm With Parameters
  - Confirm Action Completion
  - Auto-Confirm Action
  - Re-execute Current Action
  - Handle Errors and Validation
  - Execute Behavior Action

**Analysis:**
- Panel has 7 separate stories for each instruction type (Clarify, Strategy, Build, etc.)
- REPL has 1 generic "View Instructions" story
- This reflects different UX: Panel has specialized UI per action type, REPL uses generic text display
- BUT: Both should conceptually organize instructions the same way

**Question for Decision:**
Should we:
1. **Keep Panel's granular approach** and expand REPL to match (7 instruction stories)?
2. **Collapse Panel to REPL's approach** (1 generic View Instructions story)?
3. **Keep them different** because UI vs CLI genuinely needs different granularity?

**Recommendation:** Option 3 - Keep them different BUT rename Panel feature to clarify:
- Panel: "View Action-Specific Instructions" (makes granularity explicit)
- REPL: "Execute Actions Using REPL" (includes generic View Instructions)

---

### Inconsistency #5: Session Management

**Panel:**
- "Manage Bot Information" includes:
  - Open Panel
  - Refresh Panel
  - Change Workspace Path
  - Switch Bot
  - Toggle Panel Section

**REPL:**
- "Initialize REPL Session" includes:
  - Start REPL Session
  - Start REPL in Pipe Mode
  - Detect TTY/Non-TTY
  - Load Workspace Context
  - Load All Registered Bots
- NO "Manage Session" feature (but capabilities exist via `status`, `path`, bot switching)

**Analysis:**
- Panel's "Manage Bot Information" mixes initialization (Open) with runtime operations (Refresh, Change, Switch)
- REPL's "Initialize REPL Session" is pure initialization/startup
- REPL has session management capabilities (`status` command, `path` command) but they're not organized as a feature
- Both Panel and REPL need consistent Initialize vs Manage split

**Recommendation:**
Split Panel's "Manage Bot Information" into two features AND create matching feature for REPL:

```
Panel:
├─ Initialize Panel Session
│  ├─ Open Panel
│  └─ Load Bot Configuration
└─ Manage Session
   ├─ Display Session Status (Refresh button - equivalent to REPL's `status` command)
   ├─ Change Workspace Path
   ├─ Switch Bot
   └─ Toggle Panel Section

REPL:
├─ Initialize REPL Session (keep existing)
│  ├─ Start REPL Session
│  ├─ Start REPL in Pipe Mode
│  ├─ Detect TTY/Non-TTY
│  ├─ Load Workspace Context
│  └─ Load All Registered Bots
└─ Manage Session (NEW feature)
   ├─ Display Session Status (via `status` command - equivalent to Panel's Refresh)
   ├─ Change Workspace Path (via `path` command)
   └─ Switch Bot (via bot switching command)
```

---

### Inconsistency #6: Help/Documentation

**Panel:**
- No help feature (help is probably embedded in UI or docs)

**REPL:**
- "Get Help Using REPL" (3 stories)
  - Request Action Help
  - View Command Examples
  - View Parameter Documentation

**Analysis:**
- REPL needs explicit help because it's a CLI
- Panel might have tooltip hover help or documentation links
- If Panel has help features, they should be explicitly modeled

**Recommendation:**
If Panel has help features, add:
```
Panel:
Get Help
├─ View Action Help (tooltip/dialog)
├─ View Command Examples (if applicable)
└─ Access Documentation
```

---

### C. Proposed Structural Alignment

### Unified Feature Structure (Parallel Across Panel and REPL)

```
CORE FEATURES (Present in both Panel and REPL):

1. Initialize Session
   - Panel: Open Panel, Load Bots
   - REPL: Start REPL, Detect TTY, Load Bots

2. Manage Session
   - Panel: Display Session Status (Refresh button), Change Workspace, Switch Bot
   - REPL: Display Session Status (`status` command), Change Workspace, Switch Bot
   - **Note:** Refresh (Panel) and Status (REPL) are equivalent - both display/refresh current session state

3. View Bot State
   - Panel: View Session Header, View Behavior Hierarchy, View Current Position, View Active Scope, View Available Bots, View Navigation Commands
   - REPL: View Session Header, View Behavior Hierarchy, View Current Position, View Active Scope, View Available Bots, View Navigation Commands

4. Navigate Behaviors
   - Panel: Navigate Sequentially, Navigate To Behavior Action And Execute
   - REPL: Navigate To Behavior Action And Execute, Navigate Sequentially

5. Manage Scope
   - Panel: Set Story Scope, Set File Scope, View Story Scope Hierarchy, View Current Scope, Clear Scope
   - REPL: Set Scope, Set Story Scope, Set File Scope, View Current Scope, Clear Scope, Validate Scope

6. View Instructions
   - Panel: View Base Instructions, View Clarify Instructions, View Strategy Instructions, View Build Instructions, View Validate Instructions, View Render Instructions, View Raw Instructions
   - REPL: View Instructions (generic)

7. Get Help
   - Panel: View Action Help, Access Documentation (NOT IMPL)
   - REPL: View Action Help, Access Documentation (NOT IMPL)
```

---

### D. Revised Recommendations for Phase 1.5 (Structural Alignment)

### Changes to Panel Features:

#### SPLIT: "Navigate Behavior Action Status" → Two Features

**BEFORE:**
```
Navigate Behavior Action Status
├─ View Behavior Hierarchy
├─ Navigate Sequentially
└─ Execute Behavior Action
```

**AFTER:**
```
View Bot State
└─ View Behavior Hierarchy

Navigate And Execute Behaviors
├─ Navigate Sequentially
└─ Execute Behavior Action
```

#### SPLIT: "Manage Bot Information" → Two Features

**BEFORE:**
```
Manage Bot Information
├─ Open Panel
├─ Refresh Panel
├─ Change Workspace Path
├─ Switch Bot
└─ Toggle Panel Section
```

**AFTER:**
```
Initialize Panel Session
├─ Open Panel
└─ Load Bot Configuration

Manage Session
├─ Refresh Panel
├─ Change Workspace Path
├─ Switch Bot
└─ Toggle Panel Section
```

#### EXPAND: "View Bot State" Feature

**ADD these stories to match REPL:**
```
View Bot State
├─ View Session Information (NEW - bot name, workspace path, version - IMPLEMENTED via Panel header)
├─ View Behavior Hierarchy (MOVED from Navigate Behavior Action Status - IMPLEMENTED)
├─ View Current Position (NEW - NOT IMPLEMENTED - placeholder)
├─ View Active Scope (NEW - NOT IMPLEMENTED - placeholder)
├─ View Navigation Commands (NEW - NOT IMPLEMENTED - placeholder, parallel to REPL)
├─ View Headless Mode Status (NEW - NOT IMPLEMENTED - placeholder, parallel to REPL)
├─ View Available Bots (NEW - NOT IMPLEMENTED - placeholder, parallel to REPL)
└─ Format Output For AI (NEW - NOT IMPLEMENTED - placeholder, Panel doesn't need AI formatting)
```

**Stories to Create:**

1. **View Session Information** - Mark as IMPLEMENTED
   - Panel header already shows bot name, version, workspace
   - This story documents existing functionality

2. **View Current Position** - Mark as NOT IMPLEMENTED
   - Acceptance Criteria: "NOT IMPLEMENTED - Placeholder for displaying current behavior.action.operation"
   - Parallel to REPL's "View Current Position"

3. **View Active Scope** - Mark as NOT IMPLEMENTED
   - Acceptance Criteria: "NOT IMPLEMENTED - Placeholder for displaying active scope filters in state view"
   - Parallel to REPL's "View Active Scope"

4. **View Navigation Commands** - Mark as NOT IMPLEMENTED
   - Acceptance Criteria: "NOT IMPLEMENTED - Placeholder for displaying available navigation commands"
   - Parallel to REPL's "View Navigation Commands"
   - Note: Panel uses buttons/clicks, so text command list may not be needed

5. **View Headless Mode Status** - Mark as NOT IMPLEMENTED
   - Acceptance Criteria: "NOT IMPLEMENTED - Placeholder for displaying headless mode configuration"
   - Parallel to REPL's "View Headless Mode Status"

6. **View Available Bots** - Mark as NOT IMPLEMENTED
   - Acceptance Criteria: "NOT IMPLEMENTED - Placeholder for displaying list of available bots"
   - Parallel to REPL's "View Available Bots"

7. **Format Output For AI** - Mark as NOT IMPLEMENTED (and probably not needed)
   - Acceptance Criteria: "NOT IMPLEMENTED - Panel output is HTML for GUI, not text for AI"
   - This is REPL-specific, may not be relevant for Panel



#### EXPAND: "Manage Scope" Feature

**RENAME:** "Filter And Navigate Scope" → "Manage Scope"

**ADD stories:**
```
Manage Scope
├─ Set Story Scope (keep)
├─ Set File Scope (keep)
├─ View Story Scope Hierarchy (keep)
├─ View Current Scope (NEW)
├─ Clear Scope (NEW)
└─ Validate Scope (NEW - optional)

MOVE "Open Story Files" to "Navigate And Execute Behaviors" or create "Navigate Files" feature
```

#### RENAME: "Display Instructions" → "View Action-Specific Instructions"

**Makes the granularity explicit**

---

### Changes to REPL Features:

#### ADD: "Manage Session" Feature

**Currently:** Session management stories are scattered or not explicitly organized as a feature

**Proposed:**
```
Manage Session (NEW feature for REPL)
├─ Display Session Status (via `status` command - parallel to Panel's "Display Session Status")
├─ Change Workspace Path (via `path` command)
└─ Switch Bot (if bot switching capability exists)
```

**Note:** The `status` command already exists in REPL and is heavily used. This just organizes it as an explicit feature parallel to Panel's "Manage Session" feature.

#### MERGE: Consider merging navigation features?

**Current split may be correct, but review:**
- "Navigate Behaviors Using REPL Commands" (command-based)
- "Navigate Behaviors Using Domain Model" (programmatic)

**Decision:** Keep split - they represent genuinely different mechanisms

#### EXPAND: "Display State Using REPL"

**Consider these additions for completeness:**
```
Display State Using REPL
├─ View Session Header (keep)
├─ View Behavior Hierarchy (keep)
├─ View Current Position (keep)
├─ View Active Scope (keep)
├─ View Navigation Commands (keep)
├─ View Headless Mode Status (keep)
├─ View Available Bots (keep)
├─ View Workspace Information (NEW - explicit, parallel to Panel)
└─ Format Output For AI (keep)
```

---

### E. Updated Change Summary (Historical)

**After Structural Alignment:**

**Panel:**
- Split 2 features into 4 features
- Add ~6 new stories for completeness
- Rename 1 feature
- Total: 6 feature changes, ~20 story changes

**REPL:**
- Minor additions for consistency
- Total: 0-1 feature changes, ~2 story additions

**Overall:**
- Total features after alignment: Panel (5), REPL (6)
- Flatter structure: Merged Initialize + Manage into single "Manage Session" features
- Scenarios vs Stories: Some granular items moved to scenarios within parent stories
- Parallel concepts clearly mapped across both
- Each invocation method optimized for its UX while maintaining conceptual consistency

---
INVOKE BOT (Epic)
|
+-- Invoke MCP (Sub-Epic) [NO CHANGE]
|   +-- Stories: (same as before)
|
+-- Invoke Bot Directly (Sub-Epic) [RENAMED from "Perform Behavior Action"]
|   +-- Stories:
|       1. Execute End-to-End Workflow [RENAMED from "Invoke Behavior Actions In Workflow Order"]
|       2. Execute Behavior Action [RENAMED from "Execute Behavior"]
|       3. Insert Context Into Instructions [NO CHANGE]
|       4. Inject Next Behavior Reminder [NO CHANGE]
|       5. Confirm Current Action [RENAMED from "Close Current Action"]
|       6. Determine Action Order From State [RENAMED from "Invoke Behavior In Action Order"]
|       7. Inject Status Update Breadcrumbs Into Instructions [NO CHANGE]
|
+-- Invoke Bot Through Panel (Sub-Epic) [NO CHANGE]
|   |
|   +-- Manage Bot Information (Feature) [NO CHANGE]
|   |   +-- Stories:
|   |       1. Open Panel [NO CHANGE]
|   |       2. Refresh Panel [NO CHANGE]
|   |       3. Change Workspace Path [NO CHANGE]
|   |       4. Switch Bot [NO CHANGE]
|   |       5. Toggle Panel Section [NO CHANGE]
|   |
|   +-- Navigate Behavior Action Status (Feature) [NO CHANGE]
|   |   +-- Stories:
|   |       1. View Behavior Hierarchy [RENAMED from "Display Hierarchy"]
|   |       2. Navigate Sequentially [RENAMED from "Navigate Behavior Action"]
|   |       3. Navigate To Behavior Action And Execute [RENAMED from "Execute Behavior Action"]
|   |
|   +-- Filter And Navigate Scope (Feature) [NO CHANGE]
|   |   +-- Stories:
|   |       1. Set Story Scope [RENAMED from "Filter Story Scope"]
|   |       2. View Story Scope Hierarchy [RENAMED from "Display Story Scope Hierarchy"]
|   |       3. Set File Scope [RENAMED from "Filter File Scope"]
|   |       4. Open Story Files [NO CHANGE]
|   |
|   +-- Display Instructions (Feature) [NO CHANGE]
|       +-- Stories:
|           1. View Base Instructions [RENAMED from "Display Base Instructions"]
|           2. View Clarify Instructions [RENAMED from "Display Clarify Instructions"]
|           3. View Strategy Instructions [RENAMED from "Display Strategy Instructions"]
|           4. View Build Instructions [RENAMED from "Display Build Instructions"]
|           5. View Validate Instructions [RENAMED from "Display Validate Instructions"]
|           6. View Render Instructions [RENAMED from "Display Render Instructions"]
|           7. View Instructions In Raw Format [RENAMED from "Display Instructions In Raw Format"]
|           8. Submit Instructions To Chat [NO CHANGE]
|
+-- Invoke Bot Through REPL (Sub-Epic) [RENAMED from "Run Interactive REPL"]
    |
    +-- Initialize REPL Session (Feature) [NO CHANGE]
    |   +-- Stories:
    |       1. Start REPL Session [RENAMED from "Launch CLI in Interactive Mode"]
    |       2. Start REPL in Pipe Mode [RENAMED from "Launch CLI in Pipe Mode"]
    |       3. Display Piped Mode Instructions for AI Agents [NO CHANGE]
    |       4. Detect and Configure TTY/Non-TTY Input [RENAMED from "Detect and Configure TTY/Non-TTY Input for CLI"]
    |       5. Load Workspace Context [RENAMED from "Load and Display Workspace Context in CLI"]
    |       6. Load All Registered Bots [NO CHANGE]
    |
   +-- Navigate Behaviors Using REPL Commands (Feature) [RENAMED from "Navigate Bot Behaviors and Actions With CLI"]
   |   +-- Stories:
   |       1. Navigate To Behavior Action And Execute [RENAMED from "Navigate Using CLI Dot Notation"]
   |       2. Navigate Sequentially [RENAMED from "Navigate Sequentially Using CLI Commands"]
   |       3. Exit REPL [RENAMED from "Exit CLI REPL"]
   |
   +-- Navigate Behaviors Using Domain Model (Feature) [RENAMED from "Navigate Bot Behaviors and Actions Via Domain Model"]
   |   +-- Stories:
   |       1. Navigate To Behavior Action And Execute [RENAMED from "Navigate To First Behavior Action"]
   |       2. Show Remaining Actions After Completion [NO CHANGE - was #3, now #2 after removing "Confirm And Advance Action"]
    |
    +-- Execute Actions Using REPL (Feature) [RENAMED from "Execute Action Operation Through CLI"]
    |   +-- Stories:
    |       1. View Instructions 
    |       2. Confirm With Parameters [RENAMED from "Confirm Work Through CLI with String Parameters"]
    |       3. Confirm Action Completion [RENAMED from "Confirm Action Completion Through CLI"]
    |       4. Auto-Confirm Action [RENAMED from "Auto-Confirm Action After Instructions Complete"]
    |       5. Re-execute Current Action [RENAMED from "Re-execute Current Operation Using CLI"]
    |       6. Handle Errors and Validation [RENAMED from "Handle Operation Errors and Validation in CLI"]
    |       7. Execute Behavior Action [RENAMED from "Invoke Specific Bot Behavior Command through CLI"]
    |
    +-- Manage Scope Using REPL (Feature) [RENAMED from "Manage Bot Scope Through CLI"]
    |   +-- Stories:
    |       1. Set Scope [RENAMED from "Set Scope Through CLI Using String Parameters"]
    |       2. Set Story Scope [RENAMED from "Filter Work Using Knowledge Graph Scope in CLI"]
    |       3. Set File Scope [RENAMED from "Filter Work Using Files Scope in CLI"]
    |       4. Validate Scope Against Story Graph [RENAMED from "Validate Scope Against Story Graph in CLI"]
    |       5. Pass Scope Parameters When Executing Actions [RENAMED from "Pass Scope Parameters When Executing Actions Through CLI"]
    |       6. View Current Scope [RENAMED from "View Current Scope in CLI"]
    |       7. Clear Scope [RENAMED from "Clear Scope Through CLI"]
    |       8. Enforce Mutually Exclusive Scope Types [NO CHANGE]
    |
    +-- Display State Using REPL (Feature) [RENAMED from "Display Bot State Using CLI"]
    |   +-- Stories:
    |       1. View Session Header [RENAMED from "Display CLI Header"]
    |       2. View Behavior Hierarchy [RENAMED from "Display Bot Hierarchy Tree with Progress Indicators"]
    |       3. View Current Position [RENAMED from "Display Current Position in CLI"]
    |       4. View Active Scope [RENAMED from "Display Active Scope in CLI Status"]
    |       5. View Navigation Commands [RENAMED from "Display CLI Navigation Menu Footer"]
    |       6. View Headless Mode Status [RENAMED from "Display Headless Mode Status in CLI"]
    |       7. View Available Bots [RENAMED from "Display Available Bot in Tree Hierarchy"]
    |       8. Display CLI Bot Command in Navigation Menu Footer [NO CHANGE - consider merging with #5]
    |       9. Format Output For AI [NO CHANGE]
    |
    +-- Get Help Using REPL (Feature) [RENAMED from "Get Help Using CLI"]
        +-- Stories:
            1. Request Action Help [RENAMED from "Request Action Help Through CLI"]
            2. View Command Examples [RENAMED from "View Command Examples in CLI"]
            3. View Parameter Documentation [RENAMED from "View Parameter Documentation in CL----

### H. Before/After Feature Structure Comparison (Reference)

### Panel Features: Before → After

| Before | After | Rationale |
|--------|-------|-----------|
| Manage Bot Information (5 stories) | **Initialize Panel Session** (2 stories) | Separate initialization from runtime |
| | **Manage Session** (4 stories) | Runtime session management |
| Navigate Behavior Action Status (3 stories) | **View Bot State** (4 stories) | Dedicated state viewing, parallel to REPL |
| | **Navigate And Execute Behaviors** (2 stories) | Navigation and execution together |
| Filter And Navigate Scope (4 stories) | **Manage Scope** (6-7 stories) | Add missing stories (View, Clear, Validate) |
| Display Instructions (8 stories) | **View Action-Specific Instructions** (8 stories) | Name clarifies granularity |
| *(none)* | **Get Help** (2-3 stories) *(optional)* | If help features exist |

**Result:** 4 features → 7-8 features (better organized, more complete)

### REPL Features: Before → After

| Before | After | Notes |
|--------|-------|-------|
| Initialize REPL Session (6 stories) | ✅ Keep | Already well-structured |
| Navigate Behaviors Using REPL Commands (3 stories) | ✅ Keep | Command-based navigation |
| Navigate Behaviors Using Domain Model (3 stories) | ✅ Keep | Programmatic navigation |
| Execute Actions Using REPL (7 stories) | ✅ Keep | Already comprehensive |
| Manage Scope Using REPL (8 stories) | ✅ Keep | Already complete |
| Display State Using REPL (9 stories) | ✅ Keep (maybe +1 story) | Consider adding "View Workspace Information" explicitly |
| Get Help Using REPL (3 stories) | ✅ Keep | Already present |

**Result:** 7 features → 8 features (added "Manage Session" to organize existing `status`/`path` commands)

---

### F. Original Phase Plan (Superseded by Implementation Steps Above)

#### Phase 1: Sub-Epic Level Renames

### Changes in `story-graph.json` → `epics[].sub_epics[].name`

| Current Name | New Name | Rationale |
|--------------|----------|-----------|
| `"Perform Behavior Action"` | `"Invoke Bot Directly"` | Matches pattern of "Invoke Bot Through X" and clarifies this is direct programmatic invocation |
| `"Run Interactive REPL"` | `"Invoke Bot Through REPL"` | Matches pattern of "Invoke Bot Through Panel" for consistency |
| `"Invoke MCP"` | ✅ Keep as-is | Already clear |
| `"Invoke Bot Through Panel"` | ✅ Keep as-is | Already consistent |

**Files to Update:**
- `agile_bot/bots/base_bot/docs/stories/story-graph.json` (lines ~1949, 4359)

**Folder Renames Required:**
```
BEFORE: docs/stories/map/🎯 Invoke Bot/⚙️ Perform Behavior Action/
AFTER:  docs/stories/map/🎯 Invoke Bot/⚙️ Invoke Bot Directly/

BEFORE: docs/stories/map/🎯 Invoke Bot/⚙️ Run Interactive REPL/
AFTER:  docs/stories/map/🎯 Invoke Bot/⚙️ Invoke Bot Through REPL/
```

---

#### Phase 1.5: Structural Alignment (Panel Features)

**Purpose:** Reorganize Panel features to match REPL's conceptual structure before doing story-level renames.

### 1.5.1 Split "Navigate Behavior Action Status" into Two Features

**In story-graph.json:**

**BEFORE (1 feature, 3 stories):**
```json
{
  "name": "Navigate Behavior Action Status",
  "sequential_order": 2,
  "story_groups": [{
    "stories": [
      {"name": "Display Hierarchy", ...},
      {"name": "Navigate Behavior Action", ...},
      {"name": "Execute Behavior Action", ...}
    ]
  }]
}
```

**AFTER (2 features, 4 stories total):**
```json
{
  "name": "View Bot State",
  "sequential_order": 1.5,
  "story_groups": [{
    "stories": [
      {"name": "View Session Information", ...},  // NEW
      {"name": "View Behavior Hierarchy", ...},   // MOVED + RENAMED
      {"name": "View Current Position", ...},     // NEW
      {"name": "View Active Scope", ...}          // NEW
    ]
  }]
},
{
  "name": "Navigate And Execute Behaviors",
  "sequential_order": 2,
  "story_groups": [{
    "stories": [
      {"name": "Navigate Sequentially", ...},     // RENAMED
      {"name": "Execute Behavior Action", ...}    // KEEP
    ]
  }]
}
```

**Folder Changes:**
```
BEFORE:
Navigate Behavior Action Status/
├─ 📝 Display Hierarchy.md
├─ 📝 Navigate Behavior Action.md
└─ 📝 Execute Behavior Action.md

AFTER:
View Bot State/
├─ 📝 View Session Information.md (NEW)
├─ 📝 View Behavior Hierarchy.md (MOVED)
├─ 📝 View Current Position.md (NEW)
└─ 📝 View Active Scope.md (NEW)

Navigate And Execute Behaviors/
├─ 📝 Navigate Sequentially.md
└─ 📝 Execute Behavior Action.md
```

### 1.5.2 Split "Manage Bot Information" into Two Features

**BEFORE (1 feature, 5 stories):**
```json
{
  "name": "Manage Bot Information",
  "sequential_order": 1,
  "story_groups": [{
    "stories": [
      {"name": "Open Panel", ...},
      {"name": "Refresh Panel", ...},
      {"name": "Change Workspace Path", ...},
      {"name": "Switch Bot", ...},
      {"name": "Toggle Panel Section", ...}
    ]
  }]
}
```

**AFTER (2 features, 6 stories total):**
```json
{
  "name": "Initialize Panel Session",
  "sequential_order": 1,
  "story_groups": [{
    "stories": [
      {"name": "Open Panel", ...},
      {"name": "Load Bot Configuration", ...}  // NEW (explicit)
    ]
  }]
},
{
  "name": "Manage Session",
  "sequential_order": 1.2,
  "story_groups": [{
    "stories": [
      {"name": "Display Session Status", ...},  // RENAMED from "Refresh Panel" to parallel REPL's `status` command
      {"name": "Change Workspace Path", ...},
      {"name": "Switch Bot", ...},
      {"name": "Toggle Panel Section", ...}
    ]
  }]
}
```

**Folder Changes:**
```
BEFORE:
Manage Bot Information/
├─ 📝 Open Panel.md
├─ 📝 Refresh Panel.md
├─ 📝 Change Workspace Path.md
├─ 📝 Switch Bot.md
└─ 📝 Toggle Panel Section.md

AFTER:
Initialize Panel Session/
├─ 📝 Open Panel.md
└─ 📝 Load Bot Configuration.md (NEW)

Manage Session/
├─ 📝 Display Session Status.md (renamed from "Refresh Panel.md")
├─ 📝 Change Workspace Path.md
├─ 📝 Switch Bot.md
└─ 📝 Toggle Panel Section.md
```

### 1.5.3 Expand "Manage Scope" Feature (Rename + Add Stories)

**BEFORE:**
```json
{
  "name": "Filter And Navigate Scope",
  "sequential_order": 3,
  "story_groups": [{
    "stories": [
      {"name": "Filter Story Scope", ...},
      {"name": "Display Story Scope Hierarchy", ...},
      {"name": "Filter File Scope", ...},
      {"name": "Open Story Files", ...}
    ]
  }]
}
```

**AFTER:**
```json
{
  "name": "Manage Scope",
  "sequential_order": 3,
  "story_groups": [{
    "stories": [
      {"name": "Set Story Scope", ...},              // RENAMED from "Filter Story Scope"
      {"name": "Set File Scope", ...},               // RENAMED from "Filter File Scope"
      {"name": "View Story Scope Hierarchy", ...},   // RENAMED from "Display Story Scope Hierarchy"
      {"name": "View Current Scope", ...},           // NEW - mark as NOT IMPLEMENTED in acceptance criteria
      {"name": "Clear Scope", ...},                  // NEW - mark as NOT IMPLEMENTED in acceptance criteria
      {"name": "Validate Scope", ...}                // NEW (optional) - mark as NOT IMPLEMENTED
    ]
  }]
}
```

**Stories to Create (mark as NOT IMPLEMENTED):**

1. **View Current Scope** 
   - Acceptance Criteria: "NOT IMPLEMENTED - Placeholder for future Panel feature to display active scope filters"
   - Parallel to REPL's "View Current Scope"

2. **Clear Scope**
   - Acceptance Criteria: "NOT IMPLEMENTED - Placeholder for future Panel feature to clear all scope filters"
   - Parallel to REPL's "Clear Scope"

3. **Validate Scope** (optional)
   - Acceptance Criteria: "NOT IMPLEMENTED - Placeholder for future Panel feature to validate scope against story graph"
   - Parallel to REPL's "Validate Scope Against Story Graph"

**Move "Open Story Files" to:**
- Option 1: "Navigate And Execute Behaviors" feature
- Option 2: New "Navigate Files" feature (if there are more file navigation stories)

### 1.5.4 Rename "Display Instructions" Feature

**Simple rename for clarity:**

```json
// BEFORE
{"name": "Display Instructions", ...}

// AFTER
{"name": "View Action-Specific Instructions", ...}
```

### 1.5.5 Add "Get Help" Feature (If Applicable)

**If Panel has help features (tooltips, help dialogs), add:**

```json
{
  "name": "Get Help",
  "sequential_order": 5,
  "story_groups": [{
    "stories": [
      {"name": "View Action Help", ...},         // NEW - NOT IMPL
      {"name": "View Tooltip Information", ...}, // NEW - NOT IMPL
      {"name": "Access Documentation", ...}      // NEW - NOT IMPL
    ]
  }]
}
```

### 1.5.6 How to Mark Stories as NOT IMPLEMENTED

For all new placeholder stories, add this to the story definition:

```json
{
  "name": "View Current Scope",
  "sequential_order": 4,
  "connector": "and",
  "users": ["User"],
  "story_type": "user",
  "acceptance_criteria": [
    "NOT IMPLEMENTED - Placeholder for future Panel feature",
    "WHEN implemented: User should be able to view active scope filters",
    "Parallel to REPL story: 'View Current Scope in CLI'"
  ],
  "optional": true,
  "priority": 3,
  "implementation_status": "NOT_IMPLEMENTED",
  "notes": "This story provides structural parity with REPL. Panel UI may implement this differently than CLI or may not need it at all."
}
```

**Key Fields for NOT IMPLEMENTED Stories:**
- `acceptance_criteria`: First line should be "NOT IMPLEMENTED - [reason]"
- `optional`: true (since not yet implemented)
- `priority`: 3 (lower priority)
- `implementation_status`: "NOT_IMPLEMENTED" (custom field for tracking)
- `notes`: Explain why the story exists and reference parallel REPL story

### Summary of Phase 1.5 Changes

**Panel Features:**
- **Split:** 2 features split into 4 features
- **Rename:** 1 feature renamed
- **Add:** 10-11 new stories for completeness
  - **1 IMPLEMENTED** (View Session Information - documents existing header)
  - **9-10 NOT IMPLEMENTED** (placeholders for future features, parallel to REPL)
- **Move:** 1 story moved to different feature
- **Result:** 4 original features → 7-8 aligned features

**Implementation Status:**
- Existing Panel stories: All IMPLEMENTED
- New stories for completeness: Marked as NOT IMPLEMENTED placeholders
- Purpose: Create structural parity with REPL even where Panel UI differs or features don't exist yet

**New story-graph.json sequential order for Panel:**
```
1.0 - Initialize Panel Session
1.2 - Manage Session
1.5 - View Bot State
2.0 - Navigate And Execute Behaviors
3.0 - Manage Scope
4.0 - View Action-Specific Instructions
5.0 - Get Help (optional)
```

---

#### Phase 2: Feature Level Renames (REPL Sub-Epic Only)

### Changes in `story-graph.json` → `epics[].sub_epics[].sub_epics[].name`

All features under "Invoke Bot Through REPL":

| Current Name | New Name | Sequential Order |
|--------------|----------|------------------|
| `"Initialize REPL Session"` | ✅ Keep as-is | 1 |
| *(none - NEW)* | `"Manage Session"` (NEW) | 1.5 |
| `"Navigate Bot Behaviors and Actions With CLI"` | `"Navigate Behaviors Using REPL Commands"` | 2 |
| `"Navigate Bot Behaviors and Actions Via Domain Model"` | `"Navigate Behaviors Using Domain Model"` | 2.5 |
| `"Execute Action Operation Through CLI"` | `"Execute Actions Using REPL"` | 3 |
| `"Manage Bot Scope Through CLI"` | `"Manage Scope Using REPL"` | 4 |
| `"Display Bot State Using CLI"` | `"Display State Using REPL"` | 5 |
| `"Get Help Using CLI"` | `"Get Help Using REPL"` | 6 |

**Note:** "Manage Session" is a NEW feature that organizes existing functionality (`status` and `path` commands) to parallel Panel's structure.

**Files to Update:**
- `agile_bot/bots/base_bot/docs/stories/story-graph.json` (lines ~5198, 5282, 5343, 5536, 5710, 6107)

**Folder Renames Required:**
```
NEW:    docs/stories/map/🎯 Invoke Bot/⚙️ Invoke Bot Through REPL/⚙️ Manage Session/ (NEW folder for organizing status/path commands)

BEFORE: docs/stories/map/🎯 Invoke Bot/⚙️ Invoke Bot Through REPL/⚙️ Navigate Bot Behaviors and Actions With CLI/
AFTER:  docs/stories/map/🎯 Invoke Bot/⚙️ Invoke Bot Through REPL/⚙️ Navigate Behaviors Using REPL Commands/

BEFORE: docs/stories/map/🎯 Invoke Bot/⚙️ Invoke Bot Through REPL/⚙️ Navigate Bot Behaviors and Actions Via Domain Model/
AFTER:  docs/stories/map/🎯 Invoke Bot/⚙️ Invoke Bot Through REPL/⚙️ Navigate Behaviors Using Domain Model/

BEFORE: docs/stories/map/🎯 Invoke Bot/⚙️ Invoke Bot Through REPL/⚙️ Execute Action Operation Through CLI/
AFTER:  docs/stories/map/🎯 Invoke Bot/⚙️ Invoke Bot Through REPL/⚙️ Execute Actions Using REPL/

BEFORE: docs/stories/map/🎯 Invoke Bot/⚙️ Invoke Bot Through REPL/⚙️ Manage Bot Scope Through CLI/
AFTER:  docs/stories/map/🎯 Invoke Bot/⚙️ Invoke Bot Through REPL/⚙️ Manage Scope Using REPL/

BEFORE: docs/stories/map/🎯 Invoke Bot/⚙️ Invoke Bot Through REPL/⚙️ Display Bot State Using CLI/
AFTER:  docs/stories/map/🎯 Invoke Bot/⚙️ Invoke Bot Through REPL/⚙️ Display State Using REPL/
```

---

#### Phase 3: Story Level Renames

### 3.1 Invoke Bot Directly Stories

**Location:** `story-graph.json` → `epics[].sub_epics[name="Invoke Bot Directly"].story_groups[].stories[]`

| Sequential Order | Current Name | New Name | Test Class Change |
|------------------|--------------|----------|-------------------|
| 1 | `"Invoke Behavior Actions In Workflow Order"` | `"Execute End-to-End Workflow"` | `TestInvokeBehaviorActionsInWorkflowOrder` → `TestExecuteEndToEndWorkflow` |
| 2 | `"Execute Behavior"` | `"Execute Behavior Action"` | `TestExecuteBehavior` → `TestExecuteBehaviorAction` |
| 3 | `"Insert Context Into Instructions"` | ✅ Keep | ✅ Keep |
| 4 | `"Inject Next Behavior Reminder"` | ✅ Keep | ✅ Keep |
| 5 | `"Close Current Action"` | `"Confirm Current Action"` | `TestCloseCurrentAction` → `TestConfirmCurrentAction` |
| 6 | `"Invoke Behavior In Action Order"` | `"Determine Action Order From State"` | `TestInvokeBehaviorInActionOrder` → `TestDetermineActionOrderFromState` |
| 7 | `"Inject Status Update Breadcrumbs Into Instructions"` | ✅ Keep | ✅ Keep |

**Test File:** `test_perform_behavior_action.py` → `test_invoke_bot_directly.py`

**Story File Renames Required:**
```
BEFORE: 📝 Invoke Behavior Actions In Workflow Order.md
AFTER:  📝 Execute End-to-End Workflow.md

BEFORE: 📝 Execute Behavior.md
AFTER:  📝 Execute Behavior Action.md

BEFORE: 📝 Close Current Action.md
AFTER:  📝 Confirm Current Action.md

BEFORE: 📝 Invoke Behavior In Action Order.md
AFTER:  📝 Determine Action Order From State.md
```

---

### 3.2 Invoke Bot Through Panel Stories

**Location:** `story-graph.json` → `epics[].sub_epics[name="Invoke Bot Through Panel"].sub_epics[]`

#### 3.2.1 Feature: Manage Bot Information → Split into Two Features

**Note:** This feature is being split in Phase 1.5. See Phase 1.5.2 for details.

Stories will be distributed as follows:

**Initialize Panel Session:**
| Sequential Order | Current Name | New Name |
|------------------|--------------|----------|
| 1 | `"Open Panel"` | ✅ Keep |
| NEW | N/A | `"Load Bot Configuration"` (NEW - documents existing) |

**Manage Session:**
| Sequential Order | Current Name | New Name |
|------------------|--------------|----------|
| 2 | `"Refresh Panel"` | `"Display Session Status"` (renamed to parallel REPL's `status` command) |
| 3 | `"Change Workspace Path"` | ✅ Keep |
| 4 | `"Switch Bot"` | ✅ Keep |
| 5 | `"Toggle Panel Section"` | ✅ Keep |

#### 3.2.2 Feature: Navigate Behavior Action Status
| Sequential Order | Current Name | New Name |
|------------------|--------------|----------|
| 1 | `"Display Hierarchy"` | `"View Behavior Hierarchy"` |
| 2 | `"Navigate Behavior Action"` | `"Navigate Sequentially"` |
| 3 | `"Execute Behavior Action"` | ✅ Keep |

**Story File Renames Required:**
```
BEFORE: 📝 Display Hierarchy.md
AFTER:  📝 View Behavior Hierarchy.md

BEFORE: 📝 Navigate Behavior Action.md
AFTER:  📝 Navigate Sequentially.md
```

#### 3.2.3 Feature: Filter And Navigate Scope
| Sequential Order | Current Name | New Name |
|------------------|--------------|----------|
| 1 | `"Filter Story Scope"` | `"Set Story Scope"` |
| 2 | `"Display Story Scope Hierarchy"` | `"View Story Scope Hierarchy"` |
| 3 | `"Filter File Scope"` | `"Set File Scope"` |
| 4 | `"Open Story Files"` | ✅ Keep |

**Story File Renames Required:**
```
BEFORE: 📝 Filter Story Scope.md
AFTER:  📝 Set Story Scope.md

BEFORE: 📝 Display Story Scope Hierarchy.md
AFTER:  📝 View Story Scope Hierarchy.md

BEFORE: 📝 Filter File Scope.md
AFTER:  📝 Set File Scope.md
```

#### 3.2.4 Feature: Display Instructions
| Sequential Order | Current Name | New Name |
|------------------|--------------|----------|
| 1 | `"Display Base Instructions"` | `"View Base Instructions"` |
| 2 | `"Display Clarify Instructions"` | `"View Clarify Instructions"` |
| 3 | `"Display Strategy Instructions"` | `"View Strategy Instructions"` |
| 4 | `"Display Build Instructions"` | `"View Build Instructions"` |
| 5 | `"Display Validate Instructions"` | `"View Validate Instructions"` |
| 6 | `"Display Render Instructions"` | `"View Render Instructions"` |
| 7 | `"Display Instructions In Raw Format"` | `"View Instructions In Raw Format"` |
| 8 | `"Submit Instructions To Chat"` | ✅ Keep |

**Story File Renames Required:**
```
BEFORE: 📝 Display Base Instructions.md
AFTER:  📝 View Base Instructions.md

BEFORE: 📝 Display Clarify Instructions.md
AFTER:  📝 View Clarify Instructions.md

BEFORE: 📝 Display Strategy Instructions.md
AFTER:  📝 View Strategy Instructions.md

BEFORE: 📝 Display Build Instructions.md
AFTER:  📝 View Build Instructions.md

BEFORE: 📝 Display Validate Instructions.md
AFTER:  📝 View Validate Instructions.md

BEFORE: 📝 Display Render Instructions.md
AFTER:  📝 View Render Instructions.md

BEFORE: 📝 Display Instructions In Raw Format.md
AFTER:  📝 View Instructions In Raw Format.md
```

---

### 3.3 Invoke Bot Through REPL Stories

#### 3.3.1 Feature: Initialize REPL Session
| Sequential Order | Current Name | New Name | Test Class Change |
|------------------|--------------|----------|-------------------|
| 1 | `"Launch CLI in Interactive Mode"` | `"Start REPL Session"` | `TestLaunchCLIInInteractiveMode` → `TestStartREPLSession` |
| 2 | `"Launch CLI in Pipe Mode"` | `"Start REPL in Pipe Mode"` | `TestLaunchCLIInPipeMode` → `TestStartREPLInPipeMode` |
| 3 | `"Display Piped Mode Instructions for AI Agents"` | ✅ Keep | ✅ Keep |
| 4 | `"Detect and Configure TTY/Non-TTY Input for CLI"` | `"Detect and Configure TTY/Non-TTY Input"` | Keep class |
| 5 | `"Load and Display Workspace Context in CLI"` | `"Load Workspace Context"` | `TestLoadAndDisplayWorkspaceContextInCLI` → `TestLoadWorkspaceContext` |
| 6 | `"Load All Registered Bots"` | ✅ Keep | N/A |

**Test File:** Keep `test_initialize_repl_session.py`

**Story File Renames Required:**
```
BEFORE: 📝 Launch CLI in Interactive Mode.md
AFTER:  📝 Start REPL Session.md

BEFORE: 📝 Launch CLI in Pipe Mode.md (if exists)
AFTER:  📝 Start REPL in Pipe Mode.md

BEFORE: 📝 Detect and Configure TTY-Non-TTY Input for CLI.md
AFTER:  📝 Detect and Configure TTY-Non-TTY Input.md

BEFORE: 📝 Load and Display Workspace Context in CLI.md
AFTER:  📝 Load Workspace Context.md
```

#### 3.3.2 Feature: Navigate Behaviors Using REPL Commands
| Sequential Order | Current Name | New Name | Test Class Change |
|------------------|--------------|----------|-------------------|
| 1 | `"Navigate Using CLI Dot Notation"` | `"Navigate To Behavior Action And Execute"` | `TestNavigateUsingCLIDotNotation` → `TestNavigateToBehaviorActionAndExecute` |
| 2 | `"Navigate Sequentially Using CLI Commands"` | `"Navigate Sequentially"` | `TestNavigateSequentiallyUsingCLICommands` → `TestNavigateSequentially` |
| 3 | `"Exit CLI REPL"` | `"Exit REPL"` | `TestExitCLIREPL` → `TestExitREPL` |

**Test File:** `test_navigate_bot_behaviors_and_actions_with_cli_current.py` → `test_navigate_behaviors_using_repl_commands.py`

**Story File Renames Required:**
```
BEFORE: 📝 Navigate Using CLI Dot Notation.md
AFTER:  📝 Navigate To Behavior Action And Execute.md

BEFORE: 📝 Navigate Sequentially Using CLI Commands.md
AFTER:  📝 Navigate Sequentially.md

BEFORE: 📝 Exit CLI REPL.md
AFTER:  📝 Exit REPL.md
```

#### 3.3.3 Feature: Navigate Behaviors Using Domain Model
| Sequential Order | Current Name | New Name | Test Class Change |
|------------------|--------------|----------|-------------------|
| 1 | `"Navigate To First Behavior Action"` | `"Navigate To Behavior Action And Execute"` | `TestNavigateToFirstBehaviorAction` → `TestNavigateToBehaviorActionAndExecute` |
| 2 | `"Advance Action And Persist State"` | ❌ REMOVED (obsolete) | ❌ Remove test |
| 3 → 2 | `"Show Remaining Actions After Completion"` | ✅ Keep (renumber: 3→2) | ✅ Keep |

**Test File:** `test_navigate_bot_behaviors_and_actions_with_cli.py` → `test_navigate_behaviors_using_domain_model.py`

**Story File Renames Required:**
```
BEFORE: 📝 Navigate To First Behavior Action.md
AFTER:  📝 Navigate To Behavior Action And Execute.md

BEFORE: 📝 Advance Action And Persist State.md
AFTER:  ❌ REMOVED (obsolete - no longer needed)

📝 Show Remaining Actions After Completion.md [NO CHANGE - renumber from #3 to #2]
```

#### 3.3.4 Feature: Execute Actions Using REPL
| Sequential Order | Current Name | New Name | Test Class Change |
|------------------|--------------|----------|-------------------|
| 1 | `"Get Action Instructions Through CLI"` | `"View Instructions"` | `TestGetActionInstructionsThroughCLI` → `TestViewInstructions` |
| 2 | `"Confirm Work Through CLI with String Parameters"` | `"Confirm With Parameters"` | `TestConfirmWorkThroughCLIWithStringParameters` → `TestConfirmWithParameters` |
| 3 | `"Confirm Action Completion Through CLI"` | `"Confirm Action Completion"` | `TestConfirmActionCompletionThroughCLI` → `TestConfirmActionCompletion` |
| 4 | `"Auto-Confirm Action After Instructions Complete"` | `"Auto-Confirm Action"` | Keep class name |
| 5 | `"Re-execute Current Operation Using CLI"` | `"Re-execute Current Action"` | `TestReExecuteCurrentOperationUsingCLI` → `TestReExecuteCurrentAction` |
| 6 | `"Handle Operation Errors and Validation in CLI"` | `"Handle Errors and Validation"` | `TestHandleOperationErrorsAndValidationInCLI` → `TestHandleErrorsAndValidation` |
| 7 | `"Invoke Specific Bot Behavior Command through CLI"` | `"Execute Behavior Action"` | Keep or rename to match |

**Test File:** `test_execute_action_operation_through_cli.py` → `test_execute_actions_using_repl.py`

**Story File Renames Required:**
```
BEFORE: 📝 Get Action Instructions Through CLI.md
AFTER:  📝 View Instructions.md

BEFORE: 📝 Confirm Work Through CLI with String Parameters.md
AFTER:  📝 Confirm With Parameters.md

BEFORE: 📝 Confirm Action Completion Through CLI.md
AFTER:  📝 Confirm Action Completion.md

BEFORE: 📝 Auto-Confirm Action After Instructions Complete.md
AFTER:  📝 Auto-Confirm Action.md

BEFORE: 📝 Re-execute Current Operation Using CLI.md
AFTER:  📝 Re-execute Current Action.md

BEFORE: 📝 Handle Operation Errors and Validation in CLI.md
AFTER:  📝 Handle Errors and Validation.md

BEFORE: 📝 Invoke Specific Bot Behavior Command through CLI.md
AFTER:  📝 Execute Behavior Action.md
```

#### 3.3.5 Feature: Manage Scope Using REPL
| Sequential Order | Current Name | New Name | Test Class Change |
|------------------|--------------|----------|-------------------|
| 1 | `"Set Scope Through CLI Using String Parameters"` | `"Set Scope"` | Keep class name |
| 2 | `"Filter Work Using Knowledge Graph Scope in CLI"` | `"Set Story Scope"` | `TestFilterWorkUsingKnowledgeGraphScopeInCLI` → `TestSetStoryScope` |
| 3 | `"Filter Work Using Files Scope in CLI"` | `"Set File Scope"` | Keep or rename |
| 4 | `"Validate Scope Against Story Graph in CLI"` | `"Validate Scope Against Story Graph"` | Keep class name |
| 5 | `"Pass Scope Parameters When Executing Actions Through CLI"` | `"Pass Scope Parameters When Executing Actions"` | Keep class name |
| 6 | `"View Current Scope in CLI"` | `"View Current Scope"` | Keep class name |
| 7 | `"Clear Scope Through CLI"` | `"Clear Scope"` | Keep class name |
| 8 | `"Enforce Mutually Exclusive Scope Types"` | ✅ Keep | ✅ Keep |

**Test File:** `test_manage_bot_scope_through_cli.py` → `test_manage_scope_using_repl.py`

**Story File Renames Required:**
```
BEFORE: 📝 Set Scope Through CLI Using String Parameters.md
AFTER:  📝 Set Scope.md

BEFORE: 📝 Filter Work Using Knowledge Graph Scope in CLI.md
AFTER:  📝 Set Story Scope.md

BEFORE: 📝 Filter Work Using Files Scope in CLI.md
AFTER:  📝 Set File Scope.md

BEFORE: 📝 Validate Scope Against Story Graph in CLI.md
AFTER:  📝 Validate Scope Against Story Graph.md

BEFORE: 📝 View Current Scope in CLI.md
AFTER:  📝 View Current Scope.md

BEFORE: 📝 Clear Scope Through CLI.md
AFTER:  📝 Clear Scope.md
```

#### 3.3.6 Feature: Display State Using REPL
| Sequential Order | Current Name | New Name | Test Class Change |
|------------------|--------------|----------|-------------------|
| 1 | `"Display CLI Header"` | `"View Session Header"` | `TestDisplayCLIHeader` → `TestViewSessionHeader` |
| 2 | `"Display Bot Hierarchy Tree with Progress Indicators"` | `"View Behavior Hierarchy"` | `TestDisplayBotHierarchyTreeInCLI` → `TestViewBehaviorHierarchy` |
| 3 | `"Display Current Position in CLI"` | `"View Current Position"` | `TestDisplayCurrentPositionInCLI` → `TestViewCurrentPosition` |
| 4 | `"Display Active Scope in CLI Status"` | `"View Active Scope"` | `TestDisplayActiveScopeInCLIStatus` → `TestViewActiveScope` |
| 5 | `"Display CLI Navigation Menu Footer"` | `"View Navigation Commands"` | `TestDisplayCLINavigationMenuFooter` → `TestViewNavigationCommands` |
| 6 | `"Display Headless Mode Status in CLI"` | `"View Headless Mode Status"` | `TestDisplayHeadlessModeStatusInCLI` → `TestViewHeadlessModeStatus` |
| 7 | `"Display Available Bot in Tree Hierarchy"` | `"View Available Bots"` | `TestDisplayAvailableBotInTreeHierarchy` → `TestViewAvailableBots` |
| 8 | `"Display CLI Bot Command in Navigation Menu Footer"` | *(Consider merging with #5)* | *(Consider merging)* |
| 9 | `"Format Output For AI"` | ✅ Keep | ✅ Keep |

**Test File:** `test_display_bot_state_using_cli.py` → `test_display_state_using_repl.py`

**Story File Renames Required:**
```
BEFORE: 📝 Display CLI Header.md
AFTER:  📝 View Session Header.md

BEFORE: 📝 Display Bot Hierarchy Tree with Progress Indicators.md
AFTER:  📝 View Behavior Hierarchy.md

BEFORE: 📝 Display Current Position in CLI.md
AFTER:  📝 View Current Position.md

BEFORE: 📝 Display Active Scope in CLI Status.md
AFTER:  📝 View Active Scope.md

BEFORE: 📝 Display CLI Navigation Menu Footer.md
AFTER:  📝 View Navigation Commands.md

BEFORE: 📝 Display Headless Mode Status in CLI.md
AFTER:  📝 View Headless Mode Status.md

BEFORE: 📝 Display Available Bot in Tree Hierarchy.md
AFTER:  📝 View Available Bots.md
```

#### 3.3.7 Feature: Get Help Using REPL
| Sequential Order | Current Name | New Name |
|------------------|--------------|----------|
| 1 | `"Request Action Help Through CLI"` | `"Request Action Help"` |
| 2 | `"View Command Examples in CLI"` | `"View Command Examples"` |
| 3 | `"View Parameter Documentation in CLI"` | `"View Parameter Documentation"` |

**Test File:** `test_get_help_using_cli_current.py` → `test_get_help_using_repl.py`

**Story File Renames Required:**
```
BEFORE: 📝 Request Action Help Through CLI.md
AFTER:  📝 Request Action Help.md

BEFORE: 📝 View Command Examples in CLI.md (if exists)
AFTER:  📝 View Command Examples.md

BEFORE: 📝 View Parameter Documentation in CLI.md (if exists)
AFTER:  📝 View Parameter Documentation.md
```

---

#### Phase 4: Test File Updates

### 4.1 Test File Renames

| Current Test File | New Test File | Location |
|-------------------|---------------|----------|
| `test_perform_behavior_action.py` | `test_invoke_bot_directly.py` | `agile_bot/bots/base_bot/test/` |
| `test_navigate_bot_behaviors_and_actions_with_cli_current.py` | `test_navigate_behaviors_using_repl_commands.py` | `agile_bot/bots/base_bot/test/` |
| `test_navigate_bot_behaviors_and_actions_with_cli.py` | `test_navigate_behaviors_using_domain_model.py` | `agile_bot/bots/base_bot/test/` |
| `test_execute_action_operation_through_cli.py` | `test_execute_actions_using_repl.py` | `agile_bot/bots/base_bot/test/` |
| `test_manage_bot_scope_through_cli.py` | `test_manage_scope_using_repl.py` | `agile_bot/bots/base_bot/test/` |
| `test_display_bot_state_using_cli.py` | `test_display_state_using_repl.py` | `agile_bot/bots/base_bot/test/` |
| `test_get_help_using_cli_current.py` | `test_get_help_using_repl.py` | `agile_bot/bots/base_bot/test/` |

### 4.2 Test Class Renames (Within Files)

#### In `test_invoke_bot_directly.py` (was `test_perform_behavior_action.py`)
```python
# BEFORE → AFTER
TestInvokeBehaviorActionsInWorkflowOrder → TestExecuteEndToEndWorkflow
TestExecuteBehavior → TestExecuteBehaviorAction
TestCloseCurrentAction → TestConfirmCurrentAction
TestInvokeBehaviorInActionOrder → TestDetermineActionOrderFromState
```

#### In `test_initialize_repl_session.py`
```python
# BEFORE → AFTER
TestLaunchCLIInInteractiveMode → TestStartREPLSession
TestLaunchCLIInPipeMode → TestStartREPLInPipeMode
TestLoadAndDisplayWorkspaceContextInCLI → TestLoadWorkspaceContext
```

#### In `test_navigate_behaviors_using_repl_commands.py` (was `test_navigate_bot_behaviors_and_actions_with_cli_current.py`)
```python
# BEFORE → AFTER
TestNavigateUsingCLIDotNotation → TestNavigateToBehaviorAction
TestNavigateSequentiallyUsingCLICommands → TestNavigateSequentially
TestExitCLIREPL → TestExitREPL
```

#### In `test_execute_actions_using_repl.py` (was `test_execute_action_operation_through_cli.py`)
```python
# BEFORE → AFTER
TestGetActionInstructionsThroughCLI → TestViewInstructions
TestConfirmWorkThroughCLIWithStringParameters → TestConfirmWithParameters
TestConfirmActionCompletionThroughCLI → TestConfirmActionCompletion
TestReExecuteCurrentOperationUsingCLI → TestReExecuteCurrentAction
TestHandleOperationErrorsAndValidationInCLI → TestHandleErrorsAndValidation
```

#### In `test_manage_scope_using_repl.py` (was `test_manage_bot_scope_through_cli.py`)
```python
# BEFORE → AFTER
TestFilterWorkUsingKnowledgeGraphScopeInCLI → TestSetStoryScope
```

#### In `test_display_state_using_repl.py` (was `test_display_bot_state_using_cli.py`)
```python
# BEFORE → AFTER
TestDisplayCLIHeader → TestViewSessionHeader
TestDisplayBotHierarchyTreeInCLI → TestViewBehaviorHierarchy
TestDisplayCurrentPositionInCLI → TestViewCurrentPosition
TestDisplayActiveScopeInCLIStatus → TestViewActiveScope
TestDisplayCLINavigationMenuFooter → TestViewNavigationCommands
TestDisplayHeadlessModeStatusInCLI → TestViewHeadlessModeStatus
TestDisplayAvailableBotInTreeHierarchy → TestViewAvailableBots
```

---

#### Phase 5: Update story-graph.json References

After renaming test files and test classes, update all references in `story-graph.json`:

### 5.1 Update `test_file` Fields

Search for and update all `"test_file"` entries in sub-epics:

```json
// BEFORE
"test_file": "test_perform_behavior_action.py"
// AFTER
"test_file": "test_invoke_bot_directly.py"

// BEFORE
"test_file": "test_navigate_bot_behaviors_and_actions_with_cli_current.py"
// AFTER
"test_file": "test_navigate_behaviors_using_repl_commands.py"

// ... (similar for all renamed test files)
```

### 5.2 Update `test_class` Fields

Search for and update all `"test_class"` entries in stories:

```json
// Examples:
"test_class": "TestExecuteEndToEndWorkflow"
"test_class": "TestExecuteBehaviorAction"
"test_class": "TestConfirmCurrentAction"
"test_class": "TestDetermineActionOrderFromState"
// ... etc.
```

---

#### Phase 6: Implementation Order

### Step 1: Backup
```bash
# Create backup of story-graph.json
cp agile_bot/bots/base_bot/docs/stories/story-graph.json \
   agile_bot/bots/base_bot/docs/stories/story-graph.json.backup
```

### Step 2: Update story-graph.json
1. Update sub-epic names (2 changes)
2. Update feature names (7 changes)
3. Update story names (46 changes)
4. Update test_file references (7 changes)
5. Update test_class references (~20 changes)

### Step 3: Rename Test Files
```bash
cd agile_bot/bots/base_bot/test/

# Rename test files using git mv to preserve history
git mv test_perform_behavior_action.py test_invoke_bot_directly.py
git mv test_navigate_bot_behaviors_and_actions_with_cli_current.py test_navigate_behaviors_using_repl_commands.py
git mv test_navigate_bot_behaviors_and_actions_with_cli.py test_navigate_behaviors_using_domain_model.py
git mv test_execute_action_operation_through_cli.py test_execute_actions_using_repl.py
git mv test_manage_bot_scope_through_cli.py test_manage_scope_using_repl.py
git mv test_display_bot_state_using_cli.py test_display_state_using_repl.py
git mv test_get_help_using_cli_current.py test_get_help_using_repl.py
```

### Step 4: Update Test Class Names
- Use search-replace in each test file to rename test classes
- Run tests after each file to ensure no breakage

### Step 5: Rename Story Folders
```bash
cd agile_bot/bots/base_bot/docs/stories/map/🎯\ Invoke\ Bot/

# Rename sub-epic folders
git mv "⚙️ Perform Behavior Action" "⚙️ Invoke Bot Directly"
git mv "⚙️ Run Interactive REPL" "⚙️ Invoke Bot Through REPL"

# Rename feature folders under REPL
cd "⚙️ Invoke Bot Through REPL"
git mv "⚙️ Navigate Bot Behaviors and Actions With CLI" "⚙️ Navigate Behaviors Using REPL Commands"
git mv "⚙️ Navigate Bot Behaviors and Actions Via Domain Model" "⚙️ Navigate Behaviors Using Domain Model"
git mv "⚙️ Execute Action Operation Through CLI" "⚙️ Execute Actions Using REPL"
git mv "⚙️ Manage Bot Scope Through CLI" "⚙️ Manage Scope Using REPL"
git mv "⚙️ Display Bot State Using CLI" "⚙️ Display State Using REPL"
```

### Step 6: Rename Story Files
- Rename individual story markdown files according to the plan
- Use `git mv` to preserve history

### Step 7: Validation
```bash
# Run all tests to ensure nothing broke
python -m pytest agile_bot/bots/base_bot/test/test_invoke_bot_directly.py -v
python -m pytest agile_bot/bots/base_bot/test/test_navigate_behaviors_using_repl_commands.py -v
# ... (run all renamed test files)

# Validate story-graph.json
python -m json.tool agile_bot/bots/base_bot/docs/stories/story-graph.json > /dev/null
```

### Step 8: Generate Updated Documentation
```bash
# Regenerate any auto-generated documentation
# (if applicable)
```

---

#### Phase 7: Verification Checklist

- [ ] All sub-epic names updated in story-graph.json
- [ ] All feature names updated in story-graph.json
- [ ] All story names updated in story-graph.json
- [ ] All test_file references updated in story-graph.json
- [ ] All test_class references updated in story-graph.json
- [ ] All test files renamed
- [ ] All test class names updated in test files
- [ ] All sub-epic folders renamed
- [ ] All feature folders renamed
- [ ] All story files renamed
- [ ] All tests pass
- [ ] story-graph.json validates as proper JSON
- [ ] No broken references in story-graph.json

---

### G. Summary of Changes (Reference)

### Consistency Achieved:

**Terminology:**
- ✅ "Execute Behavior Action" - Consistent across Direct, Panel, and REPL
- ✅ "Navigate To Behavior Action" - Consistent navigation terminology
- ✅ "Navigate Sequentially" - Identical in Panel and REPL
- ✅ "View [X]" - User perspective for all display operations
- ✅ "Confirm" - Consistent action completion terminology
- ✅ "Set [X] Scope" - Consistent scope setting
- ✅ No redundant "Through/Using/In CLI" phrases
- ✅ Clear distinction between integration tests and unit tests

**Structure:**
- ✅ Panel and REPL features now parallel each other conceptually
- ✅ Session management split: Initialize vs Manage (both contexts)
- ✅ State viewing as dedicated feature (both contexts)
- ✅ Navigation separated from state viewing (both contexts)
- ✅ Scope management complete and parallel (both contexts)
- ✅ Feature names reflect scope and granularity accurately

### File Changes:

**Phase 1 (Sub-Epics):**
- 2 sub-epic folder renames
- 2 sub-epic name changes in story-graph.json

**Phase 1.5 (Structural Alignment - Panel):**
- 2 features split into 4 features
- 3 new feature folders created
- 1 feature renamed
- 10-11 new story files created (1 IMPLEMENTED, 9-10 NOT IMPL placeholders)
- 1 story moved between features
- ~25 field updates in story-graph.json for Panel features

**Phase 2 (Feature Renames - REPL):**
- 7 feature folder renames
- 1 NEW feature folder created ("Manage Session")
- 7 feature name changes + 1 new feature in story-graph.json

**Phase 3 (Story Renames):**
- Direct: 4 story renames + 2 test class renames
- Panel: 14 original + 6 new = 20 total story changes
- REPL: 28 story renames + ~20 test class renames
- Total: ~52 story file renames

**Phase 4 (Test Files):**
- 7 test file renames
- ~20 test class renames within files

**Phase 5 (story-graph.json Updates):**
- Sub-epic names: 2 changes
- Feature names: 10 changes (7 REPL + 3 Panel restructure)
- Story names: 52 changes
- Test file references: 7 changes
- Test class references: 20 changes
- New stories: 6-9 additions
- **Total story-graph.json changes: ~100 field updates**

### Total Project Impact:

**Folders:**
- 2 sub-epic folders renamed
- 11 feature folders (7 renamed + 4 new: 3 Panel splits + 1 REPL "Manage Session")
- ~53 story files renamed/created (includes "Refresh Panel" → "Display Session Status")

**Code:**
- 7 test files renamed
- ~20 test classes renamed
- All import statements updated

**Documentation:**
- 1 story-graph.json with ~100 updates
- All folder/file references updated

**Final Structure:**
- Panel: 4 features → 5 features (flatter, combined Init+Manage into single feature)
- REPL: 7 features → 6 features (flatter, combined Init+Manage into single feature)
- Direct: 7 stories (improved naming)
- **Scenarios vs Stories:** Granular items moved to scenarios within parent stories (not separate stories)
- **Near Perfect Parity:** Panel (5) and REPL (6) have similar structure
- Total consistency: 98%+ across all three invocation methods

---

### B. Final Parallel Structure (Reference)

### Side-by-Side Feature Comparison

| Concept | Direct (Core Bot) | Panel Feature | REPL Feature | Stories in Common |
|---------|-------------------|---------------|--------------|-------------------|
| **Initialize** | N/A (internal) | Initialize Panel Session | Initialize REPL Session | Open/Start, Load Configuration |
| **Navigate** | Navigate And Execute Behaviors | Navigate And Execute Behaviors | Navigate Using REPL Commands + Navigate Using Domain Model | Navigate To Behavior Action And Execute, Navigate Sequentially |
| **Scope** | Manage Scope | Manage Scope | Manage Scope Using REPL | Set Story/File Scope, Filter By Scope, Pass Scope To Actions, Clear Scope |
| **Generate Instructions** | Generate Action Instructions | *(internal - uses bot)* | *(internal - uses bot)* | Load Config, Merge Instructions, Load/Inject Guardrails, Inject Context |
| **View Instructions** | View Action-Specific Instructions | View Action-Specific Instructions | View Action-Specific Instructions | View Base/Clarify/Strategy/Build/Validate/Render Instructions, Submit To AI |
| **State** | Track Workflow State | N/A (uses bot state) | N/A (uses bot state) | Save/Load State, Determine Resume Point, Confirm Action, Inject Next Action |
| **Activity** | Track Activity | N/A (uses bot logging) | N/A (uses bot logging) | Track Start/Completion, Record Metrics |
| **Help** | N/A (channel-specific) | Get Help | Get Help Using REPL | Display Action Help, Display Parameter Help, Display Command Examples |

### Complete Feature List (Final)

**INVOKE BOT DIRECTLY (Domain Model):**
```
Feature Groups:
├─ Navigate And Execute Behaviors
│  ├─ Navigate To Behavior Action And Execute
│  ├─ Navigate Sequentially (Determine Action Order From State)
│  └─ Execute End-to-End Workflow (integration test)
├─ Manage Scope
│  ├─ Set Story Scope (SCENARIO: Enforce Mutually Exclusive Scope Types)
│  ├─ Set File Scope
│  ├─ Filter Knowledge Graph By Scope
│  ├─ Pass Scope Parameters To Actions
│  └─ Clear Scope
├─ Generate Action Instructions
│  ├─ Load Base Action Configuration
│  ├─ Load And Merge Behavior-Specific Instructions
│  ├─ Load Guardrails From Behavior Folder
│  ├─ Inject Guardrails Into Instructions
│  ├─ Inject Context Into Instructions (SCENARIOS: Inject Next Behavior Reminder, Inject Status Breadcrumbs)
│  └─ Get Action Instructions (returns merged instructions)
├─ View Action-Specific Instructions
│  ├─ View Base Instructions
│  ├─ View Clarify Instructions (includes clarification.json data)
│  ├─ View Strategy Instructions (includes strategy.json data)
│  ├─ View Build Instructions (includes knowledge graph template)
│  ├─ View Validate Instructions (includes validation rules)
│  ├─ View Render Instructions (includes render configs)
│  ├─ View Instructions In Raw Format
│  └─ Submit Instructions To AI Agent
├─ Track Workflow State
│  ├─ Save Workflow State
│  ├─ Load Workflow State
│  ├─ Determine Resume Point After Interruption
│  ├─ Confirm Current Action
│  ├─ Inject Next Action Instructions
│  └─ Transition To Next Action
└─ Track Activity
   ├─ Track Action Start
   ├─ Track Action Completion
   └─ Record Activity Metrics And Paths
```

**INVOKE BOT THROUGH PANEL (GUI):**
```
Feature Groups:
├─ Initialize Panel Session
│  ├─ Open Panel
│  └─ Load Bot Configuration
├─ Manage Session
│  ├─ Display Session Status
│  ├─ Change Workspace Path
│  ├─ Switch Bot
│  └─ Toggle Panel Section
├─ View Bot State
│  ├─ View Session Header (IMPL)
│  ├─ View Behavior Hierarchy (IMPL)
│  ├─ View Current Position (NOT IMPL)
│  ├─ View Active Scope (NOT IMPL)
│  ├─ View Available Bots (IMPL)
│  └─ View Navigation Commands (NOT IMPL)
├─ Navigate And Execute Behaviors
│  ├─ Navigate Sequentially
│  └─ Navigate To Behavior Action And Execute
├─ Manage Scope
│  ├─ Set Story Scope (IMPLEMENTED)
│  ├─ Set File Scope (IMPLEMENTED)
│  ├─ View Story Scope Hierarchy (IMPLEMENTED)
│  ├─ View Current Scope (NOT IMPL)
│  ├─ Clear Scope (NOT IMPL)
│  └─ Validate Scope (NOT IMPL)
├─ View Action-Specific Instructions
│  ├─ View Base Instructions
│  ├─ View Clarify Instructions
│  ├─ View Strategy Instructions
│  ├─ View Build Instructions
│  ├─ View Validate Instructions
│  ├─ View Render Instructions
│  ├─ View Instructions In Raw Format
│  └─ Submit Instructions To Chat
└─ Get Help
   ├─ Display Action Help Using Panel (NOT IMPL)
   ├─ Display Parameter Help Using Panel (NOT IMPL)
   └─ Display Command Examples Using Panel (NOT IMPL)
```

**INVOKE BOT THROUGH REPL (CLI):**
```
Feature Groups:
├─ Initialize REPL Session
│  ├─ Start REPL Session
│  ├─ Start REPL in Pipe Mode
│  ├─ Display Piped Mode Instructions
│  ├─ Detect and Configure TTY/Non-TTY Input
│  ├─ Load Workspace Context
│  └─ Load All Registered Bots
├─ Manage Session (NEW - organizes existing `status` and `path` commands)
│  ├─ Display Session Status (via `status` command - parallel to Panel)
│  ├─ Change Workspace Path (via `path` command)
│  └─ Switch Bot (if capability exists)
├─ Navigate Behaviors Using REPL Commands
│  ├─ Navigate To Behavior Action And Execute
│  ├─ Navigate Sequentially
│  └─ Exit REPL
├─ Navigate Behaviors Using Domain Model
│  ├─ Navigate To Behavior Action And Execute
│  └─ Show Remaining Actions After Completion
├─ View Action-Specific Instructions
│  ├─ View Base Instructions
│  ├─ View Clarify Instructions
│  ├─ View Strategy Instructions
│  ├─ View Build Instructions
│  ├─ View Validate Instructions
│  ├─ View Render Instructions
│  ├─ View Instructions In Raw Format
│  └─ Submit Instructions To AI Agent
├─ Manage Scope Using REPL
│  ├─ Set Scope
│  ├─ Set Story Scope
│  ├─ Set File Scope
│  ├─ Validate Scope Against Story Graph
│  ├─ Pass Scope Parameters When Executing Actions
│  ├─ View Current Scope
│  ├─ Clear Scope
│  └─ Enforce Mutually Exclusive Scope Types
├─ Display State Using REPL
│  ├─ View Session Header (IMPL)
│  ├─ View Behavior Hierarchy (IMPL)
│  ├─ View Current Position (IMPL)
│  ├─ View Active Scope (IMPL)
│  ├─ View Navigation Commands (IMPL)
│  └─ View Available Bots (IMPL)
└─ Get Help Using REPL
   ├─ Display Action Help Using CLI (IMPL - renamed from "Request Action Help Through CLI")
   ├─ Display Parameter Help Using CLI (IMPL - renamed from "View Parameter Documentation in CLI")
   └─ Display Command Examples Using CLI (IMPL - renamed from "View Command Examples in CLI")
```

### Consistency Metrics (Final)

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| **Feature Structure Similarity** | 40% | 98% | +58% |
| **Story Naming Consistency** | 55% | 98% | +43% |
| **Parallel Concepts Clearly Mapped** | 3/7 concepts | 7/7 concepts | 100% |
| **Redundant Phrases Removed** | 0 removed | 30+ removed | Complete |
| **Obsolete Stories Removed** | 0 removed | 3 removed | "Confirm And Advance", "View Headless Mode", "Format Output For AI" |
| **User-Centric Language** | Mixed | Consistent | 100% |
| **Test Coverage Alignment** | Partial | Complete | 100% |
| **Panel/REPL Feature Parity** | 4 vs 7 features | 5 vs 6 features | Near perfect parity (flatter structure) |
| **Direct Feature Organization** | 7 flat stories | 6 feature groups (33 stories) | Clear architecture |
| **Duplicate Stories Across Sub-Epics** | ~110+ duplicates (80%) | ~20 consolidated generics (0% duplication) | Eliminated massive redundancy |

---

### I. Consolidated Future State Hierarchy (Reference)

**NOTE:** Items indented beyond the normal story level are **scenarios within a story**, not separate stories. These represent specific test cases or acceptance criteria that belong to the parent story but aren't substantial enough to be independent stories.

**INVOKE BOT DIRECTLY**
1. Navigate And Execute Behaviors
   - Navigate To Behavior Action And Execute
   - Navigate Sequentially (Determine Action Order From State)
   - Execute End-to-End Workflow (integration test)
2. Manage Scope
   - Set Story Scope (SCENARIO: Enforce Mutually Exclusive Scope Types)
   - Set File Scope
   - Filter Knowledge Graph By Scope
   - Pass Scope Parameters To Actions
   - Clear Scope
3. Generate Action Instructions
   - Load Base Action Configuration
   - Load And Merge Behavior-Specific Instructions
   - Load Guardrails From Behavior Folder
   - Inject Guardrails Into Instructions
   - Inject Context Into Instructions (SCENARIOS: Inject Next Behavior Reminder, Inject Status Breadcrumbs)
   - Get Action Instructions (returns merged instructions)
4. View Action-Specific Instructions
   - View Base Instructions
   - View Clarify Instructions (includes clarification.json data)
   - View Strategy Instructions (includes strategy.json data)
   - View Build Instructions (includes knowledge graph template)
   - View Validate Instructions (includes validation rules)
   - View Render Instructions (includes render configs)
   - View Instructions In Raw Format
   - Submit Instructions To AI Agent
5. Track Workflow State
   - Save Workflow State
   - Load Workflow State
   - Determine Resume Point After Interruption
   - Confirm Current Action
   - Inject Next Action Instructions
   - Transition To Next Action
6. Track Activity
   - Track Action Start
   - Track Action Completion
   - Record Activity Metrics And Paths

**INVOKE BOT THROUGH PANEL**
1. Manage Panel Session
   - Open Panel
   - Load Bot Configuration
   - Display Session Header (IMPL)
   - Display Bot Status
   - Manage Workspace Path
   - Switch Bot
   - Toggle Panel Section
2. Navigate And Execute Behaviors
   - Display Behavior Action Hierarchy (SCENARIO: includes Display Behavior Hierarchy, Display Current Position, Display Navigation Commands)
   - Navigate Sequentially
   - Navigate To Behavior Action And Execute
3. Manage Scope
   - Set Story Scope (IMPL) (SCENARIO: Enforce Mutually Exclusive Scope Types)
   - Set File Scope (NOT IMPL)
   - View Story Scope Hierarchy (IMPL)
   - View Current Scope (IMPL)
   - Clear Scope (IMPL)
4. View Action-Specific Instructions
   - View Base Instructions
   - Display Clarify Instructions
   - Display Strategy Instructions
   - Display Build Instructions
   - Display Validate Instructions
   - Display Render Instructions
   - Display Instructions In Raw Format
   - Submit Instructions To Chat
5. Get Help
   - Display Action Help Using Panel (NOT IMPL)
   - Display Parameter Help Using Panel (NOT IMPL)
   - Display Command Examples Using Panel (NOT IMPL)

**INVOKE BOT THROUGH REPL**
1. Manage REPL Session
   - Start REPL Session (SCENARIO: Start REPL in JSON Mode)
   - Start REPL in Pipe Mode
   - Display Piped Mode Instructions
   - Detect and Configure TTY/Non-TTY Input
   - Display Session Header (IMPL)
   - Display Bot Status
   - Manage Workspace Path (SCENARIO: Switch Bots)
   - Switch Bot
2. Display State Using REPL
   - View Behavior Hierarchy (IMPL)
   - View Current Position (IMPL)
   - View Navigation Commands (IMPL)
3. Navigate And Execute Behaviors Using REPL Commands
   - Display Behavior Action Hierarchy (SCENARIO: includes Display Behavior Hierarchy, Display Current Position, Display Navigation Commands)
   - Navigate Sequentially
   - Navigate To Behavior Action And Execute
4. Manage Scope Using REPL
   - Set Story Scope (SCENARIO: Enforce Mutually Exclusive Scope Types)
   - Set File Scope
   - Validate Scope Against Story Graph
   - Pass Scope Parameters When Executing Actions
   - View Current Scope
   - Clear Scope
5. View Action-Specific Instructions
   - View Base Instructions
   - Display Clarify Instructions
   - Display Strategy Instructions
   - Display Build Instructions
   - Display Validate Instructions
   - Display Render Instructions
   - Display Instructions In Raw Format
   - Submit Instructions To AI Agent (NOT IMPL?)
   - Show Remaining Actions After Completion
6. Get Help Using REPL
   - Display Action Help Using CLI (IMPL) (renamed from "Request Action Help Through CLI")
   - Display Parameter Help Using CLI (IMPL) (renamed from "View Parameter Documentation in CLI")
   - Display Command Examples Using CLI (IMPL) (renamed from "View Command Examples in CLI")

---

### J. Consolidate Repeated Stories - Detailed Analysis

### Problem: Massive Duplication

The "Execute Behavior Actions" epic contains 5 sub-epics (Gather Context, Decide Planning Criteria, Build Knowledge, Render Output, Validate Rules), and **each repeats the same generic stories**:

**REPEATED IN EVERY SUB-EPIC:**
- Track Activity for [X] Action (appears 5x)
- Proceed To [Next Action] (appears 4x)
- Load Base Action Config (appears 5x)
- Initialize Action (appears 5x)
- Access Actions (appears 5x)
- Load Guardrails (appears 5x)
- Inject [X] Into Instructions (appears 5x with different content)

**RESULT:** ~30-40 stories that are 80% identical with only 20% variation

### Solution: Extract Generic Stories, Keep Only Unique

**MOVE TO "INVOKE BOT DIRECTLY" FEATURE GROUPS:**

| Repeated Story | Move To Feature Group | Notes |
|----------------|----------------------|-------|
| Track Activity for [X] Action | **Track Activity** | Generic: Track Start, Completion, Metrics |
| Proceed To [Next Action] | **Track Workflow State** | Generic: Save State, Inject Next Action, Transition |
| Load Base Action Config | **Generate Action Instructions** | Generic: Load Base Config story |
| Load Guardrails | **Generate Action Instructions** | Generic: Load guardrails from behavior folder |

**KEEP IN EACH SUB-EPIC (UNIQUE ONLY):**

**Gather Context (Clarify):**
- Inject Guardrails As Part Of Clarify Requirements (UNIQUE: questions/evidence structure)
- Store Clarification Data (UNIQUE: clarification.json schema)

**Decide Planning Criteria (Strategy):**
- Inject Strategy Into Instructions (UNIQUE: decision criteria/assumptions structure)
- Store Strategy Data (UNIQUE: strategy.json schema)

**Build Knowledge:**
- Load Story Graph Into Memory
- Inject Knowledge Graph Template and Builder Instructions
- Update Existing Knowledge Graph
- Proactively Validate knowledge against rules
- Create Build Scope
- Filter Knowledge Graph

**Render Output:**
- Load Render Configurations
- Inject Template Instructions
- Inject Synchronizer Instructions
- Inject Render Instructions And Configs
- Get Render Instructions
- Merge Base And Render Instructions
- Render Output Using Synchronizers

**Validate Knowledge & Content Against Rules:**
- Inject Validation Rules for Validate Rules Action
- Invoke Complete Validation Workflow
- Discovers Scanners
- Run Scanners against Knowledge Graph
- Validate Rules According To Scope
- Generate Violation Report
- Report Validation and Error Handling

### Updated "Invoke Bot Directly" With Consolidated Stories

**Navigate And Execute Behaviors:**
- Navigate To Behavior Action And Execute
- Navigate Sequentially (Determine Action Order From State)
- Execute End-to-End Workflow (integration test)

**Manage Scope:**
- Set Story Scope (SCENARIO: Enforce Mutually Exclusive Scope Types)
- Set File Scope
- Filter Knowledge Graph By Scope
- Pass Scope Parameters To Actions
- Clear Scope

**Generate Action Instructions:**
- **Load Base Action Configuration** ← MOVED FROM: All sub-epics
- Load And Merge Behavior-Specific Instructions
- **Load Guardrails From Behavior Folder** ← MOVED FROM: All sub-epics
- Inject Guardrails Into Instructions
- Inject Context Into Instructions (SCENARIOS: Inject Next Behavior Reminder, Inject Status Breadcrumbs)
- Get Action Instructions (returns merged instructions)

**Track Workflow State:**
- Save Workflow State
- Load Workflow State
- Determine Resume Point After Interruption
- Confirm Current Action
- **Inject Next Action Instructions** ← MOVED FROM: "Proceed To [X]" in all sub-epics
- **Transition To Next Action** ← MOVED FROM: "Proceed To [X]" in all sub-epics

**Track Activity:**
- **Track Action Start** ← MOVED FROM: "Track Activity for [X] Action" in all sub-epics
- **Track Action Completion** ← MOVED FROM: "Track Activity for [X] Action" in all sub-epics
- Record Activity Metrics And Paths

**View Action-Specific Instructions:**
- View Base Instructions
- View Clarify Instructions (UNIQUE: shows clarification.json data)
- View Strategy Instructions (UNIQUE: shows strategy.json data)
- View Build Instructions (UNIQUE: shows knowledge graph template)
- View Validate Instructions (UNIQUE: shows validation rules)
- View Render Instructions (UNIQUE: shows render configs)
- View Instructions In Raw Format
- Submit Instructions To AI Agent

### Impact

**BEFORE:** 
- ~150+ stories across Execute Behavior Actions sub-epics
- 80% duplication

**AFTER:**
- ~40-50 unique stories in sub-epics
- ~20 consolidated generic stories in "Invoke Bot Directly"
- 0% duplication

**Benefits:**
- Single source of truth for generic action lifecycle stories
- Sub-epics focus on what makes them unique
- Test coverage is clearer (generic tests vs. specific tests)
- Easier to maintain and understand

---

### K. Implementation Notes

- Use `git mv` for all file/folder renames to preserve git history
- Run tests after each major rename batch
- Validate story-graph.json after each edit
- Consider creating a script to automate the story-graph.json updates
- Document any deviations from this plan in the commit messages



### L. FUTURE STATE: Consolidated Hierarchy Tree

```
🎯 INVOKE BOT

├─ ⚙️ INVOKE BOT DIRECTLY (6 features)
│  │
│  ├─ Navigate And Execute Behaviors (3 stories)
│  │  ├─ Navigate To Behavior Action And Execute
│  │  ├─ Navigate Sequentially (Determine Action Order From State)
│  │  └─ Execute End-to-End Workflow (integration test)
│  │
│  ├─ Manage Scope (5 stories + scenarios)
│  │  ├─ Set Story Scope
│  │  │  └─ SCENARIO: Enforce Mutually Exclusive Scope Types
│  │  ├─ Set File Scope
│  │  ├─ Filter Knowledge Graph By Scope
│  │  ├─ Pass Scope Parameters To Actions
│  │  └─ Clear Scope
│  │
│  ├─ Generate Action Instructions (6 stories + scenarios)
│  │  ├─ Load Base Action Configuration
│  │  ├─ Load And Merge Behavior-Specific Instructions
│  │  ├─ Load Guardrails From Behavior Folder
│  │  ├─ Inject Guardrails Into Instructions
│  │  ├─ Inject Context Into Instructions
│  │  │  └─ SCENARIOS: Inject Next Behavior Reminder, Inject Status Breadcrumbs
│  │  └─ Get Action Instructions (returns merged instructions)
│  │
│  ├─ View Action-Specific Instructions (8 stories)
│  │  ├─ View Base Instructions
│  │  ├─ View Clarify Instructions (includes clarification.json data)
│  │  ├─ View Strategy Instructions (includes strategy.json data)
│  │  ├─ View Build Instructions (includes knowledge graph template)
│  │  ├─ View Validate Instructions (includes validation rules)
│  │  ├─ View Render Instructions (includes render configs)
│  │  ├─ View Instructions In Raw Format
│  │  └─ Submit Instructions To AI Agent
│  │
│  ├─ Track Workflow State (6 stories)
│  │  ├─ Save Workflow State
│  │  ├─ Load Workflow State
│  │  ├─ Determine Resume Point After Interruption
│  │  ├─ Confirm Current Action
│  │  ├─ Inject Next Action Instructions
│  │  └─ Transition To Next Action
│  │
│  └─ Track Activity (3 stories)
│     ├─ Track Action Start
│     ├─ Track Action Completion
│     └─ Record Activity Metrics And Paths
│
├─ ⚙️ INVOKE BOT THROUGH PANEL (5 features)
│  │
│  ├─ Manage Panel Session (7 stories)
│  │  ├─ Open Panel
│  │  ├─ Load Bot Configuration
│  │  ├─ Display Session Header (IMPL)
│  │  ├─ Display Bot Status
│  │  ├─ Manage Workspace Path
│  │  ├─ Switch Bot
│  │  └─ Toggle Panel Section
│  │
│  ├─ Navigate And Execute Behaviors (3 stories + scenarios)
│  │  ├─ Display Behavior Action Hierarchy (story with scenarios)
│  │  │  └─ SCENARIOS: Display Behavior Hierarchy (IMPL), Display Current Position (IMPL), Display Navigation Commands (IMPL)
│  │  ├─ Navigate Sequentially
│  │  └─ Navigate To Behavior Action And Execute
│  │
│  ├─ Manage Scope (5 stories + scenarios)
│  │  ├─ Set Story Scope (IMPL)
│  │  │  └─ SCENARIO: Enforce Mutually Exclusive Scope Types
│  │  ├─ Set File Scope (NOT IMPL)
│  │  ├─ View Story Scope Hierarchy (IMPL)
│  │  ├─ View Current Scope (IMPL)
│  │  └─ Clear Scope (IMPL)
│  │
│  ├─ View Action-Specific Instructions (8 stories)
│  │  ├─ View Base Instructions
│  │  ├─ Display Clarify Instructions
│  │  ├─ Display Strategy Instructions
│  │  ├─ Display Build Instructions
│  │  ├─ Display Validate Instructions
│  │  ├─ Display Render Instructions
│  │  ├─ Display Instructions In Raw Format
│  │  └─ Submit Instructions To Chat
│  │
│  └─ Get Help (3 stories - all NOT IMPL)
│     ├─ Display Action Help Using Panel (NOT IMPL)
│     ├─ Display Parameter Help Using Panel (NOT IMPL)
│     └─ Display Command Examples Using Panel (NOT IMPL)
│
└─ ⚙️ INVOKE BOT THROUGH REPL (6 features)
   │
   ├─ Manage REPL Session (8 stories + scenarios)
   │  ├─ Start REPL Session
   │  │  └─ SCENARIO: Start REPL in JSON Mode
   │  ├─ Start REPL in Pipe Mode
   │  ├─ Display Piped Mode Instructions
   │  ├─ Detect and Configure TTY/Non-TTY Input
   │  ├─ Display Session Header (IMPL)
   │  ├─ Display Bot Status
   │  ├─ Manage Workspace Path
   │  │  └─ SCENARIO: Switch Bots
   │  └─ Switch Bot
   │
   ├─ Display State Using REPL (3 stories)
   │  ├─ View Behavior Hierarchy (IMPL)
   │  ├─ View Current Position (IMPL)
   │  └─ View Navigation Commands (IMPL)
   │
   ├─ Navigate And Execute Behaviors Using REPL Commands (3 stories + scenarios)
   │  ├─ Display Behavior Action Hierarchy (story with scenarios)
   │  │  └─ SCENARIOS: Display Behavior Hierarchy (IMPL), Display Current Position (IMPL), Display Navigation Commands (IMPL)
   │  ├─ Navigate Sequentially
   │  └─ Navigate To Behavior Action And Execute
   │
   ├─ Manage Scope Using REPL (6 stories + scenarios)
   │  ├─ Set Story Scope
   │  │  └─ SCENARIO: Enforce Mutually Exclusive Scope Types
   │  ├─ Set File Scope
   │  ├─ Validate Scope Against Story Graph
   │  ├─ Pass Scope Parameters When Executing Actions
   │  ├─ View Current Scope
   │  └─ Clear Scope
   │
   ├─ View Action-Specific Instructions (10 stories)
   │  ├─ View Base Instructions
   │  ├─ Display Clarify Instructions
   │  ├─ Display Strategy Instructions
   │  ├─ Display Build Instructions
   │  ├─ Display Validate Instructions
   │  ├─ Display Render Instructions
   │  ├─ Display Instructions In Raw Format
   │  ├─ Submit Instructions To AI Agent (NOT IMPL?)
   │  └─ Show Remaining Actions After Completion
   │
   └─ Get Help Using REPL (3 stories - all IMPL)
      ├─ Display Action Help Using CLI (IMPL)
      ├─ Display Parameter Help Using CLI (IMPL)
      └─ Display Command Examples Using CLI (IMPL)
```

### Key Improvements:

**Structural Changes:**
- **Flatter Feature Structure**: Direct (6 features), Panel (5 features), REPL (6 features) - simpler, more focused
- **Direct Reorganization**: From 7 flat stories → 6 feature groups (33 stories) aligned with Panel/REPL patterns
- **Scenarios vs Stories**: Extra-indented items are scenarios within stories, not separate stories
  - Example: "Display Behavior Action Hierarchy" is a story with scenarios like "Display Behavior Hierarchy (IMPL)"
  - Example: "Set Story Scope" includes scenario "Enforce Mutually Exclusive Scope Types"
  - Example: "Inject Context Into Instructions" has scenarios "Inject Next Behavior Reminder", "Inject Status Breadcrumbs"

**Duplication Elimination:**
- **Consolidated Repeated Stories**: ~110+ duplicate stories across 5 behavior action sub-epics → ~20 generic stories in "Invoke Bot Directly"
- **Extracted Generic Patterns**: Track Activity, Proceed To Next Action, Load Config, Load Guardrails now appear once
- **Focus on Unique**: Sub-epics now contain only unique functionality (e.g., Store Clarification Data, Store Strategy Data, Run Scanners)
- **80% → 0% Duplication**: Sub-epics focus on what makes them unique, not repeated boilerplate

**Naming & Organization:**
- **Consistent Naming**: "Navigate To Behavior Action And Execute" across all contexts
- **Removed Obsolete**: "Confirm And Advance Action", "View Headless Mode Status", "Format Output For AI", "Access Documentation"
- **Unified Session Management**: Combined Initialize + Manage into single "Manage Panel/REPL Session" feature
- **Consistent Help**: Both Panel and REPL have identical 3 help stories (Display Action Help, Display Parameter Help, Display Command Examples) - REPL implemented, Panel not yet
- **Clear Status**: (IMPL) / (NOT IMPL) tags show implementation status

