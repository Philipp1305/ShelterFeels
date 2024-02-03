from gui.models.words import words
from voice_recognition_app.inference_remote import extract_key_words_online


def extract_words(*args):
    keywords = ['hello', 'world']
    # keywords = extract_key_words_online()
    if not keywords:
        print('ERROR. No keywords extracted')
        return
    words.words = keywords
