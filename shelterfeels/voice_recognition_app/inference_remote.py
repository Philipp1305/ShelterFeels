from typing import List
from datetime import datetime
from multiprocessing.managers import ListProxy
import requests

from shelterfeels.voice_recognition_app.recognition.audio_utils import record_until_interrupt
from shelterfeels.voice_recognition_app.config import url


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


def send_post(file, list: ListProxy = []) -> List[str]:
    print('sending ...')
    try:
        res = requests.post(url, files={'file': open(file, 'rb')})
    except requests.exceptions.HTTPError as e:
        print(e)

    if res.status_code != 200:
        print("Connection is unavailable")
        return []
    response = res.json()
    if response:
        list += response
    return response


if __name__ == "__main__":
    kw = extract_key_words_online()  # target function
    print("Post-processed key words:", kw)
