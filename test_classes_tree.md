# Test Classes Organized by Epic/Sub-Epic

## (E) Build Agile Bots
### test_build_agile_bots.py
- Helper file (no test classes)

### (E) Generate MCP Tools
#### test_generate_mcp_tools.py
- [OK] TestGenerateBotTools → "Generate Bot Tools"
- [OK] TestGenerateBehaviorTools → "Generate Behavior Tools"
- [OK] TestGenerateMCPBotServer → "Generate MCP Bot Server"
- [OK] TestDeployMCPBotServer → "Deploy MCP BOT Server"
- [MISSING STORY] TestRestartMCPServerToLoadCodeChanges → Story exists "Restart MCP Server To Load Code Changes" but missing test_class field
- [INFRASTRUCTURE] TestMCPGeneratorExceptions (duplicate - exception handling)

### (E) Generate CLI
#### test_generate_cli.py
- [MISSING STORY] TestGenerateBOTCLIcode → Story exists "Generate BOT CLI code" but missing test_class field
- [OK] TestGenerateCursorCommandFiles → "Generate Cursor Command Files"
- [MISSING STORY] TestGenerateHelp → No story in epics
- [MISSING STORY] TestGenerateCursorAwarenessFiles → No story in epics
- [INFRASTRUCTURE] TestGenerateHelpParametersFromActionContextClasses

## (E) Invoke Bot
### test_invoke_bot.py
- Helper file (no test classes)

### (E) Init Project
#### test_init_project.py
- [MISSING STORY] TestBootstrapWorkspace → No story in epics

### (E) Invoke MCP
#### test_invoke_mcp.py
- [OK] TestInvokeBotTool → "Invoke Bot Tool"
- [OK] TestLoadAndMergeBehaviorActionInstructions → "Load And Merge Behavior Action Instructions"
- [OK] TestForwardToCurrentBehaviorAndCurrentAction → "Forward To Current Behavior and Current Action"
- [OK] TestForwardToCurrentAction → "Forward To Current Action"
- [MISSING STORY] TestTrackActivityForWorkspace → No story in epics

### (E) Invoke CLI
#### test_invoke_cli.py
- [INFRASTRUCTURE] TestDetectTriggerWordsThroughExtension
- [INFRASTRUCTURE] TestCLIExceptions
- [INFRASTRUCTURE] TestGetTriggerPriority (duplicate)
- [INFRASTRUCTURE] TestMatchTextAgainstTriggers
- [INFRASTRUCTURE] TestCliAcceptsScopeWithPythonDictSyntax
- [INFRASTRUCTURE] TestCliNormalizesPythonDictToJson
- [INFRASTRUCTURE] TestCliBuildsParametersFromArguments
- [INFRASTRUCTURE] TestCliHandlesScopeInRealUsage
- [INFRASTRUCTURE] TestCliPreservesArrayValuesInScope
- [INFRASTRUCTURE] TestScopeBasedParameterHandling (duplicate)
- [INFRASTRUCTURE] TestValidationParameterVariations
- [INFRASTRUCTURE] TestCliTypeSafeActionContext
- [INFRASTRUCTURE] TestCliContextBuilderParsesTypedContext
- [INFRASTRUCTURE] TestCliParserGeneratorCreatesActionParsers

## (E) Execute Behavior Actions
### test_execute_behavior_actions.py
- Helper file (no test classes)

### (E) Gather Context
#### test_gather_context.py
- [MISSING STORY] TestTrackActivityForClarifyContextAction → Story has "Track Activity for Gather Context Action" with TestTrackActivityForGatherContextAction (different class name)
- [OK] TestProceedToDecidePlanning → "Proceed To Decide Planning"
- [OK] TestInjectGuardrailsAsPartOfClarifyRequirements → "Inject Guardrails As Part Of Clarify Requirements"
- [OK] TestStoreClarificationData → "Store Clarification Data"
- [INFRASTRUCTURE] TestLoadBaseActionConfig
- [INFRASTRUCTURE] TestAccessActions
- [INFRASTRUCTURE] TestInitializeAction
- [INFRASTRUCTURE] TestLoadGuardrails

