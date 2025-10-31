# Behavior Structure Feature

The **Behavior Structure** feature standardizes how AI behaviors are organized, named, and related. It ensures consistency and discoverability across all behaviors.

## Implementation

The behavior structure is implemented according to `behavior-structure-rule.mdc`:

### Rule Compliance

**Always:**
- ✅ Name files using `<feature>-<behavior-name>-<type>.<ext>` pattern
- ✅ For rules with multiple commands, add a verb suffix: `<feature>-<behavior-name>-<verb>-cmd.md`
- ✅ Keep each behavior in its own folder under `features/<feature>/cursor/`
- ✅ Link related files by prefix (same `<feature>-<behavior-name>` prefix)
- ✅ Rules must reference the commands that execute them: `**Executing Commands:**`
- ✅ Commands must reference rules, code, AI usage, and code usage
- ✅ Rules must start with `**When** <event> condition,`
- ✅ Include a short description at the top of every rule and command file

**Never:**
- ✅ Mix unrelated behaviors in the same folder
- ✅ Use ambiguous names like `new-rule.mdc` or `temp-cmd.md`
- ✅ Leave files undocumented or unreferenced

### Naming Patterns

* Rules: `<feature>-<behavior-name>-rule.mdc` (no verb suffix)
* Commands: `<feature>-<behavior-name>-cmd.md` OR `<feature>-<behavior-name>-<verb>-cmd.md` (e.g., `validate-cmd.md`, `fix-cmd.md`)
* Code: `<feature>-<behavior-name>-cmd.py` OR `<feature>-<behavior-name>-<verb>-cmd.py`
* MCP: `<feature>-<tool-name>-mcp.json`

### Relationship Sections

**Rules** must include:
- `**Executing Commands:**` section listing which commands execute the rule (e.g., `\behavior-structure validate`, `\behavior-structure fix`)

**Commands** must include:
- `**Rule:**` — Which rule this command follows
- `**Implementation:**` — Code functions this command calls
- `**AI Usage:**` — When to use AI assistance
- `**Code Usage:**` — When to use code execution

### Actions

The behavior structure command supports three actions:

#### 1. Validate

Checks structure compliance:
- File names follow naming pattern
- Rule-command linkages exist
- Relationship sections are present
- Rules start with `**When**`
- Related files share consistent prefixes

```bash
# Validate all behaviors
python behavior-structure-cmd.py validate

# Validate specific feature
python behavior-structure-cmd.py validate <feature>
```

#### 2. Fix

Automatically fixes structure issues:
- Creates missing command files for existing rules
- Creates missing implementation files for existing commands
- Adds missing relationship sections to rules and commands
- Adds basic documentation headers to empty files

```bash
# Fix all behaviors
python behavior-structure-cmd.py fix

# Fix specific feature
python behavior-structure-cmd.py fix <feature>
```

#### 3. Create

Scaffolds a new behavior with all required files:
- Rule file with When/then structure
- Command file with relationship sections
- Implementation file (optional with `--no-implementation` flag)

```bash
# Create new behavior (with Python implementation)
python behavior-structure-cmd.py create <feature> <behavior-name>

# Create AI-only behavior (no Python file)
python behavior-structure-cmd.py create <feature> <behavior-name> --no-implementation
```

### File Structure

```
features/<feature>/cursor/
  ├── <behavior-name>-rule.mdc
  ├── <behavior-name>-validate-cmd.md  ← Multiple commands for same rule
  ├── <behavior-name>-fix-cmd.md
  ├── <behavior-name>-create-cmd.md
  └── <behavior-name>-cmd.py
```

### Multiple Commands Per Rule

When a rule has multiple commands (e.g., validate, fix, create), use verb suffixes:
- `behavior-structure-rule.mdc` relates to:
  - `behavior-structure-validate-cmd.md`
  - `behavior-structure-fix-cmd.md`
  - `behavior-structure-create-cmd.md`

The validation uses prefix-based matching to link rules with multiple commands.

### Index Files

Index files (`behavior-index.json`) are stored in `features/<feature>/behavior-index.json` (not in `cursor/`) and are excluded from validation.

## Related Files

- `behavior-structure-rule.mdc` - The rule definition
- `behavior-structure-validate-cmd.md` - Validate command documentation
- `behavior-structure-fix-cmd.md` - Fix command documentation
- `behavior-structure-create-cmd.md` - Create command documentation
- `behavior-structure-cmd.py` - Implementation
