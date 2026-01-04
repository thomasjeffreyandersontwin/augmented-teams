# REPL Status Panel Extension Build Script
# Packages extension into .vsix file for VS Code installation

Write-Host "Building REPL Status Panel Extension..." -ForegroundColor Cyan

# Get the directory where this script is located
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Check if vsce is installed
$vsceInstalled = Get-Command vsce -ErrorAction SilentlyContinue

if (-not $vsceInstalled) {
    Write-Host "vsce (VS Code Extension Manager) not found." -ForegroundColor Yellow
    Write-Host "Installing vsce globally..." -ForegroundColor Yellow
    npm install -g @vscode/vsce
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Failed to install vsce. Please install manually:" -ForegroundColor Red
        Write-Host "  npm install -g @vscode/vsce" -ForegroundColor Red
        exit 1
    }
}

# Clean up old .vsix files
Write-Host "Cleaning up old builds..." -ForegroundColor Yellow
Remove-Item -Path "*.vsix" -ErrorAction SilentlyContinue

# Package the extension
Write-Host "Packaging extension..." -ForegroundColor Yellow
vsce package --allow-star-activation

if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to package extension." -ForegroundColor Red
    exit 1
}

# Find the generated .vsix file
$vsixFile = Get-ChildItem -Filter "*.vsix" | Select-Object -First 1

if ($vsixFile) {
    Write-Host "Extension packaged successfully: $($vsixFile.Name)" -ForegroundColor Green
    Write-Host ""
    Write-Host "To install in CURSOR, run:" -ForegroundColor Cyan
    Write-Host "  cursor --install-extension $($vsixFile.Name)" -ForegroundColor White
    Write-Host ""
    Write-Host "To install in VS Code, run:" -ForegroundColor Cyan
    Write-Host "  code --install-extension $($vsixFile.Name)" -ForegroundColor White
    Write-Host ""
    Write-Host "Or via UI:" -ForegroundColor Cyan
    Write-Host "  1. Press Ctrl+Shift+P" -ForegroundColor White
    Write-Host "  2. Type 'Extensions: Install from VSIX'" -ForegroundColor White
    Write-Host "  3. Select: $($vsixFile.Name)" -ForegroundColor White
    Write-Host ""
    Write-Host "After installation, reload the window:" -ForegroundColor Yellow
    Write-Host "  Ctrl+Shift+P -> 'Developer: Reload Window'" -ForegroundColor White
} else {
    Write-Host "No .vsix file found after build." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Build complete!" -ForegroundColor Green
