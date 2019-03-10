import json
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import bcrypt

from odm.view.flask_app import app

db = SQLAlchemy(app)


class User(db.Model):
    # TODO: Automatically smart derive username from Full Name with limit size and with duplicate handling

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    full_name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, full_name: str, email, password):
        self.full_name = full_name
        self.username = full_name.lower().replace(' ', '.')
        self.password = bcrypt.encrypt(password)
        self.email = email

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

    def __repr__(self):
        # TODO: Improve this function
        return "<User(username ='%s', password='%s', email='%s')>" % (self.username, self.password, self.email)

    def to_json(self):
        return {'full_name':  self.full_name, "username": self.username, "password": self.password, "email": self.email}

    @classmethod
    def from_json(cls, json):
        user_object = User()
        user_object.full_name = json['full_name']
        user_object.username = json['username']
        user_object.password = json['password']
        user_object.email = json['email']
        return user_object


db.create_all()

gandalf = User(full_name="Gandalf the Grey", email="gandalf@fellowship.me", password="NotAllThoseWhoWanderAreLost")
frodo = User(full_name="Frodo Baggins", email="frodo@hobbiton.shire", password="KeepItSecretKeepItSafe")
db.session.add(gandalf)
db.session.add(frodo)
db.session.commit()

if __name__ == '__main__':
    pass
