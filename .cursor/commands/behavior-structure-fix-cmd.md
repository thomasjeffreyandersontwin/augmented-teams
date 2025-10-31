### Command: `behavior-structure-fix-cmd.md`

**Purpose:** Automatically fix structure and naming convention issues in AI behaviors.

**Usage:**
* `\behavior-structure fix` — automatically fix structure issues across all features
* `\behavior-structure fix <feature>` — fix issues in one feature

**What It Fixes:**
1. Creates missing command files for existing rules
2. Creates missing implementation files for existing commands
3. Adds basic documentation headers to empty files
4. Adds governance sections to rules (Executing Commands) and commands (Rule, Implementation, AI Usage, Code Usage)
5. Suggests renames for files with invalid naming patterns

**Output:**
* List of files created
* List of files fixed
* Manual action required warnings (for renames that can't be auto-fixed)

**Safety:**
* Automatically creates missing linked files
* Adds documentation templates where missing
* Does not rename files automatically (requires manual confirmation)
* Preserves existing file content when adding documentation

**Example Fixes:**
* If `behavior-sync-rule.mdc` exists but `behavior-sync-cmd.md` is missing → creates the command file with template
* If `behavior-index-cmd.md` exists but `behavior-index-cmd.py` is missing → creates the implementation file with template
* Empty or undocumented files → adds basic documentation structure



**Rule:**
* `\behavior-structure-fix-rule` — [description of rule this command follows]

**Implementation:**
* `behavior_structure_fix()` — [description of code function]

**AI Usage:**
* [When to use AI assistance - e.g., for complex reasoning, content generation, etc.]

**Code Usage:**
* [When to use code execution - e.g., for file operations, data processing, etc.]