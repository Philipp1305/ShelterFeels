import string
from typing import List

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from transformers import T5Tokenizer, T5ForConditionalGeneration

nltk.download("punkt")
nltk.download("stopwords")
nltk.download('averaged_perceptron_tagger')

model = T5ForConditionalGeneration.from_pretrained("Voicelab/vlt5-base-keywords")
tokenizer = T5Tokenizer.from_pretrained("Voicelab/vlt5-base-keywords", model_max_length=512)
stop = set(stopwords.words('english') + list(string.punctuation))

task_prefix = "Keywords: "


def extract_key_words(text: str) -> str:
    """
    Text-to-text keywords extraction
    :param text: full text
    :return: with keywords
    """
    input_sequences = [task_prefix + text]
    input_ids = tokenizer(input_sequences, return_tensors="pt", truncation=True).input_ids
    output = model.generate(input_ids, no_repeat_ngram_size=3, num_beams=4, max_new_tokens=200, min_new_tokens=20)
    return tokenizer.decode(output[0], skip_special_tokens=True)


def postprocess_keywords(keywords: str, only_nouns=True) -> List[str]:
    """
    :param keywords: string
    :return: array with strings that contain keywords
    :param only_nouns: if True, only nouns are extracted
    """

    keywords = keywords.replace(",", " ").lower()
    unique_keywords = list(set(keywords.split()))
    ps = PorterStemmer()
    final_words = {}
    for x in unique_keywords:
        stemmed = ps.stem(x)
        if stemmed not in final_words:
            final_words[stemmed] = x.lower()
    words = [x for x in final_words.values() if x not in stop]
    if only_nouns:
        tokens = nltk.word_tokenize(" ".join(words))
        tags = nltk.pos_tag(tokens)
        nouns = [word for word, pos in tags if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
        words = nouns
    return words
