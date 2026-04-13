import os
import openai
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3
import tempfile

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Jarvis")

app = FastAPI()

# Allow CORS for frontend interaction (adjust origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize TTS engine (offline)
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)

conversation_history = []

class Query(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"message": f"Hello! I am {ASSISTANT_NAME}, your AI assistant. How can I help you today?"}

@app.post("/chat")
async def chat(query: Query):
    global conversation_history
    user_message = query.message.strip()
    conversation_history.append({"role": "user", "content": user_message})

    # System prompt to set assistant behavior
    system_prompt = f"You are {ASSISTANT_NAME}, a helpful, friendly, and highly capable AI assistant. " \
                    "Speak like a friend but act professionally and help with any request."

    messages = [{"role": "system", "content": system_prompt}] + conversation_history

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # or "gpt-3.5-turbo" if you prefer
            messages=messages,
            temperature=0.7,
            max_tokens=500,
        )
        assistant_reply = response['choices'][0]['message']['content'].strip()
        conversation_history.append({"role": "assistant", "content": assistant_reply})

        return {"reply": assistant_reply}
    except Exception as e:
        return {"error": str(e)}

@app.post("/reset")
async def reset_conversation():
    global conversation_history
    conversation_history = []
    return {"message": "Conversation reset."}

@app.post("/voice")
async def voice_to_text(file: UploadFile = File(...)):
    """Receive voice file (wav) and convert to text."""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(await file.read())
            temp_audio.flush()

            recognizer = sr.Recognizer()
            with sr.AudioFile(temp_audio.name) as source:
                audio_data = recognizer.record(source)

            text = recognizer.recognize_google(audio_data)
            return {"transcript": text}
    except Exception as e:
        return {"error": f"Voice recognition failed: {str(e)}"}

@app.post("/speak")
async def speak_text(text: str = Form(...)):
    """Generate speech from text and save audio file."""
    try:
        # Save audio to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            tts_engine.save_to_file(text, f.name)
            tts_engine.runAndWait()
            return {"audio_path": f.name}
    except Exception as e:
        return {"error": str(e)}