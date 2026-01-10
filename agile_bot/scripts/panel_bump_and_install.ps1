# Bump version, rebuild, and reinstall the Bot Panel extension
# Usage: .\panel_bump_and_install.ps1 [patch|minor|major]
# Default: patch (0.1.0 -> 0.1.1)

param(
    [ValidateSet('patch', 'minor', 'major')]
    [string]$BumpType = 'patch'
)

$ErrorActionPreference = 'Stop'

# Navigate to panel directory using relative paths
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$panelDir = Join-Path (Join-Path $scriptDir "src") "panel"
Set-Location $panelDir

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Bot Panel Version Bump" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Read current version from package.json
$packageJson = Get-Content "package.json" -Raw | ConvertFrom-Json
$currentVersion = $packageJson.version
Write-Host "Current version: $currentVersion" -ForegroundColor Yellow

# Parse version
$versionParts = $currentVersion -split '\.'
$major = [int]$versionParts[0]
$minor = [int]$versionParts[1]
$patch = [int]$versionParts[2]

# Bump version based on type
switch ($BumpType) {
    'major' { 
        $major++
        $minor = 0
        $patch = 0
    }
    'minor' { 
        $minor++
        $patch = 0
    }
    'patch' { 
        $patch++
    }
}

$newVersion = "$major.$minor.$patch"
Write-Host "New version:     $newVersion" -ForegroundColor Green
Write-Host ""

# Update package.json
Write-Host "[1/6] Updating package.json..." -ForegroundColor Cyan
$packageJsonContent = Get-Content "package.json" -Raw
$packageJsonContent = $packageJsonContent -replace "`"version`": `"$currentVersion`"", "`"version`": `"$newVersion`""
Set-Content "package.json" -Value $packageJsonContent -NoNewline
Write-Host "      Done: package.json updated" -ForegroundColor Green

# Package extension
Write-Host "[2/6] Packaging extension..." -ForegroundColor Cyan
npx @vscode/vsce package --allow-missing-repository --allow-star-activation | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "      ERROR: Packaging failed!" -ForegroundColor Red
    exit 1
}
Write-Host "      Done: Extension packaged: bot-panel-$newVersion.vsix" -ForegroundColor Green

# Uninstall old extension
Write-Host "[3/6] Uninstalling old extension..." -ForegroundColor Cyan
code --uninstall-extension agilebot.bot-panel | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "      Warning: Uninstall warning (may not be installed)" -ForegroundColor Yellow
} else {
    Write-Host "      Done: Old extension uninstalled" -ForegroundColor Green
}

# Install new extension
Write-Host "[4/6] Installing new extension..." -ForegroundColor Cyan
$vsixPath = Join-Path $panelDir "bot-panel-$newVersion.vsix"
$vsixPath = (Resolve-Path $vsixPath).Path
code --install-extension "$vsixPath" | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "      ERROR: Installation failed!" -ForegroundColor Red
    exit 1
}
Write-Host "      Done: Extension v$newVersion installed" -ForegroundColor Green

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "SUCCESS!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Extension upgraded: $currentVersion -> $newVersion" -ForegroundColor Green
Write-Host ""
Write-Host "[5/6] Please reload VS Code window manually:" -ForegroundColor Cyan
Write-Host "      Press Ctrl+Shift+P -> Developer: Reload Window" -ForegroundColor Yellow
Write-Host ""
Write-Host "Extension v$newVersion will be active after reload!" -ForegroundColor Green
Write-Host ""
