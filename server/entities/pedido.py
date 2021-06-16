from entities.entityBase import *

class Pedido(EntityBase):
    __tablename__ = 'pedido'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    idCliente = sqlalchemy.Column(sqlalchemy.Integer)
    dataPedido = sqlalchemy.Column(sqlalchemy.DateTime)
    confirmacaoPagamento = sqlalchemy.Column(sqlalchemy.Boolean)
