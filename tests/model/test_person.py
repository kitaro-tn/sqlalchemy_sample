import unittest
from sqlalchemy import and_, or_, case, literal_column
from sqlalchemy.orm import join, outerjoin
from sqlalchemy.sql import func, select
from sqlalchemy.sql.functions import current_timestamp, current_user
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
        persons = self.session.query(Person).limit(5).offset(5).all()
        print(persons)
        self.assertEqual(persons[0].id, 6)
        persons = self.session.query(Person).order_by(Person.id.desc()).all()
        print(persons)
        self.assertEqual(persons[0].id, 12)
        persons = self.session.query(Person.age, func.count(Person.age)).group_by(Person.age).all()
        print(persons)
        persons = self.session.query(Person).select_from(join(Person, Shop)).all()
        print(persons)
        persons = self.session.query(Person).select_from(join(Person, Shop, Person.shop_id == Shop.id)).all()
        print(persons)
        persons = self.session.query(Person).select_from(outerjoin(Person, Shop, Person.shop_id == Shop.id)).all()
        print(persons)

        persons = self.session.query(Person).filter(Person.created_at < current_timestamp()).all()
        print(persons)

        print(self.session.execute(select([current_user()])).first())
        persons = self.session.query(
                Person.id,
                Person.name,
                case(
                    [
                        (Person.height >= 165, '165以上'),
                        ],
                    else_='165未満'
                    )).all()
        print(persons)

        person = Person(name="秋山優花里", nickname="オッドボール三等軍曹", age=16, birthday="06-06", blood_type="O")
        self.session.add(person)
        self.session.commit()
        self.assertEqual(person.age, 16)
        person.age = 17
        self.session.commit()
        self.assertEqual(person.age, 17)
        self.session.delete(person)
        self.session.commit()

if __name__ == "__main__":
    unittest.main()
