import whisper


def recognize_audio_file(filepath: str) -> str:
    """
    :param filepath: path to audio file
    :return: text from audio
    """
    model = whisper.load_model("base")
    result = model.transcribe(filepath)
    return result["text"]
