# Test File and Class Rename Plan
**Epic:** 🎯 Invoke Bot  
**Status:** Planning  
**Created:** 2025-01-06  
**Purpose:** Audit and rename all test files and classes orphaned by story refactoring

---

## 🎯 EXECUTIVE SUMMARY

During the "Invoke Bot" story naming refactoring (commits 81c5986f through 6459fb0a), we renamed:
- **2 sub-epics**
- **7+ features**
- **50+ stories**
- **Restructured "Invoke Bot Directly"** from 7 flat stories to nested feature structure with 5 action sub-epics

However, **NO test files or test classes were renamed** to match the new story structure.

### Impact:
- ❌ **10 test files** still have old names (e.g., `test_perform_behavior_action.py` should be `test_invoke_bot_directly.py`)
- ❌ **60+ test classes** still have old names (e.g., `TestLaunchCLIInInteractiveMode` should be `TestStartREPLSession`)
- ❌ **story-graph.json references** still point to old test file/class names
- ❌ Git history for test evolution is unclear due to mismatched names

---

## 📋 COMPLETE CHANGE AUDIT (Chronological)

### Commit 1: 81c5986f - Rename Sub-Epics
**Date:** 2026-01-06 21:46:59  
**Changed:**
- Sub-epic: `Perform Behavior Action` → `Invoke Bot Directly`
- Sub-epic: `Run Interactive REPL` → `Invoke Bot Through REPL`

**Test Files Affected:** (NOT renamed yet)
- `test_perform_behavior_action.py` → should be `test_invoke_bot_directly.py`

### Commit 2-5: d6e9014b through ae705169 - Restructure "Invoke Bot Directly"
**Phase 3 Stages 1-4**  
**Changed:**
- Created 6 nested features under "Invoke Bot Directly"
- Moved stories into features
- Renamed 7 stories:
  - `Invoke Behavior Actions In Workflow Order` → `Execute End-to-End Workflow`
  - `Execute Behavior` → `Execute Behavior Action`
  - `Close Current Action` → `Confirm Current Action`
  - `Invoke Behavior In Action Order` → `Navigate Sequentially`

**Test Classes Affected:** (NOT renamed yet)
- `TestInvokeBehaviorActionsInWorkflowOrder` → should be `TestExecuteEndToEndWorkflow`
- `TestExecuteBehavior` → should be `TestExecuteBehaviorAction`
- `TestCloseCurrentAction` → should be `TestConfirmCurrentAction`
- `TestInvokeBehaviorInActionOrder` → should be `TestNavigateSequentially`

### Commit 6: 162f7917 - Rename Panel Features and Stories (Phase 4)
**Changed:**
- Feature: `Manage Bot Information` → `Manage Panel Session`
- Feature: `Navigate Behavior Action Status` → `Navigate And Execute Behaviors`
- Feature: `Filter And Navigate Scope` → `Manage Scope`
- Feature: `Display Instructions` → `View Action-Specific Instructions`
- Story: `Refresh Panel` → `Display Session Status`

**Test Files Affected:** (Panel tests - may not have dedicated test files)
- No direct test file changes (Panel tests may be integration tests)

### Commit 7: 2ad90bc6 - Rename REPL Features and Stories (Phase 5)
**Changed:**
- Feature: `Navigate Bot Behaviors and Actions With CLI` → `Navigate Behaviors Using REPL Commands`
- Feature: `Execute Action Operation Through CLI` → `Execute Actions Using REPL`
- Feature: `Manage Bot Scope Through CLI` → `Manage Scope Using REPL`
- Feature: `Display Bot State Using CLI` → `Display State Using REPL`
- Feature: `Get Help Using CLI` → `Get Help Using REPL`
- **30+ story renames** (all "CLI" → "REPL", removed "Through CLI", etc.)

**Test Files Affected:** (NOT renamed yet)
- `test_navigate_bot_behaviors_and_actions_with_cli_current.py` → should be `test_navigate_behaviors_using_repl_commands.py`
- `test_navigate_bot_behaviors_and_actions_with_cli.py` → should be `test_navigate_behaviors_using_domain_model.py`
- `test_execute_action_operation_through_cli_current.py` → should be `test_execute_actions_using_repl.py`
- `test_manage_bot_scope_through_cli_current.py` → should be `test_manage_scope_using_repl.py`
- `test_display_bot_state_using_cli_current.py` → should be `test_display_state_using_repl.py`
- `test_get_help_using_cli_current.py` → should be `test_get_help_using_repl.py`
- `test_initialize_repl_session_current.py` → should be `test_initialize_repl_session.py` (already exists, may need merge)

**Test Classes Affected:** (NOT renamed yet - see detailed section below)
- 40+ test classes need renaming

### Commits 8-10: Story Deletions
**Changed:**
- Deleted: `Save Workflow State`, `Load Workflow State`, `Determine Resume Point After Interruption`
- Deleted: `Auto-Confirm Action After Instructions Complete`
- Deleted: `Invoke Specific Bot Behavior Command through CLI`

**Test Classes Affected:**
- Remove: `TestSaveWorkflowState`
- Remove: `TestLoadWorkflowState`
- Remove: `TestDetermineResumePointAfterInterruption`
- Remove: `TestAutoConfirmActionAfterInstructionsComplete`
- Remove: `TestInvokeSpecificBotBehaviorCommandThroughCLI`

### Commit 11: 877dd4fa - Rename "View Action-Specific Instructions" to "Build Action Instructions"
**Changed:**
- Feature renamed across all 3 invocation methods

