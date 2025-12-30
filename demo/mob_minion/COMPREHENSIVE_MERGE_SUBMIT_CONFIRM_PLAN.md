# COMPREHENSIVE PLAN: Merge Submit with Confirm and Add --autoconfirm

## Executive Summary

This document provides a **complete, exhaustive plan** for merging the `submit` operation with `confirm` and adding `--autoconfirm` support. Every file, class, method, test, configuration, and reference that needs to change is documented here.

**Key Changes:**
1. `confirm` will take the same signature as `submit` (accepts `context: ActionContext`)
2. `confirm` will call `_do_submit(context)` internally to save parameters for strategy/clarify actions
3. `submit` method will be **COMPLETELY REMOVED** from all action classes
4. `--autoconfirm:true` parameter added to `instructions` operation (default: false)
5. Display section will show autoconfirm status
6. All references to "submit" in help, docs, tests, configs will be updated to "confirm"

---

## ⚠️ CRITICAL: NO LEGACY CODE RETENTION

**This is a COMPLETE replacement, not a migration. Submit is being ELIMINATED, not deprecated.**

### What Gets DELETED (No Fallbacks, No Legacy):
1. ❌ **ALL `submit()` methods** - removed from Action, CLIAction, and all subclasses
2. ❌ **ALL `_handle_submit_command()` methods** - removed from REPLSession and HeadlessSession
3. ❌ **ALL submit command routing** - removed from command parsers and dispatchers
4. ❌ **ALL submit references in help text** - no mention of submit anywhere
5. ❌ **ALL submit references in status displays** - completely replaced with confirm
6. ❌ **ALL submit references in tests** - every test updated to use confirm
7. ❌ **ALL submit references in configs/JSON** - action_config.json, behavior.json, etc.
8. ❌ **ALL submit references in documentation** - stories, READMEs, plans, examples
9. ❌ **ALL submit references in MCP tools** - tool descriptions, examples
10. ❌ **ALL submit references in CLI help** - command descriptions, usage examples
11. ❌ **ALL submit references in extension** - VS Code extension examples
12. ❌ **ALL submit references in scripts** - launcher scripts, examples
13. ❌ **ALL submit-related JSON parameter files** - no legacy data files
14. ❌ **ALL submit-related helper methods** - any utility functions only used by submit
15. ❌ **ALL submit-related imports** - if imported only for submit, remove the import

### What This Means:
- **NO backward compatibility** - submit command will not work, period
- **NO deprecation warnings** - submit is gone, not deprecated  
- **NO fallback logic** - no "if submit then use confirm" code
- **NO commented-out code** - DELETE, don't comment
- **NO legacy JSON files** - no old submit parameter files lying around
- **NO "just in case" code** - if it's for submit, it's deleted
- **COMPLETE removal** - if it mentions submit, it gets updated or deleted

### Deletion Policy for Each Iteration:
Every step in every iteration must explicitly state:
- **REMOVE:** What code/files/references get deleted
- **UPDATE:** What existing code gets modified
- **ADD:** What new code gets added

### Verification Commands:
After implementation, these commands should return ZERO results:
```bash
# Search for submit in Python code (excluding this plan document)
grep -r "def submit\(" agile_bot/bots/ --include="*.py"
grep -r "\.submit\(" agile_bot/bots/ --include="*.py"
grep -r "_handle_submit" agile_bot/bots/ --include="*.py"
grep -r "'submit'" agile_bot/bots/ --include="*.py"
grep -r '"submit"' agile_bot/bots/ --include="*.py"

# Search for submit in configs
grep -r "submit" agile_bot/bots/ --include="*.json"

# Search for submit in documentation
grep -r "submit" agile_bot/bots/base_bot/docs/ --include="*.md"

# Search for submit in tests
grep -r "submit" agile_bot/bots/base_bot/test/ --include="*.py"

# Search for submit in extension
grep -r "submit" agile_bot/bots/base_bot/extension/

# Search for submit in scripts
grep -r "submit" agile_bot/bots/base_bot/*.ps1 agile_bot/bots/base_bot/*.sh
```

**Expected Result:** All commands return 0 matches (except for this plan document itself)

### Why This Matters:
- **Clean codebase** - no confusion about which operation to use
- **No maintenance burden** - don't maintain dead code
- **Clear intent** - 2-phase model is the only model
- **Easier debugging** - no legacy paths to trace
- **Simpler onboarding** - new developers see only one way

---

## PART 1: CORE ACTION LAYER (BaseBot)

### 1.1 Base Action Class

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py`

**Current State:**
- Line 406-418: `submit(context)` method - calls `_do_submit(context)`
- Line 420-426: `_do_submit(context)` template method
- Line 428-444: `confirm(context)` method - only tracks completion, doesn't call submit

**Changes Required:**

1. **REMOVE** `submit()` method entirely (lines 406-418)
   - Delete the entire method

2. **UPDATE** `confirm()` method (lines 428-444):
   ```python
   def confirm(self, context: ActionContext = None) -> Dict[str, Any]:
       """Confirm action complete - saves work and advances to next action.
       
       This is the final phase of the two-phase action pattern.
       Calls _do_submit() to save work (for strategy/clarify), then updates workflow state.
       """
       if context is None:
           context = self.context_class()
       
       # Call submit logic to save work (for strategy/clarify actions)
       submit_result = self._do_submit(context)
       
       # Track activity on completion
       self.track_activity_on_completion()
       
       next_action_name = self.next_action
       return {
           'status': 'confirmed',
           'action_completed': self.action_name,
           'next_action': next_action_name,
           'submit_result': submit_result  # Include what was saved
       }
   ```

3. **KEEP** `_do_submit()` template method (lines 420-426) - no changes needed
   - This will be called by `confirm()` now

**Impact:** This is the foundational change that affects all actions

---

### 1.2 Strategy Action

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py`

**Current State:**
- Line 39-69: `_do_submit(context)` - saves decisions and assumptions to strategy.json
- Line 136-144: `save_strategy()` method - persists strategy data

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - `_do_submit()` will be called by new `confirm()` method
- ✅ Context class `StrategyActionContext` already has all needed fields (`decisions_made`, `assumptions`)

**Verification:**
- Ensure `save_strategy()` works correctly when called from `confirm()`
- Test that strategy data is saved when `confirm()` is called with `StrategyActionContext`

---

### 1.3 Clarify Action

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/clarify_action.py`

**Current State:**
- Line 39-86: `_do_submit(context)` - saves answers, evidence, and context to clarification.json
- Line 95-104: `save_clarification()` method (via RequirementsClarifications class)

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - `_do_submit()` will be called by new `confirm()` method
- ✅ Context class `ClarifyActionContext` already has all needed fields (`answers`, `evidence_provided`, `context`)

**Verification:**
- Ensure clarification data is saved when `confirm()` is called with `ClarifyActionContext`

---

### 1.4 Build Action

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_action.py`

**Current State:**
- Line 81-86: `_do_submit(context)` - returns status message only, no saving

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - `_do_submit()` already returns simple message (correct behavior)

**Verification:**
- Ensure build action doesn't save anything when `confirm()` is called (negative test)

---

### 1.5 Validate Action

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py`

**Current State:**
- Line 181-193: `_do_submit(context)` - runs validation scanners and generates reports

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - `_do_submit()` runs validation (correct behavior - reports generated, not parameters saved)

**Verification:**
- Ensure validate action doesn't save parameters when `confirm()` is called (negative test)
- Ensure validation reports are still generated correctly

---

### 1.6 Render Action

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py`

**Current State:**
- Line 73-78: `_do_submit(context)` - returns status message only, no saving

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - `_do_submit()` already returns simple message (correct behavior)

**Verification:**
- Ensure render action doesn't save anything when `confirm()` is called (negative test)

---

### 1.7 Rules Action

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules_action.py`

**Current State:**
- Line 11-21: `do_execute()` method - returns instructions only
- No `_do_submit()` method - rules action doesn't have submit/confirm operations
- Rules action is a help-only action that displays rules information

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - Rules action doesn't have submit/confirm operations
- Rules action only implements `do_execute()` which returns instructions
- When `confirm()` is called on rules action, it will call `_do_submit()` which has default implementation (returns empty dict), then track completion
- This is correct behavior for help-only actions

---

### 1.8 Help Action

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/help_action.py`

**Current State:**
- Help action is a help-only action that displays help information
- Typically implements `do_execute()` which returns help text
- No `_do_submit()` method - help action doesn't have submit/confirm operations

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - Help action doesn't have submit/confirm operations
- Help action only implements `do_execute()` which returns help information
- When `confirm()` is called on help action, it will call `_do_submit()` which has default implementation (returns empty dict), then track completion
- The new `confirm(context=None)` signature is backward compatible - if called without context, it works correctly
- This is correct behavior for help-only actions

---

## PART 2: REPL CLI LAYER (BaseBot)

### 2.1 CLI Action Wrapper

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/cli_bot/cli_actions/cli_action.py`

**Current State:**
- Line 56-64: `submit(args)` method - calls `action.submit(context)`
- Line 66-74: `confirm()` method - calls `action.confirm()` with empty context

**Changes Required:**

1. **REMOVE** `submit()` method entirely (lines 56-64):
   ```python
   # DELETE THIS ENTIRE METHOD
   def submit(self, args: str) -> str:
       ...
   ```

2. **UPDATE** `confirm()` method (lines 66-74):
   ```python
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

**Impact:** REPL CLI will now pass parameters to confirm

---

### 2.2 REPL Session - Command Handlers

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py`

**Current State:**
- Line 333: Command routing for 'submit' → `_handle_submit_command(command_args)`
- Line 335: Command routing for 'confirm' → `_handle_confirm_command()` (no args)
- Line 560-578: `_handle_submit_command(args)` method
- Line 580-626: `_handle_confirm_command()` method (no args)
- Line 434: Calls `_handle_submit_command("")`
- Line 1024: Calls `_handle_submit_command(args)`
- Line 1026: Calls `_handle_confirm_command()`
- Line 1059: Calls `_handle_submit_command(args)`
- Line 1061: Calls `_handle_confirm_command()`
- Line 1109: Calls `_handle_submit_command(args)`
- Line 1111: Calls `_handle_confirm_command()`
- Line 1184: Calls `_handle_submit_command("")`
- Line 1186: Calls `_handle_confirm_command()`

**Changes Required:**

1. **REMOVE** `_handle_submit_command()` method entirely (lines 560-578)

2. **UPDATE** `_handle_confirm_command()` to accept args (lines 580-626):
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
           
           # If not at last action, advance to next action and auto-execute instructions
           if not is_last_action:
               return self._handle_instructions_command()
           
           # At last action - behavior is complete
           self._mark_behavior_complete(current_behavior_name)
           
           # Check for next behavior
           next_behavior = self.cli_bot.behaviors.next
           if next_behavior:
               # Advance to next behavior
               self.cli_bot.behaviors.domain_behaviors.close_current()
               # Navigate to next behavior's first action and auto-execute instructions
               if next_behavior.actions.all:
                   self.navigate_to_behavior_action(next_behavior.name, next_behavior.actions.all[0])
                   return self._handle_instructions_command()
           
           # No more behaviors - all complete
           return REPLCommandResponse(
               output=f"COMPLETE: {current_behavior_name} behavior finished\n\nALL BEHAVIORS COMPLETE!",
               response="COMPLETE: All behaviors finished",
               status="success"
           )
       except Exception as e:
           return REPLCommandResponse(
               output=f"ERROR confirming: {str(e)}",
               response=f"ERROR confirming: {str(e)}",
               status="error"
           )
   ```

