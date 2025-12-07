import React from 'react';
import './HomeContent.css';

function HomeContent() {
  return (
    <div className="home-content">
      <div className="features-grid">
        <div className="feature-card">
          <div className="feature-icon">🛡️</div>
          <h3>Content Safety</h3>
          <p>Analyze URLs for toxic content, hate speech, and harmful material using advanced AI models</p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">🎯</div>
          <h3>Sentiment Analysis</h3>
          <p>Understand the emotional tone and sentiment of any content with high accuracy</p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">⚡</div>
          <h3>Real-time Analysis</h3>
          <p>Get instant results with comprehensive risk scores and detailed breakdowns</p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">🌐</div>
          <h3>Multi-Platform</h3>
          <p>Support for Reddit, YouTube, news sites, and various social media platforms</p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">📊</div>
          <h3>Risk Scoring</h3>
          <p>Comprehensive risk assessment with scores from 0-100 and detailed factor analysis</p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">🔍</div>
          <h3>Deep Insights</h3>
          <p>Get detailed analysis including toxicity, hate speech, NSFW detection, and content categorization</p>
        </div>
      </div>

      <div className="cta-section">
        <h2>How to Use</h2>
        <div className="steps">
          <div className="step">
            <div className="step-number">1</div>
            <p>Paste any URL from supported platforms</p>
          </div>
          <div className="step-arrow">→</div>
          <div className="step">
            <div className="step-number">2</div>
            <p>Click Analyze to start the process</p>
          </div>
          <div className="step-arrow">→</div>
          <div className="step">
            <div className="step-number">3</div>
            <p>View comprehensive safety report</p>
          </div>
        </div>
      </div>

      <div className="info-banner">
        <h3>Trusted AI-Powered Analysis</h3>
        <p>Our models achieve 85-92% accuracy across different content types, using state-of-the-art transformer models for reliable content safety detection.</p>
      </div>
    </div>
  );
}

export default HomeContent;
