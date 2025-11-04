### Command: `bdd-workflow-cmd.md`

**Purpose:** Guide developers through true BDD (Test-Driven Development) with the Red-Green-Refactor cycle for BDD tests.

**Usage:**
* `\BDD-workflow` — Start BDD workflow on current file (auto-creates test file if needed)
* `\BDD-workflow --scope describe` — Work on current describe block
* `\BDD-workflow --scope next:3` — Work on next 3 test signatures
* `\BDD-workflow --scope next:1` — Work on next single test
* `\BDD-workflow --scope all` — Work on all test signatures in file
* `\BDD-workflow --phase signatures` — Build test signatures only
* `\BDD-workflow --phase red` — Jump to RED phase (write failing test)
* `\BDD-workflow --phase green` — Jump to GREEN phase (implement code)
* `\BDD-workflow --phase refactor` — Jump to REFACTOR phase (suggest improvements)
* `python behaviors/bdd-behavior/bdd-workflow-cmd.py <file-path> [options]` — Run from command line

**Note:** Can be invoked on either test files or production files. If invoked on a production file, automatically creates corresponding test file.

**Rules:**
* `\bdd-workflow-rule` — Core BDD workflow (Red-Green-Refactor cycle)
* `\bdd-rule` — BDD principles (referenced throughout TDD cycle)
* `\bdd-jest-rule` — Jest-specific patterns
* `\bdd-mamba-rule` — Mamba-specific patterns

**Valid Files** (same as BDD behavior rules):
* **Jest**: `["**/*.test.js", "**/*.spec.js", "**/*.test.ts", "**/*.spec.ts", "**/*.test.jsx", "**/*.spec.jsx", "**/*.test.tsx", "**/*.spec.tsx", "**/*.test.mjs", "**/*.spec.mjs"]`
* **Mamba**: `["**/*_test.py", "**/test_*.py", "**/*_spec.py", "**/spec_*.py", "**/*_test.pyi", "**/test_*.pyi", "**/*_spec.pyi", "**/spec_*.pyi"]`

**Implementation:**
* `tdd_workflow()` in `behaviors/bdd-behavior/bdd-workflow-cmd.py` — Main orchestrator
* `is_test_file()` — Check if file matches test file patterns
* `generate_test_file_path()` — Generate test file path from production file path
* `parse_test_structure()` — Extract test signatures and implementation status
* `determine_test_scope()` — Filter tests by scope option
* `run_tests()` — Execute tests and capture results
* `identify_code_relationships()` — Find related code under test and test files

**AI Usage:**
* AI Agent creates test signatures during Phase 0 (SIGNATURES)
* AI Agent validates tests with `/bdd-validate` after EVERY phase
* AI Agent fixes ALL BDD violations before proceeding
* AI Agent implements test code during Phase 1 (RED)
* AI Agent implements production code during Phase 2 (GREEN)  
* AI Agent suggests refactorings during Phase 3a (REFACTOR)
* AI Agent implements approved refactorings during Phase 3b (IMPLEMENT)

**Code Usage:**
* Code parses test file structure and detects implementation status
* Code runs tests and captures pass/fail results
* Code tracks workflow state across sessions
* Code identifies code relationships and impacts

**Steps:**

1. **User** invokes `\bdd-workflow` on file (with optional scope and phase flags)
2. **Code** `tdd_workflow()` checks if file is a test file (matches glob patterns)
3. **IF NOT a test file**: 
   - **Code** `detect_framework_from_file()` detects framework from file extension (.mjs → Jest, .py → Mamba)
   - **Code** `generate_test_file_path()` creates corresponding test file path (e.g., `foo.mjs` → `foo.test.mjs`)
   - **Code** checks if test file already exists
   - **IF test file does NOT exist**: 
     - **Code** presents production file and proposed test file path to AI Agent
     - **AI Agent** creates initial test file structure with imports and basic describe block
     - **Code** saves new test file
   - **Code** switches context to the newly created/found test file
4. **Code** `detect_framework_from_file()` detects framework from file path (Jest vs Mamba)
5. **Code** `TDDWorkflowState()` loads or initializes workflow state from `.tdd-workflow/<filename>.state.json`
6. **Code** `parse_test_structure()` parses test file into describe/it blocks with implementation status
7. **Code** `determine_test_scope()` filters tests based on scope option (describe block, next N, all, line number)
8. **Code** identifies current phase from state or user-provided phase flag
9. **Code** presents test structure, scope, and workflow data to AI Agent

