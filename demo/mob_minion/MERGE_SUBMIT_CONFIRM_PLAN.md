# Plan: Merge Submit with Confirm

## Overview
Merge `submit` and `confirm` operations so that `confirm` takes the same parameters as `submit` and saves data based on the action type. Add `--autoconfirm:true` parameter (default: false) for the instructions operation.

## Key Requirements
1. `confirm` will have the same signature as `submit` (takes `context: ActionContext`)
2. For `strategy` and `clarify` operations: parameters need to be saved
3. For `build`, `validate`, and `render`: nothing gets saved
4. Add `--autoconfirm:true` parameter (default: false) for instructions operation
5. Add display in the section to show autoconfirm status
6. Ensure all operations work correctly across BaseBot, StoryBot, and CRCBot

---

## 1. CORE ACTION CLASSES (BaseBot)

### 1.1 `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py`

**Changes:**
- **Line 406-418 (`submit` method)**: 
  - Change signature to accept `context: ActionContext = None` (already has this)
  - Keep `_do_submit` template method pattern
  - Document that submit now saves data for strategy/clarify, but not for build/validate/render

- **Line 428-444 (`confirm` method)**:
  - **MAJOR CHANGE**: Update signature to match `submit`: `def confirm(self, context: ActionContext = None) -> Dict[str, Any]`
  - **MAJOR CHANGE**: Call `_do_submit(context)` first to save parameters (for strategy/clarify)
  - **MAJOR CHANGE**: Then call `_do_confirm(context)` template method
  - Keep workflow advancement logic (track completion, return next_action)
  - Return combined result with both submit and confirm status

- **New method**: Add `_do_confirm(self, context: ActionContext) -> Dict[str, Any]` template method
  - Default implementation: just track completion and return next action info
  - Subclasses can override if needed

**Impact**: This is the core change that affects all actions

---

### 1.2 Action Subclasses - Strategy Action

**File**: `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py`

**Changes:**
- **Line 39-69 (`_do_submit` method)**:
  - Already saves strategy decisions and assumptions
  - No changes needed - this will be called from `confirm` now

- **Verify**: Ensure `save_strategy` method (line 136-144) works correctly when called from confirm

**Impact**: Strategy action will save data when confirm is called (as intended)

---

### 1.3 Action Subclasses - Clarify Action

**File**: `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/clarify_action.py`

**Changes:**
- **Line 39-86 (`_do_submit` method)**:
  - Already saves clarification answers, evidence, and context
  - No changes needed - this will be called from `confirm` now

- **Verify**: Ensure `save_clarification` method (line 95-104) works correctly when called from confirm

**Impact**: Clarify action will save data when confirm is called (as intended)

---

### 1.4 Action Subclasses - Build Action

**File**: `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_action.py`

**Changes:**
- **Line 81-86 (`_do_submit` method)**:
  - Currently returns status message only (no saving)
  - No changes needed - this is correct behavior

**Impact**: Build action will continue to not save anything (as intended)

---

### 1.5 Action Subclasses - Validate Action

**File**: `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py`

**Changes:**
- **Line 181-193 (`_do_submit` method)**:
  - Currently runs validation scanners and generates reports
  - No changes needed - this is correct behavior (reports are generated, not saved as parameters)

**Impact**: Validate action will continue to not save parameters (as intended)

---

### 1.6 Action Subclasses - Render Action

**File**: `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py`

**Changes:**
- **Line 73-78 (`_do_submit` method)**:
  - Currently returns status message only (no saving)
  - No changes needed - this is correct behavior

**Impact**: Render action will continue to not save anything (as intended)

---

## 2. REPL CLI LAYER

### 2.1 `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/cli_bot/cli_actions/cli_action.py`

**Changes:**
- **Line 56-64 (`submit` method)**:
  - Already accepts `args: str` and parses to context
  - No signature changes needed

- **Line 66-74 (`confirm` method)**:
  - **MAJOR CHANGE**: Update signature to match `submit`: `def confirm(self, args: str = "") -> str`
  - **MAJOR CHANGE**: Parse args to context (same as submit): `context = self._parse_args_to_context(args)`
  - **MAJOR CHANGE**: Pass context to action: `result = self._action.confirm(context)`
  - Update phase tracking: `self._session.set_action_phase('confirming')`

