### Command: `behavior-index-cmd.md`

**Purpose:** Maintain an up-to-date index of all AI behaviors across features.

**Usage:**
* `\behavior-index` — rebuild the global index
* `\behavior-index <feature>` — rebuild the index for one feature

**File Types Indexed:**
* `.mdc` files (rules)
* `.md` files (commands)
* `.py` files (functions)
* `.json` files (MCP configs)

**Steps:**
1. Run `python features/cursor-behavior/cursor/behavior-index-cmd.py` to generate the index
2. The function scans all `features/*/cursor/` folders for behavior files
3. Detects changed or missing files
4. Skips draft or experimental behaviors
5. Records feature name, file type, path, modification timestamp, and extracted purpose
    6. Updates both local (`features/<feature>/behavior-index.json`) and global (`.cursor/behavior-index.json`) indexes
7. Prints summary with feature counts and last updated time
    8. **After the index is generated, review `.cursor/behavior-index.json` and determine appropriate one-liner purposes for any entries that have nonsensical or missing purposes**
    9. **Update the purpose field in the global index (`.cursor/behavior-index.json`) with clear, concise one-liner descriptions based on the file content**
    10. **After updating purposes in the global index, run `python features/cursor-behavior/cursor/behavior-index-cmd.py sync-purposes` to copy the updated purposes from global to all local index files (stored at `features/<feature>/behavior-index.json`)**
    11. **After indexing, consider running `\behavior-consistency` to validate for inconsistencies, overlaps, or contradictions in behaviors**

**Output:**
The index contains entries with:
* `feature` - Feature name
* `file` - File name
* `type` - File extension (.mdc, .md, .py, .json)
* `path` - Full file path
* `modified` - Modification timestamp

**Cursor Environment Integration:**
* The Cursor environment **must constantly refer to `.cursor/behavior-index.json` during chat** to discover and use available commands, rules, functions, and MCP configs.
* This ensures the AI assistant has visibility into all available behaviors across all features.
* The index serves as the single source of truth for what behaviors are available.



**Rule:**
* `\behavior-index-rule` — [description of rule this command follows]

**Implementation:**
* `behavior_index()` — [description of code function]

**AI Usage:**
* [When to use AI assistance - e.g., for complex reasoning, content generation, etc.]

**Code Usage:**
* [When to use code execution - e.g., for file operations, data processing, etc.]