import uvicorn as uvicorn
from fastapi import FastAPI, UploadFile, File

from shelterfeels.voice_recognition_app.config import records_folder, server_port
from shelterfeels.voice_recognition_app.inference_local import extract_key_words_text
from shelterfeels.voice_recognition_app.utils import save_upload_file

app = FastAPI()


@app.post('/extract_key_words')
def extract_key_words_endpoint(file: UploadFile = File(...)):
    print(file.filename)
    audiofile = save_upload_file(records_folder / file.filename, file)
    print(audiofile)
    keywords = extract_key_words_text(audiofile)
    print("Post processed keywords:", keywords)
    return keywords


@app.get('/liveness_check')
def liveness_check():
    return "good"


if __name__ == "__main__":
    print(f'Service is listening on {server_port}')
    uvicorn.run(app, host="0.0.0.0", port=server_port)
