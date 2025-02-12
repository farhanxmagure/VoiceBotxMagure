# AI Conversational Chatbot 🤖

An AI-powered voice bot built using **Python, Streamlit, OpenAI Gemini, Whisper, and ElevenLabs**. This chatbot provides an interactive experience where users can communicate via text or voice, receive AI-generated responses, and listen to spoken replies.

## 🚀 Features
- **Real-time Voice & Text Interaction**: Users can input queries via text or speech.
- **AI-Powered Responses**: Utilizes **Google Gemini** to generate intelligent responses.
- **Speech-to-Text Conversion**: Uses **Whisper** for accurate speech recognition.
- **Text-to-Speech Generation**: Uses **ElevenLabs API** for natural-sounding audio responses.
- **Interactive UI with Streamlit**: A simple, intuitive user interface for smooth interaction.
- **Session Persistence**: Maintains conversation history during the session.

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **AI Processing**: OpenAI Whisper, Google Gemini
- **Text-to-Speech**: ElevenLabs
- **Voice Input**: `audio_recorder_streamlit`
- **Logging & Debugging**: Python `logging`

## 📌 Installation & Setup
### Prerequisites
Ensure you have **Python 3.8+** installed.

### Clone the Repository
```bash
git clone https://github.com/yourusername/ai-conversational-chatbot.git
cd ai-conversational-chatbot
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set API Keys
Create a `.env` file in the root directory and add:
```env
ELEVEN_API_KEY=your-elevenlabs-api-key
GEMINI_API_KEY=your-google-gemini-api-key
```

### Run the Application
```bash
streamlit run app.py
```

## 📌 How It Works
1. Run the application using Streamlit.
2. Use the chat interface to enter a text message or record audio input.
3. The bot processes your message using AI and returns a response.
4. If enabled, the bot will also convert the response to speech and play it.

## 📸 Screenshots & Demo
![Screenshot](https://github.com/farhanxmagure/VoiceBotxMagure/blob/main/Screenshot%202025-02-12%20150447.png)

🎥 **Demo Video**: [Watch here](https://github.com/farhanxmagure/VoiceBotxMagure/blob/main/Recording%202025-02-12%20101856.mp4)

## 🔧 Project Structure
```
📂 ai-conversational-chatbot
 ├── 📂 utils                 # Utility functions (AI, speech, etc.)
 ├── app.py                   # Main Streamlit application
 ├── requirements.txt          # Required dependencies
 ├── README.md                 # Project documentation
 ├── .env                      # API keys (excluded from repo)
```
