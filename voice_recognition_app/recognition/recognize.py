import whisper
import torch

def recognize_audio_file(filepath: str) -> str:
    """
    :param filepath: path to audio file
    :return: text from audio
    """
    model = whisper.load_model("base")
    if torch.cuda.is_available():
        result = model.transcribe(filepath)
    else:
        result = model.transcribe(filepath, fp16=False)
    return result["text"]
