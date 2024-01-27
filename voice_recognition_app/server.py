import uvicorn as uvicorn
from fastapi import FastAPI, UploadFile, File

from utils import save_upload_file
from config import records_folder

app = FastAPI()


@app.post('/extract_key_words')
def extract_key_words_endpoint(file: UploadFile = File(...)):
    save_upload_file(records_folder / file.filename, file)


@app.get('/liveness_check')
def liveness_check():
    return "good"


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8000
    print(f'Service is listening on {host}:{port}')
    uvicorn.run(app, host=host, port=port)
