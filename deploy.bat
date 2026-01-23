@echo off
REM Docker Deployment Script for E-Commerce Delivery Prediction
REM This script sets up and runs the application with Docker

echo.
echo ============================================
echo E-Commerce Delivery Delay Predictor
echo Docker Deployment Setup
echo ============================================
echo.

REM Check if Docker is installed
docker --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker is not installed or not in PATH
    echo Please install Docker Desktop: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

REM Check if Docker Compose is installed
docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker Compose is not installed
    echo Please install Docker Desktop which includes Docker Compose
    pause
    exit /b 1
)

echo ✓ Docker found: 
docker --version
echo ✓ Docker Compose found: 
docker-compose --version
echo.

REM Check if model file exists
if not exist "model\delivery_deay_model.pkl" (
    if not exist "delivery_delay_model.pkl" (
        echo ERROR: Model file not found!
        echo Expected: model\delivery_deay_model.pkl
        pause
        exit /b 1
    )
)
echo ✓ Model file found
echo.

REM Build Docker images
echo Building Docker images (this may take 2-3 minutes)...
docker-compose build

if errorlevel 1 (
    echo ERROR: Docker build failed
    echo Check the logs above for details
    pause
    exit /b 1
)

echo.
echo ============================================
echo Build successful! Starting services...
echo ============================================
echo.

REM Start services
docker-compose up -d

if errorlevel 1 (
    echo ERROR: Failed to start services
    docker-compose logs
    pause
    exit /b 1
)

echo.
echo ✓ Services started successfully!
echo.
echo ============================================
echo Access the applications:
echo ============================================
echo.
echo FastAPI Documentation:  http://localhost:8000/docs
echo Streamlit UI:           http://localhost:8501
echo.
echo ============================================
echo Useful Commands:
echo ============================================
echo.
echo View logs:               docker-compose logs -f
echo View API logs:           docker-compose logs -f api
echo View Streamlit logs:     docker-compose logs -f streamlit
echo Stop services:           docker-compose down
echo.
echo For more info, see DEPLOYMENT.md
echo.
pause
