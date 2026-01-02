# REPL Status Display Panel - Implementation Plan

## Overview

Create a VS Code extension that displays the REPL CLI status dashboard in a dedicated panel above the chat interface. The panel provides read-only visualization of bot workflow state, scope, and commands.

## Goals

1. **Visual Dashboard**: Display REPL status exactly like CLI output but in a rich UI panel
2. **Minimal New Code**: Reuse existing `repl_cli` infrastructure by calling it as subprocess
3. **Interactive Elements**: Refresh button, scope hyperlinks to open files
4. **Auto-sync**: Panel reads same state files as CLI, stays in sync automatically
5. **No Command Entry**: Display-only interface, no command execution

## Architecture

### File Structure

```
base_bot/src/display_panel/
├── DISPLAY_PANEL_PLAN.md          # This document
├── extension/
│   ├── package.json               # Extension manifest
│   ├── extension.js               # Main extension entry point
│   ├── status_panel.js            # Webview panel controller
│   ├── status_data_provider.js    # Python CLI subprocess interface
│   ├── status_parser.js           # Parse CLI output into structured data
│   ├── html_renderer.js           # Generate HTML/CSS for webview
│   ├── README.md                  # Extension documentation
│   └── rebuild.ps1                # Build and package script
└── test/
    └── test_status_panel.py       # Python tests for CLI integration
```

### Components

#### 1. Extension Entry Point (`extension.js`)
- **Responsibility**: VS Code extension lifecycle (activate/deactivate)
- **Exports**: `activate()`, `deactivate()` functions
- **Actions**:
  - Register command: `agilebot.showStatus`
  - Create StatusPanel singleton
  - Manage extension subscriptions

#### 2. Status Panel Controller (`status_panel.js`)
- **Responsibility**: Manage webview panel lifecycle and interactions
- **Pattern**: Singleton panel (create or reveal existing)
- **Actions**:
  - Create/show webview panel
  - Handle refresh requests
  - Handle file open requests (scope links)
  - Coordinate data fetch and rendering
  - Manage panel disposal

#### 3. Status Data Provider (`status_data_provider.js`)
- **Responsibility**: Interface with Python REPL CLI
- **Method**: Spawn Python subprocess, send 'status' command via stdin
- **Returns**: Raw CLI text output
- **Error Handling**: Capture stderr, timeout handling
- **Reuses**: Existing `repl_main.py` status command

#### 4. Status Parser (`status_parser.js`)
- **Responsibility**: Parse CLI text output into structured data
- **Input**: Raw status text from CLI
- **Output**: Structured JSON object:
  ```javascript
  {
    header: { botName, botPath, workingArea },
    behaviors: [{ name, isCurrent, actions: [...] }],
    scope: { filter, links: [...] },
    headless: { status, lines: [...] },
    commands: "..."
  }
  ```
- **Logic**: Line-by-line parsing matching CLI output format

#### 5. HTML Renderer (`html_renderer.js`)
- **Responsibility**: Generate HTML/CSS for webview display
- **Input**: Structured status data
- **Output**: Complete HTML document with:
  - VS Code theme-aware CSS variables
  - Behavior/action/operation hierarchy
  - Status markers ([*] current, [ ] pending, [✓] completed)
  - Interactive buttons (refresh, scope links)
  - JavaScript for VSCode message passing

## Data Flow

```
User Clicks → Command → StatusPanel.createOrShow()
                            ↓
                        StatusDataProvider.getStatus()
                            ↓
                        Spawn Python: repl_main.py
                        Send: "status\n"
                            ↓
                        Parse stdout → StatusParser.parse()
                            ↓
                        Structured Data → HtmlRenderer.render()
                            ↓
                        HTML → webview.html
                            ↓
                        Display Panel
```

## Reuse Strategy

### From REPL CLI (`base_bot/src/repl_cli/`)

**Direct Reuse (via subprocess)**:
- `repl_main.py` - Entry point, status command handler
- `repl_status.py` - Status generation logic
- `status_display.py` - Hierarchical status rendering
- `formatter.py` - Status markers and formatting
- `cli_scope.py` - Scope display with links