3. **UPDATE** command routing (line 332-335):
   ```python
   if command_verb == 'instructions':
       return self._handle_instructions_command(command_args)
   # REMOVE: if command_verb == 'submit': ...
   if command_verb == 'confirm':
       return self._handle_confirm_command(command_args)  # ADD command_args
   ```

4. **UPDATE** all calls to `_handle_submit_command()` → replace with `_handle_confirm_command()`:
   - Line 434: `return self._handle_submit_command("")` → `return self._handle_confirm_command("")`
   - Line 1024: `return self._handle_submit_command(args)` → `return self._handle_confirm_command(args)`
   - Line 1059: `return self._handle_submit_command(args)` → `return self._handle_confirm_command(args)`
   - Line 1109: `return self._handle_submit_command(args)` → `return self._handle_confirm_command(args)`
   - Line 1184: `return self._handle_submit_command("")` → `return self._handle_confirm_command("")`

5. **UPDATE** all calls to `_handle_confirm_command()` to pass args:
   - Line 1026: `return self._handle_confirm_command()` → `return self._handle_confirm_command(args)`
   - Line 1061: `return self._handle_confirm_command()` → `return self._handle_confirm_command(args)`
   - Line 1111: `return self._handle_confirm_command()` → `return self._handle_confirm_command(args)`
   - Line 1186: `return self._handle_confirm_command()` → `return self._handle_confirm_command(args)`

6. **SEARCH** for any other references to `_handle_submit_command` or `submit` command in this file and update

**Impact:** REPL session will handle confirm with parameters

---

### 2.3 REPL Session - Instructions Command (Add --autoconfirm)

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py`

**Current State:**
- Line 507-558: `_handle_instructions_command(args)` - displays instructions and returns

**Changes Required:**

1. **ADD** autoconfirm parsing and logic to `_handle_instructions_command()`:
   ```python
   def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
       if not self.has_current_action:
           return REPLCommandResponse(
               output="ERROR: No current action to get instructions for",
               response="ERROR: No current action",
               status="error"
           )
       
       action = self.current_action
       
       # Parse --autoconfirm flag
       autoconfirm = self._parse_autoconfirm_flag(args)
       # Remove --autoconfirm from args before passing to action
       cleaned_args = self._remove_autoconfirm_flag(args)
       
       # Parse CLI-style arguments if present (use cleaned_args)
       context = None
       if cleaned_args and cleaned_args.strip().startswith('--'):
           cli_args = self._tokenize_cli_args(cleaned_args)
           try:
               from agile_bot.bots.base_bot.src.cli.cli_context_builder import CliContextBuilder
               builder = CliContextBuilder()
               underlying_action = action._action if hasattr(action, '_action') else action
               context = builder.build_context(underlying_action, cli_args)
               
               if context and hasattr(context, 'scope') and context.scope:
                   context.scope.apply_to_bot(self.workspace_directory)
           except ValueError as e:
               error_msg = str(e)
               if "Invalid scope type" in error_msg or "invalid_type" in error_msg:
                   return REPLCommandResponse(
                       output=f"ERROR: {error_msg}",
                       response=f"ERROR: {error_msg}",
                       status="error"
                   )
               context = None
           except Exception:
               context = None
       
       try:
           # Call with context if we have one, otherwise pass cleaned_args as string
           if context:
               output = action.instructions(args="", context=context)
           else:
               output = action.instructions(cleaned_args)
           
           # If autoconfirm=true, automatically call confirm
           if autoconfirm:
               # Wrap instructions with context header showing autoconfirm status
               instructions_response = self._wrap_with_context_header(
                   output, 
                   "Instructions displayed (auto-confirming)"
               )
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
           return self._wrap_with_context_header(output, "Instructions displayed")
       except Exception as e:
           return REPLCommandResponse(
               output=f"ERROR getting instructions: {str(e)}",
               response=f"ERROR getting instructions: {str(e)}",
               status="error"
           )
   ```

2. **ADD** helper methods for autoconfirm parsing:
   ```python
   def _parse_autoconfirm_flag(self, args: str) -> bool:
       """Parse --autoconfirm flag from args string."""
       import re
       if not args:
           return False
       # Look for --autoconfirm=true or --autoconfirm true or just --autoconfirm
       if '--autoconfirm' in args.lower():
           # Check if explicitly set to false
           if re.search(r'--autoconfirm[=\s]+false', args, re.IGNORECASE):
               return False
           # Check if explicitly set to true
           if re.search(r'--autoconfirm[=\s]+true', args, re.IGNORECASE):
               return True
           # Just --autoconfirm (no value) defaults to true
           return True
       return False
   
   def _remove_autoconfirm_flag(self, args: str) -> str:
       """Remove --autoconfirm flag from args string."""
       import re
       if not args:
           return ""
       # Remove --autoconfirm=value or --autoconfirm value or --autoconfirm
       cleaned = re.sub(r'--autoconfirm(?:[=\s]+\w+)?', '', args, flags=re.IGNORECASE)
       return cleaned.strip()
   ```

**Impact:** Instructions command will support --autoconfirm flag

---

### 2.4 REPL Status Display

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_status.py`

**Current State:**
- Line 200-215: `_get_submit_params(action)` method - gets parameter hints for submit
- Line 116-123: Operation display shows "submit" operation in hierarchical status
- Line 293-295: `_operation_status_items` property shows submit in operation list

**Changes Required:**

1. **RENAME** `_get_submit_params()` → `_get_confirm_params()` (line 200):
   ```python
   def _get_confirm_params(self, action) -> str:
       """Get parameter hints for confirm operation."""
       params = []
       if hasattr(action, 'context_class') and action.context_class:
           try:
               import dataclasses
               if dataclasses.is_dataclass(action.context_class):
                   fields = [f.name for f in dataclasses.fields(action.context_class)]
                   if 'decisions' in fields:
                       params.append('--decisions="1:option,..."')
                   if 'assumptions_made' in fields or 'assumptions' in fields:
                       params.append('--assumptions="..."')
           except:
               pass
       if params:
           return ' ' + ' '.join(params)
       return ''
   ```

2. **REMOVE** submit operation from hierarchical status display (lines 116-123):
   ```python
   # REMOVE these lines:
   # Submit
   # if stage == 'submitting':
   #     submit_marker = self.formatter.status_marker(is_current=True, is_completed=False)
   # elif stage in ('instructions', 'not_started'):
   #     submit_marker = self.formatter.status_marker(is_current=False, is_completed=False)
   # else:
   #     submit_marker = self.formatter.status_marker(is_current=False, is_completed=True)
   # lines.append(f"    {submit_marker} submit")
   
   # UPDATE confirm logic to check for 'instructions_given' instead of 'submitted':
   # Confirm
   if stage == 'confirming':
       confirm_marker = self.formatter.status_marker(is_current=True, is_completed=False)
   elif stage in ('instructions', 'not_started', 'instructions_given'):
       confirm_marker = self.formatter.status_marker(is_current=False, is_completed=False)
   else:
       confirm_marker = self.formatter.status_marker(is_current=False, is_completed=True)
   lines.append(f"    {confirm_marker} confirm")
   ```

3. **UPDATE** `_operation_status_items` property (lines 286-296):
   ```python
   @property
   def _operation_status_items(self) -> List[str]:
       stage = self.state.stage_name
       current_marker = self.formatter.status_marker(is_current=True, is_completed=False)
       pending_marker = self.formatter.status_marker(is_current=False, is_completed=False)
       completed_marker = self.formatter.status_marker(is_current=False, is_completed=True)
       
       if stage == 'instructions':
           return [f"instructions {current_marker}", f"confirm {pending_marker}"]
       elif stage == 'confirming':
           return [f"instructions {completed_marker}", f"confirm {current_marker}"]
       elif stage in ('instructions_given', 'confirmed'):
           return [f"instructions {completed_marker}", f"confirm {completed_marker}"]
       return []
   ```

4. **SEARCH** for all callers of `_get_submit_params()` and update to `_get_confirm_params()`
   - Check if REPLSession has wrapper methods like `_get_submit_params_hint()` that call this

**Impact:** Status display will show confirm parameters instead of submit, and remove submit from operation list

---

### 2.5 REPL Help System

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_help.py`

**Current State:**
- Line 90: Shows "instructions|submit|confirm" in usage
- Line 92: "Action Stages (three steps)"
- Line 101: "instructions → submit → confirm" cycling note
- Line 112-135: `_stages` property with 3 stages (instructions, submit, confirm)
- Line 122-126: Submit stage description
- Line 299, 325: References to `self.session._get_submit_params_hint(action)`
- Line 330-341: Operation display showing "submit"

**Changes Required:**

1. **UPDATE** usage line (line 90):
   ```python
   f"  {self.action_name} [instructions|confirm]",  # REMOVE submit
   ```

2. **UPDATE** stages description (line 92):
   ```python
   "Action Stages (two steps):",  # Change from "three steps"
   ```

3. **UPDATE** cycling note (line 101):
   ```python
   "Note: Calling action name without stage cycles through: instructions → confirm",
   ```

4. **UPDATE** `_stages` property (lines 112-135):
   ```python
   @property
   def _stages(self) -> List[List[str]]:
       return [
           [
               "  1. instructions",
               "     Request: Get instructions for the action",
               "     Response: Shows instructions, questions to answer, evidence to provide",
               f"     Example: {self.action_name} instructions  (or just: {self.action_name})",
               f"     With autoconfirm: {self.action_name} instructions --autoconfirm",
               "",
           ],
           [
               "  2. confirm",
               "     Request: Confirm action complete (saves work if needed)",
               "     Response: Auto-executes next action and shows its instructions",
               f"     Example: {self.action_name} confirm  (or call {self.action_name} again to cycle)",
               f"     With params: {self.action_name} confirm --decisions='...' --assumptions='...'",
               "",
           ],
       ]
   ```

5. **UPDATE** action help display (lines 298-312):
   ```python
   # Change from:
   submit_hint = self.session._get_submit_params_hint(action)
   # To:
   confirm_hint = self.session._get_confirm_params_hint(action)  # Note: may need to add this wrapper method
   
   # Update hints combination:
   hints = []
   if instructions_hint:
       hints.append(instructions_hint)
   if confirm_hint:  # Changed from submit_hint
       hints.append(confirm_hint)
   ```

6. **UPDATE** operation display (lines 321-341):
   ```python
   # Change from:
   submit_hint = self.session._get_submit_params_hint(action_obj)
   
   if instructions_hint:
       lines.append(f"      instructions  {instructions_hint}")
   else:
       lines.append(f"      instructions")
   
   if submit_hint:
       lines.append(f"      submit        {submit_hint}")
   else:
       lines.append(f"      submit")
   
   lines.append(f"      confirm")
   # To:
   confirm_hint = self.session._get_confirm_params_hint(action_obj)  # Note: may need to add this wrapper method
   
   if instructions_hint:
       lines.append(f"      instructions  {instructions_hint}")
   else:
       lines.append(f"      instructions")
   
   if confirm_hint:
       lines.append(f"      confirm       {confirm_hint}")
   else:
       lines.append(f"      confirm")
   ```

7. **UPDATE** generic operation list (lines 339-341):
   ```python
   # Change from:
   lines.append(f"      instructions  [context, scope, or action-specific params]")
   lines.append(f"      submit        [scope, decisions, assumptions, or action-specific params]")
   lines.append(f"      confirm")
   # To:
   lines.append(f"      instructions  [context, scope, --autoconfirm, or action-specific params]")
   lines.append(f"      confirm       [scope, decisions, assumptions, or action-specific params]")
   ```

8. **SEARCH** for all other references to "submit" in help text and update to "confirm"

**Note:** If `_get_submit_params_hint()` is a wrapper method in REPLSession, it needs to be renamed to `_get_confirm_params_hint()` and updated to call `_get_confirm_params()` from REPLStatus.

**Impact:** Help system will reflect new 2-phase workflow

---

### 2.6 Action Cycling Logic

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py`

