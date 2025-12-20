# Validation Status - tests
Started: 2025-12-20 15:39:34
Files: 1

## call_production_code_directly
**test_invoke_cli.py** - 2 violation(s)

[X] ERROR (line 431)
Line 431 uses fake/stub implementation - tests should call real production code directly

[X] ERROR (line 674)
Line 674 uses fake/stub implementation - tests should call real production code directly

---

## match_specification_scenarios
**test_invoke_cli.py** - 14 violation(s)

[!] WARNING (line 573)
Test "test_trigger_bot_only_no_behavior_or_action_specified" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Trigger bot only (no behavior or action specified)
        GIVEN: user types mess...

[!] WARNING (line 598)
Test "test_trigger_bot_and_behavior_no_action_specified" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Trigger bot and behavior (no action specified)
        GIVEN: user types message ...

[!] WARNING (line 618)
Test "test_trigger_bot_behavior_and_action_explicitly" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Trigger bot, behavior, and action explicitly
        GIVEN: user types message co...

[!] WARNING (line 639)
Test "test_trigger_close_current_action" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Trigger close current action
        GIVEN: user types message containing close t...

[!] WARNING (line 693)
Test "test_cli_returns_generic_description_for_unknown_command" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: CLI returns generic description when parameter description cannot be inferred
   ...

[!] WARNING (line 803)
Test "test_priority_property_returns_configured_priority_or_zero" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Priority property returns configured priority or zero
        GIVEN: BehaviorConf...

[!] WARNING (line 824)
Test "test_matches_returns_true_when_text_matches_any_pattern" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches returns true when text matches any pattern
        GIVEN: BehaviorConfig ...

[!] WARNING (line 841)
Test "test_matches_returns_false_when_no_patterns_match" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches returns false when no patterns match
        GIVEN: BehaviorConfig with p...

[!] WARNING (line 858)
Test "test_matches_returns_false_when_no_triggers_configured" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches returns false when no triggers configured
        GIVEN: BehaviorConfig w...

[!] WARNING (line 875)
Test "test_matches_works_with_list_trigger_format" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches works with list trigger format
        GIVEN: BehaviorConfig with list tr...

[!] WARNING (line 892)
Test "test_matches_checks_all_patterns_until_match_found" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches checks all patterns until match found
        GIVEN: BehaviorConfig with ...

[!] WARNING (line 909)
Test "test_matches_handles_regex_patterns" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches handles regex patterns
        GIVEN: BehaviorConfig with regex pattern '...

[!] WARNING (line 926)
Test "test_matches_is_case_insensitive" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches is case insensitive
        GIVEN: BehaviorConfig with pattern 'TEST'
   ...

[!] WARNING (line 943)
Test "test_matches_handles_invalid_regex_patterns_by_falling_back_to_literal" has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches handles invalid regex patterns by falling back to literal
        GIVEN: ...

---

## place_imports_at_top
**test_invoke_cli.py** - 7 violation(s)

[X] ERROR (line 26)
Import statement found at line 26 after non-import code. Move all imports to the top of the file.

[X] ERROR (line 30)
Import statement found at line 30 after non-import code. Move all imports to the top of the file.

[X] ERROR (line 33)
Import statement found at line 33 after non-import code. Move all imports to the top of the file.

[X] ERROR (line 34)
Import statement found at line 34 after non-import code. Move all imports to the top of the file.

[X] ERROR (line 719)
Import statement found at line 719 after non-import code. Move all imports to the top of the file.

[X] ERROR (line 720)
Import statement found at line 720 after non-import code. Move all imports to the top of the file.

[X] ERROR (line 721)
Import statement found at line 721 after non-import code. Move all imports to the top of the file.

---

## self_documenting_tests
**test_invoke_cli.py** - 87 violation(s)

[X] ERROR (line 41)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 54)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 74)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 89)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 103)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 113)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 120)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 131)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 138)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 149)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 161)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 173)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 201)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 223)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 237)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 241)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 252)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 271)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 280)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 300)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 310)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 316)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 322)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 328)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 336)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 343)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 364)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 401)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 434)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 473)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 482)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 486)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 491)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 504)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 516)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 526)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 538)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 545)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 562)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 571)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 574)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 599)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 619)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 640)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 672)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 681)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 691)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 694)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 725)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 735)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 742)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 749)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 755)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 760)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 765)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 770)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 779)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 782)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 793)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 804)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 822)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 825)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 842)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 859)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 876)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 893)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 910)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 927)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 944)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

[X] ERROR (line 36)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 38)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 245)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 247)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 282)
Useless comment: "# Create or update behavior.json file with trigger words (RE" - delete it or improve the code instead

[X] ERROR (line 290)
Useless comment: "# Update trigger_words in behavior.json (router reads from b" - delete it or improve the code instead

[X] ERROR (line 556)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 558)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 566)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 568)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 667)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 669)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 715)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 717)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 774)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 776)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 961)
Useless comment: "# ==========================================================" - delete it or improve the code instead

[X] ERROR (line 963)
Useless comment: "# ==========================================================" - delete it or improve the code instead

---

## test_observable_behavior
**test_invoke_cli.py** - 3 violation(s)

[X] ERROR (line 182)
Line 182 tests internal implementation (mocks/spies) - tests should focus on observable behavior, not internal calls

[X] ERROR (line 185)
Line 185 tests internal implementation (mocks/spies) - tests should focus on observable behavior, not internal calls

[X] ERROR (line 354)
Line 354 tests internal implementation (mocks/spies) - tests should focus on observable behavior, not internal calls

---

## use_exact_variable_names
**test_invoke_cli.py** - 9 violation(s)

[!] WARNING (line 815)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 836)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 853)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 870)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 887)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 904)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 921)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 938)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

[!] WARNING (line 955)
Variable "result" uses generic name - use exact domain concept name from scenario/AC

---

Completed: 2025-12-20 15:39:35
Total violations: 122
Scanners executed: 23
