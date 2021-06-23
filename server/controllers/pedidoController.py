from datetime import datetime
from database.session import *
from entities.pedido import Pedido
from entities.cliente import Cliente
from entities.pedidoLivro import PedidoLivro
from entities.livro import Livro


class PedidoController:
    def __init__(self):
        return

    def mapPedidoSimples(self, pedido):
         return {
            "id": pedido.id,
            "dataPedido": pedido.dataPedido
         }

    def mapPedido(self, pedido, cliente, pedidoLivros):
        return {
            "id": pedido.id,
            "cliente": self.mapCliente(cliente),
            "dataPedido": pedido.dataPedido,
            "finalizado": pedido.confirmacaoPagamento,
            "livros": [self.mapPedidoLivro(pedidoLivro)
                for pedidoLivro in pedidoLivros]
        }

    def mapCliente(self, cliente):
        if (cliente is None):
            return None
        return {
            "nome": cliente.nome
        }
    
    def mapPedidoLivro(self, pedidoLivro):
        return {
            "id": pedidoLivro.idLivro,
            "titulo": "",
            "quantidade": pedidoLivro.quantidade,
            "preco": pedidoLivro.preco
        }

    def getAll(self):
        session = NewSession()
        pedidos = session.query(Pedido).all()
        return [self.mapPedidoSimples(pedido)
            for pedido in pedidos]

    def getAllFinalizados(self):
        session = NewSession()
        pedidos = session.query(Pedido).filter(Pedido.confirmacaoPagamento == True)
        return [self.mapPedidoSimples(pedido)
            for pedido in pedidos]

    def create(self):
        session = NewSession()
        pedido = Pedido(dataPedido=datetime.now(), confirmacaoPagamento=False)
        session.add(pedido)
        session.commit()
        return self.mapPedidoSimples(pedido)

    def get(self, id):
        session = NewSession()
        pedido = session.query(Pedido).get(id)
        if (pedido is None):
            raise Exception(f"Pedido {id} não existe")
        cliente = session.query(Cliente).get(pedido.idCliente)
        pedidoLivros = session.query(PedidoLivro).filter(PedidoLivro.idPedido == id)
        return self.mapPedido(pedido, cliente, pedidoLivros)

    def addLivro(self, id, idLivro):
        session = NewSession()

        pedido = session.query(Pedido).get(id)
        if (pedido is None):
            raise Exception(f"Pedido {id} não existe")

        livro = session.query(Livro).get(idLivro)
        if (livro is None):
            raise Exception(f"Livro {idLivro} não existe")

        pedidoLivro = session.query(PedidoLivro).get((id, idLivro))
        if (pedidoLivro is None):
            novoPedidoLivro = PedidoLivro(idPedido=id, idLivro=idLivro, quantidade=1, preco=livro.preco)
            session.add(novoPedidoLivro)
        else:
            pedidoLivro.quantidade += 1
        
        session.commit()

    def remLivro(self, id, idLivro):
        session = NewSession()

        pedido = session.query(Pedido).get(id)
        if (pedido is None):
            raise Exception(f"Pedido {id} não existe")

        livro = session.query(Livro).get(idLivro)
        if (livro is None):
            raise Exception(f"Livro {idLivro} não existe")

        pedidoLivro = session.query(PedidoLivro).get((id, idLivro))
        if (pedidoLivro is None):
            raise Exception(f"Livro {idLivro} não está no pedido {id}")

        pedidoLivro.quantidade -= 1
        if (pedidoLivro.quantidade == 0):
            session.delete(pedidoLivro)
        
        session.commit()

    def setCliente(self, id, cpf):
        session = NewSession()

        pedido = session.query(Pedido).get(id)
        if (pedido is None):
            raise Exception(f"Pedido {id} não existe")

        cliente = session.query(Cliente).filter(Cliente.cpf == cpf).first()
        if (cliente is None):
            raise Exception(f"Cliente com cpf {cpf} não existe")

        pedido.idCliente = cliente.id

        session.commit()

    def finalizar(self, id):
        session = NewSession()

        pedido = session.query(Pedido).get(id)
        if (pedido is None):
            raise Exception(f"Pedido {id} não existe")

        if (pedido.idCliente is None):
            raise Exception(f"Pedido não possui cliente")

        pedido.confirmacaoPagamento = True

        session.commit()
