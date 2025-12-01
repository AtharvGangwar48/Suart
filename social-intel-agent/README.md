# Social Intelligence Agent

A comprehensive social media analysis tool that extracts, analyzes, and reports on social media content.

## Features

- Multi-platform social media scraping
- Text sentiment and toxicity analysis
- Media content analysis (images, videos, audio)
- Risk scoring and intelligence reporting
- Async processing with queue management

## Setup

1. Copy `.env.example` to `.env` and configure
2. Install dependencies: `pip install -r requirements.txt`
3. Run with Docker: `docker-compose up`

## API Endpoints

- `POST /analyze` - Analyze social media content
- `GET /health` - Health check