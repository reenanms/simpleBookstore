from entities.entityBase import *

class Livro(EntityBase):
    __tablename__ = 'livro'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    isbn = sqlalchemy.Column(sqlalchemy.String(length=20))
    titulo = sqlalchemy.Column(sqlalchemy.String(length=255))
    autor = sqlalchemy.Column(sqlalchemy.String(length=255))
    anoPublicacao = sqlalchemy.Column(sqlalchemy.Integer)
    quantidadeEstoque = sqlalchemy.Column(sqlalchemy.Integer)
    preco = sqlalchemy.Column(sqlalchemy.Float)
    ativo = sqlalchemy.Column(sqlalchemy.Boolean)
