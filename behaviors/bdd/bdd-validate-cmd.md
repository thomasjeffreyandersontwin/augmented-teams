### Command: `bdd-behavior-validate-cmd.md`

**Purpose:** Validate actual BDD test files against BDD principles (readable language, comprehensive coverage, proper structure, etc.)

**Usage:**
* `\bdd-validate` — Validate currently open test file against BDD principles
* `\bdd-validate <file-path>` — Validate specific test file
* `python behaviors/bdd-behavior/bdd-behavior-validate-cmd.py <file-path>` — Run validation from command line

**Rule:**
* `\bdd-rule` — Framework-agnostic BDD testing principles
* `\bdd-jest-rule` — Jest-specific BDD patterns
* `\bdd-mamba-rule` — Mamba-specific BDD patterns

**Valid Files** (uses same glob patterns as rules):
* **Jest**: `["**/*.test.js", "**/*.spec.js", "**/*.test.ts", "**/*.spec.ts", "**/*.test.jsx", "**/*.spec.jsx", "**/*.test.tsx", "**/*.spec.tsx", "**/*.test.mjs", "**/*.spec.mjs"]`
* **Mamba**: `["**/*_test.py", "**/test_*.py", "**/*_spec.py", "**/spec_*.py", "**/*_test.pyi", "**/test_*.pyi", "**/*_spec.pyi", "**/spec_*.pyi"]`
* **Any test file**: Matches glob patterns from `bdd-rule.mdc` (all of the above)

**Implementation:**
* `bdd_validate_test_file()` in `behaviors/bdd-behavior/bdd-validate-cmd.py` — Extracts and presents data
* **AI Agent (in conversation)** analyzes presented data and identifies violations

**Division of Labor:**
* **Code** extracts and presents data in focused chunks:
  - Test file structure (describe/it blocks with line numbers)
  - DO/DON'T examples organized by section (1-5)
  - Reference file examples (if `--thorough` mode)
  - Static issues (missing "should", `_private` calls, etc.)
* **AI Agent** (chat in conversation) analyzes the data:
  - Compares test chunks against DO/DON'T examples
  - Identifies BDD principle violations with line numbers
  - Suggests fixes using DO examples as templates
  - Reports findings to user

**Steps:**

1. **User** invokes validation via `\bdd-validate` (validates open file) or `\bdd-validate <file-path>` with optional `--thorough` flag
2. **Code** detects framework from file path patterns (Jest vs Mamba)
3. **Code** loads appropriate specialized rule file (bdd-jest-rule.mdc or bdd-mamba-rule.mdc)
4. **Code** extracts ALL DO/DON'T examples from rule, organized by section (1-5)
5. **Code** parses test file into describe/it structure chunks (to manage token limits for large files)
6. **Code** (if `--thorough`) loads detailed examples from reference file
7. **Code** performs static checks (naming patterns, structure issues)
8. **Code** presents extracted data to AI Agent:
   - Test chunks with line numbers
   - DO/DON'T examples organized by section
   - Reference examples (if thorough mode)
   - Static issues found
9. **AI Agent** (in conversation) reviews presented data:
   - Compares test code chunks against DO/DON'T examples
   - Identifies violations with specific line numbers
   - References which BDD principle was violated
   - Suggests fixes using DO examples
10. **AI Agent** reports findings to user with violations and suggested fixes
11. **User** decides next action (fix manually or ignore)

**Note on Data Extraction:** The command chunks large test files by `describe` blocks to stay under token limits while preserving context. The AI Agent then analyzes each chunk against BDD principles and reports violations.

**Example Output:**

```
============================================================
BDD Test Validation: UserService.test.js (Jest)
============================================================

❌ Line 5: describe('getUserById', ...) 
   Violation: Uses action verb instead of noun
   Fix: Use "a user" or "user retrieval" instead of "getUserById"
   Reference: bdd-jest-rule.mdc § 1. Business Readable Language

❌ Line 12: it('returns user', ...)
   Violation: Missing "should" prefix
   Fix: Start with "should return user when ID exists"
   Reference: bdd-jest-rule.mdc § 1. Business Readable Language

⚠️  Line 25: expect(service._validateToken).toHaveBeenCalled()
   Warning: Testing private method
   Suggestion: Test observable behavior, not internals
   Reference: bdd-jest-rule.mdc § 2. Comprehensive and Brief

✅ Line 40: Proper describe nesting (broad → specific)
✅ Line 50: Good use of beforeEach for setup
✅ Line 60: Tests normal and failure paths

============================================================
Validation Summary
============================================================
❌ 2 violations found
⚠️  1 warning
✅ 3 principles followed correctly
```

**Integration:**

This command can be integrated into:
- Pre-commit hooks to validate changes
- CI/CD pipelines for automated checking
- Development workflow as a manual check
- Sync process to validate before deployment

