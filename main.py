import os
import pickle
import streamlit as st
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.layers import TFSMLayer

working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/sentiment_analysis_model"
# Load the pre-trained model
model = TFSMLayer(model_path, call_endpoint="serving_default")

# Load tokenizer
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Function to predict the sentiment
def predict_sentiment(review):
    sequence = tokenizer.texts_to_sequences([review])
    padded_sequence = pad_sequences(sequence, maxlen=200)
    padded_sequence = padded_sequence.astype("float32")
    prediction = model(padded_sequence, training=False)
    print(prediction)
    # Extract tensor from dict
    prob = prediction['output_0'].numpy()[0][0]

    sentiment = 'positive' if prob > 0.5 else 'negative'
    return sentiment


# Streamlit App
st.title('Movie Sentiment analyst')

# Text input
user_input = st.text_area("Enter a movie review:")

# Display text and analyze sentiment when button clicked
if user_input.strip() != "":
    st.write("**Your input:**", user_input)
    
    if st.button('Analyse Sentiment'):
        prediction = predict_sentiment(user_input)
        st.success(f'Prediction: {prediction}')

