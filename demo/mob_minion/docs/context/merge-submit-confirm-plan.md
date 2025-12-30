# Comprehensive Plan: Merge Submit with Confirm and Add --autoconfirm

## Executive Summary

This plan outlines all changes required to:
1. **Merge `submit` operation with `confirm` operation** - `confirm` will take the same parameters as `submit` did
2. **Add `--autoconfirm` parameter to `instructions` operation** - defaults to `false`, when `true` automatically calls confirm after displaying instructions
3. **Update all documentation, help text, tests, and display logic** across BaseBot, StoryBot, and CRCBot

## Scope of Changes

### Actions That Save Parameters (Need Context in Confirm)
- **strategy** - saves decisions and assumptions via `StrategyActionContext`
- **clarify** - saves answers, evidence_provided, and context via `ClarifyActionContext`

### Actions That Don't Save (No Context Needed in Confirm)
- **build** - no submit logic, just returns message
- **validate** - no submit logic, just returns message  
- **render** - no submit logic, just returns message
- **help** - no submit/confirm operations
- **rules** - no submit/confirm operations

---

## Phase 1: Core Action Layer Changes

### 1.1 Action Base Class (`agile_bot/bots/base_bot/src/actions/action.py`)

**Current State:**
- `submit(context)` - calls `_do_submit(context)` template method
- `confirm(context)` - just marks complete, doesn't call submit
- `_do_submit(context)` - template method for subclasses

**Changes Required:**
```python
def confirm(self, context: ActionContext = None) -> Dict[str, Any]:
    """Confirm action complete - saves work and advances to next action.
    
    This is the final phase of the three-phase action pattern.
    Calls _do_submit() to save work, then updates workflow state.
    """
    if context is None:
        context = self.context_class()
    
    # Call submit logic to save work
    submit_result = self._do_submit(context)
    
    # Track activity on completion
    self.track_activity_on_completion()
    
    # Return combined result
    next_action_name = self.next_action
    return {
        'status': 'confirmed',
        'action_completed': self.action_name,
        'next_action': next_action_name,
        'submit_result': submit_result  # Include what was saved
    }

# REMOVE: def submit() method entirely
```

**Files to Change:**
- `agile_bot/bots/base_bot/src/actions/action.py` (lines 406-444)

### 1.2 Strategy Action (`agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py`)

**Current State:**
- Has `_do_submit(context: StrategyActionContext)` that saves decisions/assumptions

**Changes Required:**
- ✅ No changes needed - `_do_submit()` will be called by new `confirm()`
- Context class `StrategyActionContext` already has all needed fields

**Files to Change:**
- None (already compatible)

### 1.3 Clarify Action (`agile_bot/bots/base_bot/src/actions/clarify/clarify_action.py`)

**Current State:**
- Has `_do_submit(context: ClarifyActionContext)` that saves answers/evidence

**Changes Required:**
- ✅ No changes needed - `_do_submit()` will be called by new `confirm()`
- Context class `ClarifyActionContext` already has all needed fields

**Files to Change:**
- None (already compatible)

### 1.4 Build/Validate/Render Actions

**Current State:**
- All have `_do_submit()` that returns simple messages, no saving

**Changes Required:**
- ✅ No changes needed - `_do_submit()` will be called by new `confirm()`

**Files to Change:**
- None (already compatible)

---

## Phase 2: REPL CLI Layer Changes

### 2.1 CLI Action Wrapper (`agile_bot/bots/base_bot/src/repl_cli/cli_bot/cli_actions/cli_action.py`)

**Current State:**
- Has `submit(args)` method that calls `action.submit(context)`
- Has `confirm()` method that calls `action.confirm(empty_context)`

**Changes Required:**
```python
# REMOVE submit() method entirely (lines 56-64)

def confirm(self, args: str = "") -> str:
    """Confirm action - saves work with parameters and advances."""
    try:
        # Update phase to 'confirming'
        self._session.set_action_phase('confirming')
        # Parse args to context (same as old submit did)
        context = self._parse_args_to_context(args)
        # Call confirm with context
        result = self._action.confirm(context)
        return self._format_result(result)
    except Exception as e:
        return f"Error confirming: {str(e)}"
```

**Files to Change:**
- `agile_bot/bots/base_bot/src/repl_cli/cli_bot/cli_actions/cli_action.py` (lines 56-74)

### 2.2 REPL Session Command Handlers (`agile_bot/bots/base_bot/src/repl_cli/repl_session.py`)

