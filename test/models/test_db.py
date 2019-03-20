import unittest

from odm.application import db
from odm.models.db import User


class TestDB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        db.create_all()
        gandalf = User(full_name="Gandalf the Grey", email="gandalf@fellowship.me",
                       password="NotAllThoseWhoWanderAreLost")
        frodo = User(full_name="Frodo Baggins", email="frodo@hobbiton.shire", password="KeepItSecretKeepItSafe")
        db.session.add(gandalf)
        db.session.add(frodo)
        db.session.commit()

    def test_num_of_users(self):
        users = db.session.query(User).all()
        self.assertEqual(len(users), 2)


if __name__ == '__main__':
    unittest.main()