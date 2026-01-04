# Validation Status - tests
Started: 2026-01-02 20:23:18
Files: 32

## no_defensive_code_in_tests
**test_perform_behavior_action.py** - 5 violation(s)

[X] ERROR (line 4367)
Line 4367: CRITICAL - Variable truthiness check - test should fail if variable is None/empty. Guard clauses are FORBIDDEN in tests. Assume test code works - if setup is wrong, let the test fail. Remove the guard clause.

[X] ERROR (line 4369)
Line 4369: CRITICAL - Variable truthiness check - test should fail if variable is None/empty. Guard clauses are FORBIDDEN in tests. Assume test code works - if setup is wrong, let the test fail. Remove the guard clause.

[X] ERROR (line 4367)
Line 4367: CRITICAL - Guard clause detected. Guard clauses are FORBIDDEN in tests. Assume test code works correctly - if setup is wrong, let the test fail. Remove defensive checks.

[X] ERROR (line 4369)
Line 4369: CRITICAL - Guard clause detected. Guard clauses are FORBIDDEN in tests. Assume test code works correctly - if setup is wrong, let the test fail. Remove defensive checks.

[X] ERROR (line 4916)
Line 4916: CRITICAL - Guard clause detected. Guard clauses are FORBIDDEN in tests. Assume test code works correctly - if setup is wrong, let the test fail. Remove defensive checks.

---

## call_production_code_directly
**conftest.py** - 4 violation(s)

[X] ERROR (line 97)
Line 97 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 101)
Line 101 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 104)
Line 104 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 183)
Line 183 uses fake/stub implementation - tests should call real production code directly

---

## call_production_code_directly
**test_formatters.py** - 8 violation(s)

[X] ERROR (line 134)
Line 134 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 139)
Line 139 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 143)
Line 143 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 149)
Line 149 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 157)
Line 157 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 162)
Line 162 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 167)
Line 167 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 172)
Line 172 uses fake/stub implementation - tests should call real production code directly

---

## call_production_code_directly
**test_generate_mcp_tools.py** - 14 violation(s)

[X] ERROR (line 1192)
Line 1192 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 1193)
Line 1193 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 1194)
Line 1194 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 1195)
Line 1195 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 1537)
Line 1537 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 1539)
Line 1539 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 1541)
Line 1541 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 1543)
Line 1543 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 1549)
Line 1549 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 1555)
Line 1555 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 1579)
Line 1579 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 1593)
Line 1593 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 1595)
Line 1595 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 1601)
Line 1601 uses fake/stub implementation - tests should call real production code directly

---

## call_production_code_directly
**test_perform_behavior_action.py** - 1 violation(s)

[X] ERROR (line 1697)
Test method 'test_behavior_requires_actions_workflow_json_no_fallback' (line 1697) is empty or only contains TODO comments. Tests must call production code directly from src folder, even if the code doesn't exist yet. The test should fail with ImportError or AttributeError if production code is missing.

---

