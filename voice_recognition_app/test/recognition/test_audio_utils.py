from recognition.audio_utils import record_wav


def test_record_short():
    record_wav(5)  # FIXME doesnt work in wsl/no device found


def test_record_long():
    record_wav(20)  # FIXME doesnt work in wsl/no device found
