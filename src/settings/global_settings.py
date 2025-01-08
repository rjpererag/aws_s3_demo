from dataclasses import dataclass
from decouple import config


@dataclass
class Settings:
    bucket_name: str = config("BUCKET_NAME")
    folder_name: str = config("FOLDER_NAME")
    new_folder_name: str = config("NEW_FOLDER_NAME")
    file_name: str = config("FILE_NAME")
