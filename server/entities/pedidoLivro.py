from entities.entityBase import *

class PedidoLivro(EntityBase):
    __tablename__ = 'pedidoLivro'
    idPedido = sqlalchemy.Column(sqlalchemy.Integer)
    idLivro = sqlalchemy.Column(sqlalchemy.Integer)
    quantidade = sqlalchemy.Column(sqlalchemy.Integer)
    preco = sqlalchemy.Column(sqlalchemy.Float)