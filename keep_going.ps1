# PowerShell script to keep AI assistant running continuously
# Usage: .\keep_going.ps1 [-Interval 60] [-Message "continue"] [-MaxIterations 100]

param(
    [int]$Interval = 60,
    [string]$Message = "continue",
    [int]$MaxIterations = 0  # 0 = infinite
)

$iteration = 0
$startTime = Get-Date

Write-Host "[$startTime] Starting keep-alive loop (interval: $Interval seconds)" -ForegroundColor Green
Write-Host "[$startTime] Message: '$Message'" -ForegroundColor Green
if ($MaxIterations -gt 0) {
    Write-Host "[$startTime] Will stop after $MaxIterations iterations" -ForegroundColor Yellow
}
Write-Host "[$startTime] Press Ctrl+C to stop`n" -ForegroundColor Cyan

try {
    while ($true) {
        if ($MaxIterations -gt 0 -and $iteration -ge $MaxIterations) {
            Write-Host "`n[$(Get-Date)] Reached max iterations ($MaxIterations), stopping" -ForegroundColor Yellow
            break
        }
        
        $iteration++
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Write-Host "[$timestamp] Iteration $iteration : $Message" -ForegroundColor Gray
        
        # TODO: Integrate with your chat interface to actually send the message
        # Example: Send-ChatMessage -Message $Message
        
        Start-Sleep -Seconds $Interval
    }
} catch {
    Write-Host "`n[$(Get-Date)] Stopped by user after $iteration iterations" -ForegroundColor Yellow
}















