# Docker Deployment Script for E-Commerce Delivery Prediction
# PowerShell version

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "E-Commerce Delivery Delay Predictor" -ForegroundColor Cyan
Write-Host "Docker Deployment Setup" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Check if Docker is installed
try {
    $dockerVersion = docker --version
    Write-Host "✓ Docker found: $dockerVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Docker is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Docker Desktop: https://www.docker.com/products/docker-desktop" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if Docker Compose is installed
try {
    $composeVersion = docker-compose --version
    Write-Host "✓ Docker Compose found: $composeVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Docker Compose is not installed" -ForegroundColor Red
    Write-Host "Please install Docker Desktop which includes Docker Compose" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Check if model file exists
$modelPath1 = "model\delivery_deay_model.pkl"
$modelPath2 = "delivery_delay_model.pkl"

if (-not (Test-Path $modelPath1) -and -not (Test-Path $modelPath2)) {
    Write-Host "ERROR: Model file not found!" -ForegroundColor Red
    Write-Host "Expected: $modelPath1" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✓ Model file found" -ForegroundColor Green
Write-Host ""

# Build Docker images
Write-Host "Building Docker images (this may take 2-3 minutes)..." -ForegroundColor Yellow
docker-compose build

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Docker build failed" -ForegroundColor Red
    Write-Host "Check the logs above for details" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Build successful! Starting services..." -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Start services
docker-compose up -d

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to start services" -ForegroundColor Red
    docker-compose logs
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "✓ Services started successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Access the applications:" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "FastAPI Documentation:  " -NoNewLine -ForegroundColor White
Write-Host "http://localhost:8000/docs" -ForegroundColor Yellow
Write-Host "Streamlit UI:           " -NoNewLine -ForegroundColor White
Write-Host "http://localhost:8501" -ForegroundColor Yellow
Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Useful Commands:" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "View logs:               " -NoNewLine
Write-Host "docker-compose logs -f" -ForegroundColor Cyan
Write-Host "View API logs:           " -NoNewLine
Write-Host "docker-compose logs -f api" -ForegroundColor Cyan
Write-Host "View Streamlit logs:     " -NoNewLine
Write-Host "docker-compose logs -f streamlit" -ForegroundColor Cyan
Write-Host "Stop services:           " -NoNewLine
Write-Host "docker-compose down" -ForegroundColor Cyan
Write-Host ""
Write-Host "For more info, see DEPLOYMENT.md" -ForegroundColor Green
Write-Host ""
