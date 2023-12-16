from datetime import datetime

import sounddevice as sd
from scipy.io.wavfile import write

from config import records_folder


def record_wav(seconds: int = 3, rate: int = 44100):
    """
    records wav file
    :param seconds:
    :param rate:
    :return:
    """
    myrecording = sd.rec(int(seconds * rate), samplerate=rate, channels=2)
    sd.wait()
    filenme = records_folder / f'{datetime.now()}.wav'
    write(str(filenme), rate, myrecording)
    return filenme
