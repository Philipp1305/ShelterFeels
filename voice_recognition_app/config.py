from pathlib import Path
import sounddevice as sd

records_folder = Path(__file__).parent / "recordings"
records_folder.mkdir(exist_ok=True, parents=True)


whisper_model_name = "base"
whisper_model_language = "en"
number_of_audio_channels_in = 2
# sd.default.device = sd.default.device