**Current State:**
- Line 1150: `phase_map = {'not_started': 'instructions', 'instructions_given': 'submit', 'submitted': 'confirm'}`
- Line 1151: Uses phase_map to determine next operation when action name called without operation
- Line 425-443: `_handle_current_command()` - checks operation from progress and cycles
  - Line 431: checks for 'instructions'
  - Line 433: checks for 'submit' - needs to be removed
  - Line 435: checks for 'confirm'
- Line 1020-1026: `_handle_dot_notation()` - handles `.operation` syntax
  - Line 1023: checks for 'submit' - needs to be removed
  - Line 1025: checks for 'confirm'
- Line 1040: Validates operations list includes 'submit' - needs to be removed
- Line 1058-1061: Calls submit/confirm handlers - needs to be updated
- Line 1108-1111: Calls submit/confirm handlers - needs to be updated
- Line 1157: Checks for "submit" or "confirm" - needs to be updated
- Line 1183-1186: Calls submit/confirm handlers - needs to be updated
- Line 1189: Error message mentions 'submit' - needs to be updated

**Changes Required:**

1. **UPDATE** phase_map (line 1150):
   ```python
   phase_map = {'not_started': 'instructions', 'instructions_given': 'confirm', 'confirmed': 'instructions'}
   ```
   Note: After confirm, cycle back to instructions for next action

2. **UPDATE** `_handle_current_command()` (line 433):
   ```python
   # REMOVE this line:
   elif operation == 'submit':
       return self._handle_submit_command("")
   # Keep only instructions and confirm checks
   ```

3. **UPDATE** `_handle_dot_notation()` - remove submit checks:
   - Line 1023: Remove `elif operation == 'submit': return self._handle_submit_command(args)`
   - Line 1040: Change `if operation not in ('instructions', 'submit', 'confirm'):` to `if operation not in ('instructions', 'confirm'):`
   - Line 1058: Remove `elif operation == 'submit': return self._handle_submit_command(args)`
   - Line 1108: Remove `elif operation == 'submit': return self._handle_submit_command(args)`
   - Line 1029: Update error message: `"ERROR: Unknown operation '{operation}'\nUse: instructions or confirm"`

4. **UPDATE** `_handle_action_shortcut()` (line 1157):
   ```python
   # Change from:
   if subcommand in ("submit", "confirm"):
   # To:
   if subcommand == "confirm":
   ```

5. **UPDATE** `_handle_action_shortcut()` (line 1183-1186):
   ```python
   # Remove submit handling:
   # if subcommand == "submit":
   #     return self._handle_submit_command("")
   # Keep only confirm:
   if subcommand == "confirm":
       return self._handle_confirm_command("")
   ```

6. **UPDATE** error message (line 1189):
   ```python
   # Change from:
   output=f"ERROR: Unknown subcommand '{subcommand}'. Use 'instructions', 'submit', or 'confirm'."
   # To:
   output=f"ERROR: Unknown subcommand '{subcommand}'. Use 'instructions' or 'confirm'."
   ```

**Impact:** Action cycling will skip submit phase and go directly: instructions → confirm

---

### 2.7 Command Parser

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/command_parser.py`

**Current State:**
- Line 34: `OPERATIONS = ['instructions', 'submit', 'confirm']`

**Changes Required:**

1. **UPDATE** operations list (line 34):
   ```python
   OPERATIONS = ['instructions', 'confirm']  # REMOVE submit
   ```

**Impact:** Command parser will recognize confirm but not submit

---

### 2.8 REPL Main (Examples)

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_main.py`

**Current State:**
- Line 10: Example comment shows `shape.build.submit`

**Changes Required:**

1. **UPDATE** example comment (line 10):
   ```python
   python repl_main.py headless shape.build.confirm        # Headless mode: run single operation
   ```

**Impact:** Examples will show correct operation name

---

## PART 3: CLI LAYER (BaseBotCli)

### 3.1 CLI Executor

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py`

**Current State:**
- Line 102-112: `_execute_command()` method - routes to action execution via `self.cli.run()`
- Line 110: Calls `self.cli.run(behavior_name=args.behavior, action_name=action_name, cli_args=cli_args)`
- This eventually routes through `CliCommandRouter` which calls `action.execute(context)`

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - CLI executor routes to `action.execute()` which handles full workflow
- The `execute()` method internally handles instructions → confirm workflow, so when `confirm()` is updated to call `_do_submit()`, it will work correctly
- CLI executor doesn't need to know about individual operations (instructions/submit/confirm)

**Impact:** CLI executor will work correctly without changes

---

### 3.2 CLI Command Router

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_command_router.py`

**Current State:**
- Line 31-38: `_route_to_specific_action()` - calls `action.execute(context)` (line 36)
- Line 57-65: `_execute_current_action()` - calls `action.execute()` without context (line 63)
- Both methods use `action.execute()` which handles the full workflow internally

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - CLI command router uses `action.execute()` which handles full workflow
- The `execute()` method internally manages instructions → confirm workflow
- When `confirm()` is updated to call `_do_submit()` internally, `execute()` will work correctly
- CLI doesn't need separate operation support (instructions/submit/confirm) - execute() is sufficient

**Impact:** CLI routing will work correctly without changes

---

### 3.3 CLI Parameter Parser

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py`

**Current State:**
- Line 36-52: `_create_argument_parser()` - creates argparse parser
- Line 18-33: `_build_remaining_args()` - builds remaining args list
- Line 62-81: `_build_params_from_args()` - builds params dict

**Changes Required:**

1. **ADD** `--autoconfirm` argument to parser (line 36-52):
   ```python
   parser.add_argument('--autoconfirm', action='store_true', 
                       help='Auto-confirm after instructions (default: False)')
   ```

2. **ADD** autoconfirm to remaining args (line 18-33):
   ```python
   if getattr(args, 'autoconfirm', False):
       remaining.append('--autoconfirm')
   ```

3. **ADD** autoconfirm to params (line 62-81):
   ```python
   if getattr(args, 'autoconfirm', False):
       params['autoconfirm'] = True
   ```

**Impact:** CLI will parse autoconfirm parameter

---

### 3.4 CLI Context Builder

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_context_builder.py`

**Current State:**
- Line 24-40: `build_context()` - builds context from CLI args using action's `context_class`
- Line 42-53: `build_parser_from_context_class()` - creates argparse parser from dataclass fields
- Line 86-103: `_build_context_from_parsed()` - converts parsed args to typed context object
- Works for any operation that needs context (instructions, confirm, etc.)

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - Context builder works generically for any operation
- `build_context()` takes action and CLI args, builds appropriate context type (StrategyActionContext, ClarifyActionContext, etc.)
- When `confirm()` is called with context, the context builder will work correctly
- Autoconfirm parameter is handled at REPL session level, not in context - so no interference

**Impact:** Context building will work correctly for confirm operation without changes

---

## PART 4: MCP SERVER IMPLEMENTATIONS

### 4.1 StoryBot MCP Server

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot/src/story_bot_mcp_server.py`

**Current State:**
- Line 69: `bot_tool` calls `action.execute(parameters or {})`
- Line 152, 165, 178, 191, 204, 217, 230: All behavior tools call `action.execute(parameters or {})`
- All MCP tools use `execute()` which handles full workflow internally

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - MCP tools use `action.execute()` which handles full workflow
- The `execute()` method internally manages instructions → confirm workflow
- Parameters are passed as dict to `execute()`, which builds context and calls operations internally
- When `confirm()` is updated to call `_do_submit()` internally, `execute()` will work correctly
- MCP tools don't need separate operation support - execute() is sufficient

**Impact:** MCP tools will work correctly without changes

---

### 4.2 CRCBot MCP Server

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/crc_bot/src/crc_bot_mcp_server.py`

**Current State:**
- Line 69: `bot_tool` calls `action.execute(parameters or {})`
- Line 152, 165, 178: All behavior tools call `action.execute(parameters or {})`
- All MCP tools use `execute()` which handles full workflow internally

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - MCP tools use `action.execute()` which handles full workflow
- The `execute()` method internally manages instructions → confirm workflow
- Parameters are passed as dict to `execute()`, which builds context and calls operations internally
- When `confirm()` is updated to call `_do_submit()` internally, `execute()` will work correctly
- MCP tools don't need separate operation support - execute() is sufficient

**Impact:** MCP tools will work correctly without changes

---

### 4.3 BaseBot MCP Server (if exists)

**Files:**
- `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_code_visitor.py`
- `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/mcp_code_visitor.py`

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - These files generate MCP server code that calls `action.execute(parameters)`
- Generated MCP tools use `execute()` which handles full workflow internally
- When `confirm()` is updated to call `_do_submit()` internally, generated code will work correctly
- Code generation doesn't need to know about individual operations - execute() is sufficient

**Impact:** BaseBot MCP code generation will work correctly without changes

---

## PART 5: ACTION CONTEXT CLASSES

### 5.1 Action Context Base

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py`

**Current State:**
- Line 456-460: `ClarifyActionContext` - has `answers`, `evidence_provided`, `context` fields
- Line 463-498: `StrategyActionContext` - has `decisions_made`, `assumptions`, `assumptions_made` fields
- Base `ActionContext` class (line ~1-50) - base class for all action contexts

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - Context classes already have all needed fields for action data
- ✅ **DECISION MADE**: Autoconfirm should NOT be part of ActionContext
  - Autoconfirm is a REPL session-level flag that controls workflow behavior
  - It's not action data that needs to be saved or passed to actions
  - Handle autoconfirm separately in REPL session (see section 2.3)

**Impact:** Context classes will work correctly without changes - autoconfirm handled at session level

---

## PART 6: INSTRUCTIONS CLASS

### 6.1 Instructions

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py`

**Current State:**
- Line 9-16: `Instructions` class - stores base_instructions and display_content
- Line 23-26: `add_display()` method - adds lines to display_content
- Line 28-30: `display_content` property - returns display content list
- Instructions class is for action instructions content, not workflow control

**Changes Required:**
- ✅ **NO CHANGES NEEDED** - Instructions class doesn't need to store autoconfirm flag
- Autoconfirm is handled at REPL session level (see section 2.3)
- Display of autoconfirm status is handled in REPL session's `_wrap_with_context_header()` or `_handle_instructions_command()` (see section 2.3)
- Instructions class remains focused on action instruction content only

