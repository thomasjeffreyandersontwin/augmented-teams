### Command: `behavior-structure-fix-cmd.md`

**Purpose:** Automatically fix structure and naming convention issues in AI behaviors.

**Usage:**
* `\behavior-structure fix` — automatically fix structure issues across all features
* `\behavior-structure fix <feature>` — fix issues in one feature

**What It Fixes:**
1. Creates missing Behavior Feature outline files (`<feature>-outline.md`) with template structure based on existing behaviors
2. Creates missing command files for existing rules (with all required sections including Steps)
3. Creates missing implementation files for existing commands
4. Adds basic documentation headers to empty files
5. Adds missing relationship sections:
   * Rules: `**Executing Commands:**` section
   * Commands: `**Rule:**`, `**Implementation:**`, `**AI Usage:**`, `**Code Usage:**`, and `**Steps:**` sections (adds placeholder Steps if missing)
6. Fixes rule format to ensure it starts with `**When** <event> condition,`
7. Suggests renames for files with invalid naming patterns

**Behavior Features Organization:**
* All files are organized in Behavior Features (`features/<feature>/cursor/`) - collections of tightly-knit, strongly related behaviors
* Files belonging to the same feature are kept together in one directory
* Never scatter behaviors into separate areas or break them up by component type

**What It Does NOT Fix (Requires Manual AI Review):**
* Steps that don't specify who/what performs them — The AI agent must manually update steps to include performers (e.g., "The AI agent...", "The code function...", "The user...")

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
* File I/O to create and fix behavior files
* Pattern matching and validation logic
* Template generation for missing files

**Steps:**
1. The code function `behavior_structure(action="fix")` validates structure and identifies fixable issues
2. The code function creates missing command files for existing rules (with template sections)
3. The code function creates missing implementation files for existing commands (with template code)
4. The code function adds missing relationship sections to rules (e.g., `**Executing Commands:**`)
5. The code function adds missing relationship sections to commands (e.g., `**Rule:**`, `**Implementation:**`, `**AI Usage:**`, `**Code Usage:**`, `**Steps:**`)
6. The code function fixes rule format to ensure it starts with `**When** <event> condition,`
7. The code function reports what was fixed and what requires manual attention (e.g., file renames)
8. The AI agent reviews the fix results and handles issues that couldn't be auto-fixed (e.g., steps that don't specify performers)

**Output Integration:**
* When `behavior_structure()` runs with action="fix" and generates results, the AI should automatically:
  1. Check the command output for fix results
  2. Present a summary of fixes applied to the user in the chat window:
     - Number of files created
     - Number of issues fixed
     - List of files that were created or modified
  3. Highlight any issues that require manual attention (e.g., files that need manual renaming)
  4. Suggest next steps (e.g., run `\behavior-index` to update the index, or review the fixed files)
* The AI should present fix results immediately after the command completes to inform the user of changes made