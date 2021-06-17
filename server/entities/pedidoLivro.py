from sqlalchemy import PrimaryKeyConstraint
from entities.entityBase import *

class PedidoLivro(EntityBase):
    __tablename__ = 'pedidoLivro'
    idPedido = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    idLivro = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    quantidade = sqlalchemy.Column(sqlalchemy.Integer)
    preco = sqlalchemy.Column(sqlalchemy.Float)
    