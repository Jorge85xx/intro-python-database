from catalogo.model.person import Person
from typing import List


class PersonRepository:

    def __int__(self):
        self.storage: List[Person] = []
        self.last_used_id: int = 0

    def insert(self, person: Person) -> None:
        assert person.id is None, "Person's should be None"
        self.storage.append(person)
        self.last_used_id += 1
        person.id = self.last_used_id

    def count(self):
        return len(self.storage)
