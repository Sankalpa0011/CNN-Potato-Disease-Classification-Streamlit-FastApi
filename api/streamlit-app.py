import streamlit as st
import requests
import numpy as np
from PIL import Image
from io import BytesIO
import cv2

# Function to read file as image
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

# Function to make prediction request to FastAPI
def predict(image: np.ndarray):
    url = "http://localhost:8000/predict"
    _, im_buf_arr = cv2.imencode(".jpg", image)
    files = {'file': ('image.jpg', im_buf_arr.tobytes(), 'image/jpeg')}
    response = requests.post(url, files=files)
    return response.json()

# Streamlit interface
st.title("Plant Disease Prediction")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Read the image
    image = read_file_as_image(uploaded_file.read())
    
    # Display the image
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    
    # Make a prediction
    result = predict(image)
    
    # Display the result
    st.write(f"Prediction: {result['class']}")
    st.write(f"Confidence: {result['confidence']:.2f}")
