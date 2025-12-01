from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Backend API URL
API_BASE_URL = "http://127.0.0.1:8001"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url')
    deep_analysis = data.get('deep_analysis', False)
    
    try:
        response = requests.post(f"{API_BASE_URL}/analyze/", 
                               json={"url": url, "deep_analysis": deep_analysis})
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health')
def health():
    try:
        response = requests.get(f"{API_BASE_URL}/health/")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)