**Current State:**
- `_handle_submit_command(args)` - calls `action.submit(args)` (line 560)
- `_handle_confirm_command()` - calls `action.confirm()` with no args (line 580)
- Command routing in `_handle_simple_command()` has both 'submit' and 'confirm' (lines 332-335)

**Changes Required:**

1. **Remove `_handle_submit_command()` method** (lines 560-578)

2. **Update `_handle_confirm_command()` to accept args** (lines 580-625):
```python
def _handle_confirm_command(self, args: str = "") -> REPLCommandResponse:
    if not self.has_current_action:
        return REPLCommandResponse(
            output="ERROR: No current action to confirm",
            response="ERROR: No current action",
            status="error"
        )
    
    behavior = self.current_behavior
    action = self.current_action
    current_behavior_name = behavior.name
    current_action_name = action.name
    
    try:
        # Call confirm on the action WITH ARGS
        result_output = action.confirm(args)
        
        # Check if at last action BEFORE closing
        action_names = behavior.actions.all
        is_last_action = (current_action_name == action_names[-1] if action_names else False)
        
        # Mark current action as complete and advance
        behavior.actions.domain_actions.close_current()
        
        # ... rest of logic unchanged ...
```

3. **Remove 'submit' from command routing** (line 332-333):
```python
# REMOVE these lines:
if command_verb == 'submit':
    return self._handle_submit_command(command_args)
```

4. **Update confirm command routing to pass args** (line 334-335):
```python
if command_verb == 'confirm':
    return self._handle_confirm_command(command_args)  # ADD command_args
```

5. **Update all other places that call `_handle_submit_command`** - search for all occurrences and replace with `_handle_confirm_command`:
   - Line 434: `return self._handle_submit_command("")` → `return self._handle_confirm_command("")`
   - Line 1024: `return self._handle_submit_command(args)` → `return self._handle_confirm_command(args)`
   - Line 1059: `return self._handle_submit_command(args)` → `return self._handle_confirm_command(args)`
   - Line 1109: `return self._handle_submit_command(args)` → `return self._handle_confirm_command(args)`
   - Line 1184: `return self._handle_submit_command("")` → `return self._handle_confirm_command("")`

6. **Remove `_get_submit_params_hint()` helper method** from session (if it exists)

**Files to Change:**
- `agile_bot/bots/base_bot/src/repl_cli/repl_session.py` (multiple locations)

### 2.3 Instructions Command - Add --autoconfirm

**Current State:**
- `_handle_instructions_command(args)` displays instructions and returns (line 507)

**Changes Required:**
```python
def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
    # ... existing validation code ...
    
    action = self.current_action
    try:
        # Parse args to check for --autoconfirm flag
        autoconfirm = self._parse_autoconfirm_flag(args)
        # Remove --autoconfirm from args before passing to action
        cleaned_args = self._remove_autoconfirm_flag(args)
        
        output = action.instructions(cleaned_args)
        
        # If autoconfirm=true, automatically call confirm
        if autoconfirm:
            # Wrap instructions with context header
            instructions_response = self._wrap_with_context_header(output, "Instructions (auto-confirming)")
            # Call confirm with empty args (instructions don't save anything)
            confirm_response = self._handle_confirm_command("")
            # Combine outputs
            combined_output = instructions_response.output + "\n\n" + confirm_response.output
            return REPLCommandResponse(
                output=combined_output,
                response=confirm_response.response,
                status=confirm_response.status
            )
        
        # Normal path - just show instructions
        return self._wrap_with_context_header(output, "Instructions ready")
    except Exception as e:
        return REPLCommandResponse(...)

def _parse_autoconfirm_flag(self, args: str) -> bool:
    """Parse --autoconfirm flag from args string."""
    import re
    # Look for --autoconfirm=true or --autoconfirm true or just --autoconfirm
    if '--autoconfirm' in args.lower():
        # Check if explicitly set to false
        if re.search(r'--autoconfirm[=\s]+false', args, re.IGNORECASE):
            return False
        return True
    return False

def _remove_autoconfirm_flag(self, args: str) -> str:
    """Remove --autoconfirm flag from args string."""
    import re
    # Remove --autoconfirm=value or --autoconfirm value or --autoconfirm
    cleaned = re.sub(r'--autoconfirm(?:[=\s]+\w+)?', '', args, flags=re.IGNORECASE)
    return cleaned.strip()
```

**Files to Change:**
- `agile_bot/bots/base_bot/src/repl_cli/repl_session.py` (lines 507-558)

### 2.4 REPL Status Display (`agile_bot/bots/base_bot/src/repl_cli/repl_status.py`)

