import sys 
import tempfile
import queue
import sys

from datetime import datetime

import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write

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
    

def record_untill_interrupt(rate: int = 44100):
    filename = records_folder / f'{datetime.now().strftime("%Y %m %d - %H-%M-%S")}.wav'
    try:
        with sf.SoundFile(str(filename), mode='x', channels=2, samplerate=rate) as file:
            with sd.InputStream(callback=callback, samplerate=rate):
                print('#' * 80)
                print('press Ctrl+C to stop the recording')
                print('#' * 80)
                while True:
                    file.write(q.get())
    except KeyboardInterrupt:
        print('\nRecording finished: ' + str(filename))
    return filename
    # except Exception as e:
    #     .exit(type(e).__name__ + ': ' + str(e))
