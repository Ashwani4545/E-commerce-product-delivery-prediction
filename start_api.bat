@echo off
echo ====================================
echo Starting E-Commerce Prediction API
echo ====================================
echo.
echo API will be available at: http://localhost:8000
echo API Docs will be available at: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

cd /d "%~dp0"
C:\Users\DELL\AppData\Local\Python\pythoncore-3.10-64\python.exe -m uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
pause
