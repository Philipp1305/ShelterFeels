import whisper
import torch

model = whisper.load_model("tiny")
    
def recognize_audio_file(filepath: str) -> str:
    """
    :param filepath: path to audio file
    :return: text from audio
    """
    print("Recognizing: ", filepath)

    if torch.cuda.is_available():
        result = model.transcribe(filepath, language='de')
    else:
        result = model.transcribe(filepath, fp16=False)
    return result["text"]