### Phase 0: Build Signatures

#### 0.1: Create Test File (if needed)
1. **IF test file does NOT exist** (invoked on production file):
   - **AI Agent** analyzes production file structure (classes, functions, modules)
   - **AI Agent** determines appropriate test file name (e.g., `foo.mjs` → `foo.test.mjs`)
   - **AI Agent** creates test file with:
     - Proper imports from production file
     - Framework-specific setup (Jest: `describe`, Mamba: `with describe`)
     - Top-level describe block matching module/class name
     - Empty body ready for test signatures
   - **AI Agent** saves new test file
   - **Code** confirms test file creation and switches context

#### 0.2: Build Test Signatures
1. **AI Agent** analyzes test structure and identifies missing test signatures in scope
2. **AI Agent** analyzes corresponding production code to understand functionality
3. **Code** `parse_test_structure()` identifies SAMPLE SIZE (one complete lower-level describe block) to start with
4. **AI Agent** creates SAMPLE test signatures for that describe block following `bdd-rule.mdc` § 1 (fluent language, proper nesting)
5. **MANDATORY**: **AI Agent** AUTOMATICALLY runs `/bdd-validate` on sample signatures (NO EXCEPTIONS)
6. **MANDATORY**: **AI Agent** fixes ALL violations before proceeding (VALIDATION MUST PASS)
7. **AI Agent** LEARNS patterns from violations to apply to next iteration
8. **AI Agent** creates ANOTHER sample describe block applying learned patterns
9. **MANDATORY**: **AI Agent** AUTOMATICALLY runs `/bdd-validate` on new sample (NO EXCEPTIONS)
10. **IF errors found**: LOOP back to step 6 (fix-learn-build-validate) - MUST achieve zero violations
11. **IF NO errors**: Expand to REST of signatures in scope, applying all learned patterns
12. **MANDATORY**: **AI Agent** AUTOMATICALLY runs `/bdd-validate` on complete set (NO EXCEPTIONS)
13. **MANDATORY**: **AI Agent** fixes ALL violations - PHASE CANNOT PROCEED WITH ANY VIOLATIONS
14. **AI Agent** ensures comprehensive coverage: normal, edge, and failure paths
15. **STOP**: If ANY violations remain, AI Agent MUST NOT proceed to step 16
16. **Code** `TDDWorkflowState.save()` updates workflow state with created signatures ONLY IF validation passes
17. **User** reviews test signatures and proceeds to Phase 1

### Phase 1: RED - Write Failing Test

1. **Code** `TDDWorkflowState.get_next_test()` identifies next unimplemented test in scope
2. **Code** presents test signature and context to AI Agent
3. **AI Agent** identifies SAMPLE SIZE (1-2 tests if multiple in scope)
4. **AI Agent** writes SAMPLE test implementation following `bdd-rule.mdc` § 2-5 (arrange/act/assert, helpers, mocking)
5. **MANDATORY**: **AI Agent** AUTOMATICALLY runs `/bdd-validate` on sample test (NO EXCEPTIONS)
6. **MANDATORY**: **AI Agent** fixes ALL violations before proceeding (VALIDATION MUST PASS)
7. **AI Agent** LEARNS patterns from violations to apply to next iteration
8. **IF more tests in scope**: Write ANOTHER test applying learned patterns
9. **MANDATORY**: **AI Agent** AUTOMATICALLY runs `/bdd-validate` on new test (NO EXCEPTIONS)
10. **IF errors found**: LOOP back to step 6 (fix-learn-build-validate) - MUST achieve zero violations
11. **IF NO errors and more tests remain**: Expand to REST of tests in scope, applying all learned patterns
12. **MANDATORY**: **AI Agent** AUTOMATICALLY runs `/bdd-validate` on all implemented tests (NO EXCEPTIONS)
13. **MANDATORY**: **AI Agent** fixes ALL violations - PHASE CANNOT PROCEED WITH ANY VIOLATIONS
14. **STOP**: If ANY violations remain, AI Agent MUST NOT proceed to step 15
15. **Code** `run_tests()` runs the test(s) and captures failure output
16. **Code** verifies failure reason (should be "not defined" error, not syntax error)
17. **Code** presents failure details to AI Agent
18. **AI Agent** confirms test(s) fail for RIGHT reason
19. **Code** `TDDWorkflowState.update_test_status()` marks test(s) as RED
20. **User** reviews failing test(s) and proceeds to Phase 2

