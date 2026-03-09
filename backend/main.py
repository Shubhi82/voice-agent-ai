from fastapi import FastAPI, UploadFile
from agent import decide_action
from stt import speech_to_text
from tts import text_to_voice
from scheduler import run_reminder

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Voice Agent Running"}

@app.get("/check_emis")
def check_emis():
    run_reminder()
    return {"status": "reminder triggered"}

@app.post("/voice")
async def process_voice(file: UploadFile):

    audio_path = f"temp_{file.filename}"

    with open(audio_path, "wb") as f:
        f.write(await file.read())

    text = speech_to_text(audio_path)

    decision = decide_action(text)

    response = f"You said: {text}. Decision: {decision}"

    voice = text_to_voice(response)

    return {
        "text": text,
        "decision": decision,
        "voice_file": voice
    }
