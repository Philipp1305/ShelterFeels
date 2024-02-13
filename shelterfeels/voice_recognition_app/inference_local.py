from typing import List
from datetime import datetime

from shelterfeels.voice_recognition_app.recognition.recognize import recognize_audio_file
from shelterfeels.voice_recognition_app.recognition.audio_utils import record_until_interrupt
from shelterfeels.voice_recognition_app.text_processing.key_word_extractor import extract_key_words, \
    postprocess_keywords
from shelterfeels.voice_recognition_app.config import records_folder


def extract_key_words_audio() -> List[str]:
    """
    Records audio and extracts keywords from this audio
    :return: list of strings with keywords
    """
    print("Recording! \nTo stop recording please enter Ctrl+C")
    start = datetime.now()
    audiofile = record_until_interrupt()
    processing_start = datetime.now()
    print('Recording time:', (processing_start - start))
    print("Processing...")
    return extract_key_words_text(audiofile)


def extract_key_words_text(audiofile: str) -> List[str]:
    start = datetime.now()
    processing_start = datetime.now()
    print("Processing...")
    recognition_start = datetime.now()
    print('Recording time:', (processing_start - start))
    text = recognize_audio_file(str(audiofile))
    print("Recognized text:", text)
    with open(records_folder / f"{audiofile.stem}.txt", "w", encoding="utf-8") as f:
        f.write(text)
    keywords_start = datetime.now()
    print('Recognition time:', (keywords_start - recognition_start))
    keywords = extract_key_words_local(text)
    keywords_finish = datetime.now()
    print('Keyword extraction time:', (keywords_finish - keywords_start))
    return keywords


def extract_key_words_local(text: str) -> List[str]:
    """
    Extracts keywords from given text
    :return: list of strings with keywords
    """
    keywords = extract_key_words(text)
    print("Key words:", keywords)
    result = postprocess_keywords(keywords)
    return result


if __name__ == "__main__":
    kw = extract_key_words_audio()
    print("Post-processed key words:", kw)
