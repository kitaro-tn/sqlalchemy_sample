import unittest
from sqlalchemy import and_, or_
from sqlalchemy.sql import func
from app.model.person import Person
from app.model.shop import Shop
from app import Session

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.session = Session().session

    def tearDown(self):
        self.session.close()

    def test_select(self):
        person = self.session.query(Person.name).filter(Person.id == 1).first()
        self.assertEqual(person.name, "保登 心愛")
        persons = self.session.query(Person).filter(Person.height < 150).all()
        self.assertEqual(len(persons), 3)
        persons = self.session.query(Person).filter(Person.name.like("%保登%")).all()
        self.assertEqual(len(persons), 2)
        persons = self.session.query(Person).filter(Person.id.in_([1, 2])).all()
        self.assertEqual(persons[1].name, "香風 智乃")
        persons = self.session.query(Person).filter(~Person.id.in_([1, 2])).all()
        self.assertEqual(persons[0].name, "天々座 理世")
        persons = self.session.query(Person).filter(and_(Person.age == 13, Person.blood_type == "A")).all()
        self.assertEqual(persons[0].nickname, "メグ")
        persons = self.session.query(func.avg(Person.height).label("avg_height")).first()
        self.assertTrue(isinstance(persons.avg_height, float))
        print(persons)
        persons = self.session.query(func.sum(Person.age).label("sum_age")).first()
        # self.assertTrue(isinstance(persons.sum_age, int))
        print(persons.sum_age)
        persons = self.session.query(func.count(Person.id).label("count_person")).first()
        print(persons.count_person)
        persons2 = self.session.query(Person.id).count()
        print(persons2)

if __name__ == "__main__":
    unittest.main()
