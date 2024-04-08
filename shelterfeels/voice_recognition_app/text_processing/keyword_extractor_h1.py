# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("transformer3/H1-keywordextractor")
model = AutoModelForSeq2SeqLM.from_pretrained("transformer3/H1-keywordextractor")


def inference(text: str):
    inputs = tokenizer([text], max_length=1024, return_tensors="pt")
    summary_ids = model.generate(inputs["input_ids"], num_beams=2, min_length=10, max_length=300)
    res = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    return res
