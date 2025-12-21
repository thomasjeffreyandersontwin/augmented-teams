# Validation Status - code
Started: 2025-12-21 17:39:47
Files: 1

## avoid_excessive_guards
**code_scanner.py** - 1 violation(s)

[!] WARNING (line 75)
Line 75: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

---

## keep_classes_small_with_single_responsibility
**code_scanner.py** - 1 violation(s)

[!] WARNING (line 11)
Class "CodeScanner" is 471 lines - should be under 300 lines (extract related methods into separate classes)

---

## maintain_vertical_density
**code_scanner.py** - 3 violation(s)

[i] INFO (line 81)
Function "_extract_domain_terms" is 123 lines - consider improving vertical density by declaring variables near usage

[i] INFO (line 362)
Function "_extract_code_snippet" is 56 lines - consider improving vertical density by declaring variables near usage

[i] INFO (line 419)
Function "_create_violation_with_snippet" is 63 lines - consider improving vertical density by declaring variables near usage

---

## provide_meaningful_context
**code_scanner.py** - 7 violation(s)

[!] WARNING (line 385)
Line 385 uses numbered variable "start_line_0" - use meaningful descriptive name

[!] WARNING (line 389)
Line 389 uses numbered variable "end_line_0" - use meaningful descriptive name

[!] WARNING (line 392)
Line 392 uses numbered variable "end_line_0" - use meaningful descriptive name

[!] WARNING (line 398)
Line 398 uses numbered variable "start_line_0" - use meaningful descriptive name

[!] WARNING (line 400)
Line 400 uses numbered variable "end_line_0" - use meaningful descriptive name

[!] WARNING (line 402)
Line 402 uses numbered variable "end_line_0" - use meaningful descriptive name

[!] WARNING (line 395)
Line 395 uses numbered variable "end_line_0" - use meaningful descriptive name

---

## simplify_control_flow
**code_scanner.py** - 2 violation(s)

[!] WARNING (line 81)
Function "_extract_domain_terms" has nesting depth of 12 - use guard clauses and extract nested blocks to reduce nesting

[!] WARNING (line 362)
Function "_extract_code_snippet" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

---

## stop_writing_useless_comments
**code_scanner.py** - 6 violation(s)

[X] ERROR (line 12)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 82)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 206)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 219)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 283)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 304)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

---

## use_clear_function_parameters
**code_scanner.py** - 4 violation(s)

[!] WARNING (line 23)
Function "scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

[!] WARNING (line 253)
Function "scan_cross_file" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

[!] WARNING (line 362)
Function "_extract_code_snippet" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

[!] WARNING (line 419)
Function "_create_violation_with_snippet" has 12 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

---

## use_natural_english
**code_scanner.py** - 12 violation(s)

[i] INFO (line 385)
Variable "start_line_0" uses technical notation. Use natural English instead.

[i] INFO (line 389)
Variable "end_line_0" uses technical notation. Use natural English instead.

[i] INFO (line 392)
Variable "end_line_0" uses technical notation. Use natural English instead.

[i] INFO (line 398)
Variable "start_line_0" uses technical notation. Use natural English instead.

[i] INFO (line 408)
Variable "start_line_0" uses technical notation. Use natural English instead.

[i] INFO (line 409)
Variable "end_line_0" uses technical notation. Use natural English instead.

[i] INFO (line 392)
Variable "start_line_0" uses technical notation. Use natural English instead.

[i] INFO (line 400)
Variable "end_line_0" uses technical notation. Use natural English instead.

[i] INFO (line 402)
Variable "end_line_0" uses technical notation. Use natural English instead.

[i] INFO (line 395)
Variable "end_line_0" uses technical notation. Use natural English instead.

[i] INFO (line 402)
Variable "start_line_0" uses technical notation. Use natural English instead.

[i] INFO (line 395)
Variable "end_line_0" uses technical notation. Use natural English instead.

---

Completed: 2025-12-21 17:39:48
Total violations: 36
Scanners executed: 30
