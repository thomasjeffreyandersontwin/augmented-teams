## Command: create-command [command_name] [domain]

Creates a Cursor command and its supporting code function.

**Args:**
- `command_name` (required) - Name of the command (without extension). Filename becomes the Cursor command name.
- `domain` (optional) - Domain folder name (ex: "testing", "development approach"). Defaults to determining from context.

**Usage:**
```bash
create-command mamba-debug testing
create-command playwright-debug testing
```

**What it creates:**
1. **Cursor command file** - `[domain]/[command_name].md` markdown file containing:
   - `## Command: [name] [args]` - Command header with name and parameters
   - Description of what the command does
   - **Args:** section listing all parameters with descriptions
   - **Usage:** section showing how to invoke the command (usually `python commands/[name].py`)
   - **Examples:** concrete usage examples
   - **Features:** key capabilities of the command
   - **Related Rules:** links to relevant rules files
   - **Integration:** how it works with config files, MCP tools, etc.

2. **Command function code** - `commands/[command_name].py` or `[domain]/[command_name].py` executable script that actually runs the command

**Placement:**
- **Command files** (`.md`): Domain folder (ex: `testing/mamba-debug.md` = Cursor command `mamba-debug`)
- **Code functions** (`.py`): 
  - Global utilities → `commands/[name].py`
  - Domain-specific → `[domain]/[name].py`

**Function code structure:**
- Python module (`.py`)
- Main function handling `sys.argv` or `argparse`
- Console output for success/failure
- Error handling

**Related Rules:**
- `development approach/command-automation.mdc` - Guidelines for building command functions

**Examples:**
- `create-command mamba-debug testing` → `testing/mamba-debug.md` + `testing/mamba-debug.py`
- `create-command playwright-debug testing` → `testing/playwright-debug.md` + `testing/playwright-debug.mjs` (Playwright stays JS)
- `create-command api-test api` → `api/api-test.md` + `api/api-test.py`


