# Social Intelligence API

## Overview
API that analyzes social media content for harmful language, sentiment, and risk assessment.

![API Interface](https://github.com/user-attachments/assets/6fa2ac8d-c3a9-43f9-8801-d9b602a2bc72)
![Result on Webapp](https://github.com/user-attachments/assets/a069a374-f9c3-4797-b2e6-ec94f4a5e2be)
)

## How It Works

![API Working](https://github.com/user-attachments/assets/c3ff8272-eaf4-4d3f-b84c-eeb1af353334)

### 1. Content Extraction
- Takes a URL (Twitter, Reddit, YouTube, etc.)
- Scrapes and extracts text content from the page

![Actual Reddit Post](https://github.com/user-attachments/assets/d1bb95f5-a1a3-41cc-be21-0c659ffea494)

### 2. AI Analysis Pipeline
The API runs 4 AI models to check and analyze words:

**Sentiment Analysis**
- Checks if text is POSITIVE or NEGATIVE
- Uses: `distilbert-base-uncased-finetuned-sst-2-english`

**Toxicity Detection**
- Finds toxic/offensive language
- Uses: `unitary/toxic-bert`

**Hate Speech Detection**
- Identifies hate speech patterns
- Uses: `facebook/roberta-hate-speech-dynabench-r4-target`

**Content Classification**
- Categorizes harmful content (violence, harassment, misinformation)
- Uses: `facebook/bart-large-mnli`

### 3. Risk Scoring
Combines all analysis results into a single risk score:
- **LOW** (0-30): Safe content
- **MEDIUM** (31-60): Potentially concerning
- **HIGH** (61-100): Harmful content detected

![Result of API](https://github.com/user-attachments/assets/af6301a3-1b36-4ef1-882a-7085f36613e1)

## API Endpoint

```
POST /analyze/
```

**Request:**
```json
{
  "url": "https://twitter.com/example/status/123",
  "deep_analysis": false
}
```

**Response:**
```json
{
  "analysis_id": "uuid",
  "risk_assessment": {
    "level": "LOW|MEDIUM|HIGH",
    "score": 25
  },
  "content_analysis": {
    "sentiment": {"label": "POSITIVE", "score": 0.95},
    "toxicity": {"is_toxic": false, "confidence": 0.12},
    "hate_speech": {"is_hate_speech": false, "confidence": 0.08},
    "content_categories": {"is_flagged": false}
  },
  "summary": "Risk Level: LOW | Sentiment: POSITIVE"
}
```

## Tech Stack
- **Backend**: FastAPI (Python)
- **AI Models**: Hugging Face Transformers
- **Frontend**: React
- **Scraping**: BeautifulSoup4, Playwright

## Quick Start

**Backend:**
```bash
cd social-intel-agent
pip install -r requirements.txt
uvicorn src.app:app --reload
```

![Running Uvicorn](https://github.com/user-attachments/assets/5d5a3a74-b9ff-44c7-9115-4eb559d380e6)

![Working API at Terminal](https://github.com/user-attachments/assets/c7e9e9d5-38aa-465a-9e8e-388119b1b00a)

**Frontend:**
```bash
cd react-frontend
npm install
npm start
```

API runs on `http://localhost:8000`
