from typing import List
from datetime import datetime
import requests

from recognition.audio_utils import record_until_interrupt
from config import url


def extract_key_words_online() -> List[str]:
    """
    Records audio and extracts keywords from this audio
    :return: list of strings with keywords
    """
    print("Recording! \nTo stop recording please enter Ctrl+C")
    start = datetime.now()
    audiofile = record_until_interrupt()
    processing_start = datetime.now()
    print("Processing...")
    print('Recording time:', (processing_start - start))
    return send_post(str(audiofile))
    
def send_post(file):
    res = requests.post(url, files={'file': open(file, 'rb')})
    print(res.json())

if __name__ == "__main__":
    kw = extract_key_words_online()
    print("Post-processed key words:", kw)
