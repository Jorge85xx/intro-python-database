import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Person:
    id: Optional[int] = None
    name: str = None
    birthdate: Optional[datetime.datetime] = None