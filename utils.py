import google.generativeai as genai
import logging
import base64
import streamlit as st
import whisper
from elevenlabs.client import ElevenLabs

ELEVEN_API_KEY = "API-KEY"
client = ElevenLabs(api_key=ELEVEN_API_KEY)

GEMINI_API_KEY = "API-KEY"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def get_answer(messages):
    try:
        system_message = "You are a helpful AI chatbot that answers questions asked by the user."
        formatted_messages = "\n".join([msg["content"] for msg in messages])
        response = model.generate_content(system_message + "\n\n" + formatted_messages)
        return response.text
    except Exception as e:
        print(f"Error in get_answer: {str(e)}")
        return "I apologize, but I encountered an error generating the response."

def speech_to_text(audio_data):
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_data)
        return result["text"]
    except Exception as e:
        print(f"Error in speech_to_text: {str(e)}")
        return None

logging.basicConfig(level=logging.DEBUG)

def text_to_speech(input_text):
    try:
        logging.debug("Generating audio using ElevenLabs API...")
        audio = client.generate(
            text=input_text,
            model="eleven_turbo_v2"
        )
        
        file_path = "output_audio.mp3"
        with open(file_path, "wb") as f:
            for chunk in audio:
                f.write(chunk)

        logging.debug(f"Audio saved to {file_path}")
        return file_path
    except Exception as e:
        logging.error(f"Error in text_to_speech: {str(e)}")
        return None


def autoplay_audio(file_path: str):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode("utf-8")
        md = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)
    except Exception as e:
        print(f"Error in autoplay_audio: {str(e)}")