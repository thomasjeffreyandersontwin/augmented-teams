# Cursor Indexing Performance Analysis

## Summary

This analysis identifies files and directories that may be slowing down Cursor's indexing performance.

## Key Findings

### 1. Missing `.cursorignore` File
- **Issue**: No `.cursorignore` file exists, so Cursor may be indexing all files
- **Solution**: Created `.cursorignore` file with common exclusion patterns

### 2. Log Files
- **Found**: Multiple log files throughout the project:
  - Test output logs (`test_output.log`, `workflow_output.log`, `assert_output.log`)
  - Character MCP server logs in `agile_bot/bots/character/code/logs/`
  - Azure command logs in `behaviors/.azure/commands/`
- **Impact**: Log files change frequently and don't need to be indexed
- **Solution**: Added `*.log` and specific log patterns to `.cursorignore`

### 3. Cache Directories
- **Found**: Multiple cache directories:
  - `.bun/` directories (Bun runtime cache)
  - `__pycache__/` (Python bytecode cache)
  - `.pytest_cache/` (Pytest cache)
- **Impact**: Cache files are regenerated and don't need indexing
- **Solution**: Added cache directory patterns to `.cursorignore`

### 4. Binary Files
- **Found**: Binary files like PDFs, images, executables
- **Impact**: Binary files are large and can't be meaningfully indexed
- **Solution**: Added binary file patterns to `.cursorignore`

### 5. Test Output Files
- **Found**: Test output files in `agile_bot/bots/story_bot/test/synchronizers/story-io/acceptance/scenarios/`
- **Impact**: These are generated artifacts that don't need indexing
- **Solution**: Added test output patterns to `.cursorignore`

### 6. Large JSON Files
- **Found**: Many JSON files (581+ according to directory listings)
- **Impact**: Large JSON files can slow down indexing
- **Note**: Most JSON files are likely needed for indexing (configs, story graphs, etc.)
- **Solution**: Left JSON files indexed by default, but added comments in `.cursorignore` for optional exclusions

### 7. DrawIO Diagram Files
- **Found**: 42+ `.drawio` files (XML-based diagram files)
- **Impact**: These can be large XML files
- **Solution**: Added commented-out exclusion in `.cursorignore` - uncomment if you don't need diagram content indexed

## Recommendations

1. **Use `.cursorignore`**: The created `.cursorignore` file will immediately improve indexing performance

2. **Review DrawIO Files**: Consider uncommenting `*.drawio` in `.cursorignore` if you don't need diagram content in your AI context

3. **Review Demo Directories**: The `demo/` directory is excluded - remove this exclusion if you need those files indexed

4. **Clean Up Log Files**: Consider periodically cleaning up log files:
   ```powershell
   Get-ChildItem -Recurse -Filter "*.log" | Remove-Item
   ```

5. **Review Large JSON Files**: If you have very large JSON files that don't need indexing, add specific patterns to `.cursorignore`

## Files to Monitor

After applying `.cursorignore`, monitor these areas:

- **agile_bot/bots/story_bot/behaviors/**: Contains many JSON configuration files (may be necessary for indexing)
- **agile_bot/bots/story_bot/test/**: Contains test files and output logs (logs now excluded)
- **demo/**: Currently excluded - remove from `.cursorignore` if needed

## Next Steps

1. Review the generated `.cursorignore` file
2. Restart Cursor to apply the new indexing exclusions
3. Monitor indexing performance improvement
4. Adjust `.cursorignore` as needed based on your workflow
