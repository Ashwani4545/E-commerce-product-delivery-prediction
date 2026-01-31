@echo off
echo ====================================
echo Starting Streamlit App
echo ====================================
echo.
echo App will open in your browser at: http://localhost:8501
echo Make sure FastAPI server is running first!
echo.
echo Press Ctrl+C to stop the app
echo.

cd /d "%~dp0"
C:\Users\DELL\AppData\Local\Python\pythoncore-3.10-64\python.exe -m streamlit run app/streamlit_app.py
pause
