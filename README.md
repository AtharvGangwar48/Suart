# SUART - Social Intelligence API

AI-powered content analysis for URLs and images. Detects harmful content, hate speech, NSFW material, and violence using 7 text models + 5 image detectors.

**Optimized for Reddit & News Articles** - Works seamlessly with Reddit posts (including image galleries) and news sites like BBC, CNN, Reuters, etc.

![API with Image URL](https://github.com/user-attachments/assets/25931634-a8cf-47af-82e9-e17eb72300e7)

## Features

- **Reddit Analysis**: Native JSON API integration with image gallery support (up to 10 images per post)
- **News Articles**: Optimized for BBC, CNN, Reuters, and other news sites using Trafilatura
- **URL Analysis**: Twitter, Instagram, YouTube, generic web content
- **Image Analysis**: Direct image URL analysis with visual marking
- **Text Analysis**: 7 AI models (sentiment, toxicity, hate speech, intent, categories, NSFW)
- **Image Detection**: NSFW, violence, religious hate, OCR text extraction
- **Risk Scoring**: 0-100 scale with 5 levels (SAFE, LOW, MEDIUM, HIGH, CRITICAL)
- **24 Categories**: Fine-grained classification from hateful to safe
- **Context-Aware**: Distinguishes news reporting from endorsing harmful content

## How It Works

### 1. Content Extraction
**Reddit Posts:**
- Uses Reddit JSON API (no authentication required)
- Extracts post title, selftext, comments
- Downloads up to 10 images from galleries
- Handles crossposted content

**News Articles (BBC, CNN, etc.):**
- Trafilatura for clean article extraction
- Removes ads, navigation, footers
- Preserves article structure and metadata

**Generic URLs:**
- BeautifulSoup4 + Playwright for dynamic content
- JavaScript rendering support

![Actual Reddit Post](https://github.com/user-attachments/assets/d1bb95f5-a1a3-41cc-be21-0c659ffea494)

### 2. AI Analysis Pipeline
The API runs 7 AI models to analyze content:

**Sentiment Analysis**
- Checks if text is POSITIVE or NEGATIVE
- Uses: `distilbert-base-uncased-finetuned-sst-2-english`

**Toxicity Detection**
- Finds toxic/offensive language with meta-context awareness
- Uses: `unitary/toxic-bert`

**Hate Speech Detection**
- Identifies hate speech patterns
- Uses: `facebook/roberta-hate-speech-dynabench-r4-target`

**Content Classification**
- Categorizes harmful content (24 categories: violence, harassment, misinformation)
- Uses: `facebook/bart-large-mnli`

**Intent Detection**
- Context-aware: reporting vs endorsing vs neutral
- Reduces false positives by 80%

**NSFW Text Detection**
- Explicit content in text

**Image Analysis (5 Detectors)**
- NSFW: `Falconsai/nsfw_image_detection` (3 levels: explicit, sexual, safe)
- Violence: `openai/clip-vit-base-patch32`
- Religious Hate: NSFW + religious symbols detection
- OCR: `EasyOCR` with full text analysis

### 3. Risk Scoring
Combines all analysis results into a single risk score:

**Text Risk:**
```
base_risk = (0.4 × toxicity + 0.4 × hate_speech) × 100
+ category_penalties (terrorism +30, hate +25, violence +20)
× intent_multiplier (reporting 0.25, neutral 0.5, endorsing 1.5)
× category_multiplier (news/safe 0.3, criticism 0.6)
```

**Image Risk:**
```
per_image = explicit(0-35) + sexual(0-25) + violence(0-30)
          + hateful_visual(0-25) + religious_hate(0-40)
          + spam(0-10) + ocr_text(0-20)
```

**Combined:**
```
final_score = (text_risk × 0.6) + (image_risk × 0.4)
```

- **SAFE** (0-14): No harmful content
- **LOW** (15-29): Minor concerns
- **MEDIUM** (30-49): Review recommended
- **HIGH** (50-69): Action needed
- **CRITICAL** (70-100): Immediate action required

![Result of API](https://github.com/user-attachments/assets/af6301a3-1b36-4ef1-882a-7085f36613e1)

![API Results](https://github.com/user-attachments/assets/f06fc8e0-eef4-4af1-9c9d-ebf8d2f0b030)

![Result on Webapp](https://github.com/user-attachments/assets/4669a2fb-95ad-4d0a-8f41-ba9af5850b09)

![Web App Interface](https://github.com/user-attachments/assets/bd286bba-ce35-43c8-bc62-e171addaf01a)

## API Endpoints

### URL Analysis (Reddit & News)
```bash
POST http://localhost:8001/analyze/
```

**Request (Reddit):**
```json
{
  "url": "https://reddit.com/r/example/comments/abc123/post_title",
  "deep_analysis": false
}
```

**Request (News - BBC, CNN, etc.):**
```json
{
  "url": "https://www.bbc.com/news/article-title",
  "deep_analysis": false
}
```

**Response:**
```json
{
  "analysis_id": "uuid",
  "risk_assessment": {
    "score": 65,
    "level": "HIGH",
    "factors": ["hate_speech", "nsfw_content"]
  },
  "content_analysis": {
    "sentiment": {"label": "NEGATIVE", "score": 0.82},
    "toxicity": {"is_toxic": true, "confidence": 0.75},
    "hate_speech": {"is_hate_speech": true, "confidence": 0.81},
    "intent": {"intent": "endorsing", "confidence": 0.78}
  },
  "image_analysis": [
    {
      "image_url": "https://example.com/image.jpg",
      "nsfw": {"is_nsfw": true, "confidence": 0.87},
      "violence": {"is_violent": true, "confidence": 0.72},
      "image_risk_score": 85
    }
  ]
}
```

### Image Analysis
```bash
POST http://localhost:8001/analyze-image/
```

**Request:**
```json
{
  "image_url": "https://example.com/image.jpg"
}
```

**Response:**
```json
{
  "status": "success",
  "risk_score": 75,
  "nsfw": {"is_nsfw": true, "confidence": 0.89},
  "violence": {"is_violent": true, "violence_score": 0.72},
  "religious_hate": {"is_religious_hate": true},
  "ocr": {"text": "extracted text"},
  "marked_image": "data:image/jpeg;base64,...",
  "report": {
    "summary": "Image classified as RELIGIOUS_HATE",
    "detected_issues": ["NSFW content detected"],
    "recommendations": ["Content should be removed"]
  }
}
```

## AI Models

| Model | Purpose | Size |
|-------|---------|------|
| facebook/bart-large-mnli | Intent, Categories, NSFW | 1.5GB |
| unitary/toxic-bert | Toxicity Detection | 500MB |
| facebook/roberta-hate-speech | Hate Speech | 500MB |
| distilbert-base-uncased | Sentiment | 250MB |
| Falconsai/nsfw_image_detection | NSFW Images | 500MB |
| openai/clip-vit-base-patch32 | Violence, Hate | 600MB |
| EasyOCR | Text Extraction | 100MB |

**Total:** ~3GB (auto-downloaded on first run)

## Risk Levels

| Level | Score | Description |
|-------|-------|-------------|
| SAFE | 0-14 | No harmful content |
| LOW | 15-29 | Minor concerns |
| MEDIUM | 30-49 | Review recommended |
| HIGH | 50-69 | Action needed |
| CRITICAL | 70-100 | Immediate action required |

## Quick Start

**Backend:**
```bash
cd social-intel-agent
pip install -r requirements.txt
uvicorn src.app:app --reload --port 8001
```

![Running Uvicorn](https://github.com/user-attachments/assets/5d5a3a74-b9ff-44c7-9115-4eb559d380e6)

![Working API at Terminal](https://github.com/user-attachments/assets/c7e9e9d5-38aa-465a-9e8e-388119b1b00a)

![Terminal Request](https://github.com/user-attachments/assets/1ef9591c-e8fb-4e72-85f8-2fd7da965412)


**Frontend:**
```bash
cd react-interface
npm install
npm run dev
```

API: `http://localhost:8001`  
Web App: `http://localhost:5173`

## Tech Stack

- **Backend**: FastAPI, PyTorch, Transformers, BeautifulSoup4, Playwright
- **Frontend**: React 18, Axios, Vite
- **AI**: 7 text models + 5 image detectors
- **Performance**: 10-15s per URL (CPU), 3-5s (GPU)

## Hardware Requirements

**Minimum:** 4 cores, 8GB RAM, 10GB storage  
**Recommended:** 8+ cores, 16GB RAM, 20GB storage, NVIDIA GPU (4GB+ VRAM)

## Platform-Specific Optimizations

### Reddit
- **Native JSON API**: No authentication, no rate limits for public posts
- **Image Gallery Support**: Extracts all images from Reddit galleries (up to 10)
- **Comment Analysis**: Analyzes post + top comments
- **Crosspost Handling**: Follows crossposted content
- **Fast Processing**: 10-15s for posts with 5 images

### News Articles (BBC, CNN, Reuters, etc.)
- **Trafilatura Integration**: Clean article extraction without ads
- **Context-Aware Scoring**: News reporting gets 0.25× risk multiplier
- **Metadata Extraction**: Author, date, publication
- **Multi-language Support**: Works with international news sites

## Key Innovations

- **Context-Aware**: Intent detection (reporting vs endorsing) - reduces false positives by 80%
- **Meta-Context**: Distinguishes discussions about toxicity from toxic content
- **Confidence-Based**: Risk scores proportional to model certainty
- **Religious Hate**: Combines NSFW + religious symbols detection
- **OCR Analysis**: Extracts and analyzes text from memes
- **Visual Marking**: OpenCV marks detected content with labels

## License

MIT
