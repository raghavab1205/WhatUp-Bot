from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

import sys
import os

# Step up two levels from /backend/model/ to the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.config.data_flow import store_input, check_cache, store_cache

app = Flask(__name__)
CORS(app)  # Enable CORS so your React app can communicate with this backend

# Load your pre-trained model and vectorizer (make sure these files exist in your working directory)
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Define the text-cleaning function (same logic as used during training)
def get_clean_data(text):
    tokenizer = RegexpTokenizer(r"\w+")
    lem = WordNetLemmatizer()
    e_sw = set(stopwords.words("english"))
    
    if isinstance(text, str):
        text = text.lower().strip()
        text = re.sub(r'[^a-z\s]', '', text)
        tokens = tokenizer.tokenize(text)
        clean_tokens = [lem.lemmatize(token) for token in tokens if token not in e_sw]
        return " ".join(clean_tokens)
    return ""

@app.route('/')
def index():
    return "Flask-React model prediction API is running!"

# Prediction endpoint: accepts POST with JSON payload {"text": "..."}
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400
    
    user_input = data["text"]
    # Store the user input for logging purposes
    store_input(user_input)
    
    # Check if we already have a cached response
    cached_response = check_cache(user_input)
    if cached_response is not None:
        return jsonify({"prediction": cached_response}), 200
    
    # Clean and process the input text
    cleaned_text = get_clean_data(user_input)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)[0]
    
    # Map the numeric prediction to a descriptive label
    responses_map = {
        0: "Anxiety",
        1: "Bipolar",
        2: "Depression",
        3: "Normal",
        4: "Personality Disorder",
        5: "Stress",
        6: "Suicidal"
    }
    prediction_label = responses_map.get(prediction, "Unknown")
    
    # Cache the result for future queries
    store_cache(user_input, prediction_label)
    
    return jsonify({"prediction": prediction_label}), 200

if __name__ == '__main__':
    app.run(debug=True)