**Pattern**: Call Python CLI as subprocess, parse output
**Benefit**: Zero duplication, automatic sync with CLI changes

### From Base Bot Extension (`base_bot/extension/`)

**Reuse Pattern**:
- Extension structure: `package.json`, `activate()`, `deactivate()`
- Subprocess spawning: `cp.spawn("python", [...])`
- Workspace root detection
- VS Code API patterns

**Integration**: Can merge or keep separate (recommend separate for clarity)

## Visual Design

### Theme Integration
- Use VS Code CSS variables for colors
- `--vscode-foreground` - primary text
- `--vscode-descriptionForeground` - secondary text
- `--vscode-panel-border` - borders
- `--vscode-button-background` - buttons
- `--vscode-textLink-foreground` - links
- `--vscode-terminal-ansiYellow` - current marker
- `--vscode-terminal-ansiGreen` - completed marker

### Layout Structure

```
┌─────────────────────────────────────┐
│ BOT NAME CLI                        │
│ Bot Path: /path/to/bot              │
│ Working Area: /workspace            │
├─────────────────────────────────────┤
│ [🔄 Refresh] [🎯 View Scope]        │
├─────────────────────────────────────┤
│ Workflow Status                     │
│   [*] current_behavior              │
│       [*] current_action            │
│           [*] instructions          │
│           [ ] confirm               │
│   [ ] next_behavior                 │
├─────────────────────────────────────┤
│ 🎯 Scope                            │
│   Filter: Epic Name, Story Name     │
│   [Graph] | [Map]                   │
├─────────────────────────────────────┤
│ Headless Mode                       │
│   Status: Available                 │
├─────────────────────────────────────┤
│ Commands: status | back | next ...  │
└─────────────────────────────────────┘
```

### Status Markers
- `[*]` - Current (yellow) - What's active now
- `[ ]` - Pending (gray) - Not started yet
- `[✓]` - Completed (green) - Already done

## Implementation Steps

### Phase 1: Core Infrastructure
1. Create directory structure under `base_bot/src/display_panel/extension/`
2. Create `package.json` with extension manifest
3. Create `extension.js` with basic activation
4. Test extension loads in VS Code

### Phase 2: Data Provider
1. Create `status_data_provider.js`
2. Implement subprocess spawning for `repl_main.py status`
3. Handle stdout/stderr capture
4. Add error handling and timeout
5. Test data retrieval

### Phase 3: Parser
1. Create `status_parser.js`
2. Implement line-by-line parsing logic
3. Match patterns for behaviors, actions, operations
4. Extract scope, headless, commands sections
5. Return structured data object
6. Unit test with sample CLI outputs

### Phase 4: Renderer
1. Create `html_renderer.js`
2. Build HTML template with CSS
3. Implement behavior tree rendering
4. Add scope section with links
5. Add interactive buttons
6. Test rendering with various states

### Phase 5: Panel Controller
1. Create `status_panel.js`
2. Implement singleton pattern
3. Wire up data provider + parser + renderer
4. Handle webview messages (refresh, open file)
5. Test panel lifecycle (create, reveal, dispose)

### Phase 6: Integration
1. Update `extension.js` to register command
2. Test full flow: command → panel → display
3. Test refresh functionality
4. Test scope link clicks
5. Test panel positioning and resizing

### Phase 7: Polish
1. Add loading indicator during refresh
2. Add error display for CLI failures
3. Add README with usage instructions
4. Create `rebuild.ps1` packaging script
5. Test .vsix installation

## Testing Strategy

### Manual Testing
1. **Status Display**: Verify matches CLI output exactly
2. **Refresh**: Click refresh, verify updates
3. **Scope Links**: Click links, verify files open
4. **Theme**: Switch VS Code themes, verify colors adapt
5. **Error Cases**: Test with bot not initialized, CLI errors
6. **Multiple Calls**: Open panel multiple times, verify singleton

### Automated Testing
1. **Parser Tests**: Unit tests for CLI output parsing
2. **Mock CLI**: Test with sample status outputs
3. **Edge Cases**: Empty state, no behaviors, long paths

