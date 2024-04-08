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


def send_post(file, keywords_list=None) -> List[str]:
    if keywords_list is None:
        keywords_list = []
    print('sending', file, 'to', url)
    try:
        res = requests.post(url, files={'file': open(file, 'rb')})
    except requests.exceptions.HTTPError as e:
        print(e)
        return keywords_list

    if res.status_code != 200:
        print("Connection is unavailable")
        return []
    print('Got result', res.status_code)
    response = res.json()
    if response:
        keywords_list += response
    return keywords_list


if __name__ == "__main__":
    kw = extract_key_words_online()  # target function
    print("Post-processed key words:", kw)
