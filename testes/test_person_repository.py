from catalogo.model.person import Person
from catalogo.repositorio.person_repository import PersonRepository
import datetime
import unittest


class PersonRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        self.repository: PersonRepository = PersonRepository()

    def test_insert_operation(self):
        person: Person = Person(name='Luccas Venezian Povoa', birthdate=datetime.datetime(year=1990, month=2, day=1))

        old_person_count: int = self.repository.count()

        self.assertIsNone(person.id)
        self.repository.insert(person)
        self.assertIsInstance(person.id, int)
        new_person_count: int = self.repository.count()
        self.assertEquals(new_person_count, old_person_count + 1)