**Test Classes Affected:** (story names didn't change, just feature)
- No direct impact (stories within feature kept same names)

### Commit 12: 6abe3951 - Move Inject Stories to Build Action Instructions
**Changed:**
- Moved and renamed 5 "Inject XXX" stories to "Build XXX Instructions"
- Stories moved from action sub-epics to "Build Action Instructions"

**Test Classes Affected:**
- `TestInjectGuardrailsAsPartOfClarifyRequirements` → merged into `TestBuildClarifyInstructions`
- `TestInjectStrategyIntoInstructions` → merged into `TestBuildStrategyInstructions`
- `TestInjectKnowledgeGraphTemplateAndBuilderInstructions` → merged into `TestBuildInstructions`
- `TestInjectValidationRulesForValidateRulesAction` → merged into `TestBuildValidateInstructions`
- `TestInjectRenderInstructionsAndConfigs` → merged into `TestBuildRenderInstructions`

### Commit 13: 8b253517 - Nest 5 Action Sub-Epics into "Build Action Instructions"
**Changed:**
- Moved sub-epics: Gather Context, Decide Planning Criteria, Build Knowledge, Render Output, Validate Rules
- Nested them under "Build Action Instructions" (now called "Display Action Instructions")

**Test Files Affected:**
- `test_gather_context.py` - potentially needs updated references
- `test_decide_strategy_criteria_action.py` - potentially needs updated references
- `test_build_knowledge.py` - potentially needs updated references
- `test_render_output.py` - potentially needs updated references
- `test_validate_knowledge_and_content_against_rules.py` - potentially needs updated references

### Commit 14: 0fea65b2 - Move "Build XXX Instructions" Stories into Action Sub-Epics
**Changed:**
- Moved stories from top-level "Build Action Instructions" into nested action sub-epics

**Test Classes Affected:**
- Test classes for "Build XXX Instructions" stories moved to different test files

### Commit 15: 728420ad - Delete "Track Activity" and "Proceed To" Stories
**Changed:**
- Deleted all "Track Activity for XXX" stories from action sub-epics
- Deleted all "Proceed To XXX" stories from action sub-epics

**Test Classes Affected:**
- Remove: `TestTrackActivityForGatherContextAction`
- Remove: `TestTrackActivityForDecidePlanningAction`
- Remove: `TestTrackActivityForBuildKnowledgeAction`
- Remove: `TestTrackActivityForRenderOutputAction`
- Remove: `TestTrackActivityForValidateRulesAction`
- Remove: `TestProceedToDecidePlanning`
- Remove: `TestProceedToBuildKnowledge`
- Remove: `TestProceedToRenderOutput`
- Remove: `TestProceedToValidateRules`

### Commit 16: 065e35be - Delete "Execute Behavior Actions" Epic
**Changed:**
- Moved domain concepts to "Build Action Instructions"
- Deleted entire "Execute Behavior Actions" epic

**Test Files Affected:**
- Consolidated test coverage into existing action test files

### Commit 17: 8a236c94 - Rename "Generate Action Instructions"
**Changed:**
- `Generate Action Instructions` → `Build Common Instructions For Actions`
- Moved into "Build Action Instructions" as first nested sub-epic

**Test Classes Affected:**
- Feature rename only, stories kept same names

### Commit 18: cca9a03c - Delete "Track Workflow State" Feature
**Changed:**
- Deleted entire feature and its 3 stories

**Test Classes Affected:**
- Remove: `TestSaveWorkflowState` (if not already removed)
- Remove: `TestLoadWorkflowState` (if not already removed)
- Remove: `TestDetermineResumePointAfterInterruption` (if not already removed)

### Commit 19: 6ce6737b - Add "Through Panel" to Panel Sub-Epic Names
**Changed:**
- Added suffix "Through Panel" to Panel sub-epic names for consistency

**Test Files Affected:**
- No test file changes (naming convention only)

### Commit 20: 6459fb0a - Rename "Build Action Instructions" to "Display Action Instructions"
**Changed:**
- `Build Action Instructions` → `Display Action Instructions` (Panel and REPL only)
- "Invoke Bot Directly" kept "Build Action Instructions"

**Test Classes Affected:**
- No test class renames (feature name change only)

---

## 📊 CURRENT STATE vs REQUIRED STATE

### Test Files That Exist But Need Renaming

| Current Filename | Should Be Named | Location | Reason |
|-----------------|-----------------|----------|--------|
| `test_perform_behavior_action.py` | `test_invoke_bot_directly.py` | `agile_bot/bots/base_bot/test/` | Sub-epic renamed in commit 81c5986f |
| `test_navigate_bot_behaviors_and_actions_with_cli_current.py` | `test_navigate_behaviors_using_repl_commands.py` | `agile_bot/bots/base_bot/test/` | Feature renamed in commit 2ad90bc6 |
| `test_navigate_bot_behaviors_and_actions_with_cli.py` | `test_navigate_behaviors_using_domain_model.py` | `agile_bot/bots/base_bot/test/` | Feature split/renamed in commit 2ad90bc6 |
| `test_execute_action_operation_through_cli_current.py` | `test_execute_actions_using_repl.py` | `agile_bot/bots/base_bot/test/` | Feature renamed in commit 2ad90bc6 |
| `test_manage_bot_scope_through_cli_current.py` | `test_manage_scope_using_repl.py` | `agile_bot/bots/base_bot/test/` | Feature renamed in commit 2ad90bc6 |
| `test_display_bot_state_using_cli_current.py` | `test_display_state_using_repl.py` | `agile_bot/bots/base_bot/test/` | Feature renamed in commit 2ad90bc6 |
| `test_display_bot_state_using_cli.py` | `test_display_state_using_repl.py` (merge or archive) | `agile_bot/bots/base_bot/test/` | Feature renamed, duplicate may exist |
| `test_get_help_using_cli_current.py` | `test_get_help_using_repl.py` | `agile_bot/bots/base_bot/test/` | Feature renamed in commit 2ad90bc6 |
| `test_initialize_repl_session_current.py` | `test_initialize_repl_session.py` (consolidate) | `agile_bot/bots/base_bot/test/` | Remove "_current" suffix |
| `test_execute_action_operation_through_cli.py` | Archive or merge | `agile_bot/bots/base_bot/test/` | Old version, may be obsolete |

### Test Files Referenced in story-graph.json

| Test File in story-graph.json | Status | Notes |
|------------------------------|--------|-------|
| `test_generate_mcp_tools.py` | ✅ OK | Not affected by refactor |
| `test_generate_repl_cli.py` | ✅ OK | Not affected by refactor |
| `test_invoke_mcp.py` | ✅ OK | Not affected by refactor |
| `test_gather_context.py` | ✅ OK | Exists, may need class updates |
| `test_decide_strategy_criteria_action.py` | ✅ OK | Exists, may need class updates |
| `test_build_knowledge.py` | ✅ OK | Exists, may need class updates |
| `test_render_output.py` | ✅ OK | Exists, may need class updates |
| `test_validate_knowledge_and_content_against_rules.py` | ⚠️ MISSING | Referenced but doesn't exist in test/ |
| **`test_perform_behavior_action.py`** | ❌ WRONG | Should be `test_invoke_bot_directly.py` |
| `test_initialize_repl_session.py` | ⚠️ DUPLICATE | `test_initialize_repl_session_current.py` also exists |
| **`test_navigate_bot_behaviors_and_actions_with_cli_current.py`** | ❌ WRONG | Should be `test_navigate_behaviors_using_repl_commands.py` |
| **`test_navigate_bot_behaviors_and_actions_with_cli.py`** | ❌ WRONG | Should be `test_navigate_behaviors_using_domain_model.py` |
| **`test_execute_action_operation_through_cli.py`** | ❌ WRONG | Should be `test_execute_actions_using_repl.py` |
| **`test_manage_bot_scope_through_cli.py`** | ❌ WRONG | Should be `test_manage_scope_using_repl.py` |
| **`test_display_bot_state_using_cli.py`** | ❌ WRONG | Should be `test_display_state_using_repl.py` |
| **`test_get_help_using_cli_current.py`** | ❌ WRONG | Should be `test_get_help_using_repl.py` |

---

## 🔧 DETAILED TEST CLASS RENAMES

### 1. test_invoke_bot_directly.py (was test_perform_behavior_action.py)

| Current Test Class | Should Be Named | Story Name | Commit |
|-------------------|-----------------|------------|--------|
| `TestInvokeBehaviorActionsInWorkflowOrder` | `TestExecuteEndToEndWorkflow` | Execute End-to-End Workflow | d6e9014b |
| `TestExecuteBehavior` | `TestExecuteBehaviorAction` | Execute Behavior Action | d6e9014b |
| `TestInsertContextIntoInstructions` | `TestInjectContextIntoInstructions` | Inject Context Into Instructions | d6e9014b |
| `TestCloseCurrentAction` | `TestConfirmCurrentAction` | Confirm Current Action | d6e9014b |
| `TestInvokeBehaviorInActionOrder` | `TestNavigateSequentially` | Navigate Sequentially | d6e9014b |
| `TestInjectNextBehaviorReminder` | *Move to scenarios in TestInjectContextIntoInstructions* | (scenario) | ae705169 |
| `TestInjectStatusUpdateBreadcrumbs` | *Move to scenarios in TestInjectContextIntoInstructions* | (scenario) | ae705169 |

### 2. test_initialize_repl_session.py (consolidate _current variant)

| Current Test Class | Should Be Named | Story Name | Commit |
|-------------------|-----------------|------------|--------|
| `TestLaunchCLIInInteractiveMode` | `TestStartREPLSession` | Start REPL Session | 2ad90bc6 |
| `TestLaunchCLIInPipeMode` | `TestStartREPLInPipeMode` | Start REPL in Pipe Mode | 2ad90bc6 |
| `TestDisplayPipedModeInstructionsForAIAgents` | ✅ Keep | Display Piped Mode Instructions | - |
| `TestDetectAndConfigureTTYNonTTYInputForCLI` | `TestDetectAndConfigureTTYNonTTYInput` | Detect and Configure TTY/Non-TTY Input | 2ad90bc6 |
| `TestLoadAndDisplayWorkspaceContextInCLI` | `TestLoadWorkspaceContext` | Load Workspace Context | 2ad90bc6 |

### 3. test_navigate_behaviors_using_repl_commands.py (was test_navigate_bot_behaviors_and_actions_with_cli_current.py)

| Current Test Class | Should Be Named | Story Name | Commit |
|-------------------|-----------------|------------|--------|
| `TestNavigateUsingCLIDotNotation` | `TestNavigateToBehaviorActionAndExecute` | Navigate To Behavior Action And Execute | 2ad90bc6 |
| `TestNavigateSequentiallyUsingCLICommands` | `TestNavigateSequentially` | Navigate Sequentially | 2ad90bc6 |
| `TestExitCLIREPL` | `TestExitREPL` | Exit REPL | 2ad90bc6 |

### 4. test_navigate_behaviors_using_domain_model.py (was test_navigate_bot_behaviors_and_actions_with_cli.py)

| Current Test Class | Should Be Named | Story Name | Commit |
|-------------------|-----------------|------------|--------|
| `TestNavigateToFirstBehaviorAction` | `TestNavigateToBehaviorActionAndExecute` | Navigate To Behavior Action And Execute | 2ad90bc6 |
| `TestAdvanceActionAndPersistState` | *REMOVE* | (deleted story) | 2ad90bc6 |
| `TestShowRemainingActionsAfterCompletion` | ✅ Keep | Show Remaining Actions After Completion | - |

### 5. test_execute_actions_using_repl.py (was test_execute_action_operation_through_cli_current.py)

| Current Test Class | Should Be Named | Story Name | Commit |
|-------------------|-----------------|------------|--------|
| `TestGetActionInstructionsThroughCLI` | `TestViewInstructions` | View Instructions | 2ad90bc6 |
| `TestConfirmWorkThroughCLIWithStringParameters` | `TestConfirmWithParameters` | Confirm With Parameters | 2ad90bc6 |
| `TestConfirmActionCompletionThroughCLI` | `TestConfirmActionCompletion` | Confirm Action Completion | 2ad90bc6 |
| `TestAutoConfirmActionAfterInstructionsComplete` | *REMOVE* | (deleted story) | 01c25d09 |
| `TestReExecuteCurrentOperationUsingCLI` | `TestReExecuteCurrentAction` | Re-execute Current Action | 2ad90bc6 |
| `TestHandleOperationErrorsAndValidationInCLI` | `TestHandleErrorsAndValidation` | Handle Errors and Validation | 2ad90bc6 |
| `TestInvokeSpecificBotBehaviorCommandThroughCLI` | *REMOVE* | (deleted story) | 127037cb |

### 6. test_manage_scope_using_repl.py (was test_manage_bot_scope_through_cli_current.py)

| Current Test Class | Should Be Named | Story Name | Commit |
|-------------------|-----------------|------------|--------|
| `TestSetScopeThroughCLIUsingStringParameters` | `TestSetScope` | Set Scope | 2ad90bc6 |
| `TestFilterWorkUsingKnowledgeGraphScopeInCLI` | `TestSetStoryScope` | Set Story Scope | 2ad90bc6 |
| `TestFilterWorkUsingFilesScopeInCLI` | `TestSetFileScope` | Set File Scope | 2ad90bc6 |
| `TestValidateScopeAgainstStoryGraphInCLI` | `TestValidateScopeAgainstStoryGraph` | Validate Scope Against Story Graph | 2ad90bc6 |
| `TestPassScopeParametersWhenExecutingActionsThroughCLI` | `TestPassScopeParametersWhenExecutingActions` | Pass Scope Parameters When Executing Actions | 2ad90bc6 |
| `TestViewCurrentScopeInCLI` | `TestViewCurrentScope` | View Current Scope | 2ad90bc6 |
| `TestClearScopeThroughCLI` | `TestClearScope` | Clear Scope | 2ad90bc6 |
| `TestScopeTypesMutuallyExclusive` | ✅ Keep | Enforce Mutually Exclusive Scope Types | - |

### 7. test_display_state_using_repl.py (was test_display_bot_state_using_cli_current.py)

| Current Test Class | Should Be Named | Story Name | Commit |
|-------------------|-----------------|------------|--------|
| `TestDisplayCLIHeader` | `TestViewSessionHeader` | View Session Header | 2ad90bc6 |
| `TestDisplayBotHierarchyTreeInCLI` | `TestViewBehaviorHierarchy` | View Behavior Hierarchy | 2ad90bc6 |
| `TestDisplayCurrentPositionInCLI` | `TestViewCurrentPosition` | View Current Position | 2ad90bc6 |
| `TestDisplayActiveScopeInCLIStatus` | `TestViewActiveScope` | View Active Scope | 2ad90bc6 |
| `TestDisplayCLINavigationMenuFooter` | `TestViewNavigationCommands` | View Navigation Commands | 2ad90bc6 |
| `TestDisplayHeadlessModeStatusInCLI` | `TestViewHeadlessModeStatus` | View Headless Mode Status | 2ad90bc6 |
| `TestDisplayAvailableBotInTreeHierarchy` | `TestViewAvailableBots` | View Available Bots | 2ad90bc6 |
| `TestDisplayCLIBotCommandInNavigationMenuFooter` | *Consider merging with TestViewNavigationCommands* | (duplicate?) | - |
| `TestFormatOutputForAI` | *REMOVE* | (deleted story) | 2ad90bc6 |

### 8. test_get_help_using_repl.py (was test_get_help_using_cli_current.py)

| Current Test Class | Should Be Named | Story Name | Commit |
|-------------------|-----------------|------------|--------|
| `TestViewAvailableCommandsUsingCLIHelp` | `TestDisplayActionHelpUsingCLI` | Display Action Help Using CLI | 2ad90bc6 |
| `TestRequestActionHelpThroughCLI` | `TestDisplayActionHelpUsingCLI` (duplicate?) | Display Action Help Using CLI | 2ad90bc6 |
| `TestViewParameterDocumentationInCLI` | `TestDisplayParameterHelpUsingCLI` | Display Parameter Help Using CLI | 2ad90bc6 |
| `TestViewCommandExamplesInCLI` | `TestDisplayCommandExamplesUsingCLI` | Display Command Examples Using CLI | 2ad90bc6 |

### 9. Action Sub-Epic Test Files (gather_context, decide_strategy, build_knowledge, render_output, validate)

These test files exist and reference the action sub-epics. After commits 8b253517, 0fea65b2, 728420ad, the following test classes need updates:

**test_gather_context.py:**
- Remove: `TestTrackActivityForGatherContextAction`
- Remove: `TestProceedToDecidePlanning`
- Remove: `TestLoadBaseActionConfig`
- Remove: `TestAccessActions`
- Remove: `TestInitializeAction`
- Remove: `TestLoadGuardrails`
- Keep: `TestStoreClarificationData`
- Rename: `TestInjectGuardrailsAsPartOfClarifyRequirements` → `TestBuildClarifyInstructions` (if exists)

**test_decide_strategy_criteria_action.py:**
- Remove: `TestTrackActivityForDecidePlanningAction`
- Remove: `TestProceedToBuildKnowledge`
- Remove: `TestLoadBaseActionConfig`
- Remove: `TestAccessActions`
- Remove: `TestInitializeAction`
- Remove: `TestLoadGuardrails`
- Keep: `TestStoreStrategyData`
- Rename: `TestInjectStrategyIntoInstructions` → `TestBuildStrategyInstructions` (if exists)

**test_build_knowledge.py:**
- Remove: `TestTrackActivityForBuildKnowledgeAction`
- Remove: `TestProceedToRenderOutput`
- Remove: `TestLoadBaseActionConfig`
- Remove: `TestAccessActions`
- Remove: `TestInitializeAction`
- Remove: `TestLoadGuardrails`
- Keep: All unique Build Knowledge stories
- Rename: `TestInjectKnowledgeGraphTemplateAndBuilderInstructions` → `TestBuildInstructions` (if exists)

**test_render_output.py:**
- Remove: `TestTrackActivityForRenderOutputAction`
- Remove: `TestProceedToValidateRules`
- Remove: `TestLoadBaseActionConfig`
- Remove: `TestAccessActions`
- Remove: `TestInitializeAction`
- Remove: `TestLoadGuardrails`
- Keep: All unique Render Output stories
- Rename: `TestInjectRenderInstructionsAndConfigs` → `TestBuildRenderInstructions` (if exists)

**test_validate_knowledge_and_content_against_rules.py:** (referenced in story-graph.json but missing from test/)
- If this file is created or found:
  - Remove: `TestTrackActivityForValidateRulesAction`
  - Remove: `TestLoadBaseActionConfig`
  - Remove: `TestAccessActions`
  - Remove: `TestInitializeAction`
  - Remove: `TestLoadGuardrails`
  - Keep: All unique Validate Rules stories
  - Rename: `TestInjectValidationRulesForValidateRulesAction` → `TestBuildValidateInstructions` (if exists)

---

## 🎯 IMPLEMENTATION PLAN

### Phase 1: Backup and Validation (30 minutes)

**Step 1.1: Create Backup**
```powershell
# Create backup branch
git checkout -b backup-before-test-rename
git push origin backup-before-test-rename

# Return to working branch
git checkout refactor-invoke-bot-stories
```

**Step 1.2: Run All Tests - Baseline**
```powershell
cd agile_bot/bots/base_bot
pytest test/ -v > test-results-before-test-rename.txt
```

**Step 1.3: Document Current State**
```powershell
# List all test files
Get-ChildItem test/test_*.py | Select-Object Name > test-files-before.txt

# Grep all test classes
Select-String -Path "test/test_*.py" -Pattern "^class Test" > test-classes-before.txt
```

---

### Phase 2: Rename Test Files (1 hour)

**Priority: High-impact renames first**

```powershell
cd agile_bot/bots/base_bot/test

# 1. Rename main test file
git mv test_perform_behavior_action.py test_invoke_bot_directly.py

# 2. Rename REPL test files
git mv test_navigate_bot_behaviors_and_actions_with_cli_current.py test_navigate_behaviors_using_repl_commands.py
git mv test_navigate_bot_behaviors_and_actions_with_cli.py test_navigate_behaviors_using_domain_model.py
git mv test_execute_action_operation_through_cli_current.py test_execute_actions_using_repl.py
git mv test_manage_bot_scope_through_cli_current.py test_manage_scope_using_repl.py
git mv test_display_bot_state_using_cli_current.py test_display_state_using_repl.py
git mv test_get_help_using_cli_current.py test_get_help_using_repl.py

# 3. Handle duplicates/old versions
# Option A: Archive old versions
mkdir -p z_archive
git mv test_display_bot_state_using_cli.py z_archive/
git mv test_execute_action_operation_through_cli.py z_archive/
git mv test_manage_bot_scope_through_cli.py z_archive/

# Option B: Or delete if confirmed obsolete
# git rm test_display_bot_state_using_cli.py
# git rm test_execute_action_operation_through_cli.py
# git rm test_manage_bot_scope_through_cli.py

# 4. Consolidate initialize_repl_session files
# Manually merge test_initialize_repl_session_current.py into test_initialize_repl_session.py
# Then: git rm test_initialize_repl_session_current.py

# 5. Commit file renames
git add -A
git commit -m "refactor(tests): rename test files to match refactored story structure"
```

---

### Phase 3: Update Test Class Names (3-4 hours)

**Process for each file:**
1. Open file
2. Use search/replace for each class rename
3. Run tests after each file to ensure no breakage
4. Commit after each file (or small batches)

#### Phase 3.1: test_invoke_bot_directly.py

```powershell
# In test_invoke_bot_directly.py, rename:
# TestInvokeBehaviorActionsInWorkflowOrder → TestExecuteEndToEndWorkflow
# TestExecuteBehavior → TestExecuteBehaviorAction
# TestInsertContextIntoInstructions → TestInjectContextIntoInstructions
# TestCloseCurrentAction → TestConfirmCurrentAction
# TestInvokeBehaviorInActionOrder → TestNavigateSequentially

# Move TestInjectNextBehaviorReminder and TestInjectStatusUpdateBreadcrumbs
# into TestInjectContextIntoInstructions as test methods

# Test
pytest test_invoke_bot_directly.py -v

# Commit
git add test_invoke_bot_directly.py
git commit -m "refactor(tests): rename test classes in test_invoke_bot_directly.py"
```

#### Phase 3.2: test_initialize_repl_session.py

```powershell
# Rename:
# TestLaunchCLIInInteractiveMode → TestStartREPLSession
# TestLaunchCLIInPipeMode → TestStartREPLInPipeMode
# TestDetectAndConfigureTTYNonTTYInputForCLI → TestDetectAndConfigureTTYNonTTYInput
# TestLoadAndDisplayWorkspaceContextInCLI → TestLoadWorkspaceContext

pytest test_initialize_repl_session.py -v
git add test_initialize_repl_session.py
git commit -m "refactor(tests): rename test classes in test_initialize_repl_session.py"
```

#### Phase 3.3: test_navigate_behaviors_using_repl_commands.py

```powershell
# Rename:
# TestNavigateUsingCLIDotNotation → TestNavigateToBehaviorActionAndExecute
# TestNavigateSequentiallyUsingCLICommands → TestNavigateSequentially
# TestExitCLIREPL → TestExitREPL

pytest test_navigate_behaviors_using_repl_commands.py -v
git add test_navigate_behaviors_using_repl_commands.py
git commit -m "refactor(tests): rename test classes in test_navigate_behaviors_using_repl_commands.py"
```

#### Phase 3.4: test_navigate_behaviors_using_domain_model.py

```powershell
# Rename:
# TestNavigateToFirstBehaviorAction → TestNavigateToBehaviorActionAndExecute

# Remove:
# TestAdvanceActionAndPersistState (story deleted)

pytest test_navigate_behaviors_using_domain_model.py -v
git add test_navigate_behaviors_using_domain_model.py
git commit -m "refactor(tests): rename test classes in test_navigate_behaviors_using_domain_model.py, remove obsolete tests"
```

#### Phase 3.5: test_execute_actions_using_repl.py

```powershell
# Rename:
# TestGetActionInstructionsThroughCLI → TestViewInstructions
# TestConfirmWorkThroughCLIWithStringParameters → TestConfirmWithParameters
# TestConfirmActionCompletionThroughCLI → TestConfirmActionCompletion
# TestReExecuteCurrentOperationUsingCLI → TestReExecuteCurrentAction
# TestHandleOperationErrorsAndValidationInCLI → TestHandleErrorsAndValidation

# Remove:
# TestAutoConfirmActionAfterInstructionsComplete (story deleted)
# TestInvokeSpecificBotBehaviorCommandThroughCLI (story deleted)

pytest test_execute_actions_using_repl.py -v
git add test_execute_actions_using_repl.py
git commit -m "refactor(tests): rename test classes in test_execute_actions_using_repl.py, remove obsolete tests"
```

#### Phase 3.6: test_manage_scope_using_repl.py

```powershell
# Rename:
# TestSetScopeThroughCLIUsingStringParameters → TestSetScope
# TestFilterWorkUsingKnowledgeGraphScopeInCLI → TestSetStoryScope
# TestFilterWorkUsingFilesScopeInCLI → TestSetFileScope
# TestValidateScopeAgainstStoryGraphInCLI → TestValidateScopeAgainstStoryGraph
# TestPassScopeParametersWhenExecutingActionsThroughCLI → TestPassScopeParametersWhenExecutingActions
# TestViewCurrentScopeInCLI → TestViewCurrentScope
# TestClearScopeThroughCLI → TestClearScope (note: was TestClearScopeFiltersInCLI in story-graph.json)

pytest test_manage_scope_using_repl.py -v
git add test_manage_scope_using_repl.py
git commit -m "refactor(tests): rename test classes in test_manage_scope_using_repl.py"
```

#### Phase 3.7: test_display_state_using_repl.py

```powershell
# Rename:
# TestDisplayCLIHeader → TestViewSessionHeader
# TestDisplayBotHierarchyTreeInCLI → TestViewBehaviorHierarchy
# TestDisplayCurrentPositionInCLI → TestViewCurrentPosition
# TestDisplayActiveScopeInCLIStatus → TestViewActiveScope
# TestDisplayCLINavigationMenuFooter → TestViewNavigationCommands
# TestDisplayHeadlessModeStatusInCLI → TestViewHeadlessModeStatus
# TestDisplayAvailableBotInTreeHierarchy → TestViewAvailableBots

# Remove or merge:
# TestDisplayCLIBotCommandInNavigationMenuFooter (consider merging with TestViewNavigationCommands)
# TestFormatOutputForAI (story deleted)

pytest test_display_state_using_repl.py -v
git add test_display_state_using_repl.py
git commit -m "refactor(tests): rename test classes in test_display_state_using_repl.py, remove obsolete tests"
```

#### Phase 3.8: test_get_help_using_repl.py

```powershell
# Rename:
# TestViewAvailableCommandsUsingCLIHelp → TestDisplayActionHelpUsingCLI
# TestRequestActionHelpThroughCLI → remove if duplicate of above
# TestViewParameterDocumentationInCLI → TestDisplayParameterHelpUsingCLI
# TestViewCommandExamplesInCLI → TestDisplayCommandExamplesUsingCLI

pytest test_get_help_using_repl.py -v
git add test_get_help_using_repl.py
git commit -m "refactor(tests): rename test classes in test_get_help_using_repl.py"
```

#### Phase 3.9: Action Sub-Epic Test Files

For each file (test_gather_context.py, test_decide_strategy_criteria_action.py, test_build_knowledge.py, test_render_output.py):

```powershell
# 1. Remove obsolete test classes:
#    - TestTrackActivityFor[Action]Action
#    - TestProceedTo[NextAction]
#    - TestLoadBaseActionConfig
#    - TestAccessActions
#    - TestInitializeAction
#    - TestLoadGuardrails

# 2. Rename "Inject" to "Build" test classes:
#    - TestInject...Instructions → TestBuild...Instructions

# 3. Test and commit each file individually
pytest test_gather_context.py -v
git add test_gather_context.py
git commit -m "refactor(tests): remove obsolete tests from test_gather_context.py, rename Inject→Build"

# Repeat for other action test files
```

---

### Phase 4: Update story-graph.json References (1 hour)

**Step 4.1: Update test_file References**

Create a Python script to update all test_file references:

```python
import json

# Map of old → new test file names
TEST_FILE_RENAMES = {
    "test_perform_behavior_action.py": "test_invoke_bot_directly.py",
    "test_navigate_bot_behaviors_and_actions_with_cli_current.py": "test_navigate_behaviors_using_repl_commands.py",
    "test_navigate_bot_behaviors_and_actions_with_cli.py": "test_navigate_behaviors_using_domain_model.py",
    "test_execute_action_operation_through_cli.py": "test_execute_actions_using_repl.py",
    "test_manage_bot_scope_through_cli.py": "test_manage_scope_using_repl.py",
    "test_display_bot_state_using_cli.py": "test_display_state_using_repl.py",
    "test_get_help_using_cli_current.py": "test_get_help_using_repl.py",
}

def update_test_file_references(story_graph_path):
    with open(story_graph_path, 'r') as f:
        data = json.load(f)
    
    # Recursively update test_file references
    def update_node(node):
        if isinstance(node, dict):
            if "test_file" in node and node["test_file"] in TEST_FILE_RENAMES:
                old = node["test_file"]
                new = TEST_FILE_RENAMES[old]
                print(f"  {old} → {new}")
                node["test_file"] = new
            for value in node.values():
                update_node(value)
        elif isinstance(node, list):
            for item in node:
                update_node(item)
    
    update_node(data)
    
    with open(story_graph_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print("\n[OK] Updated test_file references!")

update_test_file_references("agile_bot/bots/base_bot/docs/stories/story-graph.json")
```

**Step 4.2: Update test_class References**

Create a comprehensive mapping and update script:

```python
# Map of old → new test class names (see detailed tables above)
TEST_CLASS_RENAMES = {
    # From test_invoke_bot_directly.py
    "TestInvokeBehaviorActionsInWorkflowOrder": "TestExecuteEndToEndWorkflow",
    "TestExecuteBehavior": "TestExecuteBehaviorAction",
    "TestInsertContextIntoInstructions": "TestInjectContextIntoInstructions",
    "TestCloseCurrentAction": "TestConfirmCurrentAction",
    "TestInvokeBehaviorInActionOrder": "TestNavigateSequentially",
    
    # From test_initialize_repl_session.py
    "TestLaunchCLIInInteractiveMode": "TestStartREPLSession",
    "TestLaunchCLIInPipeMode": "TestStartREPLInPipeMode",
    "TestDetectAndConfigureTTYNonTTYInputForCLI": "TestDetectAndConfigureTTYNonTTYInput",
    "TestLoadAndDisplayWorkspaceContextInCLI": "TestLoadWorkspaceContext",
    
    # From test_navigate_behaviors_using_repl_commands.py
    "TestNavigateUsingCLIDotNotation": "TestNavigateToBehaviorActionAndExecute",
    "TestNavigateSequentiallyUsingCLICommands": "TestNavigateSequentially",
    "TestExitCLIREPL": "TestExitREPL",
    
    # From test_navigate_behaviors_using_domain_model.py
    "TestNavigateToFirstBehaviorAction": "TestNavigateToBehaviorActionAndExecute",
    
    # From test_execute_actions_using_repl.py
    "TestGetActionInstructionsThroughCLI": "TestViewInstructions",
    "TestConfirmWorkThroughCLIWithStringParameters": "TestConfirmWithParameters",
    "TestConfirmActionCompletionThroughCLI": "TestConfirmActionCompletion",
    "TestReExecuteCurrentOperationUsingCLI": "TestReExecuteCurrentAction",
    "TestHandleOperationErrorsAndValidationInCLI": "TestHandleErrorsAndValidation",
    
    # From test_manage_scope_using_repl.py
    "TestSetScopeThroughCLIUsingStringParameters": "TestSetScope",
    "TestFilterWorkUsingKnowledgeGraphScopeInCLI": "TestSetStoryScope",
    "TestFilterWorkUsingFilesScopeInCLI": "TestSetFileScope",
    "TestValidateScopeAgainstStoryGraphInCLI": "TestValidateScopeAgainstStoryGraph",
    "TestPassScopeParametersWhenExecutingActionsThroughCLI": "TestPassScopeParametersWhenExecutingActions",
    "TestViewCurrentScopeInCLI": "TestViewCurrentScope",
    "TestClearScopeFiltersInCLI": "TestClearScope",
    
    # From test_display_state_using_repl.py
    "TestDisplayCLIHeader": "TestViewSessionHeader",
    "TestDisplayBotHierarchyTreeInCLI": "TestViewBehaviorHierarchy",
    "TestDisplayCurrentPositionInCLI": "TestViewCurrentPosition",
    "TestDisplayActiveScopeInCLIStatus": "TestViewActiveScope",
    "TestDisplayCLINavigationMenuFooter": "TestViewNavigationCommands",
    "TestDisplayHeadlessModeStatusInCLI": "TestViewHeadlessModeStatus",
    "TestDisplayAvailableBotInTreeHierarchy": "TestViewAvailableBots",
    
    # From test_get_help_using_repl.py
    "TestViewAvailableCommandsUsingCLIHelp": "TestDisplayActionHelpUsingCLI",
    "TestViewParameterDocumentationInCLI": "TestDisplayParameterHelpUsingCLI",
    "TestViewCommandExamplesInCLI": "TestDisplayCommandExamplesUsingCLI",
}

def update_test_class_references(story_graph_path):
    with open(story_graph_path, 'r') as f:
        data = json.load(f)
    
    # Recursively update test_class references
    def update_node(node):
        if isinstance(node, dict):
            if "test_class" in node and node["test_class"] in TEST_CLASS_RENAMES:
                old = node["test_class"]
                new = TEST_CLASS_RENAMES[old]
                print(f"  {old} → {new}")
                node["test_class"] = new
            for value in node.values():
                update_node(value)
        elif isinstance(node, list):
            for item in node:
                update_node(item)
    
    update_node(data)
    
    with open(story_graph_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print("\n[OK] Updated test_class references!")

update_test_class_references("agile_bot/bots/base_bot/docs/stories/story-graph.json")
```

**Step 4.3: Remove Deleted Story References**

Stories that were deleted and should have no test_class references:
- `TestSaveWorkflowState`
- `TestLoadWorkflowState`
- `TestDetermineResumePointAfterInterruption`
- `TestAutoConfirmActionAfterInstructionsComplete`
- `TestInvokeSpecificBotBehaviorCommandThroughCLI`
- `TestFormatOutputForAI`
- All `TestTrackActivityFor[X]Action` classes
- All `TestProceedTo[X]` classes

**Step 4.4: Commit story-graph.json Updates**

```powershell
git add agile_bot/bots/base_bot/docs/stories/story-graph.json
git commit -m "refactor(story-graph): update all test_file and test_class references to match renamed tests"
```

---

### Phase 5: Validation & Testing (1 hour)

**Step 5.1: Validate story-graph.json**
```powershell
# Ensure it's still valid JSON
Get-Content agile_bot/bots/base_bot/docs/stories/story-graph.json | ConvertFrom-Json | Out-Null
```

**Step 5.2: Run All Tests**
```powershell
cd agile_bot/bots/base_bot
pytest test/ -v > test-results-after-test-rename.txt
```

**Step 5.3: Compare Test Results**
```powershell
# Compare before and after
# Should have same number passing, just different names
```

**Step 5.4: Verify story-graph.json References**
```powershell
# Check for any remaining old test file references
Select-String -Path "agile_bot/bots/base_bot/docs/stories/story-graph.json" -Pattern "test_perform_behavior_action"
Select-String -Path "agile_bot/bots/base_bot/docs/stories/story-graph.json" -Pattern "through_cli"
Select-String -Path "agile_bot/bots/base_bot/docs/stories/story-graph.json" -Pattern "_current"

# Should return no matches
```

**Step 5.5: Verify Git History Preserved**
```powershell
# Check that git log --follow works for renamed files
git log --follow --oneline test_invoke_bot_directly.py
git log --follow --oneline test_navigate_behaviors_using_repl_commands.py

# Should show history going back through old filename
```

---

### Phase 6: Documentation & Cleanup (30 minutes)

**Step 6.1: Update invoke-bot-story-naming-refactor-plan.md**

Add section documenting test file/class renames:
- Link to this document
- Note completion date
- Summarize impact

**Step 6.2: Create Summary Document**

```powershell
# Generate change summary
git log backup-before-test-rename..HEAD --oneline > TEST-RENAME-SUMMARY.txt

# Document test counts
echo "Test Files Renamed: 10" >> TEST-RENAME-SUMMARY.txt
echo "Test Classes Renamed: 60+" >> TEST-RENAME-SUMMARY.txt
echo "Test Classes Removed: 20+" >> TEST-RENAME-SUMMARY.txt
```

**Step 6.3: Update README or Test Documentation**

If there's a test README, update it with new test file names.

---

## ✅ VERIFICATION CHECKLIST

Before considering this phase complete:

- [ ] All test files renamed (10 files)
- [ ] All test classes renamed (60+ classes)
- [ ] Obsolete test classes removed (20+ classes)
- [ ] story-graph.json test_file references updated
- [ ] story-graph.json test_class references updated
- [ ] All tests pass (same count as before renames)
- [ ] story-graph.json is valid JSON
- [ ] Git history preserved (`git log --follow` works)
- [ ] No broken references in story-graph.json
- [ ] Backup branch created and preserved
- [ ] Summary documentation created

---

## 📝 ROLLBACK PLAN

If issues are discovered:

**Option 1: Revert all test rename commits**
```powershell
git log --oneline backup-before-test-rename..HEAD
# Identify commit range
git revert --no-commit <first-commit>^..<last-commit>
git commit -m "revert: rollback test file and class renames"
```

**Option 2: Restore from backup branch**
```powershell
git checkout backup-before-test-rename
git checkout -b refactor-invoke-bot-stories-restored
# Continue from backup
```

**Option 3: Fix forward**
- Identify specific broken test
- Fix test file/class reference
- Re-run tests
- Commit fix

---

## 📊 IMPACT SUMMARY

### Files Changed:
- **10 test files renamed**
- **3-5 test files archived/deleted** (duplicates/obsolete)
- **1 story-graph.json updated** (~87 test_class references + 16 test_file references)

### Classes Changed:
- **60+ test classes renamed**
- **20+ test classes removed** (deleted stories)
- **5-10 test classes merged** (scenarios moved into parent stories)

### Total Effort Estimate:
- **Planning & Analysis:** 2 hours (this document)
- **Implementation:** 6-8 hours
- **Testing & Validation:** 2 hours
- **Documentation:** 1 hour
- **Total:** 11-13 hours

### Risk Level:
- **Medium-High:** Large number of changes, but mechanical and reversible
- **Mitigation:** Backup branch, incremental commits, continuous testing

---

## 🔗 REFERENCES

- Main Refactoring Plan: `docs/refactoring/invoke-bot-story-naming-refactor-plan.md`
- Story Graph: `agile_bot/bots/base_bot/docs/stories/story-graph.json`
- Test Directory: `agile_bot/bots/base_bot/test/`
- Git Branch: `refactor-invoke-bot-stories`
- Commit Range: `81c5986f..6459fb0a`

---

**END OF PLAN**

