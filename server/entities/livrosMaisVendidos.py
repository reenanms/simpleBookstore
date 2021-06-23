from entities.entityBase import *

class LivrosMaisVendidos(EntityBase):
    __tablename__ = 'livrosMaisVendidos'
    autor = sqlalchemy.Column(sqlalchemy.String(length=255),primary_key=True)
    titulo = sqlalchemy.Column(sqlalchemy.String(length=255),primary_key=True)
    quantidade = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
