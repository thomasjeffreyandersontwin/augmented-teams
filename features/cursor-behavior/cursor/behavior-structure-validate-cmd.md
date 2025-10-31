### Command: `behavior-structure-validate-cmd.md`

**Purpose:** Validate AI behaviors for structure and naming convention compliance.

**Usage:**
* `\behavior-structure validate` — validate all behaviors for structure compliance
* `\behavior-structure validate <feature>` — validate one feature's behaviors

**What It Checks:**
1. File names follow `<feature>-<behavior-name>-<type>.<ext>` pattern
2. Rule-command linkages exist (rules have matching commands - rules can relate to multiple commands with same prefix)
3. **Relationship sections** (documentation that links rules, commands, and code):
   * Rules must list commands that execute them: `**Executing Commands:**`
   * Commands must reference:
     - `**Rule:**` — Which rule this command follows
     - `**Implementation:**` — Code functions this command calls
     - `**AI Usage:**` — When to use AI assistance
     - `**Code Usage:**` — When to use code execution
4. Files are documented with proper headers
5. Related files share consistent naming prefixes
6. Rules must start with `**When** <event> condition,`
7. Index files (`behavior-index.json`) are excluded from validation

**Output:**
* List of structure violations with details
* Missing relationships (rules without commands, etc.)
* Naming inconsistencies
* Documentation issues

**File Structure Requirements:**
* All behavior files must be in `features/<feature>/cursor/`
* Related files must share the same `<feature>-<behavior-name>` prefix
* Rules can relate to multiple commands (e.g., `behavior-structure-rule.mdc` relates to `behavior-structure-validate-cmd.md`, `behavior-structure-fix-cmd.md`, etc.)
* Index files (`behavior-index.json`) are stored in `features/<feature>/behavior-index.json` (not in cursor/)

**Naming Patterns:**
* Rules: `<feature>-<behavior-name>-rule.mdc`
* Commands: `<feature>-<behavior-name>-cmd.md`
* Code: `<feature>-<behavior-name>-cmd.py`
* MCP: `<feature>-<tool-name>-mcp.json`

**Relationship Sections Explained:**
These are documentation sections that create clear links between rules, commands, and code:

* **Rules** must include `**Executing Commands:**` section listing which commands execute the rule (e.g., `\behavior-structure validate`, `\behavior-structure fix`)
* **Commands** must include:
  * `**Rule:**` — Which rule this command follows (e.g., `\behavior-structure-rule`)
  * `**Implementation:**` — Code functions this command calls (e.g., `behavior_structure()` function)
  * `**AI Usage:**` — When to use AI assistance (e.g., for reviewing results, determining purposes)
  * `**Code Usage:**` — When to use code execution (e.g., for file operations, validation logic)

