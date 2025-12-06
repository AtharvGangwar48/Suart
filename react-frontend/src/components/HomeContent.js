import React from 'react';
import './HomeContent.css';

function HomeContent() {
  return (
    <div className="home-content">
      <div className="need-section">
        <h2>🎯 Why SUART?</h2>
        <div className="need-grid">
          <div className="need-card">
            <div className="need-icon">🛡️</div>
            <h3>Online Safety</h3>
            <p>Protect yourself and your community from harmful content before engaging with it</p>
          </div>
          <div className="need-card">
            <div className="need-icon">⚡</div>
            <h3>Instant Analysis</h3>
            <p>Get real-time content assessment in seconds, not hours of manual review</p>
          </div>
          <div className="need-card">
            <div className="need-icon">🎯</div>
            <h3>Multi-Platform</h3>
            <p>Works across Reddit, YouTube, news sites, and more - one tool for everything</p>
          </div>
          <div className="need-card">
            <div className="need-icon">🤖</div>
            <h3>AI-Powered</h3>
            <p>Advanced machine learning models detect toxicity, hate speech, and content risks</p>
          </div>
        </div>
      </div>

      <div className="faq-section">
        <h2>❓ Frequently Asked Questions</h2>
        <div className="faq-list">
          <div className="faq-item">
            <h3>What is SUART?</h3>
            <p>SUART is an AI-powered content intelligence system that analyzes social media posts and web content for sentiment, toxicity, hate speech, and categorizes content into 8 different types to assess safety risks.</p>
          </div>
          
          <div className="faq-item">
            <h3>How does it work?</h3>
            <p>Simply paste any URL from supported platforms (Reddit, YouTube, news sites, etc.). Our AI models analyze the content and provide detailed reports including sentiment analysis, toxicity detection, hate speech identification, and risk scoring.</p>
          </div>
          
          <div className="faq-item">
            <h3>Which platforms are supported?</h3>
            <p>Fully supported: Reddit, YouTube, news websites, and generic web pages. Limited support for Twitter/X, Instagram, and TikTok (requires authentication).</p>
          </div>
          
          <div className="faq-item">
            <h3>Is it accurate?</h3>
            <p>Yes! Our AI models achieve 85-92% accuracy using state-of-the-art transformer models including DistilBERT for sentiment, Toxic-BERT for toxicity, and RoBERTa for hate speech detection.</p>
          </div>
          
          <div className="faq-item">
            <h3>Is my data stored?</h3>
            <p>No. We analyze content in real-time and don't store any personal data or analyzed content. Your privacy is our priority.</p>
          </div>
          
          <div className="faq-item">
            <h3>What are the risk levels?</h3>
            <p>Content is classified as SAFE (0-3 points), WARNING (4-7), DANGEROUS (8-9), or CRITICAL (10+) based on multiple factors including sentiment, toxicity, hate speech, and content categories.</p>
          </div>
          
          <div className="faq-item">
            <h3>Can I use it for free?</h3>
            <p>Yes! SUART is free to use for personal content analysis. For commercial use or API access, contact the developer.</p>
          </div>
          
          <div className="faq-item">
            <h3>What content categories are detected?</h3>
            <p>SUART classifies content into 8 categories: hateful speech, terrorism/violence, religious extremism, sexual content, abusive language, drug-related, spam, and normal content.</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default HomeContent;
