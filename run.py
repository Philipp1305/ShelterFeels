from gui.example import build_window
from voice_recognition_app.inference_remote import extract_key_words_online


def main():
    kw = extract_key_words_online()
    build_window(kw)


if __name__ == "__main__":
    main()
