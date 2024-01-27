from recognition.audio_utils import record_wav_n_seconds, record_until_interrupt
import sounddevice as sd


def test_record_short():
    record_wav_n_seconds(5)


def test_record_long():
    record_wav_n_seconds(20)


def test_record_unlimeted():  # no control cant stop using pytest
    file = record_until_interrupt()
    print(file)


def test_audio_devices_list():
    print('devices', sd.query_devices())
