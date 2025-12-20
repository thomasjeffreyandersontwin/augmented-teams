# PowerShell script to keep AI assistant running continuously using Windows UI automation
# Usage: .\keep_going.ps1 [-Interval 60] [-Message "continue"] [-MaxIterations 100] [-WindowTitle "Cursor"]

param(
    [int]$Interval = 60,
    [string]$Message = "continue",
    [int]$MaxIterations = 0,  # 0 = infinite
    [string]$WindowTitle = "Cursor"  # Window title to send keystrokes to
)

# Load Windows Forms assembly for SendKeys
Add-Type -AssemblyName System.Windows.Forms

function Send-Keystrokes {
    param([string]$Text)
    
    # Send the text
    [System.Windows.Forms.SendKeys]::SendWait($Text)
    # Send Enter to submit
    [System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
}

function Activate-Window {
    param([string]$Title)
    
    # Try to find and activate the window
    $window = Get-Process | Where-Object { $_.MainWindowTitle -like "*$Title*" } | Select-Object -First 1
    if ($window) {
        # Bring window to foreground
        Add-Type -TypeDefinition @"
        using System;
        using System.Runtime.InteropServices;
        public class Win32 {
            [DllImport("user32.dll")]
            public static extern bool SetForegroundWindow(IntPtr hWnd);
            [DllImport("user32.dll")]
            public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
        }
"@
        [Win32]::ShowWindow($window.MainWindowHandle, 3)  # SW_MAXIMIZE = 3
        [Win32]::SetForegroundWindow($window.MainWindowHandle)
        Start-Sleep -Milliseconds 200  # Give window time to activate
        return $true
    }
    return $false
}

$iteration = 0
$startTime = Get-Date

Write-Host "[$startTime] Starting keep-alive loop (interval: $Interval seconds)" -ForegroundColor Green
Write-Host "[$startTime] Message: '$Message'" -ForegroundColor Green
Write-Host "[$startTime] Target window: '$WindowTitle'" -ForegroundColor Green
if ($MaxIterations -gt 0) {
    Write-Host "[$startTime] Will stop after $MaxIterations iterations" -ForegroundColor Yellow
}
Write-Host "[$startTime] Press Ctrl+C to stop`n" -ForegroundColor Cyan
Write-Host "[$startTime] Make sure the chat input is focused before starting!`n" -ForegroundColor Yellow

# Wait a few seconds to allow user to focus the chat input
Write-Host "[$startTime] Starting in 3 seconds... Focus the chat input now!" -ForegroundColor Cyan
Start-Sleep -Seconds 3

try {
    while ($true) {
        if ($MaxIterations -gt 0 -and $iteration -ge $MaxIterations) {
            Write-Host "`n[$(Get-Date)] Reached max iterations ($MaxIterations), stopping" -ForegroundColor Yellow
            break
        }
        
        $iteration++
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Write-Host "[$timestamp] Iteration $iteration : Sending '$Message'" -ForegroundColor Gray
        
        # Try to activate the window (optional, user should have it focused)
        # Activate-Window -Title $WindowTitle | Out-Null
        
        # Send the keystrokes
        Send-Keystrokes -Text $Message
        
        Write-Host "[$timestamp] Keystrokes sent, waiting $Interval seconds..." -ForegroundColor DarkGray
        
        Start-Sleep -Seconds $Interval
    }
} catch {
    Write-Host "`n[$(Get-Date)] Stopped by user after $iteration iterations" -ForegroundColor Yellow
    Write-Host "Error: $_" -ForegroundColor Red
}















