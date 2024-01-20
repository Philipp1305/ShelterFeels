import queue
import sys
from datetime import datetime

import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import numpy as np

from config import records_folder

q = queue.Queue()


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
    try:
        with sf.SoundFile(str(filename), mode='x', channels=2, samplerate=rate) as file:
            with sd.InputStream(callback=callback, samplerate=rate):
                print('#' * 80)
                print('press Ctrl+C to stop the recording')
                print('#' * 80)
                while True:
                    que = q.get()
                    shape = np.shape(que)
                    if len(shape) == 1 or shape[1] == 1:
                        # mono
                        file.write(np.stack([que, que]))
                    elif shape[1] == 2:
                        # stereo
                        file.write(que)
                    else:
                        # more than stereo
                        file.write(que[:, :2])
    except KeyboardInterrupt:
        print('\nRecording finished: ' + str(filename))
    return filename
