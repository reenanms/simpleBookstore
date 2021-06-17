# ROTAS:
# pedido: (todos) - OK
# pedido/ID: post (iniciar um pedido)- OK
#            get (retorna o pedido, livros e qtd) - OK
# livro/ID: get - OK
# livro: get (retorna todos) - OK
# pedido/ID/add/IDLIVRO: post (para inserir um livro, botão +.... pode retornar erro de estoque) - OK
# pedido/ID/rem/IDLIVRO: post (para remover um livro, botão -....) - OK
# pedido/ID/cli/cpf: post (vincular um cliente) - OK
# cliente: post (criar um novo or json: cpf + nome) - OK
# cliente/cpf: get (todos e por cpf) - OK


from controllers.livroController import LivroController
from controllers.pedidoController import PedidoController
from controllers.clienteController import ClienteController

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)



@app.route('/livro', methods=['GET'])
def getAllLivros():
    controller = LivroController()
    livros = controller.getAll()
    return jsonify(livros)

@app.route('/livro/<id>', methods=['GET'])
def getLivro(id):
    controller = LivroController()
    livro = controller.get(id)
    return jsonify(livro)



@app.route('/pedido', methods=['GET'])
def getAllPedidos():
    controller = PedidoController()
    pedidos = controller.getAll()
    return jsonify(pedidos)

@app.route('/pedido', methods=['POST'])
def createPedido():
    controller = PedidoController()
    pedido = controller.create()
    return jsonify(pedido)

@app.route('/pedido/<id>', methods=['GET'])
def getPedido(id):
    controller = PedidoController()
    pedido = controller.get(id)
    return jsonify(pedido)

@app.route('/pedido/<id>/add/<idLivro>', methods=['POST'])
def addLivroPedido(id, idLivro):
    controller = PedidoController()
    controller.addLivro(id, idLivro)
    return ""

@app.route('/pedido/<id>/rem/<idLivro>', methods=['POST'])
def remLivroPedido(id, idLivro):
    controller = PedidoController()
    controller.remLivro(id, idLivro)
    return ""

@app.route('/pedido/<id>/cli/<cpf>', methods=['POST'])
def setClientePedido(id, cpf):
    controller = PedidoController()
    controller.setCliente(id, cpf)
    return ""



@app.route('/cliente', methods=['POST'])
def createCliente():
    cpf = request.json['cpf']
    nome = request.json['nome']
    controller = ClienteController()
    cliente = controller.create(cpf, nome)
    return jsonify(cliente)

@app.route('/cliente/<cpf>', methods=['GET'])
def getCliente(cpf):
    controller = ClienteController()
    cliente = controller.get(cpf)
    return jsonify(cliente)
