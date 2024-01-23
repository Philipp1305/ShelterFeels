import queue
import sys
from datetime import datetime

import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import numpy as np

from config import records_folder

q = queue.Queue()
#print(sd.default.device)
sd.default.device = [2, 2]


def record_wav_n_seconds(seconds: int = 3, rate: int = 44100):
    """
    records wav file
    :param seconds:
    :param rate:
    :return:
    """
    myrecording = sd.rec(int(seconds * rate), samplerate=rate, channels=2)
    sd.wait()
    filename = records_folder / f'{datetime.now().strftime("%Y %m %d - %H-%M-%S")}.wav'
    write(str(filename), rate, myrecording)
    return filename


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())


def record_until_interrupt(rate: int = 44100):
    filename = records_folder / f'{datetime.now().strftime("%Y %m %d - %H-%M-%S")}.wav'
    print('devices',sd.query_devices())
    try:
        with sf.SoundFile(str(filename), mode='x', channels=1, samplerate=rate) as file:
            with sd.InputStream(callback=callback, samplerate=rate):
                print('#' * 80)
                print('press Ctrl+C to stop the recording')
                print('#' * 80)
                while True:
                    que = q.get()
                    #shape = np.shape(que)
                    #print(shape)
                    file.write(que)
    except KeyboardInterrupt:
        print('\nRecording finished: ' + str(filename))
    return filename
