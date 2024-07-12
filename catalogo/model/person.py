import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Person:
    name: str
    id: Optional[int] = None
    birthdate: Optional[datetime.datetime] = None
