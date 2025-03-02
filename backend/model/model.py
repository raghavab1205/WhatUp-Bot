import sys
import os

# Step up two levels from /backend/model/ to the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from backend.config.data_flow import get_data_indf
import backend.config.data_flow as data_flow
import numpy as np
import pandas as pd
import re
import joblib
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from imblearn.over_sampling import RandomOverSampler


df = get_data_indf(data_flow.main)
print(df["status"].unique())

Label_E = LabelEncoder()
df["status"] = Label_E.fit_transform(df["status"])

X = df["statement"] 
y = df["status"]
print(y.unique())

tokenizer = RegexpTokenizer(r"\w+")
lem = WordNetLemmatizer()
e_sw = set(stopwords.words("english"))

def get_clean_data(text):
    if isinstance(text, str):
        # Convert to lowercase and remove unwanted characters (optional)
        text = text.lower().strip()
        text = re.sub(r'[^a-z\s]', '', text)
        # Tokenize the text
        tokens = tokenizer.tokenize(text)

        # Remove stopwords and lemmatize tokens
        clean_tokens = [lem.lemmatize(token) for token in tokens if token not in e_sw]

        # Join the tokens back into a clean string
        clean_text = " ".join(clean_tokens)

        return clean_text

    else:
        return ""
    
    pass
    
Xa = X.to_numpy()
ya = y.to_numpy()
Xc = [get_clean_data(i) for i in Xa]

def vectorize():
    return TfidfVectorizer(max_features=5000)

vectorizer = vectorize()
Xnew = vectorizer.fit_transform(Xc)

# Handle class imbalance with RandomOverSampler
ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(Xnew, ya)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)
model1 = LogisticRegression(max_iter=500)
model1.fit(X_train, y_train)

joblib.dump(model1, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump(get_clean_data, "get_clean_data.pkl")
# Example: Save a model to a pickle file
with open('model.pkl', 'wb') as file:  # Open file in write-binary mode
    pickle.dump(model1, file)  # Replace 'model' with the actual object you want to save