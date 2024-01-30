from gui.main import main
# from voice_recognition_app.inference_remote import extract_key_words_online
from voice_recognition_app.inference_local import extract_key_words_audio


def run():
    # kw = extract_key_words_online()
    '''
    Step 1: Build a window
    Step 2: Start the extraction
    Step 3: Show result on window
    '''

    # TODO: clean up directories
    main()


if __name__ == "__main__":
    run()
