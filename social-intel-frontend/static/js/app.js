document.addEventListener('DOMContentLoaded', function() {
    const analyzeForm = document.getElementById('analyzeForm');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const healthBtn = document.getElementById('healthBtn');
    const resultsSection = document.getElementById('results');
    const resultsContent = document.getElementById('resultsContent');
    const healthStatus = document.getElementById('healthStatus');

    // Analyze form submission
    analyzeForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const url = document.getElementById('url').value;
        const deepAnalysis = document.getElementById('deepAnalysis').checked;
        
        // Show loading state
        analyzeBtn.innerHTML = '<span class="loading"></span> Analyzing...';
        analyzeBtn.disabled = true;
        
        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    url: url,
                    deep_analysis: deepAnalysis
                })
            });
            
            const data = await response.json();
            displayResults(data);
            
        } catch (error) {
            displayError('Analysis failed: ' + error.message);
        } finally {
            analyzeBtn.innerHTML = '🔍 Analyze';
            analyzeBtn.disabled = false;
        }
    });

    // Health check
    healthBtn.addEventListener('click', async function() {
        healthBtn.innerHTML = '<span class="loading"></span> Checking...';
        healthBtn.disabled = true;
        
        try {
            const response = await fetch('/health');
            const data = await response.json();
            
            if (data.status === 'healthy') {
                healthStatus.innerHTML = '<div class="health-status health-healthy">✅ System Healthy</div>';
            } else {
                healthStatus.innerHTML = '<div class="health-status health-error">❌ System Error</div>';
            }
        } catch (error) {
            healthStatus.innerHTML = '<div class="health-status health-error">❌ Connection Failed</div>';
        } finally {
            healthBtn.innerHTML = 'Check Health';
            healthBtn.disabled = false;
        }
    });

    function displayResults(data) {
        if (data.error) {
            displayError(data.error);
            return;
        }

        const riskScore = data.risk_score || 0;
        const riskClass = getRiskClass(riskScore);
        
        resultsContent.innerHTML = `
            <div class="risk-score ${riskClass}">
                Risk Score: ${(riskScore * 100).toFixed(1)}%
            </div>
            
            <div class="result-card">
                <h3>📊 Analysis Summary</h3>
                <p>${data.summary || 'Analysis completed successfully'}</p>
            </div>
            
            <div class="result-card">
                <h3>🔍 Key Findings</h3>
                <ul class="findings">
                    ${(data.findings || []).map(finding => `<li>• ${finding}</li>`).join('')}
                </ul>
            </div>
            
            <div class="result-card">
                <h3>🌐 Analyzed URL</h3>
                <p><a href="${data.url}" target="_blank">${data.url}</a></p>
            </div>
        `;
        
        resultsSection.style.display = 'block';
    }

    function displayError(message) {
        resultsContent.innerHTML = `
            <div class="result-card" style="border-left-color: #e53e3e;">
                <h3>❌ Error</h3>
                <p>${message}</p>
            </div>
        `;
        resultsSection.style.display = 'block';
    }

    function getRiskClass(score) {
        if (score < 0.3) return 'risk-low';
        if (score < 0.7) return 'risk-medium';
        return 'risk-high';
    }

    // Auto-check health on load
    healthBtn.click();
});