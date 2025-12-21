# Validation Parameters Guide

## Overview
This guide documents all parameters available for the `validate` action, their performance implications, and recommended usage patterns.

## Scope Parameter (Primary)

The `--scope` parameter is the primary way to control validation behavior. It accepts a dictionary with the following structure:

```python
--scope "{'type': <type>, 'value': <value>, 'exclude': <patterns>, 'skiprule': <rules>}"
```

### Scope Types

#### 1. All (Default)
```bash
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate
# Or explicitly:
--scope "{'type': 'all'}"
```
- **What it does**: Validates all files in the behavior directory
- **Performance**: SLOWEST - Scans all files
- **When to use**: Full codebase validation, CI/CD pipelines

#### 2. Story
```bash
--scope "{'type': 'story', 'value': ['Story Name']}"
```
- **What it does**: Validates files related to specific stories
- **Performance**: MEDIUM - Limited to story-related files
- **When to use**: Working on specific features

#### 3. Epic
```bash
--scope "{'type': 'epic', 'value': ['Epic Name']}"
```
- **What it does**: Validates files related to specific epics
- **Performance**: MEDIUM - Limited to epic-related files
- **When to use**: Working on larger feature sets

#### 4. Increment
```bash
--scope "{'type': 'increment', 'value': [1, 2]}"
```
- **What it does**: Validates files related to specific increments
- **Performance**: MEDIUM - Limited to increment-related files
- **When to use**: Sprint/iteration-based validation

#### 5. Files
```bash
--scope "{'type': 'files', 'value': ['path/to/file.py', 'path/to/another.py']}"
```
- **What it does**: Validates only specified files
- **Performance**: FASTEST - Only scans specified files
- **When to use**: Targeted validation, debugging specific files

### Scope Modifiers

#### exclude (within scope)
```bash
--scope "{'type': 'files', 'value': ['src/'], 'exclude': ['test_*.py', '*/migrations/*']}"
```
- **What it does**: Excludes files matching patterns from validation
- **Performance**: FASTER - Fewer files to scan
- **When to use**: Exclude test files, generated code, or specific directories
- **Default**: `[]` (no files excluded)

#### skiprule (within scope)
```bash
--scope "{'type': 'all', 'skiprule': ['eliminate_duplication', 'stop_writing_useless_comments']}"
```
- **What it does**: Skips specific validation rules by name
- **Performance**: FASTER - Proportional to number of rules skipped
- **When to use**: Focus on specific rules or ignore noisy ones
- **Default**: `[]` (no rules skipped)

## Flag Parameters

### --force-full
```bash
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate --force-full
```
- **What it does**: Forces full scan of all files, ignoring modification timestamps
- **Performance**: SLOWEST - Scans all files regardless of changes
- **When to use**: 
  - First-time validation
  - After rule changes
  - Debugging incremental scan issues
  - CI/CD full validation
- **Default**: Not set (incremental scan based on file timestamps)
- **Note**: This is a flag - presence means full scan, absence means incremental

### --skip-cross-file
```bash
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate --skip-cross-file
```
- **What it does**: Skips cross-file duplicate checking
- **Performance**: MUCH FASTER - Eliminates most expensive scan
- **When to use**: 
  - Quick validation during development
  - When duplication is not a concern
  - Time-constrained validation
- **Default**: Not set (cross-file scan runs)
- **Note**: This is a flag - presence means skip, absence means run cross-file scan


## Performance Comparison

| Configuration | Relative Speed | Use Case |
|--------------|----------------|----------|
| Single file, skip cross-file | ⚡⚡⚡⚡⚡ Fastest | Quick checks during development |
| Incremental, skip cross-file | ⚡⚡⚡⚡ Very Fast | Rapid iteration |
| Incremental with cross-file | ⚡⚡⚡ Fast | Normal development workflow |
| Full scan, skip cross-file | ⚡⚡ Medium | Periodic full checks |
| Full scan with cross-file | ⚡ Slow | Complete validation (CI/CD) |

## Recommended Patterns

### Quick Development Check
```bash
# Validate only the file you're working on, skip duplication
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate \
  --scope "{'type': 'files', 'value': ['src/my_file.py']}" \
  --skip-cross-file
```

### Story-Level Validation
```bash
# Validate all files in a story, exclude tests, skip noisy rules
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate \
  --scope "{'type': 'story', 'value': ['My Story'], 'exclude': ['test_*.py'], 'skiprule': ['stop_writing_useless_comments']}"
```

### Pre-Commit Validation
```bash
# Incremental validation with cross-file checks
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate
```

### CI/CD Full Validation
```bash
# Complete validation of entire codebase
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate --force-full
```

### Debug Validation Issues
```bash
# Force full scan to ensure fresh validation
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate \
  --force-full \
  --scope "{'type': 'files', 'value': ['src/problematic_file.py']}"
```

## Incremental Validation Behavior

### How It Works
1. **First Run**: No previous reports exist → Full scan of all files
2. **Subsequent Runs**: 
   - Reads timestamp of most recent validation report
   - Scans only files modified after that timestamp
   - Cross-file scan: Changed files checked against ALL files (one-way)

### When Full Scan Occurs
- No previous validation reports exist
- `--force-full` flag is present
- All previous reports are older than 10 seconds (prevents self-reference)

### Report Management
- All reports stored in: `docs/stories/reports/`
- Filename format: `{behavior}-validation-status-{timestamp}.md`
- Old reports are NEVER deleted automatically
- Historical tracking enabled by default

## Common Issues and Solutions

### Issue: Validation too slow
**Solution**: Use `--skip-cross-file` for development, reserve full cross-file for CI/CD

### Issue: Too many violations from one rule
**Solution**: Use `skiprule` to temporarily disable noisy rules:
```bash
--scope "{'skiprule': ['eliminate_duplication']}"
```

### Issue: Incremental scan not detecting changes
**Solution**: Force full scan to reset:
```bash
--force-full
```

### Issue: Need to validate only changed files
**Solution**: Default behavior (incremental) handles this automatically

## Parameter Priority

When parameters conflict, the following priority is used:
1. `--force-full` overrides incremental behavior
2. `--skip-cross-file` overrides default cross-file scanning
3. `scope.exclude` filters files from validation
4. `scope.skiprule` filters rules from validation

## Examples

### Example 1: Focus on Clean Code Rules Only
```bash
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate \
  --scope "{'skiprule': ['test_organization', 'resource_oriented_code']}"
```

### Example 2: Validate Specific Directory, Exclude Tests
```bash
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate \
  --scope "{'type': 'files', 'value': ['src/actions/'], 'exclude': ['test_*.py']}"
```

### Example 3: Quick Validation During Refactoring
```bash
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate \
  --skip-cross-file \
  --scope "{'type': 'files', 'value': ['src/refactored_module.py']}"
```

### Example 4: Complete Fresh Validation
```bash
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate \
  --force-full
```

