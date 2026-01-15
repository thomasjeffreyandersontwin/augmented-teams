# Rebuild and reinstall Bot Panel extension
# Usage: .\panel_rebuild.ps1 [patch|minor|major]
# Default: patch (0.1.0 -> 0.1.1)

param(
    [ValidateSet('patch', 'minor', 'major')]
    [string]$BumpType = 'patch'
)

$ErrorActionPreference = 'Stop'

# Navigate to panel directory using relative paths
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Split-Path -Parent $scriptDir
$panelDir = Join-Path (Join-Path $repoRoot "src") "panel"
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
$packageJsonPath = Join-Path $panelDir "package.json"
$packageJsonContent = Get-Content $packageJsonPath -Raw
$packageJsonContent = $packageJsonContent -replace "`"version`": `"$currentVersion`"", "`"version`": `"$newVersion`""

# Write without BOM to avoid vsce JSON parse errors
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$maxRetries = 3
$retryCount = 0
$writeSuccess = $false
while ($retryCount -lt $maxRetries -and -not $writeSuccess) {
    try {
        [System.IO.File]::WriteAllText($packageJsonPath, $packageJsonContent, $utf8NoBom)
        Start-Sleep -Milliseconds 100  # Give filesystem time to flush
        $writeSuccess = $true
    } catch {
        $retryCount++
        if ($retryCount -lt $maxRetries) {
            Write-Host "      Warning: File locked, retrying in 1 second... (attempt $retryCount/$maxRetries)" -ForegroundColor Yellow
            Start-Sleep -Seconds 1
        } else {
            Write-Host "      ERROR: Could not update package.json - file may be locked. Please close it and try again." -ForegroundColor Red
            exit 1
        }
    }
}

# Verify the version was actually updated
$verifyContent = Get-Content $packageJsonPath -Raw
if ($verifyContent -match "`"version`": `"$newVersion`"") {
    Write-Host "      Done: package.json updated to v$newVersion" -ForegroundColor Green
} else {
    Write-Host "      ERROR: package.json update verification failed!" -ForegroundColor Red
    Write-Host "      Expected version: $newVersion" -ForegroundColor Yellow
    Write-Host "      package.json may be open in editor - please close it and try again" -ForegroundColor Yellow
    exit 1
}


Write-Host "[2/4] Cleaning up old VSIX files..." -ForegroundColor Cyan
Get-ChildItem -Filter "*.vsix" | Remove-Item -Force -ErrorAction SilentlyContinue
Write-Host "      Done: Old VSIX files removed" -ForegroundColor Green

Write-Host "[3/4] Packaging extension..." -ForegroundColor Cyan
$packageOutput = npx @vscode/vsce package --allow-missing-repository --allow-star-activation 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "      ERROR: Packaging failed!" -ForegroundColor Red
    Write-Host "      Output: $packageOutput" -ForegroundColor Red
    exit 1
}

# Verify the VSIX file was created
$expectedVsix = "bot-panel-$newVersion.vsix"
if (-not (Test-Path $expectedVsix)) {
    Write-Host "      ERROR: VSIX file was not created: $expectedVsix" -ForegroundColor Red
    Write-Host "      Package output: $packageOutput" -ForegroundColor Yellow
    exit 1
}
Write-Host "      Done: Extension packaged: bot-panel-$newVersion.vsix" -ForegroundColor Green

Write-Host "[4/4] Uninstalling old extension..." -ForegroundColor Cyan
$cursorCli = "C:\Users\thoma\AppData\Local\Programs\cursor\resources\app\bin\cursor.cmd"
& $cursorCli --uninstall-extension agilebot.bot-panel | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "      Warning: Uninstall warning (may not be installed)" -ForegroundColor Yellow
} else {
    Write-Host "      Done: Old extension uninstalled" -ForegroundColor Green
}

# Also uninstall the old repl-status-panel if it exists
& $cursorCli --uninstall-extension agilebot.repl-status-panel | Out-Null

Write-Host "Installing new extension..." -ForegroundColor Cyan
$vsixPath = Join-Path $panelDir "bot-panel-$newVersion.vsix"
# Verify VSIX exists before installing
if (-not (Test-Path $vsixPath)) {
    Write-Host "      ERROR: VSIX file not found: $vsixPath" -ForegroundColor Red
    Write-Host "      Current directory: $(Get-Location)" -ForegroundColor Yellow
    Write-Host "      Files in directory:" -ForegroundColor Yellow
    Get-ChildItem -Filter "*.vsix" | ForEach-Object { Write-Host "        - $($_.Name)" -ForegroundColor Yellow }
    exit 1
}
$installOutput = & $cursorCli --install-extension "$vsixPath" --force 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "      ERROR: Installation failed!" -ForegroundColor Red
    Write-Host "      Output: $installOutput" -ForegroundColor Red
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
Write-Host "Reloading Cursor window..." -ForegroundColor Cyan

# Give extension time to register
Start-Sleep -Seconds 1

# Automate keyboard input to trigger reload
try {
    Add-Type -AssemblyName System.Windows.Forms
    
    # Find and focus Cursor window
    $cursorProcess = Get-Process | Where-Object { $_.ProcessName -eq "Cursor" -and $_.MainWindowTitle -ne "" } | Select-Object -First 1
    
    if ($cursorProcess) {
        # Focus the Cursor window
        $sig = '[DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr hWnd);'
        $type = Add-Type -MemberDefinition $sig -Name WindowAPI -PassThru
        $null = $type::SetForegroundWindow($cursorProcess.MainWindowHandle)
        
        Start-Sleep -Milliseconds 500
        
        # Send Ctrl+Shift+P to open command palette
        [System.Windows.Forms.SendKeys]::SendWait("^+p")
        
        Start-Sleep -Milliseconds 800
        
        # Type the reload command
        [System.Windows.Forms.SendKeys]::SendWait("Developer: Reload Window")
        
        Start-Sleep -Milliseconds 500
        
        # Press Enter
        [System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
        
        Write-Host "      Done: Cursor window reload triggered!" -ForegroundColor Green
    } else {
        Write-Host "      Warning: Could not find Cursor window. Please reload manually." -ForegroundColor Yellow
    }
} catch {
    Write-Host "      Warning: Automation failed. Please reload manually (Ctrl+Shift+P -> Developer: Reload Window)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Extension v$newVersion will be active after reload!" -ForegroundColor Green
Write-Host ""
    
