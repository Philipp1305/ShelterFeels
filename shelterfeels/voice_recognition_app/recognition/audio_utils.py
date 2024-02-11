import queue
import sys
from datetime import datetime
from ctypes import c_char_p

import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write

from voice_recognition_app.config import records_folder, number_of_audio_channels_in

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


def record_until_interrupt(rate: int = 44100, string: c_char_p = None):
    filename = records_folder / f'{datetime.now().strftime("%Y %m %d - %H-%M-%S")}.wav'
    if string: string.value = filename
    try:
        with sf.SoundFile(str(filename), mode='x', channels=number_of_audio_channels_in, samplerate=rate) as file:
            with sd.InputStream(callback=callback, samplerate=rate):
                print('#' * 80)
                print('press Ctrl+C to stop the recording')
                print('#' * 80)
                while True:
                    que = q.get()
                    file.write(que)
    except KeyboardInterrupt:
        print('\nRecording finished: ' + str(filename))
    return filename
