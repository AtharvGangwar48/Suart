import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import ResultCard from './components/ResultCard';
import HomeContent from './components/HomeContent';
import HowItWorks from './components/HowItWorks';
import Docs from './components/Docs';
import Contact from './components/Contact';

function App() {
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const [currentSection, setCurrentSection] = useState('home');

  const analyzeUrl = async () => {
    if (!url.trim()) {
      setError('Please enter a URL');
      return;
    }

    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await axios.post('http://localhost:8001/analyze/', {
        url: url,
        deep_analysis: false
      });

      if (response.data.status === 'error') {
        setError(response.data.message);
      } else {
        setResult(response.data);
      }
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to analyze content');
    } finally {
      setLoading(false);
    }
  };

  const renderContent = () => {
    switch(currentSection) {
      case 'how':
        return <HowItWorks />;
      case 'docs':
        return <Docs />;
      case 'contact':
        return <Contact />;
      default:
        return (
          <>
            <header className="header">
          <h1>SUART</h1>
          <p>AI-powered content analysis for any URL</p>
        </header>

        <div className="input-section">
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && analyzeUrl()}
            placeholder="Enter Reddit post URL or any social media link..."
            className="url-input"
          />
          <button onClick={analyzeUrl} disabled={loading} className="analyze-btn">
            {loading ? 'Analyzing...' : 'Analyze'}
          </button>
        </div>

        {loading && (
          <div className="loading">
            <div className="spinner"></div>
            <p>Analyzing content...</p>
          </div>
        )}

        {error && (
          <div className="error">
            ❌ {error}
          </div>
        )}

            {result && <ResultCard data={result} />}
            
            {!result && !loading && !error && <HomeContent />}
          </>
        );
    }
  };

  return (
    <div className="app">
      <Navbar onSectionChange={setCurrentSection} />
      <div className="container">
        {renderContent()}
      </div>
      <Footer />
    </div>
  );
}

export default App;
