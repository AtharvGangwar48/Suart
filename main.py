from flask import Flask, render_template, request, jsonify
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Use these lines if you are using this codebase for first time in your machine
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

app = Flask(__name__)

# Load the text file and process it
with open('Data.txt', 'r', errors='ignore') as f:
    raw_doc = f.read().lower()

# Tokenize the document into sentences
sent_tokens = nltk.sent_tokenize(raw_doc)

# Initialize the lemmatizer and punctuation removal dictionary
lemmer = nltk.stem.WordNetLemmatizer()
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def lemmatize_tokens(tokens):
    """Lemmatize the given tokens."""
    return [lemmer.lemmatize(token) for token in tokens]

def normalize_text(text):
    """Normalize the text by converting to lowercase and removing punctuation."""
    return lemmatize_tokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

@app.route('/asking', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/question/<string:user_response>', methods=['GET'])
def get_response(user_response):
    """Get a response based on user input."""
    tfidf_vectorizer = TfidfVectorizer(tokenizer=normalize_text, stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform([user_response] + sent_tokens)
    similarity_scores = cosine_similarity(tfidf[0:1], tfidf[1:])
    idx = similarity_scores.argsort()[0][-1]
    flat_scores = similarity_scores.flatten()
    flat_scores.sort()
    required_score = flat_scores[-1]
    
    if required_score == 0:
        return "I am sorry! I don't understand you."
    else:
        return sent_tokens[idx]

if __name__ == "__main__":
    app.run(debug=True)
