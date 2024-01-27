import shutil
from logging import getLogger
from pathlib import Path

from fastapi import UploadFile


def save_upload_file(local_path: Path, upload_file: UploadFile) -> Path:
    """
    Saved upload_file into local_archive_path
    Args:
        local_path: path to where file should be saved
        upload_file: UploadFile that should be saved
    """
    try:
        with local_path.open("wb") as buffer:
            getLogger().info(f"Writing study into {local_path}")
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()
    return local_path
