# Reinstall the AgilBot Status Panel Extension

Write-Host "Reinstalling AgilBot Status Panel Extension..." -ForegroundColor Cyan

# Get the extension directory
$extensionDir = $PSScriptRoot

# Uninstall existing extension
Write-Host "Uninstalling existing extension..." -ForegroundColor Yellow
cursor --uninstall-extension agilebot.repl-status-panel 2>$null

# Wait a moment
Start-Sleep -Seconds 1

# Package the extension
Write-Host "Packaging extension..." -ForegroundColor Yellow
if (Get-Command npx -ErrorAction SilentlyContinue) {
    npx @vscode/vsce package --allow-missing-repository --no-yarn
    if ($LASTEXITCODE -eq 0) {
        # Find the .vsix file
        $vsixFile = Get-ChildItem -Path $extensionDir -Filter "*.vsix" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
        
        if ($vsixFile) {
            Write-Host "Installing extension from: $($vsixFile.FullName)" -ForegroundColor Yellow
            cursor --install-extension $vsixFile.FullName
        } else {
            Write-Host "ERROR: Could not find .vsix file after packaging" -ForegroundColor Red
            exit 1
        }
    } else {
        Write-Host "ERROR: Packaging failed" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "ERROR: npx not found. Please install Node.js" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Installation complete!" -ForegroundColor Green
Write-Host "Please reload Cursor window (Ctrl+Shift+P -> 'Reload Window') to activate changes." -ForegroundColor Cyan