### (E) Decide Planning Criteria Action
#### test_decide_strategy_criteria_action.py
- [MISSING STORY] TestTrackActivityForStrategyAction → Story has "Track Activity for Planning Action" with TestTrackActivityForPlanningAction (different class name)
- [OK] TestProceedToBuildKnowledge → "Proceed To Build Knowledge"
- [INFRASTRUCTURE] TestInjectStrategyIntoInstructions
- [INFRASTRUCTURE] TestStoreStrategyData

### (E) Build Knowledge
#### test_build_knowledge.py
- [OK] TestTrackActivityForBuildKnowledgeAction → "Track Activity for Build Knowledge Action"
- [OK] TestProceedToRenderOutput → "Proceed To Render Output"
- [OK] TestInjectKnowledgeGraphTemplateForBuildKnowledge → "Inject Knowledge Graph Template and Builder Instructions"
- [OK] TestUpdateExistingKnowledgeGraph → "Update Existing Knowledge Graph"
- [OK] TestLoadStoryGraphIntoMemory → "Load Story Graph Into Memory"
- [MISSING STORY] TestCreateBuildScope → No story in epics
- [MISSING STORY] TestFilterKnowledgeGraph → No story in epics

### (E) Render Output
#### test_render_output.py
- [OK] TestTrackActivityForRenderOutputAction → "Track Activity for Render Output Action"
- [OK] TestProceedToValidateRules → "Proceed To Validate Rules"
- [OK] TestLoadRenderConfigurations → "Load Render Configurations"
- [OK] TestInjectTemplateInstructions → "Inject Template Instructions"
- [OK] TestInjectSynchronizerInstructions → "Inject Synchronizer Instructions"
- [INFRASTRUCTURE] TestInjectRenderInstructionsAndConfigs
- [INFRASTRUCTURE] TestGetRenderInstructions (duplicate)
- [INFRASTRUCTURE] TestMergeBaseAndRenderInstructions
- [INFRASTRUCTURE] TestRenderOutputUsingSynchronizers

### (E) Validate Knowledge & Content Against Rules
#### test_validate_knowledge_and_content_against_rules.py
- [OK] TestTrackActivityForValidateRulesAction → "Track Activity for Validate Rules Action"
- [OK] TestInvokeCompleteValidationWorkflow → "Invoke Complete Validation Workflow"
- [MISSING STORY] TestDiscoversScanners → Story exists "Discovers Scanners" but missing test_class field
- [MISSING STORY] TestRunScannersAgainstKnowledgeGraph → Story exists "Run Scanners against Knowledge Graph" but missing test_class field
- [OK] TestValidateRulesAccordingToScope → "Validate Rules According To Scope"
- [OK] TestGenerateViolationReport → "Generate Violation Report"
- [MISSING STORY] TestInjectValidationRulesForValidateRulesAction → Story exists "Inject Validation Rules for Validate Rules Action" but missing test_class field
- [INFRASTRUCTURE] TestHandleValidateRulesExceptions
- [INFRASTRUCTURE] TestRunAllScanners
- [INFRASTRUCTURE] TestRunScannersAgainstTestCode
- [INFRASTRUCTURE] TestRunScannersAgainstCode
- [INFRASTRUCTURE] TestLoadRulesCollection
- [INFRASTRUCTURE] TestFindRuleByName
- [INFRASTRUCTURE] TestIterateRules
- [INFRASTRUCTURE] TestLoadRuleFromFile
- [INFRASTRUCTURE] TestLoadScannerForRule
- [INFRASTRUCTURE] TestGetRuleProperties
- [INFRASTRUCTURE] TestCreateValidationScope
- [INFRASTRUCTURE] TestLoadScannerClass
- [INFRASTRUCTURE] TestLoadScannerClasses
- [INFRASTRUCTURE] TestPerformIncrementalValidation
- [INFRASTRUCTURE] TestScopeBasedParameterHandling (duplicate)
- [INFRASTRUCTURE] TestValidationWithAllParameterCombinations
- [INFRASTRUCTURE] TestInjectRulesIntoAIChatMessage
- [INFRASTRUCTURE] TestExampleStory (multiple - example tests)
- [INFRASTRUCTURE] TestAnotherStory (example test)

