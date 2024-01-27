import uvicorn as uvicorn
from fastapi import FastAPI, UploadFile, File
from inference_local import extract_key_words_text

from config import records_folder
from recognition.recognize import recognize_audio_file
from utils import save_upload_file

app = FastAPI()


@app.post('/extract_key_words')
def extract_key_words_endpoint(file: UploadFile = File(...)):
    print(file.filename)
    audiofile = save_upload_file(records_folder / file.filename, file)
    print(audiofile)
    text = recognize_audio_file(str(audiofile))
    print("Recognized text:", text)
    with open(records_folder / f"{audiofile.stem}.txt", "w", encoding="utf-8") as f:
        f.write(text)
    keywords = extract_key_words_text(text)
    return keywords


@app.get('/liveness_check')
def liveness_check():
    return "good"


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8000
    print(f'Service is listening on {host}:{port}')
    uvicorn.run(app, host=host, port=port)
