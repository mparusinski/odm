from passlib.hash import bcrypt
from odm.application import db

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
        self.password = bcrypt.hash(password)
        self.email = email

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

    def __repr__(self):
        return "<User(username ='%s', password='%s', email='%s')>" % (self.username, self.password, self.email)

    @classmethod
    def __json__(cls):
        return ['username', 'full_name', 'email', 'password']


if __name__ == '__main__':
    pass
