# REPL Status Display Panel - Quick Start Guide

## What Is This?

A VS Code extension that displays your REPL CLI status dashboard in a rich visual panel that can sit above your chat interface.

## 5-Minute Setup

### Step 1: Build the Extension

```powershell
cd C:\dev\augmented-teams\agile_bot\bots\base_bot\src\display_panel\extension
.\rebuild.ps1
```

This creates `repl-status-panel-0.1.0.vsix`

### Step 2: Install the Extension

```powershell
code --install-extension repl-status-panel-0.1.0.vsix
```

Or manually:
1. Open VS Code
2. Press `Ctrl+Shift+P`
3. Type: `Extensions: Install from VSIX`
4. Select the `.vsix` file

### Step 3: Open the Panel

1. Press `Ctrl+Shift+P`
2. Type: `AgilBot: Show Bot Status Dashboard`
3. Panel opens (can be dragged above chat)

### Step 4: Use It

- **Refresh**: Click 🔄 button to update status
- **View Scope**: Click 🎯 button to open story graph
- **File Links**: Click Graph/Map links to open files
- **Position**: Drag panel anywhere you want

## What You'll See

```
┌─────────────────────────────────────┐
│ BASE BOT CLI                        │
│ Bot Path: /path/to/bot              │
│ Working Area: /workspace            │
├─────────────────────────────────────┤
│ [🔄 Refresh] [🎯 View Scope]        │
├─────────────────────────────────────┤
│ Workflow Status                     │
│   [*] shape                         │
│       [*] build                     │
│           [*] instructions          │
│           [ ] confirm               │
│   [ ] discovery                     │
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

## Status Markers

- **[*]** Yellow - Currently active
- **[ ]** Gray - Not started
- **[✓]** Green - Completed (future feature)

## How It Works

1. **You click refresh** → Extension calls Python
2. **Python runs** → `python repl_main.py status`
3. **CLI outputs** → Status text (same as terminal)
4. **Extension parses** → Text → Structured data
5. **Panel renders** → HTML with VS Code theme

**Zero duplication**: Reuses all your existing REPL CLI code!

## Troubleshooting

### Panel shows but no data
1. **Press `F12`** to open Developer Tools
2. Click **Console** tab
3. Click **Refresh** button in panel
4. Look for RED error messages - they show parsing issues
5. **Report the error** to help fix the parser

### "Python not available"
```powershell
python --version  # Should show Python 3.x
```
If not, install Python and add to PATH.

### "REPL CLI not found"
Make sure you're in the right workspace:
```
C:\dev\augmented-teams\
```

### Panel shows error
1. Check "REPL Status Panel" output channel in VS Code
2. Test CLI manually: `python agile_bot/bots/base_bot/src/repl_cli/repl_main.py`
3. Type `status` and verify output

### Panel not updating
- Click 🔄 Refresh button
- Close and reopen panel
- Check for Python errors in output channel

## Tips

1. **Position**: Drag panel above chat for best view
2. **Refresh**: Click refresh after running CLI commands
3. **Files**: Click scope links to jump to files
4. **Theme**: Changes automatically with VS Code theme

## Next Steps

- See `DISPLAY_PANEL_PLAN.md` for architecture details
- See `extension/README.md` for full documentation
- Check `extension/` folder for source code

## Questions?

The panel is read-only (display only). To execute commands:
- Use the REPL CLI in terminal
- Use chat commands
- Then refresh the panel to see updates

## Architecture Summary

```
display_panel/
├── DISPLAY_PANEL_PLAN.md      # Full implementation plan
├── QUICKSTART.md              # This file
└── extension/
    ├── package.json           # Extension manifest
    ├── extension.js           # Entry point
    ├── status_panel.js        # Panel controller
    ├── status_data_provider.js # Python subprocess
    ├── status_parser.js       # Text parser
    ├── html_renderer.js       # HTML generator
    ├── README.md              # Full docs
    └── rebuild.ps1            # Build script
```

## Features

✅ Visual dashboard matching CLI exactly
✅ Refresh button for live updates  
✅ Scope section with clickable links
✅ VS Code theme integration
✅ No command entry (display only)
✅ Reuses REPL CLI (zero duplication)
✅ Can position above chat panel

Enjoy your visual REPL dashboard! 🚀
