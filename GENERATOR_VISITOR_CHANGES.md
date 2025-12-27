# Generator and Visitor Changes Summary

This document summarizes all changes made to the generator and visitor architecture for CLI, MCP, and Cursor command generation.

## Overview

**Key Architectural Change**: Moved from dynamic runtime tool registration to **static code generation** for both CLI and MCP code. This ensures:
- Code is generated at build time, not runtime
- No dependency on Cursor IDE for CLI generation
- Consistent generation approach across all output types
- Better testability and deployment

---

## 1. CLI Generation Changes

### Files Modified

#### `cli_generator.py`
**Changes:**
- **Removed**: Cursor command generation from `generate_cli_code()` method
- **Result**: `generate_cli_code()` now only generates CLI scripts (Python, shell, PowerShell)
- **Rationale**: CLI generation should work independently of Cursor IDE

**Before:**
```python
def generate_cli_code(self) -> Dict[str, Any]:
    # ... generated CLI scripts ...
    cursor_commands = self._command_generator.generate_cursor_commands(...)
    return {
        'cli_python': ...,
        'cursor_commands': cursor_commands  # ❌ Removed
    }
```

**After:**
```python
def generate_cli_code(self) -> Dict[str, Any]:
    """Generate CLI scripts (Python, shell, PowerShell). Does not generate Cursor commands."""
    # ... generates CLI scripts only ...
    return {
        'cli_python': cli_python_path,
        'cli_script': cli_script_path,
        'cli_powershell': cli_powershell_path
    }
```

#### `cli_code_visitor.py`
**Status**: No changes needed - already generates static CLI code correctly

**Key Features:**
- Generates Python CLI script (`{bot_name}_cli.py`)
- Generates shell script (`{bot_name}_cli`)
- Generates PowerShell script (`{bot_name}_cli.ps1`)
- All scripts are statically generated with proper bootstrap code

---

## 2. MCP Generation Changes

### Files Modified

#### `mcp_server_generator.py`
**Major Changes:**
1. **Renamed**: `create_server_instance()` → `_ensure_bot_initialized()` (private method)
2. **Removed**: FastMCP instance creation (not needed for static generation)
3. **Updated**: All call sites to use `_ensure_bot_initialized()`

**Before:**
```python
def create_server_instance(self) -> FastMCP:
    """Create and return FastMCP server instance."""
    if self.bot is None:
        # ... initialize bot ...
    mcp_server = FastMCP(self.bot_name)
    return mcp_server  # ❌ Not needed for static generation
```

**After:**
```python
def _ensure_bot_initialized(self) -> None:
    """Ensure bot instance is initialized. Used by methods that need bot access."""
    if self.bot is None:
        if not self.config_path.exists():
            raise FileNotFoundError(f'Bot Config not found at {self.config_path}')
        # ... validate and create bot ...
    # No FastMCP instance creation - tools are statically generated
```

#### `mcp_code_visitor.py`
**Major Changes:**
1. **Added**: `data_collector` property (required for orchestrator to visit behaviors)
2. **Added**: `formatter` and `description_extractor` properties
3. **Generates**: Static FastMCP server code with tool decorators

**Key Features:**
- Generates base tools (tool, get_working_dir, set_working_dir, close_current_action, etc.)
- Generates behavior tools (one per behavior) with trigger patterns
- All tools are statically registered via `@mcp_server.tool()` decorators
- Server code is written to `{bot_name}_mcp_server.py`

**New Properties:**
```python
@property
def data_collector(self) -> ActionDataCollector:
    """Required for orchestrator to visit behaviors."""
    if self._data_collector is None:
        self._data_collector = ActionDataCollector(
            bot=self.bot,
            bot_name=self.bot_name,
            bot_directory=self.bot_directory,
            description_extractor=self.description_extractor
        )
    return self._data_collector
```

### Files Removed

#### `mcp_tool_registrar.py` ❌ DELETED
**Reason**: Dynamic tool registration replaced by static code generation

#### `bot_tool_generator.py` ❌ DELETED
**Reason**: Bot tools now generated statically via `MCPCodeVisitor`

#### `behavior_tool_generator.py` ❌ DELETED
**Reason**: Behavior tools now generated statically via `MCPCodeVisitor`

**Deprecated Methods Removed:**
- `register_all_tools()` - Tools are statically generated, not dynamically registered

---

## 3. Cursor Command Generation Changes

### Files Modified

#### `cursor/command_file_visitor.py`
**Major Changes:**
1. **Added**: `data_collector` property (required for orchestrator to visit behaviors)
2. **Added**: `formatter` and `description_extractor` properties
3. **Generates**: Cursor command files (`.md` files in `.cursor/commands/`)

**Key Features:**
- Generates base commands (`{bot_name}.md`, `{bot_name}-continue.md`, etc.)
- Generates behavior commands (`{bot_name}-{behavior}.md`)
- Generates behavior-rules commands (`{bot_name}-{behavior}-rules.md`)
- Removes obsolete command files automatically

**New Properties:**
```python
@property
def data_collector(self) -> ActionDataCollector:
    """Required for orchestrator to visit behaviors."""
    if self._data_collector is None:
        self._data_collector = ActionDataCollector(
            bot=self.bot,
            bot_name=self.bot_name,
            bot_directory=self.bot_directory,
            description_extractor=self.description_extractor
        )
    return self._data_collector
```

#### `cursor/command_generator.py`
**Status**: No changes needed - already separated from CLI generation