## Configuration

### Extension Settings (Optional Future)
- `agilebot.statusPanel.autoRefresh`: Auto-refresh interval (default: off)
- `agilebot.statusPanel.defaultPosition`: Panel position preference

### Current (No Settings Required)
- Reads from existing `behavior_action_state.json`
- Uses workspace root detection
- No additional configuration needed

## Integration Points

### With REPL CLI
- **Input**: Calls `repl_main.py status` command
- **State**: Reads same state files (behavior_action_state.json)
- **Format**: Parses standard CLI output format

### With VS Code
- **Command Palette**: `AgilBot: Show Bot Status Dashboard`
- **Webview API**: For panel rendering
- **Workspace API**: For file opening
- **Theme API**: For color scheme

### With Existing Extension
- **Option 1**: Merge into `base_bot/extension/` (single .vsix)
- **Option 2**: Separate extension (dedicated display panel)
- **Recommendation**: Keep separate initially, merge if desired

## Benefits

### For Users
1. **Visual Dashboard**: Rich UI vs plain text CLI
2. **Always Visible**: Panel stays open while working
3. **Quick Navigation**: Click links to open relevant files
4. **State Awareness**: See workflow progress at a glance

### For Developers
1. **No Duplication**: Reuses all CLI logic via subprocess
2. **Auto-Sync**: Changes to CLI automatically appear in panel
3. **Simple Maintenance**: Single source of truth (CLI)
4. **Easy Testing**: Can test CLI and panel independently

## Future Enhancements

### Phase 2 (Post-MVP)
1. **Auto-refresh**: Watch state file changes, update automatically
2. **Command Execution**: Add quick actions (next, back, etc.)
3. **History View**: Show recent actions taken
4. **Inline Help**: Hover tooltips for behaviors/actions
5. **Progress Indicators**: Visual progress bars for workflows
6. **Multi-bot Support**: Switch between different bots
7. **Split View**: Show CLI output alongside rich UI

### Advanced Features
1. **State Editing**: Modify scope from panel
2. **Action Triggers**: Click to execute actions
3. **Log Streaming**: Live tail of bot logs
4. **Notifications**: Alert on state changes

## Success Criteria

✅ Panel displays identical information to `status` CLI command
✅ Refresh button updates display with current state
✅ Scope links open correct files in editor
✅ Panel uses VS Code theme colors
✅ No command entry (display-only)
✅ Minimal new code (reuses CLI via subprocess)
✅ Works with existing REPL CLI without modifications
✅ Can be positioned above chat panel in VS Code

## Dependencies

### Required
- VS Code API >= 1.80.0
- Node.js (built-in with VS Code)
- Python 3.x (already required for bots)
- Existing `repl_cli` infrastructure

### No New Dependencies
- Uses only built-in Node modules (`child_process`, `path`, `fs`)
- No npm packages required
- No changes to Python requirements

## Deployment

1. **Build**: Run `rebuild.ps1` to create `.vsix`
2. **Install**: `code --install-extension display-panel-0.1.0.vsix`
3. **Use**: Open command palette → "AgilBot: Show Bot Status Dashboard"
4. **Update**: Rebuild and reinstall to update

## Risk Mitigation

### Risk: CLI Output Format Changes
- **Mitigation**: Parser handles variations gracefully
- **Test**: Run parser tests on CLI output changes
- **Fallback**: Display raw output if parsing fails

### Risk: Python Not Available
- **Detection**: Check Python in PATH during activation
- **Error**: Show clear message to install Python
- **Graceful**: Extension loads but command shows error

### Risk: Performance with Large State
- **Optimization**: Parse incrementally, cache results
- **Limit**: Truncate very long outputs
- **Async**: Run parsing in background

## Conclusion

This plan provides a complete roadmap for building a VS Code display panel that mirrors the REPL CLI status dashboard. By reusing existing CLI infrastructure through subprocess calls, we minimize code duplication while providing a rich visual experience for users.

The modular architecture allows incremental development and testing, with clear separation between data acquisition, parsing, rendering, and panel management.
