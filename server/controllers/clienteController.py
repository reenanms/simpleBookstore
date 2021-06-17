from database.session import *
from entities.cliente import Cliente


import sys

class ClienteController:
    def __init__(self):
        return

    def mapSimples(self, cliente):
        return {
            "id": cliente.id
        }

    def map(self, cliente):
        return {
            "id": cliente.id,
            "cpf": cliente.cpf,
            "nome": cliente.nome
        }
    
    def create(self, cpf, nome):
        session = NewSession()
        cliente = session.query(Cliente).filter(Cliente.cpf == cpf).first()
        if (cliente is not None):
            raise Exception(f"Cliente com cpf {cpf} já cadastrado")

        novoCliente = Cliente(cpf=cpf, nome=nome)
        session.add(novoCliente)

        session.commit()
        return self.mapSimples(novoCliente)

    def get(self, cpf):
        session = NewSession()
        cliente = session.query(Cliente).filter(Cliente.cpf == cpf).first()
        if (cliente is None):
            raise Exception(f"Cliente com cpf {cpf} não existe")
        return self.map(cliente)