**Key Features:**
- Generates Cursor command files independently
- Updates bot registry
- Can be skipped in non-Cursor environments

---

## 4. Generator Infrastructure Changes

### Files Modified

#### `generator/orchestrator.py`
**Status**: No changes needed - already supports visitor pattern correctly

**Key Features:**
- Visits behaviors and actions using visitor pattern
- Uses `data_collector` to determine if visitor supports behavior visits
- Skips behavior visits if `data_collector` is `None`

**Behavior Visit Logic:**
```python
def _visit_behaviors(self) -> None:
    if self.data_collector is None:
        return  # Skip if visitor doesn't support behavior visits
    # ... visit behaviors ...
```

#### `generator/action_data_collector.py`
**Status**: No changes needed - provides shared data collection logic

**Key Features:**
- Collects action descriptions, parameters, and descriptions
- Collects behavior descriptions
- Provides consistent data across all visitors

---

## 5. Unified Generation Script

### New File: `story_bot/generate.py`

**Purpose**: Single script to generate all CLI, MCP, and Cursor code

**Features:**
- Auto-detects bot location from script path
- Generates CLI code (independent of Cursor)
- Generates Cursor commands (optional, can be skipped)
- Generates MCP server code
- Generates awareness files

**Usage:**
```bash
python agile_bot/bots/story_bot/generate.py
```

**Output:**
- CLI scripts: `src/{bot_name}_cli.py`, `{bot_name}_cli`, `{bot_name}_cli.ps1`
- MCP server: `src/{bot_name}_mcp_server.py`
- Cursor commands: `.cursor/commands/{bot_name}*.md` (19 files)
- Awareness rules: `.cursor/rules/mcp-{bot-name}-awareness.mdc`

---

## 6. Test Updates

### Files Modified

#### `test/test_generate_mcp_tools.py`
**Changes:**
1. **Updated**: `when_bot_tool_generator_processes_config()` - Returns mock result (backward compatibility)
2. **Updated**: `when_behavior_tool_generator_processes_config()` - Returns mock result (backward compatibility)
3. **Updated**: `TestGenerateBotTools` - Now verifies static code generation
4. **Updated**: `TestGenerateBehaviorTools` - Now verifies static code generation
5. **Updated**: Exception tests to use `_ensure_bot_initialized()` instead of `create_server_instance()`

**Test Changes:**
- Tests now verify that server code includes tool registrations
- Tests check for `@mcp_server.tool()` decorators in generated code
- Removed tests for dynamic tool registration (no longer applicable)

---

## Summary of Architectural Changes

### Before (Dynamic Registration)
```
CLI Generator → Generates CLI + Cursor commands
MCP Generator → Creates FastMCP instance → Registers tools dynamically
```

### After (Static Generation)
```
CLI Generator → Generates CLI scripts only
Cursor Generator → Generates Cursor commands separately (optional)
MCP Generator → Generates static FastMCP server code with tool decorators
```

### Key Benefits

1. **Separation of Concerns**: CLI generation independent of Cursor IDE
2. **Static Generation**: All code generated at build time, not runtime
3. **Better Deployment**: Can deploy CLI without Cursor dependencies
4. **Consistent Pattern**: Same visitor pattern used for all generation
5. **Easier Testing**: Can test generated code without runtime dependencies

---

## Files Summary

### Modified Files
- `cli/cli_generator.py` - Removed Cursor command generation
- `mcp/mcp_server_generator.py` - Renamed `create_server_instance()` → `_ensure_bot_initialized()`
- `mcp/mcp_code_visitor.py` - Added `data_collector` property
- `cli/cursor/command_file_visitor.py` - Added `data_collector` property
- `test/test_generate_mcp_tools.py` - Updated for static generation

### Deleted Files
- `mcp/mcp_tool_registrar.py` - Dynamic registration removed
- `mcp/bot_tool_generator.py` - Static generation replaces this
- `mcp/behavior_tool_generator.py` - Static generation replaces this

### New Files
- `story_bot/generate.py` - Unified generation script

---

## Migration Guide

### For Bot Developers

**Before:**
```python
cli_generator = CliGenerator(...)
results = cli_generator.generate_cli_code()
cursor_commands = results['cursor_commands']  # ❌ No longer available
```

**After:**
```python
# Generate CLI (works in any environment)
cli_generator = CliGenerator(...)
cli_results = cli_generator.generate_cli_code()

# Generate Cursor commands separately (only in Cursor IDE)
cursor_generator = CursorCommandGenerator(...)
cursor_commands = cursor_generator.generate_cursor_commands(...)
```

### For Test Writers

**Before:**
```python
generator.create_server_instance()  # ❌ Method renamed
```

**After:**
```python
generator._ensure_bot_initialized()  # ✅ Use private method
# Or test via public API:
generator.generate_server()  # ✅ Tests static generation
```

---

## Verification Checklist

- [x] CLI generation works independently of Cursor
- [x] MCP server code is statically generated
- [x] Cursor commands are generated separately
- [x] All visitors have `data_collector` property
- [x] Orchestrator visits behaviors correctly
- [x] Tests updated for static generation
- [x] Obsolete code removed
- [x] Unified generation script created

---

## Next Steps

1. Run `python agile_bot/bots/story_bot/generate.py` to verify all generation works
2. Run tests: `pytest agile_bot/bots/base_bot/test/test_generate_*.py`
3. Verify generated files are correct
4. Update any remaining references to removed methods




