# MindCare AI - 1-Click Vercel Deployment Script (Zero Dependencies Required)
param (
    [Parameter(Mandatory=$false)]
    [string]$Token
)

if (-not $Token) {
    $Token = Read-Host "Paste your Vercel Access Token (from https://vercel.com/account/tokens)"
}

if (-not $Token) {
    Write-Host "Error: Token is required." -ForegroundColor Red
    exit 1
}

$teamId = "team_GStZHUIb52rKciP52dVDXyXU"
$projectId = "prj_aG8JzqDhHGcCTX9nf3PwZv5TGvhh"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "Reading project files..." -ForegroundColor Cyan
$htmlContent = [System.IO.File]::ReadAllText("$scriptDir\index.html")
$vercelJsonContent = [System.IO.File]::ReadAllText("$scriptDir\vercel.json")

$payload = @{
    name = "mindcare-ai"
    project = $projectId
    target = "production"
    files = @(
        @{
            file = "index.html"
            data = $htmlContent
            encoding = "utf-8"
        },
        @{
            file = "vercel.json"
            data = $vercelJsonContent
            encoding = "utf-8"
        }
    )
} | ConvertTo-Json -Depth 10

Write-Host "Deploying MindCare AI to Vercel production..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "https://api.vercel.com/v13/deployments?teamId=$teamId" `
        -Method Post `
        -Headers @{ "Authorization" = "Bearer $Token" } `
        -ContentType "application/json" `
        -Body $payload

    Write-Host "`nSUCCESS! Your MindCare AI app is live:" -ForegroundColor Green
    Write-Host "https://$($response.url)" -ForegroundColor Green -BackgroundColor Black
    Write-Host "Production Alias: https://mindcare-ai-anweshashaily21-gmailcoms-projects.vercel.app" -ForegroundColor Cyan
} catch {
    Write-Host "Deployment failed: $_" -ForegroundColor Red
}
