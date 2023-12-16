from pathlib import Path

records_folder = Path(__file__).parent / "recordings"
records_folder.mkdir(exist_ok=True, parents=True)