**Impact**: REPL CLI will now pass parameters to confirm

---

### 2.2 `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py`

**Changes:**
- **Line 507-558 (`_handle_instructions_command` method)**:
  - **NEW**: Add support for `--autoconfirm:true` parameter parsing
  - **NEW**: Store autoconfirm flag in session state
  - **NEW**: Add display section showing autoconfirm status

- **Line 560-578 (`_handle_submit_command` method)**:
  - Already handles args correctly
  - No changes needed

- **Line 580-619 (`_handle_confirm_command` method)**:
  - **MAJOR CHANGE**: Update to accept args: `def _handle_confirm_command(self, args: str = "") -> REPLCommandResponse`
  - **MAJOR CHANGE**: Parse args and pass to action: `result_output = action.confirm(args)`
  - Keep workflow advancement logic

- **Line 431-443 (operation routing)**:
  - Verify confirm operation routing works correctly

- **Line 782-821 (`_execute_operation_locally` method)**:
  - Verify operation parameter handling for confirm

**Impact**: REPL session will handle confirm with parameters and autoconfirm flag

---

### 2.3 `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py` - Display Section

**Changes:**
- **NEW**: Add method to display autoconfirm status in instructions output
- **NEW**: Add visual indicator when autoconfirm is enabled
- **Location**: In `_handle_instructions_command` or `_wrap_with_context_header`

**Impact**: Users will see autoconfirm status in the display

---

## 3. CLI LAYER (BaseBotCli)

### 3.1 `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py`

**Changes:**
- **Line 102-112 (`_execute_command` method)**:
  - Verify that action execution handles submit/confirm correctly
  - No changes needed if routing is correct

**Impact**: CLI executor should work correctly (verify)

---

### 3.2 `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_command_router.py`

**Changes:**
- **Line 17-38 (`route_to_action` and `_route_to_specific_action` methods)**:
  - **REVIEW**: Currently calls `action.execute(context)` - this is correct for full execution
  - **VERIFY**: Check if CLI needs to support separate submit/confirm operations
  - **NOTE**: CLI may route to execute() which handles full workflow, not individual operations
  - **DECISION NEEDED**: Does CLI need to support operations (instructions/submit/confirm) or just execute()?

- **Line 57-65 (`_execute_current_action` method)**:
  - **REVIEW**: Currently calls `action.execute()` without context
  - **VERIFY**: Check if this needs to support operations

**Impact**: CLI routing should work correctly (verify - may need operation support)

---

### 3.3 `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py`

**Changes:**
- **Line 36-52 (`_create_argument_parser` method)**:
  - **NEW**: Add `--autoconfirm` argument: `parser.add_argument('--autoconfirm', action='store_true', help='Auto-confirm after instructions (default: False)')`
  - **NEW**: Or use key-value format: `--autoconfirm:true` (handled by existing `_parse_key_value_arg`)

- **Line 18-33 (`_build_remaining_args` method)**:
  - **NEW**: Add autoconfirm to remaining args if set: `if getattr(args, 'autoconfirm', False): remaining.append('--autoconfirm:true')`

- **Line 62-81 (`_build_params_from_args` method)**:
  - **NEW**: Add autoconfirm to params: `if getattr(args, 'autoconfirm', False): params['autoconfirm'] = True`

**Impact**: CLI will parse autoconfirm parameter

---

### 3.4 `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_context_builder.py`

**Changes:**
- **Review**: Verify context building works for confirm operation
- **Check**: Ensure all context types (StrategyActionContext, ClarifyActionContext, etc.) are built correctly

**Impact**: Context building should work correctly (verify)

---

## 4. MCP SERVER IMPLEMENTATIONS

### 4.1 StoryBot MCP Server

**File**: `/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot/src/story_bot_mcp_server.py`

**Changes:**
- **Line 57-71 (`bot_tool`)**:
  - Currently calls `action.execute(parameters or {})`
  - **VERIFY**: Check if this needs to handle submit/confirm operations separately
  - **CHECK**: Ensure parameters are passed correctly to confirm

