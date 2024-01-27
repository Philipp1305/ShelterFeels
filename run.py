from gui.example import build_wind
from voice_recognition_app.inference_remote import extract_key_words_online


def main():
    kw = extract_key_words_online()
    build_wind(kw)


if __name__ == "__main__":
    main()
