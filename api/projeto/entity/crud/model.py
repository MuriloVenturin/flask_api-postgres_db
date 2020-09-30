from projeto.database import (
        Column,
        relationship,
        Model,
        db
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:changeme@localhost:5432/postgres')
Base = declarative_base()

class Teste(Base):
    __tablename__ = 'TESTE'

    ID = db.Column(db.BigInteger, primary_key=True, nullable=False, autoincrement=True)
    USUARIO = db.Column(db.String, nullable=True)
    STATUS = db.Column(db.String, nullable=True)

    def __init__(self, usuario, status):
        self.USUARIO = usuario
        self.STATUS = status


    def json(self):
        return {'ID': self.ID,
                'USUARIO': self.USUARIO,
                'STATUS': self.STATUS}

    @classmethod
    def find_by_id(cls, id: int):
        return cls.query.filter_by(ID=id).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()

Base.metadata.create_all(engine)
