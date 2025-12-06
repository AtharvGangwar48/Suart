import React from 'react';
import './InfoSections.css';

function Contact() {
  return (
    <div className="info-section">
      <h2>📞 Contact</h2>

      <div className="contact-grid">
        <div className="contact-card">
          <div className="contact-icon">📧</div>
          <h3>Email</h3>
          <p>atharvgangwar8@gmail.com</p>
          <p className="contact-desc">For inquiries, support, and feedback</p>
        </div>

        <div className="contact-card">
          <div className="contact-icon">🐛</div>
          <h3>Bug Reports</h3>
          <p>atharvgangwar8@gmail.com</p>
          <p className="contact-desc">Report issues and technical problems</p>
        </div>

        <div className="contact-card">
          <div className="contact-icon">💡</div>
          <h3>Feature Requests</h3>
          <p>atharvgangwar8@gmail.com</p>
          <p className="contact-desc">Suggest new features and improvements</p>
        </div>
      </div>

      <div className="social-links">
        <h3>Connect</h3>
        <div className="social-icons">
          <a href="https://x.com/Atharv_48" target="_blank" rel="noopener noreferrer" className="social-icon">🐦 Twitter</a>
          <a href="https://www.linkedin.com/in/atharvgangwar/" target="_blank" rel="noopener noreferrer" className="social-icon">💼 LinkedIn</a>
          <a href="https://github.com/AtharvGangwar48/Suart" target="_blank" rel="noopener noreferrer" className="social-icon">🐙 GitHub</a>
          <a href="https://atharvgangwar.netlify.app/" target="_blank" rel="noopener noreferrer" className="social-icon">🌐 Portfolio</a>
        </div>
      </div>

      <div className="faq">
        <h3>❓ FAQ</h3>
        <div className="faq-item">
          <h4>How accurate is the analysis?</h4>
          <p>Our AI models achieve 85-92% accuracy across different content types, using state-of-the-art transformer models.</p>
        </div>
        <div className="faq-item">
          <h4>Is my data stored?</h4>
          <p>We only analyze content in real-time and don't store any personal data or analyzed content.</p>
        </div>
        <div className="faq-item">
          <h4>Can I use this for commercial purposes?</h4>
          <p>Yes! Contact our business team for enterprise licensing and API access.</p>
        </div>
      </div>
    </div>
  );
}

export default Contact;
