# Rebuild and reinstall Bot Panel extension
# Usage: .\rebuild.ps1

Write-Host "Cleaning up old VSIX files..." -ForegroundColor Cyan
Remove-Item *.vsix -ErrorAction SilentlyContinue

Write-Host "Packaging extension..." -ForegroundColor Cyan
npx @vscode/vsce package --allow-missing-repository

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Packaging failed!" -ForegroundColor Red
    exit 1
}

Write-Host "Finding latest VSIX..." -ForegroundColor Cyan
$vsix = Get-ChildItem -Filter *.vsix | Select-Object -First 1

if ($vsix) {
    Write-Host "Uninstalling old extensions (if exist)..." -ForegroundColor Cyan
    cursor --uninstall-extension agilebot.bot-panel 2>$null
    cursor --uninstall-extension agilebot.repl-status-panel 2>$null
    
    Write-Host "Installing $($vsix.Name)..." -ForegroundColor Cyan
    cursor --install-extension $vsix.FullName --force
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`nExtension rebuilt and installed!" -ForegroundColor Green
        Write-Host "Reload Cursor window to activate changes (Ctrl+R or Cmd+R)" -ForegroundColor Yellow
    } else {
        Write-Host "ERROR: Installation failed!" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "ERROR: No VSIX file found" -ForegroundColor Red
    exit 1
}
