@echo off
title Cyber Red Terminal
color 0C
echo.
echo  ========================================
echo     CYBER RED LOCALHOST TERMINAL
echo  ========================================
echo.
echo  Installing dependencies if needed...
pip install -r requirements.txt >nul 2>&1
echo.
echo  Starting server...
echo  (A browser window should open automatically)
echo.
echo  Keep this window open while using the app.
echo  Press Ctrl+C to stop the server.
echo.
start http://127.0.0.1:5000
python app.py
pause
