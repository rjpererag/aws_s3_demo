from datetime import datetime
from dataclasses import dataclass


@dataclass
class Bucket:
    name: str = None
    creation_date: datetime = datetime.now()


@dataclass
class Content:
    name: str = None
    last_modified: datetime = datetime.now()
