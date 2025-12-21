# Validation Parameter Test Coverage

## Overview
Comprehensive test coverage for all validation parameter variations to prevent parameter-related errors.

## Test Files
1. `test_invoke_cli.py` - CLI parameter parsing tests
2. `test_validate_knowledge_and_content_against_rules.py` - Integration tests with validation context

## Test Coverage Matrix

### CLI Parameter Parsing Tests (`test_invoke_cli.py`)

#### TestScopeBasedParameterHandling (6 tests)
| Test | What It Validates |
|------|-------------------|
| `test_scope_accepts_exclude_within_scope_dict` | Exclude patterns are parsed from scope |
| `test_scope_accepts_skiprule_within_scope_dict` | Skiprule lists are parsed from scope |
| `test_scope_accepts_both_exclude_and_skiprule_within_scope_dict` | Both exclude and skiprule work together |
| `test_cli_does_not_accept_standalone_exclude_parameter` | Legacy `--exclude` is rejected |
| `test_cli_does_not_accept_standalone_skiprule_parameter` | Legacy `--skiprule` is rejected |

#### TestValidationParameterVariations (28 tests)
| Category | Tests | What They Validate |
|----------|-------|-------------------|
| **Flag Tests** | 3 | |
| `test_force_full_flag_alone` | | `--force-full` works independently |
| `test_skip_cross_file_flag_alone` | | `--skip-cross-file` works independently |
| `test_both_flags_together` | | Both flags work together |
| **Scope Type Tests** | 5 | |
| `test_scope_with_type_all` | | `type: 'all'` is parsed correctly |
| `test_scope_with_type_story` | | `type: 'story'` with value is parsed |
| `test_scope_with_type_epic` | | `type: 'epic'` with value is parsed |
| `test_scope_with_type_increment` | | `type: 'increment'` with numeric values |
| `test_scope_with_type_files` | | `type: 'files'` with file paths |
| **Exclude Tests** | 2 | |
| `test_scope_with_single_exclude_pattern` | | Single exclude pattern works |
| `test_scope_with_multiple_exclude_patterns` | | Multiple exclude patterns work |
| **Skiprule Tests** | 2 | |
| `test_scope_with_single_skiprule` | | Single skiprule works |
| `test_scope_with_multiple_skiprules` | | Multiple skiprules work |
| **Combined Tests** | 2 | |
| `test_scope_with_exclude_and_skiprule` | | Exclude + skiprule together |
| `test_scope_with_all_parameters` | | All scope parameters together |
| **Flag + Scope Tests** | 4 | |
| `test_force_full_with_scope` | | `--force-full` + scope |
| `test_skip_cross_file_with_scope` | | `--skip-cross-file` + scope |
| `test_both_flags_with_scope` | | Both flags + scope |
| `test_flags_with_scope_containing_exclude_and_skiprule` | | Flags + full scope |
| **Edge Cases** | 4 | |
| `test_empty_scope` | | Empty scope dict `{}` |
| `test_scope_with_empty_exclude` | | `exclude: []` |
| `test_scope_with_empty_skiprule` | | `skiprule: []` |
| `test_no_parameters_at_all` | | No parameters provided |

### Validation Context Tests (`test_validate_knowledge_and_content_against_rules.py`)

#### TestScopeBasedParameterHandling (6 tests)
| Test | What It Validates |
|------|-------------------|
| `test_exclude_patterns_via_scope` | ValidationScope handles exclude patterns |
| `test_skiprule_via_scope` | ValidationScope handles skiprule lists |
| `test_combined_scope_with_exclude_and_skiprule` | ValidationScope handles both together |
| `test_force_full_flag_triggers_full_scan` | ValidationContext.force_full is set correctly |
| `test_skip_cross_file_flag_disables_cross_file_scan` | ValidationContext.skip_cross_file is set correctly |

#### TestValidationWithAllParameterCombinations (11 tests)
| Test | What It Validates |
|------|-------------------|
| `test_validation_with_force_full_only` | Force full scan works alone |
| `test_validation_with_skip_cross_file_only` | Skip cross-file works alone |
| `test_validation_with_both_flags` | Both flags work together in validation |
| `test_validation_with_scope_type_all` | Scope type 'all' works in validation |
| `test_validation_with_scope_exclude_only` | Exclude patterns work in validation |
| `test_validation_with_scope_skiprule_only` | Skiprule lists work in validation |
| `test_validation_with_force_full_and_scope_exclude` | Force full + exclude works |
| `test_validation_with_all_parameters_combined` | All parameters work together |
| `test_validation_with_no_parameters` | Validation works with no parameters |

