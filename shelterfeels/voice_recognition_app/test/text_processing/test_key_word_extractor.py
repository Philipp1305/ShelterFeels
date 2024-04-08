from shelterfeels.voice_recognition_app.text_processing.key_word_extractor_bad_quality import extract_key_words, \
    postprocess_keywords
from shelterfeels.voice_recognition_app.text_processing.keyword_extractor_h1 import inference


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
    text = " So this morning I got up and after that I learned a bit for my exam and then I went to the design fair " \
           "to meet my team for the preparation. We set up our things and we prepared our presentation. " \
           "After presenting our" \
           " stuff we went to a bar to celebrate and have some drinks."
    print(text)
    extracted = inference(text)
    print("new:", extracted)
    print("new postprocessed", postprocess_keywords(extracted))
    # extract_keywords(text, only_nouns=False)


def test_extract_key_words_2():
    text = "oday was a very sad day. Today I went to the university. I had a lot of work to do there but I " \
           "couldn't do much because of my procrastination habit. One of the good things that I met some of my " \
           "friends there we had a great chat and I were greeting that I don't spend enough time with them but " \
           "I think I will do better."
    print(text)
    extract_keywords(text)
    extract_keywords(text, only_nouns=False)


if __name__ == "__main__":
    print(test_extract_key_words())
