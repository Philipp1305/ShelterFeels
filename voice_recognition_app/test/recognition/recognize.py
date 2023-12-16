from pathlib import Path
from recognition.recognize import recognize_audio_file


def test_recognition():
    file = Path("/mnt/d/study/ixd/ShelterFeels/voice_recognition_app/recordings/Recording.m4a")
    text = recognize_audio_file(str(file))
    with open(file.parent / f"{file.stem}.txt", "w") as f:
        f.write(text)