**Impact:** Instructions class will work correctly without changes - autoconfirm handled at session level

---

## PART 7: HEADLESS MODE

### 7.1 Headless Session

**File:** `/mnt/c/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py`

**Current State:**
- Line 108: `operations = ['instructions', 'submit', 'confirm']` in `invokes_action()` method
- Line 115-131: Loop executes each operation in sequence
- Line 116: Creates message like `'Execute operation: {behavior}.{action}.{operation}'`
- Line 117: Calls `self.invokes(message, context_file)` which routes to REPL session

**Changes Required:**

1. **UPDATE** operations list (line 108):
   ```python
   operations = ['instructions', 'confirm']  # REMOVE submit
   ```

2. **VERIFY** confirm operation parameter handling:
   - ✅ **NO CHANGES NEEDED** - Headless mode calls `self.invokes()` which routes to REPL session
   - REPL session's `_handle_confirm_command()` will be updated to accept args (see section 2.2)
   - Parameters are passed through the message/context_file mechanism
   - When confirm is called, it will receive parameters correctly

3. **VERIFY** autoconfirm flag handling:
   - ✅ **NO CHANGES NEEDED** - Autoconfirm is handled in REPL session's `_handle_instructions_command()` (see section 2.3)
   - Headless mode calls `invokes()` which routes to REPL session, so autoconfirm will work correctly
   - If autoconfirm is set in instructions, REPL session will handle it automatically

**Impact:** Headless mode will work correctly with merged submit/confirm - only operations list needs update

---

## PART 8: TEST FILES

### 8.1 Base Bot Tests

**Files to Update:**

1. **`test_execute_action_operation_through_cli.py`**
   - **CHANGE**: Class `TestSubmitWorkThroughCLIWithStringParameters` → rename to `TestConfirmWorkThroughCLIWithStringParameters`
   - **CHANGE**: All test methods that call `submit` → change to `confirm`
   - **CHANGE**: Line 263: `repl_session.read_and_execute_command('submit')` → `'confirm'`
   - **CHANGE**: Line 265: Comment "CLIAction calls action.submit(context)" → "action.confirm(context)"
   - **CHANGE**: Line 267: Assertion checking for 'submit' → 'confirm'
   - **CHANGE**: Line 284: Comment "user enters 'submit'" → "user enters 'confirm'"
   - **UPDATE**: Test assertions for new behavior
   - **ADD**: New tests for `--autoconfirm` flag on instructions

2. **`test_execute_action_operation_through_cli_current.py`**
   - **CHANGE**: Similar changes as above

3. **`test_decide_strategy_criteria_action.py`**
   - **CHANGE**: Tests that call `action.submit()` → change to `action.confirm()`
   - **CHANGE**: Line 36: `when_action_executes_with_parameters()` - verify it works with confirm
   - **UPDATE**: Test assertions to verify strategy saves data on confirm
   - **ADD**: Test confirm with strategy context parameters

4. **`test_execute_behavior_actions.py`**
   - **UPDATE**: Workflow tests to use confirm instead of submit
   - **VERIFY**: Workflow advancement still works correctly

5. **`test_invoke_cli.py`**
   - **UPDATE**: CLI invocation tests
   - **VERIFY**: CLI commands work with confirm

6. **`test_invoke_mcp.py`**
   - **UPDATE**: MCP tool tests if they reference submit
   - **VERIFY**: MCP tools work correctly

7. **`test_gather_context.py`**
   - **CHANGE**: Tests that call `action.submit()` → change to `action.confirm()`
   - **UPDATE**: Test assertions to verify clarify saves data on confirm
   - **ADD**: Test confirm with clarify context parameters

8. **`test_build_knowledge.py`**
   - **VERIFY**: Ensure build action doesn't save on confirm (test negative case)
   - **UPDATE**: Tests to use confirm instead of submit

9. **`test_validate_knowledge_and_content_against_rules.py`**
   - **VERIFY**: Ensure validate action doesn't save parameters on confirm (test negative case)
   - **UPDATE**: Tests to use confirm instead of submit

10. **`test_render_output.py`**
    - **VERIFY**: Ensure render action doesn't save on confirm (test negative case)
    - **UPDATE**: Tests to use confirm instead of submit

11. **`test_initialize_repl_session.py`**
    - **UPDATE**: Tests for confirm with parameters

12. **`test_initialize_repl_session_current.py`**
    - **UPDATE**: Tests for confirm with parameters

13. **`test_current_initialize_repl_session.py`**
    - **UPDATE**: Tests for confirm with parameters

14. **`test_execute_in_headless_mode.py`**
    - **UPDATE**: Tests for confirm operation with parameters
    - **ADD**: Tests for autoconfirm in headless mode

**Changes Needed:**
1. Rename test classes/methods that reference "submit"
2. Change all `session.submit()` calls to `session.confirm()`
3. Change all `action.submit()` calls to `action.confirm()`
4. Update assertions to expect combined submit+confirm behavior
5. Add new tests for `--autoconfirm` flag on instructions
6. Update workflow tests to reflect 2-phase model

**Impact:** All tests need to be updated to reflect new confirm signature and behavior

---

### 8.2 Story Bot Tests

**Files to Review:**
- `/mnt/c/dev/augmented-teams/agile_bot/bots/story_bot/test/synchronizers/` - any tests that use submit

**Changes Needed:**
- **SEARCH** for any tests that call submit operations
- **UPDATE** to use confirm instead

---

### 8.3 CRC Bot Tests

**Files to Review:**
- Any CRC bot tests that use submit operations

**Changes Needed:**
- **SEARCH** for any tests that call submit operations
- **UPDATE** to use confirm instead

---

## PART 9: CONFIGURATION FILES

### 9.1 Base Bot Action Configs

**Files to Review:**

1. **`base_actions/strategy/action_config.json`**
   - **SEARCH** for any references to "submit" in instructions or descriptions
   - **UPDATE** to reference "confirm" instead
   - **VERIFY**: No changes needed (submit already saves)

2. **`base_actions/clarify/action_config.json`**
   - **SEARCH** for any references to "submit" in instructions or descriptions
   - **UPDATE** to reference "confirm" instead
   - **VERIFY**: No changes needed (submit already saves)

