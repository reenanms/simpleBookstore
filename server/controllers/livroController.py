from database.session import *
from entities.livro import Livro

class LivroController:
    def __init__(self):
        return

    def getAll(self):
        session = NewSession()
        livros = session.query(Livro).all()
        return livros;

