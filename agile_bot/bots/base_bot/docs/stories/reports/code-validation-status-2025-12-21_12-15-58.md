# Validation Status - code
Started: 2025-12-21 12:15:58
Files: 223

## avoid_excessive_guards
**actions.py** - 1 violation(s)

[!] WARNING (line 155)
Line 155: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**behaviors.py** - 2 violation(s)

[!] WARNING (line 247)
Line 247: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 251)
Line 251: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**code_scanner.py** - 1 violation(s)

[!] WARNING (line 75)
Line 75: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**cover_all_paths_scanner.py** - 1 violation(s)

[!] WARNING (line 43)
Line 43: Variable truthiness check detected (if has_code:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**scanner_orchestrator.py** - 1 violation(s)

[!] WARNING (line 75)
Line 75: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**violation.py** - 1 violation(s)

[!] WARNING (line 82)
Line 82: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## avoid_excessive_guards
**file_link_builder.py** - 2 violation(s)

[!] WARNING (line 27)
Line 27: Variable truthiness check detected (if not is_absolute:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 52)
Line 52: Variable truthiness check detected (if line_number:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**rules.py** - 2 violation(s)

[!] WARNING (line 43)
Line 43: Variable truthiness check detected (if has_scope_in_params:). Assume variable exists - let code fail fast if missing.

[!] WARNING (line 97)
Line 97: Variable truthiness check detected (if changed:). Assume variable exists - let code fail fast if missing.

---

## avoid_excessive_guards
**block.py** - 5 violation(s)

[!] WARNING (line 96)
Line 96: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 109)
Line 109: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 122)
Line 122: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 136)
Line 136: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

[!] WARNING (line 150)
Line 150: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---



## ERROR

Validation failed with error: CodeScanner.scan_cross_file() got an unexpected keyword argument 'all_test_files'
