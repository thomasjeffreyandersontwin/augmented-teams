### Command: `behavior-structure-create-cmd.md`

**Purpose:** Scaffold a new AI behavior with all required files and proper structure.

**Usage:**
* `\behavior-structure create <feature> <behavior-name>` — create a new behavior with all files
* `\behavior-structure create <feature> <behavior-name> --no-implementation` — create behavior without Python file (for AI-only behaviors)

**What It Creates:**
1. Rule file (`<feature>-<behavior-name>-rule.mdc`) with template
2. Command file (`<feature>-<behavior-name>-cmd.md`) with template
3. Implementation file (`<feature>-<behavior-name>-cmd.py`) with template (only if automation serves a purpose)
4. Proper documentation structure in each file
5. Cross-references between related files

**When to Use --no-implementation:**
* Use when the behavior is entirely AI-driven (no file operations, no automation needed)
* Examples: `behavior-suggest` (AI analyzes patterns), conversational behaviors
* The command file will note "No Python implementation needed — This is entirely AI-driven"

**Example:**
```bash
python behavior-structure-cmd.py create cursor-behavior test-behavior
```
Creates:
* `cursor-behavior-test-behavior-rule.mdc`
* `cursor-behavior-test-behavior-cmd.md`
* `cursor-behavior-test-behavior-cmd.py`

**Template Contents:**
* Rule file: When/then structure with Always/Never sections + `**Executing Commands:**` section
* Command file: Purpose, usage, steps + governance sections:
  * `**Rule:**` — Reference to rule this command follows
  * `**Implementation:**` — Reference to code function
  * `**AI Usage:**` — When to use AI assistance
  * `**Code Usage:**` — When to use code execution
* Implementation file: Function skeleton with Windows console encoding support

**Naming Pattern:**
* Files follow: `<feature>-<behavior-name>-<type>.<ext>`
* Function names: `<behavior_name>` (underscores, no hyphens)

**File Location:**
* All files created in `features/<feature>/cursor/`
* Directory created if it doesn't exist

