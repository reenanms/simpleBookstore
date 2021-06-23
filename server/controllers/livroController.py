from database.session import *
from entities.livro import Livro
from entities.livrosMaisVendidos import LivrosMaisVendidos


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

    def mapMaisVendido(self, maisVendido):
        return {
            "titulo": maisVendido.titulo,
            "autor": maisVendido.autor,
            "quantidade": int(maisVendido.quantidade)
        }
    
    def map(self, livro):
        return {
            "id": livro.id,
            "isbn": livro.isbn,
            "titulo": livro.titulo,
            "autor": livro.autor,
            "anoPublicacao": livro.anoPublicacao,
            "estoque": livro.quantidadeEstoque,
            "preco": livro.preco,
        }

    def getAll(self):
        session = NewSession()
        livros = session.query(Livro).filter(Livro.ativo == 1)
        return [self.mapSimples(livro) for livro in livros]

    def getMaisVendidos(self):
        session = NewSession()
        maisVendidos = session.query(LivrosMaisVendidos).all()
        return [self.mapMaisVendido(maisVendido)
            for maisVendido in maisVendidos]

    def get(self, id):
        session = NewSession()
        livro = session.query(Livro).get(id)
        if (livro is None):
            raise Exception(f"Livro {id} não existe")
        return self.map(livro);

    def create(self, isbn, titulo, autor, anoPublicacao, estoque, preco):
        session = NewSession()
        livro = Livro(isbn=isbn, titulo=titulo, autor=autor, anoPublicacao=anoPublicacao, quantidadeEstoque=estoque, preco=preco, ativo=1)
        session.add(livro)
        session.commit()
        return self.map(livro)
