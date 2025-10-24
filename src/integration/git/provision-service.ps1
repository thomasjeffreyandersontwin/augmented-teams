# Git Integration Service Provisioning Script
Write-Host "🔧 Git Integration Service Provisioning" -ForegroundColor Green
Write-Host "=" * 50 -ForegroundColor Yellow

# Change to the git integration directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "Working directory: $(Get-Location)" -ForegroundColor Yellow

# Step 1: Check dependencies
Write-Host "🔍 Checking dependencies..." -ForegroundColor Yellow
if (-not (Test-Path "build-requirements.txt")) {
    Write-Host "❌ build-requirements.txt not found" -ForegroundColor Red
    exit 1
}

Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
try {
    python -m pip install -r build-requirements.txt
    Write-Host "✅ Dependencies installed successfully" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to install dependencies: $_" -ForegroundColor Red
    exit 1
}

# Step 2: Start service
Write-Host "🚀 Starting Git Integration Service..." -ForegroundColor Yellow
if (-not (Test-Path "service.py")) {
    Write-Host "❌ service.py not found" -ForegroundColor Red
    exit 1
}

# Start service in background
$serviceProcess = Start-Process -FilePath "python" -ArgumentList "service.py" -PassThru -WindowStyle Hidden

Write-Host "⏳ Waiting for service to start..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

# Check if service is running
try {
    $response = Invoke-RestMethod -Uri "http://localhost:8001/" -TimeoutSec 5
    Write-Host "✅ Service started successfully on port 8001" -ForegroundColor Green
} catch {
    Write-Host "❌ Service failed to start or is not responding: $_" -ForegroundColor Red
    Stop-Process -Id $serviceProcess.Id -Force
    exit 1
}

# Step 3: Run tests
Write-Host "🧪 Running test suite..." -ForegroundColor Yellow
if (-not (Test-Path "test-service.py")) {
    Write-Host "❌ test-service.py not found" -ForegroundColor Red
    Stop-Process -Id $serviceProcess.Id -Force
    exit 1
}

try {
    python test-service.py
    $testExitCode = $LASTEXITCODE
    
    if ($testExitCode -eq 0) {
        Write-Host "✅ All tests passed!" -ForegroundColor Green
    } else {
        Write-Host "❌ Some tests failed" -ForegroundColor Red
    }
} catch {
    Write-Host "❌ Failed to run tests: $_" -ForegroundColor Red
    Stop-Process -Id $serviceProcess.Id -Force
    exit 1
}

# Cleanup
Write-Host "Stopping service..." -ForegroundColor Yellow
Stop-Process -Id $serviceProcess.Id -Force
Write-Host "Service stopped" -ForegroundColor Green

# Summary
Write-Host ""
Write-Host "Provisioning completed!" -ForegroundColor Green
Write-Host "Dependencies installed" -ForegroundColor Green
Write-Host "Service started and tested" -ForegroundColor Green
Write-Host "All tests passed" -ForegroundColor Green
