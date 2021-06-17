from entities.entityBase import *

class Cliente(EntityBase):
    __tablename__ = 'cliente'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    cpf = sqlalchemy.Column(sqlalchemy.String(length=15))
    nome = sqlalchemy.Column(sqlalchemy.String(length=255))
