# Production Panel Fix - CLI Initialization

**Issue:** Panel failed to load in production with error: `CLI not initialized. Call PanelView.initializeCLI() first.`

**Root Cause:** After refactoring views to use singleton CLI pattern, the production extension code (`bot_panel.js`) was not updated to initialize the singleton CLI.

## Changes Made

### 1. Updated `bot_panel.js`

#### Added PanelView Import
```javascript
const PanelView = require("./panel_view");
```

#### Added CLI Initialization in Constructor
```javascript
// Determine bot directory (from env var or default to story_bot)
const botDirectory = process.env.BOT_DIRECTORY || path.join(workspaceRoot, 'agile_bot', 'bots', 'story_bot');
console.log(`[BotPanel] Bot directory: ${botDirectory}`);

// Initialize singleton CLI (only initializes once, safe to call multiple times)
console.log("[BotPanel] Initializing singleton CLI");
PanelView.initializeCLI(workspaceRoot, botDirectory);
console.log("[BotPanel] CLI initialized successfully");
```

#### Updated BotView Constructor Calls
**Before:**
```javascript
const initialBotView = new BotView({}, null, this._workspaceRoot, null, this._panelVersion, webview, this._extensionUri);
```

**After:**
```javascript
this._botView = new BotView(this._panelVersion, webview, this._extensionUri);
```

#### Updated `_update()` Method
**Before:**
```javascript
// Get initial bot status
const initialBotView = new BotView({}, null, this._workspaceRoot, null, this._panelVersion, webview, this._extensionUri);
const initialStatus = await initialBotView.execute('status');
this._botView = new BotView(initialStatus, null, this._workspaceRoot, null, this._panelVersion, webview, this._extensionUri);
```

**After:**
```javascript
// Initialize BotView if needed (uses singleton CLI)
if (!this._botView) {
    this._botView = new BotView(this._panelVersion, webview, this._extensionUri);
}

// Render HTML using BotView (async now)
const html = this._getWebviewContent(await this._botView.render());
```

#### Updated `dispose()` Method
**Before:**
```javascript
if (this._botView) {
    this._botView.cleanup();
    this._botView = null;
}
```

**After:**
```javascript
// Clean up singleton CLI (safe since BotPanel is singleton)
console.log("[BotPanel] Cleaning up singleton CLI");
PanelView.cleanupSharedCLI();
```

## Testing

### Test Suite Results
All 54 tests passing:
```bash
$ node --test agile_bot/test/panel/test_*.js
# tests 54
# pass 54
# fail 0
```

### Extension Rebuild Process
```powershell
# 1. Navigate to panel directory
cd c:\dev\augmented-teams\agile_bot\src\panel

# 2. Package extension
npx @vscode/vsce package --allow-missing-repository

# 3. Uninstall old version
cursor --uninstall-extension agilebot.bot-panel

# 4. Install new version
cursor --install-extension bot-panel-0.1.35.vsix --force

# 5. Reload Cursor window
# Press Ctrl+Shift+P -> "Developer: Reload Window"
```

## How to Use the Fixed Panel

1. **Reload Cursor Window** (after installation):
   - Press `Ctrl+Shift+P` (Command Palette)
   - Type "Developer: Reload Window"
   - Press Enter

2. **Open the Panel**:
   - Press `Ctrl+Shift+P`
   - Type "View Bot Panel"
   - Press Enter

3. **Verify It Works**:
   - Panel should open without errors
   - Should display bot status, behaviors, scope, etc.
   - Check Output panel → "Bot Panel" for console logs

## Architecture Summary

### Singleton CLI Pattern
- **One CLI instance** shared across all views
- Initialized once in `BotPanel` constructor
- All views access via `PanelView.getCLI()`
- Cleaned up once when panel is disposed

### View Hierarchy
```
BotPanel (controller)
└─ BotView (orchestrator)
    ├─ BotHeaderView
    ├─ PathsSection
    ├─ BehaviorsView
    ├─ ScopeSection
    └─ InstructionsSection
```

### Data Flow
1. `BotPanel` initializes singleton CLI on startup
2. Each view calls `this.execute('status')` to fetch data
3. `PanelView.execute()` uses the singleton CLI
4. Views render HTML based on CLI responses
5. CLI is cleaned up when panel is disposed

## Benefits

- ✅ **Single CLI subprocess** - No more multiple processes
- ✅ **Simplified constructors** - Views don't need CLI/workspace/bot params
- ✅ **Self-contained views** - Each view fetches its own data
- ✅ **Easier testing** - Singleton pattern aligns with test architecture
- ✅ **Better resource management** - One process to manage

## Extension Version

**Package:** `agilebot.bot-panel`  
**Version:** `0.1.35`  
**VSIX:** `bot-panel-0.1.35.vsix`

## Next Steps

If you encounter any issues:
1. Check Output panel → "Bot Panel" for logs
2. Check Developer Tools console (Help → Toggle Developer Tools)
3. Verify Python is installed and CLI is accessible
4. Verify `BOT_DIRECTORY` env var or default path exists

---

**Fixed:** 2026-01-14  
**Status:** ✅ Ready for Production
