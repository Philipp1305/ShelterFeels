import whisper
import torch

from shelterfeels.voice_recognition_app.config import whisper_model_name, whisper_model_language

model = whisper.load_model(whisper_model_name)


def recognize_audio_file(filepath: str) -> str:
    """
    :param filepath: path to audio file
    :return: text from audio
    """
    print("Recognizing: ", filepath)

    if torch.cuda.is_available():
        result = model.transcribe(filepath, language=whisper_model_language)
    else:
        result = model.transcribe(filepath, fp16=False, language=whisper_model_language)
    return result["text"]
