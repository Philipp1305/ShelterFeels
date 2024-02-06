from recognition.recognize import recognize_audio_file
from shelterfeels.nfc_led.config import records_folder


def test_recognition():
    file = records_folder / "2023 12 19 - 10-43-01.wav"
    print(file)
    text = recognize_audio_file(str(file))
    with open(file.parent / f"{file.stem}.txt", "w", encoding="utf-8") as f:
        f.write(text)
