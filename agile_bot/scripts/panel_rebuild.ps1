# Rebuild and reinstall Bot Panel extension
# Usage: .\panel_rebuild.ps1

$ErrorActionPreference = 'Stop'

# Navigate to panel directory using relative paths
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$panelDir = Join-Path (Join-Path $scriptDir "src") "panel"
Set-Location $panelDir

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
    Write-Host "Uninstalling old extension (if exists)..." -ForegroundColor Cyan
    code --uninstall-extension agilebot.bot-panel 2>$null
    
    Write-Host "Installing $($vsix.Name)..." -ForegroundColor Cyan
    code --install-extension $vsix.FullName --force
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`nExtension rebuilt and installed!" -ForegroundColor Green
        Write-Host "Reload VS Code window to activate changes (Ctrl+R or Cmd+R)" -ForegroundColor Yellow
    } else {
        Write-Host "ERROR: Installation failed!" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "ERROR: No VSIX file found" -ForegroundColor Red
    exit 1
}
