# Dynamic Path Discovery Refactor

## Summary

Removed ALL hardcoded paths from code-agent runners. Now dynamically discovers behavior directories by scanning for `behavior.json` files with `deployed=true`.

## Changes Made

### 1. Created Common Utility (`code-agent-common.py`)
New shared module with helper functions:
- `find_deployed_behaviors()` - Finds all directories with `behavior.json` where `deployed=true`
- `find_all_behavior_jsons()` - Returns all behavior configs
- `get_behavior_feature_name()` - Extracts feature name from behavior directory

### 2. Updated Runners

#### `code-agent-structure-runner.py`
- ❌ **REMOVED**: Hardcoded `Path("features")`
- ✅ **ADDED**: Dynamic discovery using `find_deployed_behaviors()`
- ✅ **FIXED**: Watch mode now monitors ALL deployed behaviors

#### `code-agent-sync-runner.py`
- ❌ **REMOVED**: Hardcoded `Path("behaviors")` glob patterns
- ✅ **ADDED**: Dynamic discovery using `find_deployed_behaviors()`
- ✅ **FIXED**: Watch mode now monitors ALL deployed behaviors

#### `code-agent-consistency-runner.py`
- ❌ **REMOVED**: Hardcoded `Path("features")`
- ✅ **ADDED**: Dynamic discovery using `find_deployed_behaviors()`
- ✅ **FIXED**: Watch mode now monitors ALL deployed behaviors
- ✅ **FIXED**: File path resolution uses behavior data directly

#### `code-agent-index-runner.py`
- ❌ **REMOVED**: Hardcoded `Path("features")`
- ✅ **ADDED**: Dynamic discovery using `find_deployed_behaviors()`
- ✅ **FIXED**: Feature discovery works with any behavior directory structure

#### `code-agent-specialization-validation-runner.py`
- ❌ **REMOVED**: Hardcoded `Path("features") / feature_name`
- ✅ **ADDED**: Dynamic discovery using `find_deployed_behaviors()`
- ✅ **FIXED**: Feature validation works with any behavior directory structure

## How It Works Now

### Before (Hardcoded)
```python
src_root = Path("features")  # ❌ Assumes specific folder
features = [p for p in src_root.glob("*/cursor") if p.is_dir()]
```

### After (Dynamic)
```python
from code_agent_common import find_deployed_behaviors
features = find_deployed_behaviors()  # ✅ Finds ANY folder with behavior.json + deployed=true
```

## Benefits

1. **Flexible Structure**: Behaviors can be in ANY directory as long as they have `behavior.json` with `deployed=true`
2. **No Hardcoded Paths**: Zero assumptions about folder names or structure
3. **Single Source of Truth**: `behavior.json` controls deployment, not folder location
4. **Easier Testing**: Can create test behaviors in any location
5. **Better Organization**: Teams can organize behaviors however they want

## Migration Guide

To make a behavior discoverable:
1. Create `behavior.json` in the behavior directory
2. Set `"deployed": true` in the JSON
3. That's it! All tools will now find and process it

Example `behavior.json`:
```json
{
  "feature": "my-behavior",
  "deployed": true,
  "description": "My awesome behavior"
}
```

## Testing

All watchers now:
- ✅ Monitor ALL deployed behaviors (not just hardcoded paths)
- ✅ Automatically restart when behavior files change  
- ✅ Work with any directory structure
- ✅ Respect the `deployed` flag

## Breaking Changes

**NONE** - This is backward compatible. Existing behaviors in `behaviors/*/` with `behavior.json` continue to work exactly as before.

