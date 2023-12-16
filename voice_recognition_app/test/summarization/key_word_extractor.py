from text_processing.key_word_extractor import extract_key_words, postprocess_keywords


def extract_keywords(text):
    key_words = extract_key_words(text)
    print("Key words:", key_words)
    postprocessed = postprocess_keywords(key_words)
    print("Postprocessed key words", postprocessed)
    return postprocessed


def test_extract_key_words_from_file():
    text = open("txt_filepath").read()
    print(text)
    extract_keywords(text)


def test_extract_key_words():
    text = "So it was a pretty nice day. We had a walk in the park. I felt really relaxed and the soles and birds " \
           "there were very small and decent cold and I felt like they could use some colds right? But yeah, we're " \
           "all in a good home, felt really warm. Everything was pretty nice."
    print(text)
    extract_keywords(text)
