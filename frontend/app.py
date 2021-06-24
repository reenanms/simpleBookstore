from flask import Flask, render_template, session
from flask_cors import CORS
from flask_session import Session
import method as mt

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
CORS(app)

@app.route('/')
@app.route('/livros')
def main_page():
    livros = mt.get_livros()
    topvendas = mt.get_topvendas()
    return render_template('main_page.html', livros=livros, topvendas=topvendas)


@app.route('/sobre')
def about_page():
    return render_template('sobre_nos.html')


@app.route('/carrinho')
def car_page():
    itens = mt.get_car_itens(session.get('pedidoId'))
    return render_template('carrinho.html', itens=itens)


@app.route('/vendedor')
def acesso_vendedor():
    return render_template('acesso_vendedor.html')


@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')


@app.route('/cadastro')
def cadastro_livro():
    return render_template('cadastro_livro.html')


@app.route('/add-car/<livroId>')
def add_car(livroId):
    if not session.get('pedidoId'):
        session['pedidoId'] = mt.get_pedido_id()
    if session.get('pedidoId'):
        if mt.add_pedido(livroId) == 200:
            print('Adicionado ao pedido com sucesso')
        else:
            print('PROBLEMA ao adicionar ao pedido')

    return main_page()


@app.route('/finalizar-pedido')
def finalizar_pedido():
    if mt.finalizar_pedido(session.get('pedidoId')) == 200:
        print('Pedido Finalizado com sucesso')
    else:
        print('PROBLEMA na finalização do pedido')
    session.pop(session.get('pedidoId'))
    return main_page()


if __name__ == '__main__':
    app.run()