## Total Test Count
- **CLI Parsing Tests**: 34 tests
- **Validation Context Tests**: 17 tests
- **Total**: 51 tests

## Parameter Combinations Tested

### 1. Single Parameters
- ✅ `--force-full` alone
- ✅ `--skip-cross-file` alone
- ✅ `--scope` with type only
- ✅ `--scope` with exclude only
- ✅ `--scope` with skiprule only

### 2. Two-Parameter Combinations
- ✅ `--force-full` + `--skip-cross-file`
- ✅ `--force-full` + `--scope`
- ✅ `--skip-cross-file` + `--scope`
- ✅ `--scope` with exclude + skiprule

### 3. Three-Parameter Combinations
- ✅ `--force-full` + `--skip-cross-file` + `--scope`
- ✅ `--force-full` + `--scope` (with exclude)
- ✅ `--skip-cross-file` + `--scope` (with skiprule)

### 4. All Parameters Combined
- ✅ `--force-full` + `--skip-cross-file` + `--scope` (with type, value, exclude, skiprule)

### 5. Edge Cases
- ✅ No parameters
- ✅ Empty scope `{}`
- ✅ Empty exclude `[]`
- ✅ Empty skiprule `[]`
- ✅ Single vs multiple values in arrays

### 6. Scope Type Variations
- ✅ `type: 'all'`
- ✅ `type: 'story'`
- ✅ `type: 'epic'`
- ✅ `type: 'increment'`
- ✅ `type: 'files'`

### 7. Legacy Parameter Rejection
- ✅ Standalone `--exclude` is rejected
- ✅ Standalone `--skiprule` is rejected

## Error Scenarios Covered

### 1. Missing Required Attributes
- ✅ Args namespace without `exclude` attribute
- ✅ Args namespace without `skiprule` attribute

### 2. Type Mismatches
- ✅ String vs list for exclude patterns
- ✅ String vs list for skiprule lists
- ✅ Integer values in increment scope

### 3. Empty Values
- ✅ Empty scope dictionary
- ✅ Empty exclude list
- ✅ Empty skiprule list
- ✅ No parameters at all

### 4. Complex Combinations
- ✅ Multiple files in scope value
- ✅ Multiple patterns in exclude
- ✅ Multiple rules in skiprule
- ✅ All parameters with maximum values

## Test Execution Strategy

### Unit Tests (CLI Parsing)
```bash
pytest agile_bot/bots/base_bot/test/test_invoke_cli.py::TestScopeBasedParameterHandling -v
pytest agile_bot/bots/base_bot/test/test_invoke_cli.py::TestValidationParameterVariations -v
```

### Integration Tests (Validation Context)
```bash
pytest agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py::TestScopeBasedParameterHandling -v
pytest agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py::TestValidationWithAllParameterCombinations -v
```

### Full Test Suite
```bash
pytest agile_bot/bots/base_bot/test/test_invoke_cli.py agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py -v -k "Parameter"
```

## Continuous Integration Recommendations

### Pre-Commit Checks
1. Run all parameter-related tests
2. Verify no legacy parameters in codebase
3. Check documentation consistency

### Pull Request Requirements
1. All 51 tests must pass
2. No new standalone parameters added
3. All new scope keys documented

### Regression Prevention
1. Add test for any new parameter
2. Test all combinations with new parameter
3. Update this coverage document

## Known Limitations

### Not Tested (Intentionally)
1. Invalid JSON syntax (handled by JSON parser)
2. Network/file system errors (not parameter-related)
3. Rule file loading errors (separate concern)

### Future Test Additions
1. Performance tests for large parameter sets
2. Concurrent validation with different parameters
3. Parameter validation error messages

## Maintenance Notes

### When Adding New Parameters
1. Add to `TestValidationParameterVariations`
2. Add to `TestValidationWithAllParameterCombinations`
3. Test with all existing parameters
4. Update this document

### When Modifying Existing Parameters
1. Run full test suite
2. Update affected tests
3. Verify backward compatibility (if applicable)
4. Update documentation

## Success Criteria

✅ **All tests pass**: 51/51 tests passing
✅ **No legacy parameters**: `--exclude` and `--skiprule` rejected
✅ **All combinations work**: Every parameter combination tested
✅ **Edge cases handled**: Empty values, no parameters, etc.
✅ **Integration verified**: CLI parsing → ValidationContext → Validation execution

## Test Maintenance Schedule

- **Daily**: Run full test suite in CI
- **Weekly**: Review test coverage for new code
- **Monthly**: Audit for missing parameter combinations
- **Quarterly**: Performance test with large parameter sets


