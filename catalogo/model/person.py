import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Person:
<<<<<<< HEAD
    name: str
    id: Optional[int] = None
    birthdate: Optional[datetime.datetime] = None
=======
    id: Optional[int] = None
    name: str = None
    birthdate: Optional[datetime.datetime] = None
>>>>>>> origin/main