### Phase 2: GREEN - Implement Minimal Code

1. **AI Agent** identifies SAMPLE SIZE (1 piece of functionality if implementation is large)
2. **AI Agent** writes SAMPLE minimal code under test to make current test(s) pass
3. **AI Agent** resists adding dependencies or features no test demands yet
4. **Code** `run_tests()` runs the test(s) to verify they pass
5. **Code** `run_tests()` runs ALL tests to check for regressions
6. **Code** presents test results to AI Agent
7. **AI Agent** verifies test(s) pass and no regressions occurred
8. **MANDATORY**: **AI Agent** AUTOMATICALLY runs `/bdd-validate` on tests (NO EXCEPTIONS)
9. **MANDATORY**: **AI Agent** fixes ALL violations before proceeding (VALIDATION MUST PASS)
10. **AI Agent** LEARNS patterns from violations
11. **IF more functionality needed**: Implement ANOTHER piece applying learned patterns
12. **MANDATORY**: **AI Agent** AUTOMATICALLY runs `/bdd-validate` after each piece (NO EXCEPTIONS)
13. **IF errors found**: LOOP back to step 9 (fix-learn-build-validate) - MUST achieve zero violations
14. **IF NO errors**: Complete remaining implementation applying all learned patterns
15. **MANDATORY**: **AI Agent** AUTOMATICALLY runs `/bdd-validate` on all tests (NO EXCEPTIONS)
16. **MANDATORY**: **AI Agent** fixes ALL violations - PHASE CANNOT PROCEED WITH ANY VIOLATIONS
17. **STOP**: If ANY violations remain, AI Agent MUST NOT proceed to step 18
18. **Code** `TDDWorkflowState.update_test_status()` marks test(s) as GREEN ONLY IF validation passes
19. **User** (optional) commits changes: `git commit -m "Make test X pass"`
20. **User** decides to proceed to Phase 3a or skip to next test

### Phase 3a: REFACTOR - Suggest Improvements

1. **Code** `identify_code_relationships()` finds code under test files and test files related to current code
2. **Code** parses code under test and presents to AI Agent
3. **MANDATORY**: **AI Agent** AUTOMATICALLY runs `/bdd-validate` to ensure current tests follow BDD principles before refactoring (NO EXCEPTIONS)
4. **MANDATORY**: **AI Agent** fixes ALL violations before suggesting refactorings (VALIDATION MUST PASS)
5. **STOP**: If ANY violations remain, AI Agent MUST fix them before proceeding to refactoring suggestions
6. **AI Agent** LEARNS patterns from violations
7. **AI Agent** identifies SAMPLE code smell area (1-2 related smells)
8. **AI Agent** analyzes SAMPLE area thoroughly
9. **AI Agent** suggests specific refactorings for sample with WHAT to change and WHY
10. **IF more code areas to analyze**: Analyze ANOTHER area applying learned patterns
11. **AI Agent** identifies additional code smells (duplication, long methods, magic values, poor names)
12. **AI Agent** suggests comprehensive refactorings with WHAT to change and WHY
13. **AI Agent** lists impacted code under test files
14. **AI Agent** lists impacted test files that need updates
15. **AI Agent** explains trade-offs for each suggested refactoring
16. **User** reviews suggestions and approves which to implement (1, 2, all, skip)

### Phase 3b: IMPLEMENT - Apply Refactorings