- **Line 146-157, 159-170, 172-183, 185-196, 198-209, 211-222, 224-235 (behavior tools)**:
  - All call `action.execute(parameters or {})`
  - **VERIFY**: Check if these need to handle submit/confirm operations
  - **CHECK**: Ensure parameters are passed correctly

**Impact**: MCP tools should work correctly (verify operation handling)

---

### 4.2 CRCBot MCP Server

**File**: `/mnt/c/dev/augmented-teams/agile_bot/bots/crc_bot/src/crc_bot_mcp_server.py`

**Changes:**
- **Line 57-71 (`bot_tool`)**:
  - Currently calls `action.execute(parameters or {})`
  - **VERIFY**: Check if this needs to handle submit/confirm operations separately
  - **CHECK**: Ensure parameters are passed correctly to confirm

- **Line 146-157, 159-170, 172-183 (behavior tools)**:
  - All call `action.execute(parameters or {})`
  - **VERIFY**: Check if these need to handle submit/confirm operations
  - **CHECK**: Ensure parameters are passed correctly

**Impact**: MCP tools should work correctly (verify operation handling)

---

### 4.3 BaseBot MCP Server (if exists)

**Files**: Check for base_bot MCP server files
- `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_code_visitor.py`
- `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/mcp_code_visitor.py`

**Changes:**
- **Review**: Check if these handle submit/confirm operations
- **Verify**: Ensure parameters are passed correctly

**Impact**: BaseBot MCP should work correctly (verify)

---

## 5. ACTION CONTEXT CLASSES

### 5.1 `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py`

**Changes:**
- **Line 456-460 (`ClarifyActionContext`)**:
  - Already has `answers`, `evidence_provided`, `context` fields
  - No changes needed

- **Line 463-498 (`StrategyActionContext`)**:
  - Already has `decisions_made`, `assumptions`, `assumptions_made` fields
  - No changes needed

- **NEW**: Consider adding `autoconfirm: bool = False` field to base `ActionContext`?
  - **DECISION NEEDED**: Should autoconfirm be part of context or handled separately?

**Impact**: Context classes should work correctly (may need autoconfirm field)

---

## 6. INSTRUCTIONS CLASS

### 6.1 `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py`

**Changes:**
- **Review**: Check if instructions need to store autoconfirm flag
- **NEW**: May need to add autoconfirm to display content

**Impact**: Instructions may need autoconfirm support

---

## 7. HEADLESS MODE

### 7.1 `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py`

**Changes:**
- **Line 108**: `operations = ['instructions', 'submit', 'confirm']`
  - **VERIFY**: Ensure confirm operation handles parameters correctly
  - **CHECK**: Ensure autoconfirm flag is respected in headless mode

- **Review**: Check operation execution logic
  - **VERIFY**: Confirm operation receives parameters
  - **VERIFY**: Autoconfirm flag is passed through

**Impact**: Headless mode should work correctly with merged submit/confirm

---

## 8. TEST FILES

### 8.1 Test Files to Update

**Files to review and potentially update:**

1. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py`
   - **CHANGE**: Update tests to verify confirm accepts parameters
   - **CHANGE**: Add tests for autoconfirm parameter

2. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli_current.py`
   - **CHANGE**: Update tests to verify confirm accepts parameters
   - **CHANGE**: Add tests for autoconfirm parameter

3. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_in_headless_mode.py`
   - **CHANGE**: Update tests for confirm operation with parameters
   - **CHANGE**: Add tests for autoconfirm in headless mode

4. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py`
   - **CHANGE**: Update tests to verify strategy saves data on confirm
   - **CHANGE**: Test confirm with strategy context parameters

5. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/test/test_gather_context.py`
   - **CHANGE**: Update tests to verify clarify saves data on confirm
   - **CHANGE**: Test confirm with clarify context parameters

6. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py`
   - **VERIFY**: Ensure build action doesn't save on confirm (test negative case)

7. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py`
   - **VERIFY**: Ensure validate action doesn't save parameters on confirm (test negative case)

8. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/test/test_render_output.py`
   - **VERIFY**: Ensure render action doesn't save on confirm (test negative case)

9. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/test/test_initialize_repl_session.py`
   - **CHANGE**: Update tests for confirm with parameters

10. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/test/test_initialize_repl_session_current.py`
    - **CHANGE**: Update tests for confirm with parameters

11. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/test/test_current_initialize_repl_session.py`
    - **CHANGE**: Update tests for confirm with parameters

**Impact**: All tests need to be updated to reflect new confirm signature and behavior

---

## 9. CONFIGURATION FILES

### 9.1 Action Config Files

**Files to review:**

1. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/base_actions/strategy/action_config.json`
   - **VERIFY**: No changes needed (submit already saves)

2. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/base_actions/clarify/action_config.json`
   - **VERIFY**: No changes needed (submit already saves)

3. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/base_actions/build/action_config.json`
   - **VERIFY**: No changes needed (submit doesn't save)

4. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/base_actions/validate/action_config.json`
   - **VERIFY**: No changes needed (submit doesn't save parameters)

5. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/base_actions/render/action_config.json`
   - **VERIFY**: No changes needed (submit doesn't save)

**Impact**: Config files should be fine (verify)

---

## 10. DISPLAY AND UI CHANGES

### 10.1 Display Section for Autoconfirm

**Files to modify:**

1. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py`
   - **NEW**: Add display section showing autoconfirm status
   - **Location**: In `_handle_instructions_command` or `_wrap_with_context_header`

2. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py`
   - **NEW**: May need to add autoconfirm to display content in `_format_instructions_for_display`

3. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/cli_bot/cli_actions/cli_action.py`
   - **NEW**: May need to add autoconfirm display in instructions output

**Impact**: Users will see autoconfirm status in the display

---

## 11. DOCUMENTATION

### 11.1 Documentation Files to Update

**Files to review:**

1. `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/docs/stories/story-graph.json`
   - **REVIEW**: Check if stories mention submit/confirm operations
   - **UPDATE**: Update any stories that reference submit/confirm behavior

2. Help files and README files
   - **REVIEW**: Check for documentation about submit/confirm operations
   - **UPDATE**: Update to reflect merged behavior

**Impact**: Documentation should reflect new behavior

---

## 12. BOT-SPECIFIC FILES

### 12.1 StoryBot

**Files:**
- `/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot/src/story_bot_cli.py`
  - **VERIFY**: Uses BaseBotCli, should inherit changes automatically

- `/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot/src/story_bot_mcp_server.py`
  - **CHANGES**: See section 4.1

**Impact**: StoryBot should work correctly after base changes

---

### 12.2 CRCBot

**Files:**
- `/mnt/c/dev/augmented-teams/agile_bot/bots/crc_bot/src/crc_bot_cli.py`
  - **VERIFY**: Uses BaseBotCli, should inherit changes automatically

- `/mnt/c/dev/augmented-teams/agile_bot/bots/crc_bot/src/crc_bot_mcp_server.py`
  - **CHANGES**: See section 4.2

**Impact**: CRCBot should work correctly after base changes

---

## 13. SUMMARY OF CHANGES BY PRIORITY

### Critical Changes (Must Do)
1. **Action.py**: Update `confirm` method signature and implementation
2. **CLIAction.py**: Update `confirm` method signature and implementation
3. **REPLSession.py**: Update `_handle_confirm_command` to accept args
4. **All tests**: Update to reflect new confirm signature

### Important Changes (Should Do)
5. **REPLSession.py**: Add autoconfirm parameter parsing and display
6. **CLIParameterParser.py**: Add autoconfirm parameter support
7. **MCP Servers**: Verify operation handling
8. **Display**: Add autoconfirm status display

### Verification Changes (Verify)
9. **All action subclasses**: Verify _do_submit behavior is correct
10. **CLI routing**: Verify operation routing works correctly
11. **Context building**: Verify context building works for confirm
12. **Headless mode**: Verify headless mode works correctly

---

## 14. TESTING CHECKLIST

### Unit Tests
- [ ] Test confirm with strategy context saves data
- [ ] Test confirm with clarify context saves data
- [ ] Test confirm with build context doesn't save
- [ ] Test confirm with validate context doesn't save parameters
- [ ] Test confirm with render context doesn't save
- [ ] Test autoconfirm parameter parsing
- [ ] Test autoconfirm display

### Integration Tests
- [ ] Test REPL CLI confirm with parameters
- [ ] Test CLI confirm with parameters
- [ ] Test MCP confirm with parameters
- [ ] Test headless mode confirm with parameters
- [ ] Test workflow advancement after confirm

### End-to-End Tests
- [ ] Test full strategy workflow: instructions -> submit -> confirm
- [ ] Test full clarify workflow: instructions -> submit -> confirm
- [ ] Test full build workflow: instructions -> submit -> confirm
- [ ] Test autoconfirm in instructions operation

---

## 15. RISKS AND CONSIDERATIONS

### Risks
1. **Breaking Changes**: Changing confirm signature may break existing code
   - **Mitigation**: Update all call sites systematically

2. **Parameter Parsing**: Ensuring parameters are parsed correctly for confirm
   - **Mitigation**: Reuse submit parameter parsing logic

3. **Workflow State**: Ensuring workflow advancement still works correctly
   - **Mitigation**: Keep existing workflow logic, just add submit call before

4. **MCP Tools**: MCP tools may need updates to handle operations
   - **Mitigation**: Verify each MCP tool handles operations correctly

### Considerations
1. **Backward Compatibility**: Consider if old confirm() calls need to work
   - **Decision**: New signature should accept None for context (backward compatible)

2. **Autoconfirm Default**: Default is false, which is correct
   - **Decision**: Keep default as false

3. **Display Location**: Where to show autoconfirm status
   - **Decision**: Show in instructions display section

---

## 16. IMPLEMENTATION ORDER

### Phase 1: Core Changes
1. Update `Action.confirm()` method
2. Update `CLIAction.confirm()` method
3. Update `REPLSession._handle_confirm_command()` method

### Phase 2: Parameter Support
4. Add autoconfirm parameter parsing
5. Add autoconfirm to context (if needed)
6. Add autoconfirm display

### Phase 3: Verification
7. Update all tests
8. Verify MCP servers
9. Verify CLI routing
10. Verify headless mode

### Phase 4: Documentation
11. Update documentation
12. Update help text
13. Update examples

---

## 17. ADDITIONAL FINDINGS

### 17.1 MCP Code Generation

**Files:**
- `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_code_visitor.py`
- `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/mcp_code_visitor.py`

**Findings:**
- These files generate MCP server code
- Generated code calls `action.execute(parameters)` which handles full workflow
- MCP tools don't directly call submit/confirm operations
- **DECISION**: MCP tools will continue to use execute() - no changes needed unless we want operation support

**Impact**: MCP code generation doesn't need changes for this refactoring

---

### 17.2 CLI Operation Support

**Finding:**
- CLI currently routes to `action.execute()` which handles full workflow
- REPL CLI supports operations (instructions/submit/confirm)
- Standard CLI may not support operations - uses execute() instead
- **DECISION**: Verify if CLI needs operation support or if execute() is sufficient

**Impact**: May need to add operation support to CLI if required

---

## END OF PLAN

This plan covers all files that need to be changed to merge submit with confirm and add autoconfirm support. The changes are organized by component and priority to ensure systematic implementation.

### Key Decisions Made:
1. `confirm` will call `_do_submit` first, then `_do_confirm`
2. `confirm` signature matches `submit` (takes `context: ActionContext`)
3. Autoconfirm parameter format: `--autoconfirm:true` (default: false)
4. Autoconfirm applies to instructions operation only
5. Display autoconfirm status in instructions section
6. MCP tools continue using execute() (no operation support needed)

### Key Decisions Needed:
1. Should autoconfirm be part of ActionContext or handled separately?
2. Does standard CLI need operation support (instructions/submit/confirm) or is execute() sufficient?
3. Should MCP tools support operations, or continue using execute()?

### Estimated Impact:
- **Files to modify**: ~15-20 core files
- **Files to verify**: ~30-40 test and configuration files
- **Test files to update**: ~10-15 test files
- **Complexity**: Medium-High (signature changes affect many call sites)
