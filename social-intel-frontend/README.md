# Social Intelligence Agent - Web Interface

A beautiful web interface for the Social Intelligence Agent API.

## Setup & Run

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Make sure the backend is running:**
```bash
# In the social-intel-agent directory
uvicorn src.app:app --reload --port=8001
```

3. **Run the frontend:**
```bash
python app.py
```

4. **Open browser:**
```
http://127.0.0.1:5000
```

## Features

- 🔍 **URL Analysis**: Analyze any social media URL
- 📊 **Risk Scoring**: Visual risk assessment (0-100%)
- 🎯 **Deep Analysis**: Toggle for comprehensive analysis
- ✅ **Health Monitoring**: Check backend system status
- 📱 **Responsive Design**: Works on all devices

## Usage

1. Enter a social media URL (Twitter/X, Instagram, etc.)
2. Choose analysis depth
3. Click "Analyze"
4. View results with risk score and findings