**Current State:**
- Has `_get_submit_params(action)` method (line 200)
- Displays "submit" operation in status

**Changes Required:**

1. **Rename method** `_get_submit_params()` → `_get_confirm_params()` (line 200):
```python
def _get_confirm_params(self, action) -> str:
    """Get parameter hints for confirm operation."""
    # Same logic, just renamed
```

2. **Update all callers** of `_get_submit_params()` to use `_get_confirm_params()`

3. **Update operation display text** - change "submit" to "confirm" in status displays (around line 100-130)

**Files to Change:**
- `agile_bot/bots/base_bot/src/repl_cli/repl_status.py` (lines 200-215, and display sections)

### 2.5 Action Cycling Logic

**Current State:**
- When action name called without operation, cycles: instructions → submit → confirm

**Changes Required:**
- Update cycling logic to: instructions → confirm (skip submit since it's merged)
- Find in `repl_session.py` where cycling happens (likely in `_handle_action_shortcut()` or similar)

**Files to Change:**
- `agile_bot/bots/base_bot/src/repl_cli/repl_session.py` (action cycling logic)

---

## Phase 3: Help and Documentation

### 3.1 REPL Help System (`agile_bot/bots/base_bot/src/repl_cli/repl_help.py`)

**Current State:**
- Shows three-phase pattern: instructions → submit → confirm (lines 90-133)
- Has examples with "submit" command
- Has parameter hints for submit

**Changes Required:**

1. **Update ActionHelp class** (lines 77-134):
```python
@property
def help_text(self) -> str:
    lines = [
        f"## {self.action_name}",
        "",
        "Hierarchy: behavior → action → operation",
        "",
        "Usage:",
        f"  {self.action_name} [instructions|confirm]",  # REMOVE submit
        "",
        "Action Operations (two steps):",  # Change from "three steps"
        "",
    ]
    
    # Update _stages property to have only 2 stages
```

2. **Update _stages property** (lines 115-134):
```python
@property
def _stages(self) -> List[List[str]]:
    return [
        [
            "  1. instructions",
            "     Request: Get action instructions and context",
            "     Response: Shows formatted instructions with context",
            f"     Example: {self.action_name} instructions",
            f"     With autoconfirm: {self.action_name} instructions --autoconfirm",
            "",
        ],
        [
            "  2. confirm",
            "     Request: Confirm action complete (saves work if needed)",
            "     Response: Auto-executes next action and shows its instructions",
            f"     Example: {self.action_name} confirm",
            f"     With params: {self.action_name} confirm --decisions='...' --assumptions='...'",
            "",
        ],
    ]
```

3. **Update ParameterCollection** (lines 29-39):
```python
def format_as_lines(self) -> List[str]:
    if not self._parameters:
        return []
    result = ["Context Parameters (when confirming):"]  # Already correct
    result.extend([f"  --{param} <value>" for param in self._parameters])
    result.append("")
    return result
```

4. **Update all command examples** - search for "submit" and replace with "confirm":
   - Line 122-126: Update submit example to confirm
   - Line 200: Update headless submit example
   - Line 255-257: Update piped submit examples

5. **Remove `_get_submit_params_hint()` references** (lines 299, 325, 333):
```python
# REMOVE all calls to session._get_submit_params_hint()
# Replace with session._get_confirm_params_hint()
```

6. **Update operation display in current action help** (lines 330-341):
```python
if submit_hint:
    lines.append(f"      confirm       {submit_hint}")  # Change "submit" to "confirm"
else:
    lines.append(f"      confirm")
```

7. **Update generic operation list** (lines 339-341):
```python
lines.append(f"      instructions  [context, scope, --autoconfirm, or action-specific params]")
lines.append(f"      confirm       [scope, decisions, assumptions, or action-specific params]")
```

8. **Update cycling note** (line 101):
```python
"Note: Calling action name without operation cycles through: instructions → confirm",
```

**Files to Change:**
- `agile_bot/bots/base_bot/src/repl_cli/repl_help.py` (multiple locations throughout)

### 3.2 Main Help Text

**Current State:**
- References submit command in examples

**Changes Required:**
- Search entire help system for "submit" and update to "confirm"
- Update workflow descriptions to show 2-phase instead of 3-phase

**Files to Change:**
- `agile_bot/bots/base_bot/src/repl_cli/repl_help.py` (main help sections)

---

## Phase 4: Status Display Updates

### 4.1 Commands Menu Display

**Current State:**
- Shows "submit" in available commands

**Changes Required:**
- Update command list to show "confirm" instead of "submit"
- Add "--autoconfirm" to instructions command documentation

**Files to Check:**
- Any file that generates command menus or lists
- `agile_bot/bots/base_bot/src/repl_cli/repl_status.py`
- Display components in `agile_bot/bots/base_bot/src/repl_cli/` directory

### 4.2 Status Display in Instructions Output

**Current State:**
- Terminal output shows parameters for submit

**Changes Required:**
- Update parameter display section (lines 995-999 in terminal output shown)
- Change "submit" references to "confirm"

**Files to Change:**
- Find where this display is generated (likely in `repl_status.py` or `repl_session.py`)

---

## Phase 5: Tests

### 5.1 Base Bot Tests

**Files to Review and Update:**
- `agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py`
  - Class: `TestSubmitWorkThroughCLIWithStringParameters` → rename to `TestConfirmWorkThroughCLIWithStringParameters`
  - All test methods that call `submit` → change to `confirm`
  - Update test assertions for new behavior
  
- `agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli_current.py`
  - Similar changes as above

- `agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py`
  - Tests that call `action.submit()` → change to `action.confirm()`

- `agile_bot/bots/base_bot/test/test_execute_behavior_actions.py`
  - Update workflow tests

- `agile_bot/bots/base_bot/test/test_invoke_cli.py`
  - Update CLI invocation tests

- `agile_bot/bots/base_bot/test/test_invoke_mcp.py`
  - Update MCP tool tests if they reference submit

**Changes Needed:**
1. Rename test classes/methods that reference "submit"
2. Change all `session.submit()` calls to `session.confirm()`
3. Change all `action.submit()` calls to `action.confirm()`
4. Update assertions to expect combined submit+confirm behavior
5. Add new tests for `--autoconfirm` flag on instructions

### 5.2 Story Bot Tests

**Files to Review:**
- `agile_bot/bots/story_bot/test/synchronizers/` - any tests that use submit

**Changes Needed:**
- Update any tests that call submit operations

### 5.3 CRC Bot Tests

**Files to Review:**
- Any CRC bot tests that use submit operations

**Changes Needed:**
- Update any tests that call submit operations

---

## Phase 6: Bot-Specific Configurations

### 6.1 Base Bot Action Configs

**Files to Review:**
- `agile_bot/bots/base_bot/base_actions/*/action_config.json`
  - clarify/action_config.json
  - strategy/action_config.json
  - build/action_config.json
  - validate/action_config.json
  - render/action_config.json

**Changes Needed:**
- Review for any references to "submit" in instructions or descriptions
- Update to reference "confirm" instead

### 6.2 Story Bot Behavior Configs

**Files to Review:**
- `agile_bot/bots/story_bot/behaviors/*/guardrails/instructions.json` (if exists)
- `agile_bot/bots/story_bot/behaviors/*/behavior.json`

**Changes Needed:**
- Search for "submit" in all behavior configs
- Update to "confirm"

### 6.3 CRC Bot Behavior Configs

**Files to Review:**
- `agile_bot/bots/crc_bot/behaviors/*/guardrails/instructions.json`
- `agile_bot/bots/crc_bot/behaviors/*/behavior.json`

**Changes Needed:**
- Search for "submit" in all behavior configs
- Update to "confirm"

---

## Phase 7: Documentation Files

### 7.1 Story Documents

**Files to Review:**
- `agile_bot/bots/base_bot/docs/stories/**/*.md`
- `agile_bot/bots/base_bot/docs/stories/**/*.txt`
- Any story maps or increment documents

**Changes Needed:**
- Search for "submit" operation references
- Update to "confirm"
- Update workflow descriptions to 2-phase model

### 7.2 README and Documentation

**Files to Review:**
- `agile_bot/bots/base_bot/docs/README.md` (if exists)
- `agile_bot/bots/base_bot/test/README_API_TESTS.md`
- Any other markdown documentation

**Changes Needed:**
- Update command examples
- Update workflow descriptions

---

## Phase 8: Extension and External Integrations

### 8.1 VS Code Extension

**Files to Review:**
- `agile_bot/bots/base_bot/extension/chat_participants.js`
- `agile_bot/bots/base_bot/extension/package.json`

**Changes Needed:**
- Update any command examples that show "submit"
- Update to show "confirm"

### 8.2 Cursor Commands

**Files to Review:**
- `.cursor/commands/*.md` (if they exist)
- `.continue/config.json`

**Changes Needed:**
- Line 26: `--confirm=true` already exists (good!)
- Update any other references to submit

---

## Phase 9: Launcher Scripts

### 9.1 REPL Launcher

**Files to Review:**
- `agile_bot/repl.ps1`
- Any bash equivalents

**Changes Needed:**
- Update comments/documentation that mention submit
- Update examples to use confirm

### 9.2 Generator Scripts

**Files to Review:**
- `agile_bot/bots/base_bot/generate_bot.ps1`
- `agile_bot/bots/base_bot/generate_bot.sh`

**Changes Needed:**
- Update any template generation that includes submit references

---

## Phase 10: Headless Mode

### 10.1 Headless Session

**Files to Review:**
- `agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py` (if exists)
- Any headless execution logic

**Changes Needed:**
- Update operation routing to use confirm instead of submit
- Ensure --autoconfirm works in headless mode

---

## Implementation Order

### Priority 1 (Core Functionality)
1. Phase 1: Core Action Layer Changes
2. Phase 2: REPL CLI Layer Changes (sections 2.1-2.3)

### Priority 2 (User-Facing)
3. Phase 3: Help and Documentation
4. Phase 4: Status Display Updates

### Priority 3 (Validation)
5. Phase 5: Tests (update existing tests first)

### Priority 4 (Configuration)
6. Phase 6: Bot-Specific Configurations
7. Phase 7: Documentation Files

### Priority 5 (External)
8. Phase 8: Extension and External Integrations
9. Phase 9: Launcher Scripts
10. Phase 10: Headless Mode

---

## Summary of Files to Change

### Core Python Files (Critical)
1. `agile_bot/bots/base_bot/src/actions/action.py` - merge confirm with submit
2. `agile_bot/bots/base_bot/src/repl_cli/cli_bot/cli_actions/cli_action.py` - remove submit, update confirm
3. `agile_bot/bots/base_bot/src/repl_cli/repl_session.py` - remove submit handler, update confirm handler, add autoconfirm
4. `agile_bot/bots/base_bot/src/repl_cli/repl_status.py` - rename submit params to confirm params
5. `agile_bot/bots/base_bot/src/repl_cli/repl_help.py` - update all help text

### Test Files (Critical for Validation)
6. `agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py`
7. `agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli_current.py`
8. `agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py`
9. All other test files that reference submit

### Configuration Files (Medium Priority)
10. All `action_config.json` files in base_bot/base_actions/
11. All `behavior.json` files in story_bot/behaviors/
12. All `behavior.json` files in crc_bot/behaviors/

### Documentation Files (Low Priority)
13. All story documents in docs/stories/
14. README files
15. Extension files

### Total Estimated Files: 50-100+ files

---

## Risk Areas

1. **Breaking Changes**: This is a breaking API change - any external code calling `submit()` will break
2. **Test Coverage**: Need to ensure all tests are updated to prevent false failures
3. **Documentation Lag**: Easy to miss documentation files that reference old workflow
4. **Backward Compatibility**: No backward compatibility possible - this is a clean break
5. **User Training**: Users need to learn new command (though it's simpler)

---

## Benefits

1. **Simpler Mental Model**: 2-phase instead of 3-phase (instructions → confirm)
2. **Fewer Commands**: One less command to remember
3. **More Intuitive**: "Confirm" naturally implies "save and proceed"
4. **Autoconfirm**: Enables faster workflows with --autoconfirm flag
5. **Consistent**: Confirm always does the same thing (save + advance)

---

## Testing Strategy

1. **Unit Tests**: Update all action unit tests
2. **Integration Tests**: Update all REPL session tests
3. **End-to-End Tests**: Test full workflows with confirm
4. **Autoconfirm Tests**: Add new tests for --autoconfirm flag
5. **Manual Testing**: Test each bot (base, story, crc) manually

---

## Rollout Plan

1. **Phase 1-2**: Core changes (breaking changes)
2. **Phase 5**: Update tests (validate core changes work)
3. **Run full test suite**: Ensure nothing broken
4. **Phase 3-4**: Update help/display (user-facing)
5. **Manual testing**: Test each bot manually
6. **Phase 6-10**: Update configs, docs, extensions (cleanup)
7. **Final validation**: Full regression test

---

## Notes

- The change is simpler than it appears because the template method pattern (`_do_submit()`) means most action subclasses don't need changes
- The main complexity is in updating all the display, help, and test code
- The `--autoconfirm` flag is a simple addition that just chains instructions → confirm
- Context classes already have all needed fields for confirm to work with parameters
