import unittest
from app.model.person import Person
from app.model.shop import Shop
from app import Session

class TestShop(unittest.TestCase):

    def setUp(self):
        self.session = Session().session

    def tearDown(self):
        self.session.close()

    def test_select(self):
        shop = self.session.query(Shop.name).filter(Shop.id == 1).first()
        self.assertEqual(shop.name, "ラビットハウス")
        # print(shop.person)

if __name__ == "__main__":
    unittest.main()
