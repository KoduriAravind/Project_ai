#code
import streamlit as st
from transformers import pipeline
from gtts import gTTS
import os

# Set up your Hugging Face API token
os.environ["HUGGINGFACE_TOKEN"] = "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"

captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

st.title("Image to Audio Captioning")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Save the uploaded file to a temporary location
    with open("temp_image.png", "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Generate Audio Caption"):
        # Generate a caption for the image
        result = captioner("temp_image.png")
        caption_text = result[0]['generated_text']

        # Convert the text to speech
        tts = gTTS(caption_text)

        # Save the audio file
        tts.save("caption.mp3")

        # Play the audio file
        audio_file = open("caption.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

        # Display the caption text
        st.write("Generated Caption:", caption_text)
