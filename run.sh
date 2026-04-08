#!/bin/bash

echo "🚀 Starting SUART"

# Cleanup
lsof -ti:8001 | xargs kill -9 2>/dev/null || true
lsof -ti:5173 | xargs kill -9 2>/dev/null || true

# Backend
cd "$(dirname "$0")/social-intel-agent"
source venv/bin/activate
uvicorn src.app:app --port 8001 &
BACKEND_PID=$!

sleep 3

# Frontend
cd ../react-interface
npm run dev &
FRONTEND_PID=$!

echo ""
echo "✅ Running at http://localhost:5173"
echo "Press Ctrl+C to stop"

trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT
wait
