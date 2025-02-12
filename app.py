import streamlit as st
import os
from utils import get_answer, text_to_speech, autoplay_audio, speech_to_text
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *
import logging


logging.basicConfig(level=logging.DEBUG)
float_init()

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! How may I assist you today?"}
        ]

def main():
    st.title("AI Conversational Chatbot 🤖")
    
    initialize_session_state()
    footer_container = st.container()
    with footer_container:
        audio_bytes = audio_recorder()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if audio_bytes:
        with st.spinner("Transcribing..."):
            webm_file_path = "temp_audio.mp3"
            try:
                with open(webm_file_path, "wb") as f:
                    f.write(audio_bytes)

                transcript = speech_to_text(webm_file_path)
                if transcript:
                    st.session_state.messages.append({"role": "user", "content": transcript})
                    with st.chat_message("user"):
                        st.write(transcript)
                
                # Clean up temporary audio file
                if os.path.exists(webm_file_path):
                    os.remove(webm_file_path)
            except Exception as e:
                st.error(f"Error processing audio: {str(e)}")
                logging.error(f"Error processing audio: {str(e)}")

    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking🤔..."):
                final_response = get_answer(st.session_state.messages)
            
            if final_response:
                with st.spinner("Generating audio response..."):    
                    audio_file = text_to_speech(final_response)
                    if audio_file:
                        autoplay_audio(audio_file)
                        # Clean up audio file after playing
                        if os.path.exists(audio_file):
                            os.remove(audio_file)
                    else:
                        st.error("Failed to generate audio response.")
                        logging.error("Failed to generate audio response.")
            
            st.write(final_response)
            st.session_state.messages.append({"role": "assistant", "content": final_response})

    footer_container.float("bottom: 0rem;")

if __name__ == "__main__":
    main()