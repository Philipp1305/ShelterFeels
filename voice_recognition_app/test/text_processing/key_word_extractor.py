from text_processing.key_word_extractor import extract_key_words, postprocess_keywords


def extract_keywords(text, only_nouns=True):
    key_words = extract_key_words(text)
    print("Key words:", key_words)
    postprocessed = postprocess_keywords(key_words, only_nouns=True)
    print("Postprocessed key words", postprocessed)
    return postprocessed


def test_extract_key_words_from_file():
    text = open("txt_filepath").read()
    print(text)
    extract_keywords(text)


def test_extract_key_words():
    text = "So it was a pretty nice day. We had a walk in the park. I felt really relaxed and the soles and birds " \
           "there were very small and decent cold and I felt like they could use some coats. But yeah, we're " \
           "at home now, I feel really warm."
    print(text)
    extract_keywords(text)
    extract_keywords(text, only_nouns=False)


def test_extract_key_words_2():
    text = "So today was a very sad day. Today I went to the university. I had a lot of work to do there but I " \
           "couldn't do much because of my procrastination habit. One of the good things that I met some of my " \
           "friends there we had a great chat and I were greeting that I don't spend enough time with them but " \
           "I think I will do better."
    print(text)
    extract_keywords(text)
    extract_keywords(text, only_nouns=False)
