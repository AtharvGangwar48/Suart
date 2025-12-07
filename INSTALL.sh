#!/bin/bash
set -e

echo "🚀 SUART Installation"
echo "===================="

# Backend
cd "$(dirname "$0")/social-intel-agent"

echo "📦 Setting up backend..."
[ -d "venv" ] && rm -rf venv
python3.11 -m venv venv || python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip setuptools wheel -q
pip install -r requirements.txt -q
playwright install chromium

echo "✅ Backend ready"

# Frontend
cd ../react-frontend
echo "📦 Setting up frontend..."
npm install

echo ""
echo "✅ Installation complete!"
echo ""
echo "Start: ./run.sh"
