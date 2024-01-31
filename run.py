from gui.main_window import build_the_main_window
from voice_recognition_app.inference_remote import extract_key_words_online

def run():
    # kw = extract_key_words_online()
    '''
    Step 1: Build a window
    Step 2: Start the extraction
    Step 3: Show result on window
    '''

    # TODO: clean up directories
    build_the_main_window()


if __name__ == "__main__":
    run()
