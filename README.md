---

# Potato Disease Classification Streamlit-FastApi

---

This project is designed to classify potato diseases using a trained machine learning model. It includes a web interface built with Streamlit and a backend API powered by FastAPI.

## Features

- Potato disease classification using a trained machine learning model
- Interactive web interface built with Streamlit
- FastAPI backend for serving predictions
- Easy deployment on Streamlit

## Project Structure

```
.
├── fastapi-app.py       # FastAPI backend script
├── streamlit-app.py     # Streamlit frontend script
└── requirements.txt     # Required Python packages
```

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Sankalpa0011/potato-disease-classification.git
    cd potato-disease-classification
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

### FastAPI Backend

1. **Start the FastAPI server:**

    ```bash
    uvicorn fastapi-app:app --reload
    ```

    The FastAPI server will run on `http://127.0.0.1:8000`.

### Streamlit Frontend

1. **Start the Streamlit application:**

    ```bash
    streamlit run streamlit-app.py
    ```

    The Streamlit app will run on `http://localhost:8501`.

## Usage

1. Open the Streamlit app in your browser.
2. Upload an image of a potato leaf.
3. The app will display the predicted disease class along with a confidence score.

## Project Files

### `fastapi-app.py`

This file contains the FastAPI backend code which handles the model prediction logic. The API exposes endpoints for image upload and prediction.

### `streamlit-app.py`

This file contains the Streamlit frontend code which provides an interactive user interface for uploading images and displaying predictions.

## Dependencies

- Python 3.7+
- Streamlit
- FastAPI
- Uvicorn
- Other dependencies listed in `requirements.txt`

## Acknowledgements

- Thanks to the creators of Streamlit and FastAPI for providing excellent tools for building web applications.

## Contact

For any questions or suggestions, feel free to contact me at [sankalpakavindu09@gmail.com](mailto:sankalpakavindu09@gmail.com).

---

### Sample `requirements.txt`

Here's a sample `requirements.txt` file to include with your project:

```
streamlit
fastapi
uvicorn
pillow
numpy
scikit-learn
```
