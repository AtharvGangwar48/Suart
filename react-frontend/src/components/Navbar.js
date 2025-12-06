import React, { useState } from 'react';
import './Navbar.css';

function Navbar({ onSectionChange }) {
  const [activeSection, setActiveSection] = useState('home');

  const handleNavClick = (section) => {
    setActiveSection(section);
    onSectionChange(section);
  };

  return (
    <nav className="navbar">
      <div className="nav-container">
        <div className="nav-logo" onClick={() => handleNavClick('home')}>
          🔍 SUART
        </div>
        <div className="nav-links">
          <button 
            className={activeSection === 'home' ? 'active' : ''} 
            onClick={() => handleNavClick('home')}
          >
            Home
          </button>
          <button 
            className={activeSection === 'how' ? 'active' : ''} 
            onClick={() => handleNavClick('how')}
          >
            How It Works
          </button>
          <button 
            className={activeSection === 'docs' ? 'active' : ''} 
            onClick={() => handleNavClick('docs')}
          >
            Docs
          </button>
          <button 
            className={activeSection === 'contact' ? 'active' : ''} 
            onClick={() => handleNavClick('contact')}
          >
            Contact
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
