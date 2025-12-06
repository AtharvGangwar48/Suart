import React from 'react';
import './InfoSections.css';

function Docs() {
  return (
    <div className="info-section">
      <h2>📚 Documentation</h2>

      <div className="doc-section">
        <h3>API Endpoint</h3>
        <div className="code-block">
          POST http://localhost:8001/analyze/
        </div>
      </div>

      <div className="doc-section">
        <h3>Request Format</h3>
        <div className="code-block">
{`{
  "url": "https://www.reddit.com/r/technology/",
  "deep_analysis": false
}`}
        </div>
      </div>

      <div className="doc-section">
        <h3>Response Format</h3>
        <div className="code-block">
{`{
  "analysis_id": "uuid",
  "timestamp": "2024-01-01T12:00:00",
  "platform": "reddit",
  "status": "completed",
  "risk_assessment": {
    "level": "SAFE|WARNING|DANGEROUS|CRITICAL",
    "score": 0-20,
    "factors": ["negative_sentiment", "toxic_content"]
  },
  "content_analysis": {
    "sentiment": { "label": "POSITIVE|NEGATIVE", "score": 0-1 },
    "toxicity": { "is_toxic": boolean, "confidence": 0-1 },
    "hate_speech": { "is_hate_speech": boolean, "confidence": 0-1 },
    "content_categories": {
      "primary_category": "hateful|terror|religious|sexual|abusive|drug|spam|normal",
      "detected_categories": [],
      "category_scores": {}
    }
  }
}`}
        </div>
      </div>

      <div className="doc-section">
        <h3>Supported Platforms</h3>
        <ul>
          <li>✅ <strong>Reddit</strong> - Full support via JSON API</li>
          <li>✅ <strong>YouTube</strong> - Full support via yt-dlp</li>
          <li>✅ <strong>News Sites</strong> - Full support via trafilatura</li>
          <li>✅ <strong>Generic Web</strong> - Full support</li>
          <li>⚠️ <strong>Twitter/X</strong> - Limited (requires auth)</li>
          <li>⚠️ <strong>Instagram</strong> - Limited (requires auth)</li>
          <li>⚠️ <strong>TikTok</strong> - Limited (requires auth)</li>
        </ul>
      </div>

      <div className="doc-section">
        <h3>Risk Scoring</h3>
        <table className="risk-table">
          <thead>
            <tr>
              <th>Factor</th>
              <th>Points</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Negative Sentiment</td><td>+2</td></tr>
            <tr><td>Toxic Content</td><td>+5</td></tr>
            <tr><td>Hate Speech</td><td>+8</td></tr>
            <tr><td>Terror/Violence</td><td>+10</td></tr>
            <tr><td>Drug Content</td><td>+7</td></tr>
            <tr><td>Sexual Content</td><td>+6</td></tr>
            <tr><td>Religious Extremism</td><td>+6</td></tr>
            <tr><td>Abusive Language</td><td>+5</td></tr>
            <tr><td>Spam</td><td>+3</td></tr>
          </tbody>
        </table>
        <p><strong>Risk Levels:</strong> SAFE (0-3), WARNING (4-7), DANGEROUS (8-9), CRITICAL (10+)</p>
      </div>
    </div>
  );
}

export default Docs;
