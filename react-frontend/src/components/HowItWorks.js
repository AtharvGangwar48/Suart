import React from 'react';
import './InfoSections.css';

function HowItWorks() {
  return (
    <div className="info-section">
      <h2>🚀 How It Works</h2>
      
      <div className="step-container">
        <div className="step">
          <div className="step-number">1</div>
          <h3>Enter URL</h3>
          <p>Paste any social media post URL (Reddit, YouTube, Twitter, etc.) or web article link</p>
        </div>

        <div className="step">
          <div className="step-number">2</div>
          <h3>AI Analysis</h3>
          <p>Our AI models analyze the content for sentiment, toxicity, hate speech, and categorize into 8 content types</p>
        </div>

        <div className="step">
          <div className="step-number">3</div>
          <h3>Risk Assessment</h3>
          <p>Content is scored and classified as SAFE, WARNING, DANGEROUS, or CRITICAL based on multiple factors</p>
        </div>

        <div className="step">
          <div className="step-number">4</div>
          <h3>Get Results</h3>
          <p>View detailed analysis with visual indicators, confidence scores, and content categories</p>
        </div>
      </div>

      <div className="features">
        <h3>✨ Key Features</h3>
        <ul>
          <li>🎯 <strong>Sentiment Analysis</strong> - Detects positive or negative tone</li>
          <li>⚠️ <strong>Toxicity Detection</strong> - Identifies harmful language</li>
          <li>🚫 <strong>Hate Speech Detection</strong> - Flags discriminatory content</li>
          <li>🏷️ <strong>Content Classification</strong> - Categorizes into hateful, terror, religious, sexual, abusive, drug, spam, or normal</li>
          <li>📊 <strong>Risk Scoring</strong> - Comprehensive safety assessment</li>
          <li>🌐 <strong>Multi-Platform</strong> - Works with Reddit, YouTube, news sites, and more</li>
        </ul>
      </div>
    </div>
  );
}

export default HowItWorks;
