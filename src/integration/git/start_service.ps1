# Git Commit Service Startup Script
Write-Host "Starting Git Commit REST Service..." -ForegroundColor Green

# Change to the git integration directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "Working directory: $(Get-Location)" -ForegroundColor Yellow

# Install requirements
Write-Host "Installing dependencies..." -ForegroundColor Yellow
try {
    python -m pip install -r requirements.txt
    Write-Host "✅ Dependencies installed" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to install dependencies: $_" -ForegroundColor Red
    exit 1
}

# Start the service
Write-Host "Starting FastAPI service on port 8001..." -ForegroundColor Yellow
try {
    python git_commit.py
} catch {
    Write-Host "❌ Service failed to start: $_" -ForegroundColor Red
    exit 1
}
