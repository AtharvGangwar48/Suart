from flask import Flask, render_template, request, jsonify
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK resources if not already available
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Initialize the Flask app
app = Flask(__name__)

# Load and process the document
with open('Data.txt', 'r', errors='ignore') as file:
    document = file.read().lower()

# Tokenize document into sentences
sentences = sent_tokenize(document)

# Initialize Lemmatizer and Punctuation Removal Dictionary
lemmatizer = WordNetLemmatizer()
punctuation_removal = {ord(punctuation): None for punctuation in string.punctuation}

def process_tokens(tokens):
    """Lemmatize and clean the given list of tokens."""
    return [lemmatizer.lemmatize(token) for token in tokens]

def clean_text(text):
    """Lowercase and remove punctuation from the text."""
    return process_tokens(word_tokenize(text.lower().translate(punctuation_removal)))

@app.route('/')
def home():
    """Render the main webpage."""
    return render_template('index.html')

@app.route('/ask/<user_query>', methods=['GET'])
def answer_query(user_query):
    """Generate an answer to the user's query based on the document."""
    tfidf_vectorizer = TfidfVectorizer(tokenizer=clean_text, stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform([user_query] + sentences)
    
    # Compute cosine similarity scores between the user's query and the document sentences
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    
    # Find the sentence with the highest similarity score
    similarity_scores = similarity.flatten()
    most_similar_idx = similarity_scores.argsort()[-1]

    # Check if the similarity score is significant enough
    if similarity_scores[most_similar_idx] == 0:
        return "Sorry, I couldn't understand your question."
    else:
        return sentences[most_similar_idx]

if __name__ == "__main__":
    app.run(debug=True)
