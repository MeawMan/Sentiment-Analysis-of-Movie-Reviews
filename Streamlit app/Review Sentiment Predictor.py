import streamlit as st
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

import re
import string

def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-zA-Z]', ' ', text)  # Remove special characters and numbers
    words = text.split()  # Tokenization
    return " ".join(words)


# Load the trained model and TF-IDF Vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Streamlit app
st.title('Movie Review Sentiment Analysis')
st.write('Enter a movie review to predict its sentiment.')

user_input = st.text_area('Movie Review')

if st.button('Predict'):
    if user_input:
        # Preprocess and vectorize the input
        user_input_clean = clean_text(user_input)  # Ensure you have the clean_text function
        user_input_vectorized = vectorizer.transform([user_input_clean])

        # Predict sentiment
        prediction = model.predict(user_input_vectorized)
        sentiment = 'Positive' if prediction[0] == 1 else 'Negative'

        st.write(f'Sentiment: **{sentiment}**')
    else:
        st.write('Please enter a movie review.')
