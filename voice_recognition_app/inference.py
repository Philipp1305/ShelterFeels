from typing import List

from recognition.recognize import recognize_audio_file
from recognition.audio_utils import record_untill_interrupt
from text_processing.key_word_extractor import extract_key_words, postprocess_keywords
from config import records_folder

def extract_key_words_audio() -> List[str]:
    """
    Records audio and extracts keywords from this audio
    :return: list of strings with keywords
    """
    print("Recording! \nTo stop recording please eneter Ctrl+C")
    audiofile = record_untill_interrupt()
    print("Processing...")
    text = recognize_audio_file(str(audiofile))
    print("Text:", text)
    with open(records_folder / f"{audiofile.stem}.txt", "w") as f:
        f.write(text)
    return extract_key_words_text(text)


def extract_key_words_text(text: str) -> List[str]:
    """
    Extracts keywords from given text
    :return: list of strings with keywords
    """
    keywords = extract_key_words(text)
    print("Key words:", keywords)
    result = postprocess_keywords(keywords)
    return result

if __name__ =="__main__":
    keywords = extract_key_words_audio()
    print("post-processed key words:", keywords)