### (E) Perform Behavior Action
#### test_perform_behavior_action.py
- [OK] TestInjectNextBehaviorReminder → "Inject Next Behavior Reminder"
- [OK] TestCloseCurrentAction → "Close Current Action"
- [OK] TestInvokeBehaviorActionsInWorkflowOrder → "Invoke Behavior Actions in Workflow Order"
- [MISSING STORY] TestInvokeBehaviorInActionOrder → Story has "Invoke Behavior in Workflow Order" with TestInvokeBehaviorInWorkflowOrder (different class name)
- [OK] TestExecuteBehavior → "Execute Behavior"
- [MISSING STORY] TestInsertContextIntoInstructions → No story in epics
- [MISSING STORY] TestInjectStatusUpdateBreadcrumbsIntoInstructions → No story in epics
- [INFRASTRUCTURE] TestLoadBotConfiguration
- [INFRASTRUCTURE] TestLoadBehaviorConfiguration
- [INFRASTRUCTURE] TestLoadBotBehaviors
- [INFRASTRUCTURE] TestLoadActions
- [INFRASTRUCTURE] TestLoadBaseActionConfiguration
- [INFRASTRUCTURE] TestAccessBotPaths
- [INFRASTRUCTURE] TestGetBaseInstructions
- [INFRASTRUCTURE] TestLoadBehaviorConfig
- [INFRASTRUCTURE] TestManageBehaviorsCollection
- [INFRASTRUCTURE] TestResolveBotPaths
- [INFRASTRUCTURE] TestFilterActionBasedOnScope

## Infrastructure/Helper Test Files
### test_helpers.py
- [OK] TestFindBehaviorFolder → "Find Behavior Folder"

### test_resources.py
- [INFRASTRUCTURE] TestLineResource
- [INFRASTRUCTURE] TestFileResource
- [INFRASTRUCTURE] TestBlockResource
- [INFRASTRUCTURE] TestScopeResource
- [INFRASTRUCTURE] TestScanResource
- [INFRASTRUCTURE] TestViolationResource
- [INFRASTRUCTURE] TestBlockExtractorHelper

---

## Summary

### Test Classes Missing Stories (Need to add to epics):
1. TestGenerateHelp
2. TestGenerateCursorAwarenessFiles
3. TestBootstrapWorkspace
4. TestTrackActivityForWorkspace
5. TestCreateBuildScope
6. TestFilterKnowledgeGraph
7. TestInsertContextIntoInstructions
8. TestInjectStatusUpdateBreadcrumbsIntoInstructions

### Stories Missing test_class Fields (Need to add test_class):
1. "Restart MCP Server To Load Code Changes" → TestRestartMCPServerToLoadCodeChanges
2. "Generate BOT CLI code" → TestGenerateBOTCLIcode
3. "Discovers Scanners" → TestDiscoversScanners
4. "Run Scanners against Knowledge Graph" → TestRunScannersAgainstKnowledgeGraph
5. "Inject Validation Rules for Validate Rules Action" → TestInjectValidationRulesForValidateRulesAction

### Test Classes with Different Names (May need alignment):
1. TestTrackActivityForClarifyContextAction vs TestTrackActivityForGatherContextAction
2. TestTrackActivityForStrategyAction vs TestTrackActivityForPlanningAction
3. TestInvokeBehaviorInActionOrder vs TestInvokeBehaviorInWorkflowOrder

