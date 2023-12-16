from typing import List

from recognition.recognize import recognize_audio_file
from text_processing.key_word_extractor import extract_key_words, postprocess_keywords


def extract_key_words_audio() -> List[str]:
    """
    Records audio and extracts keywords from this audio
    :return: list of strings with keywords
    """
    audiofile = ""  # TODO record audio
    text = recognize_audio_file(audiofile)
    return extract_key_words_text(text)


def extract_key_words_text(text: str) -> List[str]:
    """
    Extracts keywords from given text
    :return: list of strings with keywords
    """
    key_words = extract_key_words(text)
    result = postprocess_keywords(key_words)
    return result
