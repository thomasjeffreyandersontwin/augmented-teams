# View Refactor Complete

## Summary

Refactored ALL panel views to follow clean design principles:

### Before (Messy):
```javascript
// Constructor takes EVERYTHING
new BehaviorsView(behaviorsData, cli, workspaceDir, botDir, webview, extensionUri)

// Render uses instance data
render() {
    // Uses this.behaviorsData
}
```

### After (Clean):
```javascript
// Constructor takes ONLY UI concerns
new BehaviorsView(webview, extensionUri)

// Render gets OWN data from singleton CLI
async render() {
    const botData = await this.execute('status');
    const behaviorsData = botData.behaviors?.all_behaviors || [];
    // ... render HTML
}
```

## Changes

### PanelView (Base Class)
- **Singleton CLI**: All views share one CLI process
- **Static methods**: `initializeCLI()`, `getCLI()`, `getWorkspaceDir()`, `getBotDir()`
- **Simple constructor**: No parameters needed

### All Views Simplified
1. **BehaviorsView**: `constructor(webview, extensionUri)`
2. **ScopeSection**: `constructor(webview, extensionUri)`
3. **InstructionsSection**: `constructor(webview, extensionUri)`
4. **BotHeaderView**: `constructor(panelVersion, webview, extensionUri)`
5. **PathsSection**: `constructor()`
6. **BotView**: `constructor(panelVersion, webview, extensionUri)`

### Key Principles
- **Single Responsibility**: Views render HTML
- **Dependency Inversion**: Views depend on PanelView abstraction
- **No God Objects**: No massive parameter lists
- **Self-Contained**: Views get their own data
- **Async**: All `render()` methods are `async` and return `Promise<string>`

## Test Changes

Tests now:
1. Initialize singleton CLI: `PanelView.initializeCLI(workspaceDir, botDir)`
2. Create views: `new ScopeView(null, null)`
3. Render: `await view.render()` - gets data from REAL CLI
4. Assert on HTML

No mocking, no data injection. Clean integration tests.

## Benefits

✅ **No parameter passing hell**  
✅ **Views are self-contained**  
✅ **Easy to test** - just initialize CLI once  
✅ **Follows SOLID principles**  
✅ **Much simpler constructors**  
✅ **Single source of truth** (CLI)  

## Files Changed

**Production:**
- `agile_bot/src/panel/panel_view.js` - Singleton CLI
- `agile_bot/src/behaviors/behaviors_view.js`
- `agile_bot/src/scope/scope_view.js`
- `agile_bot/src/instructions/instructions_view.js`
- `agile_bot/src/bot/bot_header_view.js`
- `agile_bot/src/bot/paths_section.js`
- `agile_bot/src/bot/bot_view.js`

**Tests:**
- `agile_bot/test/panel/helpers/bot_view_test_helper.js`
- `agile_bot/test/panel/helpers/behaviors_view_test_helper.js`
- `agile_bot/test/panel/helpers/scope_view_test_helper.js`
- `agile_bot/test/panel/helpers/instructions_view_test_helper.js`