3. **`base_actions/build/action_config.json`**
   - **SEARCH** for any references to "submit" in instructions or descriptions
   - **UPDATE** to reference "confirm" instead
   - **VERIFY**: No changes needed (submit doesn't save)

4. **`base_actions/validate/action_config.json`**
   - **SEARCH** for any references to "submit" in instructions or descriptions
   - **UPDATE** to reference "confirm" instead
   - **VERIFY**: No changes needed (submit doesn't save parameters)

5. **`base_actions/render/action_config.json`**
   - **SEARCH** for any references to "submit" in instructions or descriptions
   - **UPDATE** to reference "confirm" instead
   - **VERIFY**: No changes needed (submit doesn't save)

6. **`base_actions/validate/instructions.json`**
   - **SEARCH** for any references to "submit"
   - **UPDATE** to "confirm"

7. **`base_actions/build/build-instructions.txt`**
   - **SEARCH** for any references to "submit"
   - **UPDATE** to "confirm"

**Impact:** Config files should be updated to reflect new workflow

---

### 9.2 Story Bot Behavior Configs

**Files to Review:**
- `behaviors/*/guardrails/instructions.json` (if exists)
- `behaviors/*/behavior.json`

**Changes Needed:**
- **SEARCH** for "submit" in all behavior configs
- **UPDATE** to "confirm"
- **VERIFY**: Workflow descriptions reflect 2-phase model

---

### 9.3 CRC Bot Behavior Configs

**Files to Review:**
- `behaviors/*/guardrails/instructions.json`
- `behaviors/*/behavior.json`

**Changes Needed:**
- **SEARCH** for "submit" in all behavior configs
- **UPDATE** to "confirm"
- **VERIFY**: Workflow descriptions reflect 2-phase model

---

## PART 10: DISPLAY AND UI CHANGES

### 10.1 Display Section for Autoconfirm

**Files to Modify:**

1. **`repl_session.py`** - `_handle_instructions_command()` method
   - **Location**: After parsing autoconfirm flag (see section 2.3)
   - **CHANGE**: Update `_wrap_with_context_header()` call to include autoconfirm status
   - **FORMAT**: 
     ```python
     # In _handle_instructions_command(), after parsing autoconfirm:
     if autoconfirm:
         header_text = "Instructions displayed (auto-confirming)"
     else:
         header_text = "Instructions displayed"
     return self._wrap_with_context_header(output, header_text)
     ```
   - **ALTERNATIVE**: Add autoconfirm status to display content directly:
     ```python
     if autoconfirm:
         autoconfirm_line = "\n**Auto-confirm:** Enabled (will automatically confirm after displaying instructions)\n"
         output = output + autoconfirm_line
     ```

2. **`action.py`**
   - ✅ **NO CHANGES NEEDED** - Instructions display doesn't need autoconfirm status
   - Autoconfirm is a REPL session-level flag, not action-level
   - Display is handled in REPL session (see above)

3. **`cli_action.py`**
   - ✅ **NO CHANGES NEEDED** - CLI action wrapper doesn't need autoconfirm display
   - Autoconfirm is handled at REPL session level (see section 2.3)

**Impact:** Users will see autoconfirm status in the instructions display header

---

### 10.2 Commands Menu Display

**Files to Check:**
- Any file that generates command menus or lists
- `repl_status.py`
- Display components in `repl_cli/` directory

**Changes Needed:**
- **UPDATE** command list to show "confirm" instead of "submit"
- **ADD** "--autoconfirm" to instructions command documentation

---

### 10.3 Status Display in Instructions Output

**Files to Change:**
- Find where parameter display is generated (likely in `repl_status.py` or `repl_session.py`)
- **UPDATE** parameter display section to change "submit" references to "confirm"

---

## PART 11: DOCUMENTATION

### 11.1 Story Documents

**Files to Review:**
- `docs/stories/**/*.md`
- `docs/stories/**/*.txt`
- Any story maps or increment documents

**Changes Needed:**
- **SEARCH** for "submit" operation references
- **UPDATE** to "confirm"
- **UPDATE** workflow descriptions to 2-phase model

---

### 11.2 README and Documentation

**Files to Review:**
- `docs/README.md` (if exists)
- `test/README_API_TESTS.md`
- Any other markdown documentation

**Changes Needed:**
- **UPDATE** command examples
- **UPDATE** workflow descriptions
- **ADD** documentation for --autoconfirm flag

---

### 11.3 Increment Plans

**Files to Review:**
- `docs/stories/increments/increment-11-plan.md` (line 488, 494 - has submit/confirm examples)
- Any other increment plan documents

**Changes Needed:**
- **UPDATE** code examples showing submit/confirm
- **UPDATE** workflow descriptions

---

## PART 12: EXTENSION AND EXTERNAL INTEGRATIONS

### 12.1 VS Code Extension

**Files to Review:**
- `extension/chat_participants.js`
- `extension/package.json`

**Changes Needed:**
- **UPDATE** any command examples that show "submit"
- **UPDATE** to show "confirm"

---

### 12.2 Cursor Commands

**Files to Review:**
- `.cursor/commands/*.md`
- `.continue/config.json`

**Changes Needed:**
- **REVIEW**: Line 26 in config.json - `--confirm=true` already exists (good!)
- **UPDATE** any other references to submit

---

## PART 13: LAUNCHER SCRIPTS

### 13.1 REPL Launcher

**Files to Review:**
- `repl.ps1`
- Any bash equivalents

**Changes Needed:**
- **UPDATE** comments/documentation that mention submit
- **UPDATE** examples to use confirm

---

### 13.2 Generator Scripts

**Files to Review:**
- `bots/base_bot/generate_bot.ps1`
- `bots/base_bot/generate_bot.sh`

**Changes Needed:**
- **UPDATE** any template generation that includes submit references

---

## PART 14: SUMMARY OF CHANGES BY PRIORITY

### Critical Changes (Must Do - Breaking Changes)

1. **Action.py**: Remove `submit()` method, update `confirm()` to call `_do_submit()`
2. **CLIAction.py**: Remove `submit()` method, update `confirm()` to accept args
3. **REPLSession.py**: Remove `_handle_submit_command()`, update `_handle_confirm_command()` to accept args
4. **REPLSession.py**: Update all command routing (remove submit, update confirm calls)
5. **HeadlessSession.py**: Update operations list (remove submit)
6. **All tests**: Update to reflect new confirm signature

### Important Changes (Should Do - User-Facing)

7. **REPLSession.py**: Add autoconfirm parameter parsing and display
8. **CLIParameterParser.py**: Add autoconfirm parameter support
9. **REPLHelp.py**: Update all help text (3-phase → 2-phase)
10. **REPLStatus.py**: Rename submit params to confirm params
11. **Display**: Add autoconfirm status display

### Verification Changes (Verify - May Need Updates)

12. **All action subclasses**: Verify `_do_submit()` behavior is correct
13. **CLI routing**: Verify operation routing works correctly
14. **Context building**: Verify context building works for confirm
15. **MCP servers**: Verify operation handling
16. **Configuration files**: Verify and update references

### Cleanup Changes (Low Priority - Documentation)

17. **Documentation files**: Update stories, READMEs, etc.
18. **Extension files**: Update examples
19. **Launcher scripts**: Update comments

---

## PART 15: TESTING CHECKLIST

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
- [ ] Test full strategy workflow: instructions → confirm
- [ ] Test full clarify workflow: instructions → confirm
- [ ] Test full build workflow: instructions → confirm
- [ ] Test autoconfirm in instructions operation
- [ ] Test action cycling: instructions → confirm

---

## PART 16: RISKS AND CONSIDERATIONS

### Risks
1. **Breaking Changes**: Changing confirm signature may break existing code
   - **Mitigation**: Update all call sites systematically

2. **Parameter Parsing**: Ensuring parameters are parsed correctly for confirm
   - **Mitigation**: Reuse submit parameter parsing logic

3. **Workflow State**: Ensuring workflow advancement still works correctly
   - **Mitigation**: Keep existing workflow logic, just add submit call before

4. **MCP Tools**: MCP tools may need updates to handle operations
   - **Mitigation**: Verify each MCP tool handles operations correctly

5. **Test Coverage**: Many test files need updates
   - **Mitigation**: Systematic update of all test files

### Considerations
1. **Backward Compatibility**: No backward compatibility possible - this is a clean break
   - **Decision**: New signature should accept None for context (backward compatible for empty calls)

2. **Autoconfirm Default**: Default is false, which is correct
   - **Decision**: Keep default as false

3. **Display Location**: Where to show autoconfirm status
   - **Decision**: Show in instructions display section

4. **MCP Tools**: Should they support operations or continue using execute()?
   - **Decision**: Continue using execute() unless operation support is needed

---

## PART 17: TEST-DRIVEN IMPLEMENTATION ORDER

**Philosophy:** Fix tests incrementally, make them pass, validate, then move to next epic/story.

Each iteration follows this pattern:
1. **Update test(s)** for the epic/story
2. **Run tests** - expect failures
3. **Implement minimum code** to make tests pass
4. **Validate** using `code.validate.instructions` or `tests.validate.instructions`
5. **Verify** tests pass
6. **Move to next** epic/story

---

### ITERATION 1: Core Action Layer - Strategy Action

**Epic:** Merge Submit with Confirm
**Story:** Strategy action saves data on confirm

**Step 1.1: Update Test**
- File: `test/test_decide_strategy_criteria_action.py`
- **REMOVE:** All calls to `action.submit(context)` - delete these lines entirely
- **ADD:** Replace with `action.confirm(context)` calls
- **REMOVE:** Any test methods specifically testing submit behavior - delete entire methods
- **ADD:** Test that strategy data is saved when confirm is called with StrategyActionContext
- Expected: Tests FAIL (confirm doesn't call _do_submit yet)

**Step 1.2: Implement Core Change**
- File: `actions/action.py`
- **REMOVE:** Entire `submit()` method (lines 406-418) - DELETE completely, no comments
- **UPDATE:** `confirm()` method (lines 428-444) to call `_do_submit(context)` before tracking completion
- Code:
  ```python
  # DELETE THESE LINES (406-418):
  # def submit(self, context: ActionContext = None) -> Dict[str, Any]:
  #     """Submit work for current action."""
  #     if context is None:
  #         context = self.context_class()
  #     return self._do_submit(context)
  
  # REPLACE confirm() method with:
  def confirm(self, context: ActionContext = None) -> Dict[str, Any]:
      """Confirm action complete - saves work and advances to next action.
      
      This is the final phase of the two-phase action pattern.
      Calls _do_submit() to save work (for strategy/clarify), then updates workflow state.
      """
      if context is None:
          context = self.context_class()
      
      # Call submit logic to save work (for strategy/clarify actions)
      submit_result = self._do_submit(context)
      
      # Track activity on completion
      self.track_activity_on_completion()
      
      next_action_name = self.next_action
      return {
          'status': 'confirmed',
          'action_completed': self.action_name,
          'next_action': next_action_name,
          'submit_result': submit_result
      }
  ```

**Step 1.3: Validate**
- Run: `code.validate.instructions`
- Verify: No rule violations in action.py
- Verify: No references to submit() remain in action.py

**Step 1.4: Run Tests**
- Run: `pytest test/test_decide_strategy_criteria_action.py`
- Expected: Tests PASS (strategy data saved on confirm)

**Step 1.5: Verify Removal**
- Run: `grep "def submit\(" agile_bot/bots/base_bot/src/actions/action.py`
- Expected: No matches (submit method completely removed)

---

### ITERATION 2: Core Action Layer - Clarify Action

**Epic:** Merge Submit with Confirm
**Story:** Clarify action saves data on confirm

**Step 2.1: Update Test**
- File: `test/test_gather_context.py`
- **REMOVE:** All calls to `action.submit(context)`
- **ADD:** Replace with `action.confirm(context)`
- **REMOVE:** Any test methods that specifically test submit operation
- **ADD:** Test that clarification data is saved when confirm is called with ClarifyActionContext
- Expected: Tests PASS (already fixed by Iteration 1)

**Step 2.2: Validate**
- Run: `tests.validate.instructions`
- Verify: Test file follows rules

**Step 2.3: Run Tests**
- Run: `pytest test/test_gather_context.py`
- Expected: Tests PASS

---

### ITERATION 3: Core Action Layer - Build/Validate/Render Actions

**Epic:** Merge Submit with Confirm
**Story:** Build/Validate/Render actions don't save on confirm

**Step 3.1: Update Tests**
- Files: 
  - `test/test_build_knowledge.py`
  - `test/test_validate_knowledge_and_content_against_rules.py`
  - `test/test_render_output.py`
- **REMOVE:** All calls to `action.submit()` - delete these lines
- **ADD:** Replace with `action.confirm()` calls
- **REMOVE:** Any test methods specifically testing submit behavior - delete entire methods
- **REMOVE:** Any assertions about submit return values
- **ADD:** Negative tests verifying NO data is saved (these actions return status only)
- **ADD:** Assertions about confirm return values
- Expected: Tests PASS (already fixed by Iteration 1)

**Step 3.2: Validate**
- Run: `tests.validate.instructions`
- Verify: Test files follow rules
- Verify: No references to submit remain in test files

**Step 3.3: Run Tests**
- Run: `pytest test/test_build_knowledge.py test/test_validate_knowledge_and_content_against_rules.py test/test_render_output.py`
- Expected: Tests PASS

**Step 3.4: Verify Removal**
- Run: `grep "submit" test/test_build_knowledge.py test/test_validate_knowledge_and_content_against_rules.py test/test_render_output.py`
- Expected: No matches (all submit references removed)

---

### ITERATION 4: REPL CLI Layer - Confirm Command

**Epic:** REPL CLI Operations
**Story:** Confirm command accepts parameters

**Step 4.1: Update Test**
- File: `test/test_execute_action_operation_through_cli.py`
- **REMOVE:** Class `TestSubmitWorkThroughCLIWithStringParameters` (entire class)
- **ADD:** New class `TestConfirmWorkThroughCLIWithStringParameters`
- **REMOVE:** All `'submit'` command strings in tests
- **ADD:** Replace with `'confirm'` command strings
- **REMOVE:** Line 263: `repl_session.read_and_execute_command('submit')`
- **ADD:** Replace with `repl_session.read_and_execute_command('confirm')`
- **REMOVE:** Any assertions checking for submit-specific behavior
- **ADD:** Assertions checking for confirm-specific behavior
- Expected: Tests FAIL (CLI doesn't pass args to confirm yet)

**Step 4.2: Implement CLI Changes**
- File: `repl_cli/cli_bot/cli_actions/cli_action.py`
- **REMOVE:** Nothing (submit method removal happens in Iteration 8)
- **UPDATE:** Modify existing `confirm(self, args: str = "")` method to parse args and pass context
- **ADD:** New implementation:
  ```python
  def confirm(self, args: str = "") -> str:
      """Confirm action with optional parameters."""
      try:
          self._session.set_action_phase('confirming')
          context = self._parse_args_to_context(args)
          result = self._action.confirm(context)
          return self._format_result(result)
      except Exception as e:
          return f"Error confirming: {str(e)}"
  ```

**Step 4.3: Implement Session Changes**
- File: `repl_cli/repl_session.py`
- **REMOVE:** Nothing (submit handler removal happens in Iteration 8)
- **UPDATE:** Modify `_handle_confirm_command(self, args: str = "")` signature and implementation
- **ADD:** Pass args to action.confirm():
  ```python
  def _handle_confirm_command(self, args: str = "") -> REPLCommandResponse:
      # ... validation code ...
      result_output = action.confirm(args)  # Pass args instead of empty call
      # ... rest of logic ...
  ```

**Step 4.4: Validate**
- Run: `code.validate.instructions`
- Verify: No rule violations

**Step 4.5: Run Tests**
- Run: `pytest test/test_execute_action_operation_through_cli.py`
- Expected: Tests PASS

---

### ITERATION 5: REPL CLI Layer - Current Command Tests

**Epic:** REPL CLI Operations
**Story:** Current command tests work with confirm

**Step 5.1: Update Test**
- File: `test/test_execute_action_operation_through_cli_current.py`
- Change: Similar changes as Iteration 4
- Expected: Tests PASS (already fixed by Iteration 4)

**Step 5.2: Run Tests**
- Run: `pytest test/test_execute_action_operation_through_cli_current.py`
- Expected: Tests PASS

---

### ITERATION 6: REPL Session Initialization

**Epic:** REPL Session Management
**Story:** Session initialization works with confirm

**Step 6.1: Update Tests**
- Files:
  - `test/test_initialize_repl_session.py`
  - `test/test_initialize_repl_session_current.py`
  - `test/test_current_initialize_repl_session.py`
- **REMOVE:** Any tests that initialize with submit operation
- **ADD:** Tests that initialize with confirm operation
- **REMOVE:** Any submit command strings in initialization tests
- **ADD:** Replace with confirm command strings
- Expected: Tests PASS (already fixed by previous iterations)

**Step 6.2: Run Tests**
- Run: `pytest test/test_initialize_repl_session*.py test/test_current_initialize_repl_session.py`
- Expected: Tests PASS

---

### ITERATION 7: Workflow and Behavior Execution

**Epic:** Workflow Management
**Story:** Workflow advancement works with confirm

**Step 7.1: Update Test**
- File: `test/test_execute_behavior_actions.py`
- **REMOVE:** All workflow tests that reference submit operation
- **ADD:** Update workflow tests to use confirm operation
- **REMOVE:** Any assertions about 3-phase workflow (instructions → submit → confirm)
- **ADD:** Assertions about 2-phase workflow (instructions → confirm)
- Expected: Tests PASS (already fixed by previous iterations)

**Step 7.2: Run Tests**
- Run: `pytest test/test_execute_behavior_actions.py`
- Expected: Tests PASS

---

### ITERATION 8: COMPLETE REMOVAL OF SUBMIT (No Legacy Code)

**Epic:** Code Cleanup - Total Submit Elimination
**Story:** Remove ALL submit code, methods, references, and files

⚠️ **CRITICAL: This is COMPLETE DELETION, not deprecation. NO fallbacks, NO legacy code.**

---

**Step 8.1: Verify No Tests Use submit()**
- Run: `grep -r "\.submit\(" test/`
- Run: `grep -r "'submit'" test/`
- Run: `grep -r '"submit"' test/`
- Expected: **ZERO matches** (all changed to confirm in previous iterations)

---

**Step 8.2: DELETE Submit Method from Action Base Class**
- File: `actions/action.py`
- Change: **DELETE** `submit()` method entirely (lines 406-418)
- Change: **DELETE** any submit-related comments or docstrings
- Verify: No references to submit remain in file
- Expected: All tests still pass (nothing calls submit anymore)

---

**Step 8.3: DELETE Submit Method from CLIAction**
- File: `repl_cli/cli_bot/cli_actions/cli_action.py`
- Change: **DELETE** `submit()` method entirely (lines 56-64)
- Change: **DELETE** any submit-related comments
- Verify: No references to submit remain in file
- Expected: No test failures

---

**Step 8.4: DELETE Submit Command Handler from REPLSession**
- File: `repl_cli/repl_session.py`
- Change: **DELETE** `_handle_submit_command()` method entirely (lines 560-578)
- Change: **DELETE** submit from command routing (lines 332-333)
- Change: **DELETE** any submit-related helper methods
- Change: **REMOVE** submit from operations list/constants
- Verify: No references to submit remain in file
- Expected: No test failures

---

**Step 8.5: DELETE Submit from Headless Session**
- File: `repl_cli/headless/headless_session.py`
- Change: **REMOVE** 'submit' from operations list if present
- Change: **DELETE** any submit-related logic
- Verify: No references to submit remain in file
- Expected: Headless tests still pass

---

**Step 8.6: DELETE Submit References from Help System**
- File: `repl_cli/repl_help.py`
- Change: **DELETE** all submit operation help text
- Change: **DELETE** all submit examples
- Change: **DELETE** all submit references from workflow descriptions
- Verify: No references to submit remain in file
- Expected: Help text shows only 2-phase model (instructions → confirm)

---

**Step 8.7: DELETE Submit References from Status Display**
- File: `repl_cli/repl_status.py`
- Change: **DELETE** any `_get_submit_params()` methods
- Change: **DELETE** any submit status display logic
- Verify: No references to submit remain in file
- Expected: Status shows only confirm

---

**Step 8.8: DELETE Submit from All Action Subclasses**
- Files: Check all action subclasses for submit methods
  - `actions/strategy/strategy_action.py`
  - `actions/clarify/clarify_action.py`
  - `actions/build/build_action.py`
  - `actions/validate/validate_action.py`
  - `actions/render/render_action.py`
- Change: **DELETE** any overridden `submit()` methods (should be none, but verify)
- Verify: No action subclass has a submit method
- Expected: No test failures

---

**Step 8.9: DELETE Submit from MCP Server Descriptions**
- File: `src/base_bot_mcp_server.py` (or equivalent)
- Change: **DELETE** any submit tool descriptions
- Change: **DELETE** any submit examples
- Verify: MCP tools only reference confirm
- Expected: MCP tools work correctly

---

**Step 8.10: DELETE Submit from CLI Parameter Parser**
- File: `cli/cli_parameter_parser.py`
- Change: **DELETE** any submit-specific argument parsing
- Verify: No references to submit remain
- Expected: CLI parsing works correctly

---

**Step 8.11: DELETE Submit References from All Config Files**
- Files: Search all JSON config files
  - `base_actions/*/action_config.json`
  - `behaviors/*/action_config.json`
  - `bot_config.json`
  - `instructions.json`
- Change: **DELETE** or **REPLACE** all submit references with confirm
- Verify: `grep -r "submit" . --include="*.json"` returns 0 results
- Expected: Configs are clean

---

**Step 8.12: DELETE Submit References from All Documentation**
- Files: All markdown files in docs/
  - `docs/stories/*.md`
  - `docs/plans/*.md`
  - `docs/crc/*.md`
  - `README.md` files
- Change: **DELETE** or **REPLACE** all submit references with confirm
- Verify: `grep -r "submit" docs/ --include="*.md"` returns 0 results (except this plan)
- Expected: Documentation is clean

---

**Step 8.13: DELETE Submit References from Extension**
- Files: Extension files
  - `extension/chat_participants.js`
  - `extension/README.md`
  - `extension/package.json`
- Change: **DELETE** or **REPLACE** all submit references with confirm
- Verify: No submit references remain
- Expected: Extension works correctly

---

**Step 8.14: DELETE Submit References from Scripts**
- Files: Launcher scripts
  - `generate_bot.ps1`
  - `generate_bot.sh`
  - Any example scripts
- Change: **DELETE** or **REPLACE** all submit references with confirm
- Verify: No submit references remain
- Expected: Scripts work correctly

---

**Step 8.15: FINAL VERIFICATION - Zero Submit References**

Run these commands and verify **ZERO matches**:

```bash
# Python code
grep -r "def submit\(" agile_bot/bots/base_bot/src/ --include="*.py"
grep -r "\.submit\(" agile_bot/bots/base_bot/src/ --include="*.py"
grep -r "_handle_submit" agile_bot/bots/base_bot/src/ --include="*.py"
grep -r "'submit'" agile_bot/bots/base_bot/src/ --include="*.py"
grep -r '"submit"' agile_bot/bots/base_bot/src/ --include="*.py"

# Tests
grep -r "submit" agile_bot/bots/base_bot/test/ --include="*.py"

# Configs
grep -r "submit" agile_bot/bots/base_bot/base_actions/ --include="*.json"
grep -r "submit" agile_bot/bots/base_bot/behaviors/ --include="*.json"

# Documentation
grep -r "submit" agile_bot/bots/base_bot/docs/ --include="*.md"

# Extension
grep -r "submit" agile_bot/bots/base_bot/extension/

# Scripts
grep -r "submit" agile_bot/bots/base_bot/*.ps1
grep -r "submit" agile_bot/bots/base_bot/*.sh
```

**Expected Result:** ALL commands return **0 matches**

---

**Step 8.16: Run Full Test Suite**
- Run: `pytest agile_bot/bots/base_bot/test/ -v`
- Expected: **ALL tests PASS**
- Verify: No tests reference submit
- Verify: All workflows use confirm

---

**Step 8.17: Validate All Code**
- Run: `code.validate.instructions`
- Expected: **No rule violations**
- Verify: Code follows all rules
- Verify: No legacy patterns remain

---

**Step 8.18: Manual REPL Verification**

Test that submit command is completely gone:

```bash
# This should FAIL with "unknown command" or similar
echo 'shape.strategy.submit' | python repl_main.py

# This should WORK
echo 'shape.strategy.confirm' | python repl_main.py

# Help should NOT mention submit
echo 'help' | python repl_main.py | grep -i submit

# Status should NOT mention submit
echo 'status' | python repl_main.py | grep -i submit
```

**Expected:**
- ❌ Submit command fails (not recognized)
- ✅ Confirm command works
- ❌ Help contains zero submit references
- ❌ Status contains zero submit references

---

### Summary of Iteration 8:

**What Was DELETED:**
- ✅ `Action.submit()` method
- ✅ `CLIAction.submit()` method  
- ✅ `REPLSession._handle_submit_command()` method
- ✅ Submit command routing
- ✅ Submit help text
- ✅ Submit status display
- ✅ Submit references in configs
- ✅ Submit references in docs
- ✅ Submit references in extension
- ✅ Submit references in scripts
- ✅ Submit references in tests

**What Remains:**
- ❌ NOTHING - submit is completely gone

**Verification:**
- ✅ Zero grep matches for submit in codebase
- ✅ All tests pass
- ✅ REPL rejects submit command
- ✅ Only confirm exists in 2-phase model

---

### ITERATION 9: Autoconfirm Parameter - Parsing

**Epic:** Autoconfirm Feature (NEW - No Legacy Code)
**Story:** Parse --autoconfirm parameter

**Step 9.1: Add Test**
- File: `test/test_execute_action_operation_through_cli.py`
- **ADD:** New test `test_instructions_with_autoconfirm_flag()`
- **ADD:** Test that `--autoconfirm` flag automatically calls confirm after instructions
- **ADD:** Test that `--autoconfirm:true` works
- **ADD:** Test that `--autoconfirm:false` does NOT auto-confirm
- **ADD:** Test that default (no flag) does NOT auto-confirm
- Expected: Test FAILS (autoconfirm not implemented)

**Step 9.2: Implement Parsing**
- File: `repl_cli/repl_session.py`
- **ADD:** New method `_parse_autoconfirm_flag(args: str) -> bool`
  ```python
  def _parse_autoconfirm_flag(self, args: str) -> bool:
      """Parse --autoconfirm flag from args. Default is False."""
      if '--autoconfirm:true' in args or '--autoconfirm' in args:
          return True
      return False
  ```
- **ADD:** New method `_remove_autoconfirm_flag(args: str) -> str`
  ```python
  def _remove_autoconfirm_flag(self, args: str) -> str:
      """Remove --autoconfirm flag from args string."""
      args = args.replace('--autoconfirm:true', '').replace('--autoconfirm:false', '').replace('--autoconfirm', '')
      return args.strip()
  ```
- **UPDATE:** `_handle_instructions_command()` to check for autoconfirm and call confirm if true
  ```python
  def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
      # Parse autoconfirm flag
      autoconfirm = self._parse_autoconfirm_flag(args)
      args = self._remove_autoconfirm_flag(args)
      
      # ... existing instructions logic ...
      
      # If autoconfirm, automatically call confirm
      if autoconfirm:
          return self._handle_confirm_command(args)
      
      return response
  ```

**Step 9.3: Validate**
- Run: `code.validate.instructions`
- Verify: No rule violations
- Verify: New methods follow coding standards

**Step 9.4: Run Tests**
- Run: `pytest test/test_execute_action_operation_through_cli.py::test_instructions_with_autoconfirm_flag`
- Expected: Test PASSES

**Step 9.5: Verify Addition**
- Run: `grep "autoconfirm" repl_cli/repl_session.py`
- Expected: Multiple matches showing new autoconfirm functionality

---

### ITERATION 10: Autoconfirm Parameter - Display

**Epic:** Autoconfirm Feature (NEW - No Legacy Code)
**Story:** Display autoconfirm status

**Step 10.1: Add Test**
- File: `test/test_execute_action_operation_through_cli.py`
- **ADD:** Test that autoconfirm status is shown in instructions output
- **ADD:** Test that output contains "Autoconfirm: enabled" when flag is true
- **ADD:** Test that output contains "Autoconfirm: disabled" or nothing when flag is false
- Expected: Test FAILS (display not implemented)

**Step 10.2: Implement Display**
- File: `repl_cli/repl_session.py`
- **UPDATE:** `_handle_instructions_command()` to show autoconfirm status in output
  ```python
  def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
      autoconfirm = self._parse_autoconfirm_flag(args)
      # ... existing logic ...
      
      # Add autoconfirm status to output
      if autoconfirm:
          output += "\n\n[Autoconfirm: ENABLED - Will automatically confirm after instructions]"
      
      # ... rest of logic ...
  ```

**Step 10.3: Validate**
- Run: `code.validate.instructions`
- Verify: Display follows formatting standards

**Step 10.4: Run Tests**
- Run: `pytest test/test_execute_action_operation_through_cli.py`
- Expected: All tests PASS

**Step 10.5: Manual Verification**
- Run: `echo 'shape.strategy.instructions --autoconfirm' | python repl_main.py`
- Verify: Output shows autoconfirm status
- Verify: Confirm is automatically called

---

### ITERATION 11: Headless Mode

**Epic:** Headless Execution
**Story:** Headless mode works with confirm and autoconfirm

**Step 11.1: Update Test**
- File: `test/test_execute_in_headless_mode.py`
- Change: Update tests for confirm operation with parameters
- Add: Tests for autoconfirm in headless mode
- Expected: Tests FAIL (headless not updated)

**Step 11.2: Implement Headless Changes**
- File: `repl_cli/headless/headless_session.py`
- Change: Verify operations list includes confirm (not submit)
- Verify: Autoconfirm flag is passed through

**Step 11.3: Validate**
- Run: `code.validate.instructions`

**Step 11.4: Run Tests**
- Run: `pytest test/test_execute_in_headless_mode.py`
- Expected: Tests PASS

---

### ITERATION 12: Help System

**Epic:** User Documentation
**Story:** Help text reflects 2-phase model

**Step 12.1: Update Help System**
- File: `repl_cli/repl_help.py`
- **REMOVE:** All help text mentioning "submit" operation
- **REMOVE:** All examples showing submit command
- **REMOVE:** All references to 3-phase workflow (instructions → submit → confirm)
- **UPDATE:** Replace all "submit" with "confirm"
- **UPDATE:** Change workflow description to 2-phase (instructions → confirm)
- **ADD:** Documentation for --autoconfirm parameter
- **ADD:** Examples showing confirm with parameters
- **ADD:** Examples showing --autoconfirm usage

**Step 12.2: Validate**
- Run: `code.validate.instructions`
- Run: `grep -i "submit" repl_cli/repl_help.py`
- Expected: 0 matches

**Step 12.3: Manual Verification**
- Run REPL: `echo 'help' | python repl_main.py`
- Verify: Help text shows confirm (not submit)
- Verify: Help text shows 2-phase model
- Verify: Help text shows --autoconfirm parameter

---

### ITERATION 13: Status Display

**Epic:** User Documentation
**Story:** Status display shows confirm (not submit)

**Step 13.1: Update Status Display**
- File: `repl_cli/repl_status.py`
- **REMOVE:** Method `_get_submit_params()` (delete entirely)
- **ADD:** New method `_get_confirm_params()` (replaces submit version)
- **REMOVE:** All status display text mentioning "submit"
- **UPDATE:** Replace all "submit" references with "confirm"
- **REMOVE:** Any submit-specific status fields
- **ADD:** Confirm-specific status fields
- **ADD:** Display autoconfirm status if applicable

**Step 13.2: Validate**
- Run: `code.validate.instructions`
- Run: `grep -i "submit" repl_cli/repl_status.py`
- Expected: 0 matches

**Step 13.3: Manual Verification**
- Run REPL: `echo 'status' | python repl_main.py`
- Verify: Status shows confirm (not submit)
- Verify: Status shows 2-phase model
- Verify: No submit references anywhere

---

### ITERATION 14: CLI Parameter Parser

**Epic:** CLI Integration
**Story:** CLI parses autoconfirm parameter

**Step 14.1: Update Tests**
- File: `test/test_invoke_cli.py`
- **REMOVE:** Any tests for submit parameter parsing (if they exist)
- **ADD:** New test for --autoconfirm parameter parsing
- **ADD:** Test that --autoconfirm:true is parsed correctly
- **ADD:** Test that --autoconfirm:false is parsed correctly
- **ADD:** Test that default (no flag) is false
- Expected: Test FAILS (not implemented)

**Step 14.2: Implement Parser**
- File: `cli/cli_parameter_parser.py`
- **REMOVE:** Any submit-specific argument parsing (if it exists)
- **ADD:** `--autoconfirm` argument to argument parser
- **ADD:** autoconfirm to remaining args list
- **ADD:** autoconfirm to params dictionary
- **ADD:** Default value of false for autoconfirm

**Step 14.3: Validate**
- Run: `code.validate.instructions`
- Run: `grep -i "submit" cli/cli_parameter_parser.py`
- Expected: 0 matches

**Step 14.4: Run Tests**
- Run: `pytest test/test_invoke_cli.py -v`
- Expected: Tests PASS

---

### ITERATION 15: MCP Tools Verification

**Epic:** MCP Integration
**Story:** MCP tools work with confirm

**Step 15.1: Update Tests**
- File: `test/test_invoke_mcp.py`
- **REMOVE:** Any tests that specifically test submit operation via MCP
- **UPDATE:** Any references to submit → confirm
- **VERIFY:** MCP tools use execute() which internally calls confirm
- Expected: Tests PASS (MCP uses execute(), already works)

**Step 15.2: Validate**
- Run: `grep -i "submit" test/test_invoke_mcp.py`
- Expected: 0 matches

**Step 15.3: Run Tests**
- Run: `pytest test/test_invoke_mcp.py -v`
- Expected: Tests PASS

---

### ITERATION 16: Action Cycling

**Epic:** REPL Workflow
**Story:** Action cycling skips submit

**Step 16.1: Update Action Cycling Logic**
- File: `repl_cli/repl_session.py`
- **FIND:** `_handle_action_shortcut()` or action cycling method
- **REMOVE:** Submit from operation cycle list
- **UPDATE:** Cycling logic to: instructions → confirm (2-phase, skip submit)
- **REMOVE:** Any submit-specific cycling logic
- **UPDATE:** Any cycle navigation that references submit

**Step 16.2: Validate**
- Run: `code.validate.instructions`
- Run: `grep -i "submit" repl_cli/repl_session.py`
- Expected: 0 matches (submit completely removed)

**Step 16.3: Manual Verification**
- Run REPL and test cycling through operations
- Verify: Cycling goes instructions → confirm (no submit)
- Verify: No submit operation accessible via cycling

---

### ITERATION 17: Final Test Suite

**Epic:** Quality Assurance
**Story:** All tests pass

**Step 17.1: Run Full Test Suite**
- Run: `pytest test/ -v`
- Expected: All tests PASS

**Step 17.2: Validate All Code**
- Run: `code.validate.instructions`
- Expected: No rule violations

**Step 17.3: Fix Any Failures**
- If any tests fail, fix them one by one
- Re-run tests after each fix

---

### ITERATION 18: Configuration Files

**Epic:** Configuration Updates
**Story:** Update config files (no functional impact)

**Step 18.1: Update Action Configs**
- Files: All `action_config.json` files in:
  - `base_actions/*/action_config.json`
  - `behaviors/*/action_config.json`
  - `bot_config.json`
- **REMOVE:** All references to "submit" in instructions/descriptions
- **UPDATE:** Replace "submit" with "confirm"
- **UPDATE:** Update workflow descriptions to 2-phase model
- **REMOVE:** Any submit-specific configuration fields

**Step 18.2: Validate**
- Run: `code.validate.instructions`
- Run: `grep -r "submit" agile_bot/bots/ --include="*.json"`
- Expected: 0 matches

---

### ITERATION 19: Documentation

**Epic:** Documentation Updates
**Story:** Update docs (no functional impact)

**Step 19.1: Update Documentation**
- Files: All markdown documentation:
  - `docs/stories/*.md`
  - `docs/plans/*.md`
  - `docs/crc/*.md`
  - `README.md` files
- **REMOVE:** All references to "submit" operation
- **UPDATE:** Replace "submit" with "confirm"
- **REMOVE:** All references to 3-phase workflow
- **UPDATE:** Update to 2-phase workflow (instructions → confirm)
- **ADD:** Documentation for --autoconfirm parameter

**Step 19.2: Update Extension**
- Files: Extension files:
  - `extension/chat_participants.js`
  - `extension/README.md`
  - `extension/package.json`
- **REMOVE:** All submit command examples
- **UPDATE:** Replace with confirm command examples
- **ADD:** Examples showing --autoconfirm usage

**Step 19.3: Update Launchers**
- Files: Launcher scripts:
  - `generate_bot.ps1`
  - `generate_bot.sh`
  - Any example scripts
- **REMOVE:** All submit references in comments/examples
- **UPDATE:** Replace with confirm references
- **UPDATE:** Update workflow examples to 2-phase model

**Step 19.4: Final Documentation Verification**
- Run: `grep -r "submit" agile_bot/bots/base_bot/docs/ --include="*.md"`
- Run: `grep -r "submit" agile_bot/bots/base_bot/extension/`
- Run: `grep -r "submit" agile_bot/bots/base_bot/*.ps1`
- Run: `grep -r "submit" agile_bot/bots/base_bot/*.sh`
- Expected: 0 matches in all commands (except this plan document)

---

### Summary of Test-Driven Approach

**Key Principles:**
1. ✅ **Test First**: Update tests before implementation
2. ✅ **Incremental**: One epic/story at a time
3. ✅ **Validate**: Run validation after each change
4. ✅ **Verify**: Tests must pass before moving on
5. ✅ **Minimal**: Only implement what's needed for tests to pass

**Total Iterations:** 19
**Critical Path:** Iterations 1-11 (core functionality)
**Polish:** Iterations 12-19 (UX and documentation)

---

## PART 18: FILES SUMMARY

### Core Python Files (Critical - ~17 files)
1. `actions/action.py` - merge confirm with submit
2. `repl_cli/cli_bot/cli_actions/cli_action.py` - remove submit, update confirm
3. `repl_cli/repl_session.py` - remove submit handler, update confirm handler, add autoconfirm
4. `repl_cli/repl_status.py` - rename submit params to confirm params
5. `repl_cli/repl_help.py` - update all help text
6. `repl_cli/headless/headless_session.py` - update operations list
7. `repl_cli/command_parser.py` - remove submit from operations list
8. `repl_cli/repl_main.py` - update example comments
9. `cli/cli_parameter_parser.py` - add autoconfirm support

### Test Files (Critical for Validation - ~15 files)
8. `test/test_execute_action_operation_through_cli.py`
9. `test/test_execute_action_operation_through_cli_current.py`
10. `test/test_decide_strategy_criteria_action.py`
11. `test/test_gather_context.py`
12. `test/test_build_knowledge.py`
13. `test/test_validate_knowledge_and_content_against_rules.py`
14. `test/test_render_output.py`
15. `test/test_initialize_repl_session.py`
16. `test/test_initialize_repl_session_current.py`
17. `test/test_current_initialize_repl_session.py`
18. `test/test_execute_in_headless_mode.py`
19. `test/test_execute_behavior_actions.py`
20. All other test files that reference submit

### Configuration Files (Medium Priority - ~10-20 files)
21. All `action_config.json` files in base_bot/base_actions/
22. All `behavior.json` files in story_bot/behaviors/
23. All `behavior.json` files in crc_bot/behaviors/
24. All `instructions.json` files

### Documentation Files (Low Priority - ~20-50 files)
25. All story documents in docs/stories/
26. README files
27. Extension files
28. Launcher scripts

### Total Estimated Files: 60-100+ files

---

## PART 19: KEY DECISIONS MADE

1. `confirm` will call `_do_submit` first, then track completion
2. `confirm` signature matches `submit` (takes `context: ActionContext`)
3. Autoconfirm parameter format: `--autoconfirm:true` or `--autoconfirm` (default: false)
4. Autoconfirm applies to instructions operation only
5. Display autoconfirm status in instructions section
6. MCP tools continue using execute() (no operation support needed unless required)
7. Action cycling: instructions → confirm (skip submit)

---

## PART 20: KEY DECISIONS MADE

1. **Should autoconfirm be part of ActionContext or handled separately?**
   - **DECISION**: Handle separately in REPL session (not part of context)
   - **RATIONALE**: Autoconfirm is a workflow control flag, not action data. It controls REPL session behavior, not action execution logic.

2. **Does standard CLI need operation support (instructions/submit/confirm) or is execute() sufficient?**
   - **DECISION**: execute() is sufficient - no operation support needed
   - **RATIONALE**: CLI command router uses `action.execute(context)` which handles full workflow internally. The execute() method manages instructions → confirm workflow, so when confirm() is updated to call _do_submit(), it will work correctly.

3. **Should MCP tools support operations, or continue using execute()?**
   - **DECISION**: Continue using execute() - no operation support needed
   - **RATIONALE**: MCP tools call `action.execute(parameters)` which handles full workflow internally. Parameters are passed as dict, execute() builds context and calls operations internally. When confirm() is updated to call _do_submit(), execute() will work correctly.

---

---

## PART 21: FINAL VERIFICATION CHECKLIST

After completing all 19 iterations, run this comprehensive verification to ensure **ZERO legacy submit code remains**:

### 1. Code Verification (Must Return 0 Matches)

```bash
# BaseBot Python code
grep -r "def submit\(" agile_bot/bots/base_bot/src/ --include="*.py"
grep -r "\.submit\(" agile_bot/bots/base_bot/src/ --include="*.py"
grep -r "_handle_submit" agile_bot/bots/base_bot/src/ --include="*.py"
grep -r "'submit'" agile_bot/bots/base_bot/src/ --include="*.py"
grep -r '"submit"' agile_bot/bots/base_bot/src/ --include="*.py"

# BaseBot tests
grep -r "submit" agile_bot/bots/base_bot/test/ --include="*.py"

# StoryBot code
grep -r "submit" agile_bot/bots/story_bot/src/ --include="*.py"

# CRCBot code
grep -r "submit" agile_bot/bots/crc_bot/src/ --include="*.py"
```

**Expected:** ALL commands return **0 matches**

---

### 2. Configuration Verification (Must Return 0 Matches)

```bash
# BaseBot configs
grep -r "submit" agile_bot/bots/base_bot/base_actions/ --include="*.json"
grep -r "submit" agile_bot/bots/base_bot/behaviors/ --include="*.json"
grep -r "submit" agile_bot/bots/base_bot/bot_config.json
grep -r "submit" agile_bot/bots/base_bot/instructions.json

# StoryBot configs
grep -r "submit" agile_bot/bots/story_bot/behaviors/ --include="*.json"
grep -r "submit" agile_bot/bots/story_bot/bot_config.json
grep -r "submit" agile_bot/bots/story_bot/instructions.json

# CRCBot configs
grep -r "submit" agile_bot/bots/crc_bot/behaviors/ --include="*.json"
grep -r "submit" agile_bot/bots/crc_bot/bot_config.json
grep -r "submit" agile_bot/bots/crc_bot/instructions.json
```

**Expected:** ALL commands return **0 matches**

---

### 3. Documentation Verification (Must Return 0 Matches)

```bash
# BaseBot docs
grep -r "submit" agile_bot/bots/base_bot/docs/ --include="*.md"

# StoryBot docs
grep -r "submit" agile_bot/bots/story_bot/docs/ --include="*.md"

# CRCBot docs
grep -r "submit" agile_bot/bots/crc_bot/docs/ --include="*.md"

# Extension
grep -r "submit" agile_bot/bots/base_bot/extension/

# Scripts
grep -r "submit" agile_bot/bots/base_bot/*.ps1
grep -r "submit" agile_bot/bots/base_bot/*.sh
```

**Expected:** ALL commands return **0 matches** (except this plan document)

---

### 4. Functional Verification

#### 4.1 Test Suite (Must Pass 100%)
```bash
# BaseBot tests
pytest agile_bot/bots/base_bot/test/ -v

# StoryBot tests
pytest agile_bot/bots/story_bot/test/ -v

# CRCBot tests (if applicable)
pytest agile_bot/bots/crc_bot/test/ -v
```

**Expected:** ALL tests **PASS**, no failures, no skips

---

#### 4.2 REPL Manual Testing

**Test 1: Submit Command Fails**
```bash
echo 'shape.strategy.submit' | python agile_bot/bots/base_bot/src/base_bot_cli.py
```
**Expected:** Error message like "Unknown operation: submit" or "Invalid command"

---

**Test 2: Confirm Command Works**
```bash
echo 'shape.strategy.confirm --decisions="test" --assumptions="test"' | python agile_bot/bots/base_bot/src/base_bot_cli.py
```
**Expected:** Success, workflow advances

---

**Test 3: Autoconfirm Works**
```bash
echo 'shape.strategy.instructions --autoconfirm' | python agile_bot/bots/base_bot/src/base_bot_cli.py
```
**Expected:** Instructions displayed, then confirm automatically called

---

**Test 4: Help Shows No Submit**
```bash
echo 'help' | python agile_bot/bots/base_bot/src/base_bot_cli.py | grep -i submit
```
**Expected:** 0 matches (no submit in help text)

---

**Test 5: Status Shows No Submit**
```bash
echo 'status' | python agile_bot/bots/base_bot/src/base_bot_cli.py | grep -i submit
```
**Expected:** 0 matches (no submit in status)

---

**Test 6: Autoconfirm Status Displayed**
```bash
echo 'shape.strategy.instructions' | python agile_bot/bots/base_bot/src/base_bot_cli.py | grep -i autoconfirm
```
**Expected:** Shows "Autoconfirm: false" or similar

---

#### 4.3 Validation Commands

**Validate BaseBot Code**
```bash
cd agile_bot/bots/base_bot
echo 'code.validate.instructions' | python src/base_bot_cli.py
```
**Expected:** No rule violations

---

**Validate StoryBot Code**
```bash
cd agile_bot/bots/story_bot
echo 'code.validate.instructions' | python src/story_bot_cli.py
```
**Expected:** No rule violations

---

### 5. Headless Mode Verification

```bash
# Test headless with confirm
python agile_bot/bots/base_bot/src/base_bot_cli.py --headless --message "Test confirm workflow"

# Test headless with autoconfirm
python agile_bot/bots/base_bot/src/base_bot_cli.py --headless --message "Test with --autoconfirm"
```

**Expected:** Both work correctly, no submit references in output

---

### 6. MCP Tools Verification

```bash
# List MCP tools (should not mention submit)
python agile_bot/bots/base_bot/src/base_bot_mcp_server.py list-tools | grep -i submit

# Test MCP tool execution
python agile_bot/bots/base_bot/src/base_bot_mcp_server.py call-tool base_bot_shape_strategy '{"decisions": "test"}'
```

**Expected:** 
- 0 matches for submit in tool list
- Tool execution works correctly

---

### 7. Cross-Bot Verification

Verify changes propagated to all bots:

```bash
# Check all bots have no submit references
for bot in base_bot story_bot crc_bot; do
    echo "Checking $bot..."
    grep -r "submit" agile_bot/bots/$bot/src/ --include="*.py" | grep -v "# submit" | wc -l
done
```

**Expected:** All counts are **0**

---

### 8. Final Checklist

Before considering this complete, verify:

- [ ] ✅ All 19 iterations completed
- [ ] ✅ All grep commands return 0 matches
- [ ] ✅ All tests pass (100%)
- [ ] ✅ Submit command fails in REPL
- [ ] ✅ Confirm command works in REPL
- [ ] ✅ Autoconfirm works correctly
- [ ] ✅ Help text shows only 2-phase model
- [ ] ✅ Status shows only confirm
- [ ] ✅ Validation passes with no violations
- [ ] ✅ Headless mode works correctly
- [ ] ✅ MCP tools work correctly
- [ ] ✅ All three bots (BaseBot, StoryBot, CRCBot) updated
- [ ] ✅ No legacy JSON files remain
- [ ] ✅ No commented-out submit code
- [ ] ✅ No fallback logic for submit
- [ ] ✅ Documentation updated
- [ ] ✅ Extension updated
- [ ] ✅ Scripts updated

---

## END OF COMPREHENSIVE PLAN

This plan covers **every single file, class, method, test, configuration, and reference** that needs to be changed to merge submit with confirm and add autoconfirm support.

**CRITICAL REMINDERS:**
1. ❌ **NO legacy submit code** - complete deletion, not deprecation
2. ❌ **NO fallback logic** - submit is gone, period
3. ❌ **NO commented-out code** - delete, don't comment
4. ❌ **NO backward compatibility** - this is a breaking change
5. ✅ **COMPLETE verification** - all grep commands must return 0 matches
6. ✅ **Test-driven approach** - fix tests first, then implementation
7. ✅ **Incremental validation** - validate after each iteration

**The implementation is organized into 19 test-driven iterations to ensure systematic, verifiable progress with zero legacy code retention.**

**Estimated Complexity:** Medium-High (signature changes affect many call sites)
**Estimated Time:** 2-3 days for core changes, 1-2 days for tests, 1 day for docs/configs
**Risk Level:** Medium (breaking changes, but well-scoped)
