from recognition.audio_utils import record_wav_n_seconds, record_untill_interrupt


def test_record_short():
    record_wav_n_seconds(5) 


def test_record_long():
    record_wav_n_seconds(20)  

def test_record_unlimeted(): # no control cant stop using pytest
    file = record_untill_interrupt()
    print(file)