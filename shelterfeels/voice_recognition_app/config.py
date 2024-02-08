from pathlib import Path
import sounddevice as sd

records_folder = Path(__file__).parent / "recordings"
records_folder.mkdir(exist_ok=True, parents=True)

server_port = 8000

url = "http://10.147.19.228:8000/extract_key_words"
whisper_model_name = "base"
whisper_model_language = "en"
number_of_audio_channels_in = 1
sd.default.device = [2, 2]