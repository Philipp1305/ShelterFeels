import requests

url = "http://10.147.19.228:8000/extract_key_words"

files = {'file': open('/home/ShelterFeels/Code/ShelterFeels/voice_recognition_app/recordings/2024 01 23 - 11-45-58.wav',
                      'rb')}
res = requests.post(url, files=files)
print(res.json())
