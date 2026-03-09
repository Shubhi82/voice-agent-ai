from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

def text_to_voice(text, output="response.wav"):
    tts.tts_to_file(text=text, file_path=output)
    return output
