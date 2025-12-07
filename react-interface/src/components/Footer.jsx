import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-section">
          <h3>SUART</h3>
          <p>AI-powered content analysis for safer internet</p>
        </div>

        <div className="footer-section">
          <h4>Developer</h4>
          <p><strong>Atharv Gangwar</strong></p>
          <a href="https://atharvgangwar.netlify.app/" target="_blank" rel="noopener noreferrer">Portfolio</a>
          <a href="https://www.linkedin.com/in/atharvgangwar/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
          <a href="https://github.com/AtharvGangwar48/Suart" target="_blank" rel="noopener noreferrer">GitHub</a>
        </div>
      </div>

      <div className="footer-bottom">
        <p>&copy; 2026 SUART. All rights reserved.</p>
        <p>Developed by Atharv Gangwar</p>
      </div>
    </footer>
  );
}

export default Footer;
