
# ROTAS:
# pedido/ID: post (iniciar um pedido), get (retorna o pedido, livros e qtd)
# pedido/ID/livro/IDLIVRO/insert: post (para inserir um livro, botão +.... pode retornar erro de estoque)
# pedido/ID/livro/IDLIVRO/remove: post (para remover um livro, botão -....)
# pedido/ID/cliente: post (vincular um cliente)
# cliente: post (criar um novo), get (todos e por cpf)
# livro/ID: get
# livro: get (retorna todos)

from controllers.livroController import LivroController

from flask import Flask
from flask import jsonify

app = Flask(__name__)



@app.route('/livro')
def getAllBooks():
    controller = LivroController()
    livros = controller.getAll()
    return jsonify([{
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "preco": livro.preco
    } for livro in livros])