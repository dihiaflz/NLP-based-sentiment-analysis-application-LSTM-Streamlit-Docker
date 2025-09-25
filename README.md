# Movie-Sentiment-Analysis-LSTM-Streamlit-Docker

This project is a deep learning application that classifies movie reviews as positive or negative using an LSTM-based model with TensorFlow/Keras, deployed on a Streamlit App.

It includes:

- A trained AI model ready for inference

- An app interface to run predictions on custom text inputs

- A training notebook (available locally and on my Kaggle profile)  

# HOW TO ository to your local machine.
1. Clone the repository to your local machine.
2. Create a virtual environment using the command **python -m venv venv** and then activate it using **venv\Scripts\activate**
3. Move to the app folder using **cd app** and Install dependencies using **pip install -r requirements.txt**
4. Once everything is installed, you can run the app with **python -m streamlit run main.py** (considering you are in the app folder)

# Second Option : DOCKER
You can also run the app inside Docker:
1. Open your Docker Desktop App and ensure that it is activated
2. Build the Docker image using **docker build -t sentiment-analyst .**
3. Run a container from the image using **docker run -p 8501:80 sentiment-analyst:v1.0** or **docker run -p 8501:80 sentiment-analyst:latest** according to the version displayed in your docker desktop -> Images section

You can now run the app through the Local URL **localhost:8501**
USE :
1. Clone the rep
