from database.session import *
from entities.livro import Livro

class LivroController:
    def __init__(self):
        return


    def mapSimples(self, livro):
        return {
            "id": livro.id,
            "isbn": livro.isbn,
            "titulo": livro.titulo,
            "autor": livro.autor,
            "anoPublicacao": livro.anoPublicacao,
            "preco": livro.preco
        }
    
    def map(self, livro):
        return {
            "id": livro.id,
            "titulo": livro.titulo,
            "autor": livro.autor,
            "preco": livro.preco,
            "estoque": livro.quantidadeEstoque
        }

    def getAll(self):
        session = NewSession()
        livros = session.query(Livro).filter(Livro.ativo == 1)
        return [self.mapSimples(livro) for livro in livros]

    def get(self, id):
        session = NewSession()
        livro = session.query(Livro).get(id)
        if (livro is None):
            raise Exception(f"Livro {id} não existe")
        return self.map(livro);
