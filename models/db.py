from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from passlib.hash import bcrypt

Base = declarative_base()


class User(Base):
    # TODO: Automatically smart derive username from Full Name with limit size and with duplicate handling

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    full_name = Column(String(128), nullable=False, unique=False)
    email = Column(String(256), nullable=False)
    password = Column(String, nullable=False)

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


if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:', echo=True)
    ASessionMaker = sessionmaker(bind=engine)
    session = ASessionMaker()
    Base.metadata.create_all(engine)
    user = User(full_name='Crazy Horse', email='crazy.horse@lakota.org', password='TheyTookOurLand')
    session.add(user)
    session.commit()
    print(user.id)  # None

