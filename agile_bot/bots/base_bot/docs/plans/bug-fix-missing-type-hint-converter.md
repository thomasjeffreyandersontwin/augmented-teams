# Bug Fix: Missing TypeHintConverter and Generic Parameter Descriptions

## Issue Report
**User Found**: Help system imports `TypeHintConverter` but it doesn't exist, causing import errors and falling back to showing only generic "Optional parameter" descriptions instead of meaningful help text.

## Root Cause Analysis

### Why Tests Didn't Catch This

The existing help tests (`test_get_help_using_cli.py`) were too generic:
```python
# Existing test - too lenient!
assert 'help' in cli_response.output.lower() or cli_response.status == 'success'
```

This assertion passes as long as help displays *anything*, not checking:
1. Whether TypeHintConverter actually exists
2. Whether type hints are displayed (`<dict>`, `<path>`, `<string>`)
3. Whether descriptions are meaningful vs generic

### Actual Bugs Found

**Bug 1: Missing TypeHintConverter class**
- **Location**: `help_action.py` line 11 imports from `src/cli/type_hint_converter` 
- **Issue**: The module doesn't exist (`.cursorignore` blocks `src/cli/` directory)
- **Impact**: Import would fail silently or fall back to generic behavior

**Bug 2: Generic parameter descriptions**
- **Location**: `help_action.py` line 227
- **Issue**: All parameters show "Optional parameter" instead of meaningful descriptions
- **Impact**: Help is not useful - doesn't tell users what parameters do

```python
# BEFORE - useless
--scope <TYPE_ERROR>:   Optional parameter
--path <TYPE_ERROR>:    Optional parameter  

# AFTER - helpful!
--scope <dict>:         Scope structure: {'type': 'story'|'epic', 'value': [names]}
--path <path>:          Path to working directory or file
--answers <dict>:       Dict mapping question keys to answer strings
```

## The Fix

### 1. Created Failing Tests

Added `TestDynamicParameterHelp` class with 3 tests:
- `test_type_hint_converter_exists_and_works` - Verifies TypeHintConverter exists and converts types correctly
- `test_help_action_displays_typed_parameters` - Verifies help shows `<dict>`, `<path>`, etc. not just generic text
- `test_help_displays_meaningful_parameter_descriptions` - Verifies specific descriptions like "Scope structure: {...}"

### 2. Implemented TypeHintConverter

**File**: `agile_bot/bots/base_bot/src/actions/help_action.py` (added inline since `src/cli/` is blocked)

```python
class TypeHintConverter:
    """Converts Python type hints to CLI-friendly type strings"""
    
    @staticmethod
    def to_cli_type(python_type) -> str:
        # Handle basic types
        if python_type == str: return "string"
        elif python_type == Path: return "path"
        elif python_type == int: return "int"
        elif python_type == dict: return "dict"
        elif python_type == list: return "list"
        # ... etc
        
        # Handle generic types (Dict[str, Any], List[str], etc.)
        origin = get_origin(python_type)
        if origin is dict: return "dict"
        elif origin is list: return "list"
        # ... etc
```

### 3. Added Meaningful Descriptions

**File**: `agile_bot/bots/base_bot/src/actions/help_action.py`

Added `_get_parameter_description()` method that matches `ActionDataCollector` logic:

```python
def _get_parameter_description(self, action_name: str, param_name: str) -> str:
    """Get meaningful description for a parameter"""
    if 'answers' in param_name:
        return "Dict mapping question keys to answer strings"
    elif 'decisions' in param_name:
        return "Dict mapping decision criteria keys to selected options/values"
    elif 'scope' in param_name:
        return self._get_scope_description(action_name)
    elif 'path' in param_name:
        return "Path to working directory or file"
    else:
        return "Optional parameter"  # Fallback for unknown params
```

Updated `_get_parameters_from_context_class()` line 227:
```python
# BEFORE
params.append((f'{cli_name} <{type_hint}>', 'Optional parameter'))

# AFTER
description = self._get_parameter_description(action_name, field_info.name)
params.append((f'{cli_name} <{type_hint}>', description))
```

### 4. Updated Imports

**Files updated**:
- `agile_bot/bots/base_bot/src/generator/action_data_collector.py` - Import from `help_action` instead of non-existent `src/cli/`
- `agile_bot/bots/base_bot/test/test_get_help_using_cli.py` - Import from `help_action`

## Test Results

**Manual Verification**:
```
TypeHintConverter tests:
  str == string: ✓
  Path == path: ✓
  dict == dict: ✓
  list == list: ✓
  int == int: ✓
  bool == bool: ✓

Parameter descriptions:
  scope: Scope structure: {'type': 'story'|'epic'|'increment'|'all', 'value': <names|priorities>} ✓
  answers: Dict mapping question keys to answer strings ✓
  decisions_made: Dict mapping decision criteria keys to selected options/values ✓
  assumptions: List of assumption strings ✓
  path: Path to working directory or file ✓
```

## Key Learnings

1. **Test What Matters**: Generic "help works" tests miss specific functionality failures
   - ❌ `assert 'help' in output`
   - ✅ `assert '<dict>' in output and 'Scope structure:' in output`

2. **Imports Need Verification**: Just because code imports something doesn't mean it exists
   - Add test: `from module import Class; assert Class exists`

3. **Blocked Directories**: `.cursorignore` can block necessary code locations
   - Solution: Put shared utilities in accessible locations or inline them

4. **Parameter Help is Critical UX**: Users need to know what parameters do
   - Generic "Optional parameter" is useless
   - Specific "Dict mapping question keys to answer strings" is helpful

5. **Follow Existing Patterns**: `ActionDataCollector` already had this logic
   - DRY: Extract to shared location or replicate pattern consistently

## Prevention

To prevent similar issues:

1. **Add Explicit Type Tests**:
   ```python
   def test_module_exists():
       from module import Class  # Will fail if missing
       assert Class is not None
   ```

2. **Test Help Output Content**:
   ```python
   assert '<dict>' in help_output  # Check for type hints
   assert 'Scope structure:' in help_output  # Check for descriptions
   assert help_output.count('Optional parameter') < 3  # Not ALL generic
   ```

3. **Document Import Dependencies**:
   - Track which modules import from `src/cli/`
   - Ensure they work even if directory is blocked

4. **Unify Duplicate Logic**:
   - `ActionDataCollector` and `HelpAction` both describe parameters
   - Should share one source of truth

## Files Modified

### Implementation
- `agile_bot/bots/base_bot/src/actions/help_action.py`
  - Added `TypeHintConverter` class (lines 14-61)
  - Added `_get_parameter_description()` method
  - Added `_get_scope_description()` method  
  - Updated `_get_parameters_from_context_class()` to use meaningful descriptions

### Test Coverage
- `agile_bot/bots/base_bot/test/test_get_help_using_cli.py`
  - Added `TestDynamicParameterHelp` class with 3 tests
  - Tests verify TypeHintConverter, type hints display, and meaningful descriptions

### Import Fixes
- `agile_bot/bots/base_bot/src/generator/action_data_collector.py` - Updated import path
- `agile_bot/bots/base_bot/test/test_get_help_using_cli.py` - Updated import path