1. **AI Agent** implements ONE approved refactoring (SAMPLE)
2. **Code** `run_tests()` runs ALL tests after the refactoring
3. **Code** presents test results to AI Agent
4. **AI Agent** verifies all tests still pass (refactoring didn't break anything)
5. **AI Agent** runs `/bdd-validate` to ensure tests maintain BDD quality
6. **AI Agent** fixes violations
7. **AI Agent** LEARNS patterns from violations and refactoring impact
8. **IF more refactorings approved**: Implement ANOTHER refactoring applying learned patterns
9. **IF errors found**: LOOP back to step 6 (fix-learn-apply-validate)
10. **IF NO errors**: Complete remaining approved refactorings applying all learned patterns
11. **AI Agent** runs `/bdd-validate` on final state
12. **AI Agent** fixes any remaining violations
13. **User** (optional) commits: `git commit -m "Refactor: <description>"`
14. **Code** marks all refactorings as complete
15. **User** finishes refactoring and proceeds to next test

### Repeat Cycle

1. **Code** `TDDWorkflowState.get_next_test()` identifies next unimplemented test in scope
2. **Repeat** Phase 1 through Phase 3 until all tests in scope are implemented
3. **Code** `TDDWorkflowState.save()` updates state to completed
4. **User** decides next action: expand scope, start new feature, or finish session

---
REFACTORING SUGGESTIONS for UserService.authenticate():


## Workflow States

The command tracks workflow state in the test file as comments:

```javascript
// BDD-WORKFLOW-STATE: phase=red, scope=describe, test=2/5
describe('user authentication', () => {
  it('should return token when credentials are valid', () => {
    // BDD: IMPLEMENTED (GREEN)
    // ...
  });
  
  it('should throw error when credentials are invalid', () => {
    // BDD: NEXT (RED)
    // TODO: implement
  });
});
```

State markers:
* `BDD: SIGNATURE` — Test signature created, not implemented
* `BDD: RED` — Test written, currently failing
* `BDD: GREEN` — Test passing, code implemented
* `BDD: REFACTOR` — Ready for refactoring suggestions
* `BDD: NEXT` — Next test to implement

---


## Command Options

### Scope Options

* `--scope describe` (default) — Work on all tests in current describe block
* `--scope next:N` — Work on next N tests (e.g., `next:1`, `next:3`)
* `--scope all` — Work on all test signatures in file
* `--scope line:N` — Work on test at specific line number

### Phase Options

* `--phase signatures` — Only create test signatures
* `--phase red` — Jump to RED phase (skip signatures)
* `--phase green` — Jump to GREEN phase (assumes tests are failing)
* `--phase refactor` — Jump to REFACTOR phase (assumes tests passing)

### Mode Options

* `--auto` — Automatic mode (proceed through phases without prompting)
* `--interactive` (default) — Prompt for approval at each phase
* `--suggest-only` — Only suggest refactorings, don't implement

### Example Usage

```bash
# Start BDD workflow on current file (auto-creates test file if needed)
\BDD-workflow

# Start BDD workflow on production file (creates UserService.test.js)
# Open UserService.js, then:
\BDD-workflow --scope all --phase signatures

# Work on next 3 tests in auto mode
\BDD-workflow --scope next:3 --auto

# Just build test signatures for entire file
\BDD-workflow --scope all --phase signatures

# Jump to refactor phase for current test
\BDD-workflow --phase refactor

# Command line usage on test file
python behaviors/bdd-behavior/bdd-workflow-cmd.py src/auth/AuthService.test.js --scope describe

# Command line usage on production file (auto-creates test file)
python behaviors/bdd-behavior/bdd-workflow-cmd.py src/auth/AuthService.js --scope all

# Interactive with thorough refactoring suggestions
python behaviors/bdd-behavior/bdd-workflow-cmd.py src/auth/AuthService.test.js --interactive --suggest-only
```

---

## Integration

This command integrates with:
* **BDD Validation** (`\bdd-validate`) — MANDATORY validation after every phase to ensure tests follow BDD principles
* **CRITICAL**: AI Agent MUST run `/bdd-validate` and fix ALL violations before proceeding to next phase


## Implementation

**Files:**
* `behaviors/bdd-behavior/bdd-workflow-cmd.py` — Main command implementation
* `behaviors/bdd-behavior/bdd-workflow-rule.mdc` — Core BDD workflow rule
* `behaviors/bdd-workflow-jest-rule.mdc` — Jest-specific patterns
* `behaviors/bdd-workflow-mamba-rule.mdc` — Mamba-specific patterns

**Division of Labor:**
* **Code**: File parsing, test running, state tracking, result capture
* **AI Agent**: Test writing, code implementation, refactoring suggestions
* **AI Agent (MANDATORY)**: Run `/bdd-validate` after EVERY phase, fix ALL violations before proceeding

**State Management:**
* Test file comments track current phase and progress
* Separate state file (`.BDD-workflow-state.json`) tracks overall workflow state
* State persists across sessions for long workflows

#   T e s t   c h a n g e  
 