# REPL Status Display Panel

Visual dashboard for REPL CLI status - displays workflow, scope, and commands in a VS Code panel.

## Quick Links

| Document | Purpose |
|----------|---------|
| **[QUICKSTART.md](QUICKSTART.md)** | 5-minute setup and usage guide - **START HERE** |
| **[DISPLAY_PANEL_PLAN.md](DISPLAY_PANEL_PLAN.md)** | Complete implementation plan and architecture |
| **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** | What was built and how it works |
| **[extension/README.md](extension/README.md)** | Extension documentation and troubleshooting |

## What Is This?

A VS Code extension that shows your REPL CLI status dashboard in a rich visual panel:

```
┌─────────────────────────────────────┐
│ [🔄 Refresh] [🎯 View Scope]        │
├─────────────────────────────────────┤
│ Workflow Status                     │
│   [*] current_behavior              │
│       [*] current_action            │
│           [*] instructions          │
│           [ ] confirm               │
├─────────────────────────────────────┤
│ 🎯 Scope                            │
│   Filter: Epic, Story               │
│   [Graph] | [Map]                   │
└─────────────────────────────────────┘
```

## Install & Use

### 1. Build
```powershell
cd extension
.\rebuild.ps1
```

### 2. Install
```powershell
code --install-extension repl-status-panel-0.1.0.vsix
```

### 3. Use
```
Ctrl+Shift+P → "AgilBot: Show Bot Status Dashboard"
```

## Features

- 📊 **Visual Dashboard**: Rich UI display of REPL status
- 🔄 **Refresh Button**: Update status on demand
- 🎯 **Scope Links**: Click to open story files
- 🎨 **Theme Aware**: Matches VS Code colors
- 📍 **Workflow Tree**: Behaviors → Actions → Operations
- ♻️ **Zero Duplication**: Reuses REPL CLI via subprocess

## Architecture

```
extension/
├── extension.js              # Entry point
├── status_panel.js           # Panel controller
├── status_data_provider.js   # Python subprocess
├── status_parser.js          # Text → JSON parser
├── html_renderer.js          # JSON → HTML renderer
└── package.json              # Extension manifest
```

**Flow**: User → Command → Panel → Python → Parser → Renderer → Display

## Integration

- **REPL CLI**: Calls `repl_main.py status` via subprocess
- **No Changes**: Works with existing CLI unchanged
- **Auto-Sync**: CLI updates automatically appear in panel

## Documentation

1. **QUICKSTART.md** - Start here for setup
2. **DISPLAY_PANEL_PLAN.md** - Full architecture and design
3. **IMPLEMENTATION_SUMMARY.md** - What was built
4. **extension/README.md** - Extension usage and troubleshooting

## Status

✅ **Complete and Ready to Use**

- All core features implemented
- Fully documented
- Tested on Windows
- Ready for daily use

## Support

### Troubleshooting
See [extension/README.md](extension/README.md#troubleshooting)

### Questions
Check the documentation files above or open an issue.

---

**Part of the Augmented Teams Agile Bot system**
