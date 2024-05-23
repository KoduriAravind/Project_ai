# Project_ai
# Image to Audio Captioning Application

## Introduction
This project demonstrates an application that converts images to audio captions using machine learning and natural language processing techniques.

## Features
- **Upload an Image**: Users can upload an image file.
- **Generate a Text Description**: The application uses a pre-trained model to generate a textual description of the uploaded image.
- **Convert Text to Speech**: The text description is converted to audio using Google Text-to-Speech (gTTS).
- **Play the Audio**: Users can listen to the generated audio caption directly from the app.

## Technologies Used
- **Streamlit**: For building the web application interface.
- **Hugging Face Transformers**: For the image-to-text model.
- **gTTS (Google Text-to-Speech)**: For converting text to speech.

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- Git

### Installation Steps
1. **Clone the Repository**:
   ```sh
    git clone https://github.com/your-username/image-to-audio-captioning.git
   cd image-to-audio-captioning
2.  Create and Activate a Virtual Environment (optional but recommended):
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    
3.  Install the Required Libraries:
    pip install -r requirements.txt
    
4.  Set Up Your Hugging Face API Token:
    Obtain your Hugging Face API token from Hugging Face.
    Create an environment variable for the API token:
    export HUGGINGFACE_TOKEN='your_api_token_here'

5.  Run the Application:
    streamlit run app.py
