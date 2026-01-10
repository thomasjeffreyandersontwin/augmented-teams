# Bot Panel Extension - Install/Uninstall Testing Guide

## Prerequisites

1. **VS Code Extension CLI (`vsce`)**:
   ```powershell
   npm install -g @vscode/vsce
   ```

2. **Extension Files** (should be in `agile_bot/src/panel/`):
   - `package.json` - Extension manifest
   - `extension.js` - Main entry point
   - `bot_panel.js` - Panel controller
   - `img/` - Images folder (optional)

## Quick Test Workflow

### Option 1: Development Mode (Recommended for Testing)

1. **Open extension folder in VS Code**:
   ```powershell
   cd agile_bot/src/panel
   code .
   ```

2. **Press F5** to launch Extension Development Host
   - Opens a new VS Code window with your extension loaded
   - Changes reload automatically (just reload the dev window with Ctrl+R)

3. **Test the extension**:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Type "View Bot Panel" or "agilebot.viewPanel"
   - Execute the command
   - Panel should open

4. **Check Debug Console** for any errors

**Pros:**
- Instant feedback
- No need to rebuild/reinstall
- Easy to debug

**Cons:**
- Only works in development host window

### Option 2: Build and Install (For Production Testing)

#### Step 1: Build Extension Package

```powershell
cd agile_bot/src/panel
npx @vscode/vsce package
```

This creates a `.vsix` file (e.g., `bot-panel-0.1.0.vsix`)

#### Step 2: Install Extension

**Method A: Install from VSIX file**
```powershell
code --install-extension bot-panel-0.1.0.vsix --force
```

**Method B: Install from command line (if using Cursor)**
```powershell
cursor --install-extension bot-panel-0.1.0.vsix --force
```

#### Step 3: Reload VS Code/Cursor

- Press `Ctrl+Shift+P` (or `Cmd+Shift+P`)
- Type "Developer: Reload Window"
- Press Enter

#### Step 4: Test Extension

- Press `Ctrl+Shift+P`
- Type "View Bot Panel" or "agilebot.viewPanel"
- Execute the command
- Panel should open

#### Step 5: Uninstall Extension

**Method A: Uninstall by ID**
```powershell
code --uninstall-extension agilebot.bot-panel
```

**Method B: Uninstall via UI**
1. Open Extensions view (`Ctrl+Shift+X`)
2. Search for "Bot Panel"
3. Click gear icon → "Uninstall"

**Method C: Uninstall via Command Palette**
1. Press `Ctrl+Shift+P`
2. Type "Extensions: Show Installed Extensions"
3. Find "Bot Panel"
4. Right-click → "Uninstall"

## Automated Build Script

Create `agile_bot/src/panel/rebuild.ps1`:

```powershell
# Rebuild and reinstall Bot Panel extension
# Usage: .\rebuild.ps1

Write-Host "Cleaning up old VSIX files..." -ForegroundColor Cyan
Remove-Item *.vsix -ErrorAction SilentlyContinue

Write-Host "Packaging extension..." -ForegroundColor Cyan
npx @vscode/vsce package --allow-missing-repository

Write-Host "Finding latest VSIX..." -ForegroundColor Cyan
$vsix = Get-ChildItem -Filter *.vsix | Select-Object -First 1

if ($vsix) {
    Write-Host "Installing $($vsix.Name)..." -ForegroundColor Cyan
    code --install-extension $vsix.FullName --force
    
    Write-Host "`nExtension rebuilt and installed!" -ForegroundColor Green
    Write-Host "Reload VS Code window to activate changes (Ctrl+R or Cmd+R)" -ForegroundColor Yellow
} else {
    Write-Host "ERROR: No VSIX file found" -ForegroundColor Red
    exit 1
}
```

Then run:
```powershell
.\rebuild.ps1
```

## Testing Checklist

### Install Test
- [ ] Extension packages without errors
- [ ] VSIX file is created
- [ ] Extension installs successfully
- [ ] Extension appears in Extensions list
- [ ] Command "agilebot.viewPanel" is available
- [ ] Panel opens when command is executed
- [ ] Panel displays status correctly

### Uninstall Test
- [ ] Extension uninstalls successfully
- [ ] Extension disappears from Extensions list
- [ ] Command "agilebot.viewPanel" is no longer available
- [ ] No leftover files in extension directory

### Reinstall Test
- [ ] Can uninstall and reinstall multiple times
- [ ] Version updates work correctly
- [ ] No conflicts with previous versions

## Troubleshooting

### Extension Not Appearing
- Check `package.json` has correct `name` and `publisher`
- Verify `main` field points to correct file
- Check for syntax errors in `extension.js`
- View Output panel → "Extension Host" for errors

### Command Not Found
- Verify `contributes.commands` in `package.json`
- Check command ID matches exactly
- Reload window after install

### Panel Not Opening
- Check `bot_panel.js` is correct
- Verify CLI script path is correct
- Check Python is available
- View Debug Console (F5 mode) or Output panel for errors

### VSIX Packaging Errors
- Ensure `package.json` is valid JSON
- Check all required fields are present
- Verify `main` file exists
- Run `npx @vscode/vsce package --allow-missing-repository` for warnings

## Extension ID Format

Your extension ID is: `{publisher}.{name}`

From `package.json`:
- `publisher`: "agilebot"
- `name`: "bot-panel"
- **Extension ID**: `agilebot.bot-panel`

Use this ID for uninstall commands:
```powershell
code --uninstall-extension agilebot.bot-panel
```
