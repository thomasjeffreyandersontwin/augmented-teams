# REPL Status Display Panel Extension

Visual dashboard for REPL CLI status showing workflow, scope, and commands in a VS Code webview panel.

## Features

- 📊 **Visual Dashboard**: Rich UI display of REPL CLI status
- 🔄 **Live Refresh**: Update status with button click
- 🎯 **Scope Links**: Click to open story graph and map files
- 🎨 **Theme Aware**: Adapts to VS Code color theme
- 📍 **Workflow Tree**: Hierarchical view of behaviors, actions, and operations
- 🚀 **Headless Status**: See if headless mode is available

## Installation

### From Source

1. Navigate to extension directory:
   ```powershell
   cd agile_bot/bots/base_bot/src/display_panel/extension
   ```

2. Run build script:
   ```powershell
   .\rebuild.ps1
   ```

3. Install the generated `.vsix` file:

   **For Cursor:**
   ```powershell
   cursor --install-extension repl-status-panel-0.11.0.vsix
   ```

   **For VS Code:**
   ```powershell
   code --install-extension repl-status-panel-0.11.0.vsix
   ```

4. **Reload the window:**
   - Press `Ctrl+Shift+P`
   - Type "Developer: Reload Window"
   - Press Enter

### Manual Installation

1. Open Cursor or VS Code
2. Press `Ctrl+Shift+P`
3. Type "Extensions: Install from VSIX"
4. Select the `.vsix` file
5. Reload the window (Ctrl+Shift+P → "Developer: Reload Window")

## Usage

### Open the Panel

**Command Palette** (`Ctrl+Shift+P`):
```
AgilBot: Show Bot Status Dashboard
```

### Panel Features

#### Header
- Bot name and CLI identifier
- Bot directory path
- Working area (workspace) path

#### Controls
- **🔄 Refresh**: Reload status from REPL CLI
- **🎯 View Scope**: Open story graph JSON file

#### Workflow Status
Hierarchical tree showing:
- **Behaviors**: Top-level workflow phases
- **Actions**: Steps within each behavior
- **Operations**: Sub-steps (instructions, confirm)

Status markers:
- `[*]` Yellow - Currently active
- `[ ]` Gray - Not started yet
- `[✓]` Green - Completed (future)

#### Scope
- Current scope filter
- Links to story graph and map files
- Click links to open files in editor

#### Headless Mode
- Status: Available or Unavailable
- Configuration information

#### Commands
- Quick reference of available REPL commands

## Architecture

### Components

1. **extension.js**: Main entry point, activates extension
2. **status_panel.js**: Webview panel controller (singleton)
3. **status_data_provider.js**: Python CLI subprocess interface
4. **status_parser.js**: Parse CLI text output to structured data
5. **html_renderer.js**: Generate HTML/CSS for webview

### Data Flow

```
User → Command → StatusPanel
                      ↓
                  DataProvider (spawn Python)
                      ↓
                  Parser (text → JSON)
                      ↓
                  Renderer (JSON → HTML)
                      ↓
                  Webview Display
```

### Integration

**REPL CLI**:
- Calls `repl_main.py status` command
- Parses standard CLI output
- No modifications to CLI required
- Automatically syncs with CLI changes

**VS Code**:
- Uses Webview API for rendering
- Workspace API for file operations
- Theme API for colors
- Command API for activation

## Development

### Prerequisites

- Node.js (built-in with VS Code)
- Python 3.x (for REPL CLI)
- VS Code >= 1.80.0

### Local Development

1. Open workspace in VS Code
2. Press `F5` to launch Extension Development Host
3. Test extension in new window

### Debugging

- Check "REPL Status Panel" output channel
- Console logs appear in Extension Host
- Python errors captured in stderr

### Testing

Run manual tests:
- Status display matches CLI
- Refresh button works
- Scope links open correct files
- Theme colors adapt
- Error handling (no Python, CLI failure)

## Troubleshooting

### "Python not available"
- Ensure Python is in PATH
- Test: `python --version`
- Install Python 3.x if missing

### "REPL CLI not found"
- Verify workspace structure
- Check path: `agile_bot/bots/base_bot/src/repl_cli/repl_main.py`
- Ensure in correct workspace root

### "Failed to parse status"
- CLI output format may have changed
- Check "REPL Status Panel" output channel
- Compare CLI output with parser expectations

### Panel not updating
- Click refresh button
- Check for Python errors
- Verify CLI works standalone: `python repl_main.py`

## Configuration

No configuration required. Extension automatically:
- Detects workspace root
- Finds REPL CLI location
- Uses existing state files

Optional (future):
- `agilebot.statusPanel.autoRefresh`: Auto-refresh interval
- `agilebot.statusPanel.position`: Default panel position

## Limitations

- **Display Only**: No command execution from panel
- **Single Bot**: Shows one bot at a time (workspace root)
- **Manual Refresh**: No auto-refresh on state changes (yet)
- **Windows**: Tested on Windows, may need adjustments for Linux/Mac

## Future Enhancements

- Auto-refresh on file changes
- Command execution from panel
- Multi-bot support
- History view
- Progress indicators
- Inline help tooltips

## Credits

Part of the Augmented Teams Agile Bot system.

## License

Same as parent project.
