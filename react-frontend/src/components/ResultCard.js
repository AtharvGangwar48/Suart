import React from 'react';
import './ResultCard.css';

function ResultCard({ data }) {
  const riskColors = {
    SAFE: '#4ECDC4',
    WARNING: '#FFE66D',
    DANGEROUS: '#FF8E53',
    CRITICAL: '#FF6B6B'
  };

  const categoryIcons = {
    hateful: '😡',
    terror: '💣',
    religious: '🕌',
    sexual: '🔞',
    abusive: '🗣️',
    drug: '💊',
    spam: '📧',
    normal: '✅'
  };

  const categories = data.content_analysis?.content_categories;
  const riskLevel = data.risk_assessment?.level || 'SAFE';

  return (
    <div className="result-container">
      <h2>Analysis Results</h2>

      {/* Risk Assessment */}
      <div className="card">
        <h3>📊 Risk Assessment</h3>
        <div 
          className="risk-badge" 
          style={{ backgroundColor: riskColors[riskLevel] }}
        >
          {riskLevel}
        </div>
        <div className="info-row">
          <span>Score:</span>
          <strong>{data.risk_assessment?.score || 0}</strong>
        </div>
        <div className="info-row">
          <span>Factors:</span>
          <span>{data.risk_assessment?.factors?.join(', ') || 'None'}</span>
        </div>
      </div>

      {/* Sentiment */}
      <div className="card">
        <h3>💭 Sentiment Analysis</h3>
        <div className="info-row">
          <span>Label:</span>
          <strong className={data.content_analysis?.sentiment?.label === 'POSITIVE' ? 'positive' : 'negative'}>
            {data.content_analysis?.sentiment?.label || 'N/A'}
          </strong>
        </div>
        <div className="progress-bar">
          <div 
            className="progress-fill"
            style={{ 
              width: `${(data.content_analysis?.sentiment?.score || 0) * 100}%`,
              backgroundColor: data.content_analysis?.sentiment?.label === 'POSITIVE' ? '#28a745' : '#dc3545'
            }}
          />
        </div>
        <div className="info-row">
          <span>Confidence:</span>
          <span>{((data.content_analysis?.sentiment?.score || 0) * 100).toFixed(1)}%</span>
        </div>
      </div>

      {/* Toxicity */}
      <div className="card">
        <h3>⚠️ Toxicity Detection</h3>
        <div className="info-row">
          <span>Status:</span>
          <strong className={data.content_analysis?.toxicity?.is_toxic ? 'toxic' : 'clean'}>
            {data.content_analysis?.toxicity?.is_toxic ? '⚠️ Toxic' : '✅ Clean'}
          </strong>
        </div>
        <div className="progress-bar">
          <div 
            className="progress-fill toxic"
            style={{ width: `${(data.content_analysis?.toxicity?.confidence || 0) * 100}%` }}
          />
        </div>
        <div className="info-row">
          <span>Confidence:</span>
          <span>{((data.content_analysis?.toxicity?.confidence || 0) * 100).toFixed(1)}%</span>
        </div>
      </div>

      {/* Hate Speech */}
      <div className="card">
        <h3>🚫 Hate Speech Detection</h3>
        <div className="info-row">
          <span>Status:</span>
          <strong className={data.content_analysis?.hate_speech?.is_hate_speech ? 'hate' : 'clean'}>
            {data.content_analysis?.hate_speech?.is_hate_speech ? '⚠️ Detected' : '✅ Clean'}
          </strong>
        </div>
        <div className="progress-bar">
          <div 
            className="progress-fill hate"
            style={{ width: `${(data.content_analysis?.hate_speech?.confidence || 0) * 100}%` }}
          />
        </div>
        <div className="info-row">
          <span>Confidence:</span>
          <span>{((data.content_analysis?.hate_speech?.confidence || 0) * 100).toFixed(1)}%</span>
        </div>
      </div>

      {/* Content Categories */}
      {categories && (
        <div className="card">
          <h3>🏷️ Content Categories</h3>
          <div className="info-row">
            <span>Primary:</span>
            <strong>{categoryIcons[categories.primary_category]} {categories.primary_category}</strong>
          </div>
          <div className="info-row">
            <span>Detected:</span>
            <span>
              {categories.detected_categories?.length > 0 
                ? categories.detected_categories.map(cat => `${categoryIcons[cat]} ${cat}`).join(', ')
                : 'None'}
            </span>
          </div>
          
          {categories.category_scores && (
            <div className="category-scores">
              {Object.entries(categories.category_scores).map(([cat, score]) => (
                <div key={cat} className="category-item">
                  <span className="category-label">
                    {categoryIcons[cat]} {cat}
                  </span>
                  <div className="category-bar">
                    <div 
                      className="category-fill"
                      style={{ 
                        width: `${score * 100}%`,
                        backgroundColor: score > 0.5 ? '#dc3545' : score > 0.3 ? '#ffc107' : '#6c757d'
                      }}
                    />
                  </div>
                  <span className="category-score">{(score * 100).toFixed(1)}%</span>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Platform Info */}
      <div className="card">
        <h3>🌐 Platform Info</h3>
        <div className="info-row">
          <span>Platform:</span>
          <strong>{data.platform || 'Unknown'}</strong>
        </div>
        <div className="info-row">
          <span>Title:</span>
          <span>{data.metadata?.title || 'N/A'}</span>
        </div>
        <div className="info-row">
          <span>Author:</span>
          <span>{data.metadata?.author || 'N/A'}</span>
        </div>
      </div>

      {/* Summary */}
      <div className="card summary-card">
        <h3>📝 Summary</h3>
        <p>{data.summary}</p>
      </div>

      {/* Text Preview */}
      {data.text_preview && (
        <div className="card">
          <h3>📄 Text Preview</h3>
          <p className="text-preview">{data.text_preview}</p>
        </div>
      )}
    </div>
  );
}

export default ResultCard;
