#!/bin/bash
echo ""
echo " ========================================"
echo "    CYBER RED LOCALHOST TERMINAL"
echo " ========================================"
echo ""
echo " Installing dependencies if needed..."
pip3 install -r requirements.txt > /dev/null 2>&1 || pip install -r requirements.txt > /dev/null 2>&1
echo ""
echo " Starting server..."
echo " (Opening browser...)"
echo ""
echo " Keep this terminal open while using the app."
echo " Press Ctrl+C to stop."
echo ""

# Try to open browser
if command -v xdg-open > /dev/null; then
  xdg-open http://127.0.0.1:5000 &
elif command -v open > /dev/null; then
  open http://127.0.0.1:5000 &
fi

python3 app.py || python app.py
