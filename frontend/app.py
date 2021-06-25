from flask import Flask, render_template, session, request, flash
from flask_cors import CORS
from flask_session import Session
from forms import form_cadastro_livro
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
    pedidos_finalizados = mt.get_pedidos_finalizados()
    return render_template('pedidos.html', pedidos_finalizados=pedidos_finalizados)


@app.route('/cadastro')
def cadastro_livro():
    form = form_cadastro_livro()
    if form.is_submitted():
        res = request.form
        return render_template('cadastro_livro.html', res=res)
    return render_template('cadastro_livro.html', form=form)


@app.route('/add-car/<livroId>')
def add_car(livroId):
    if not session.get('pedidoId'):
        session['pedidoId'] = mt.get_pedido_id()
    if session.get('pedidoId'):
        if mt.add_pedido(livroId, session.get('pedidoId')) == 200:
            flash("Livro adicionado ao carrinho!")
        else:
            flash("Erro ao adicionar livro ao carrinho!")
    return main_page()


@app.route('/finalizar-pedido')
def finalizar_pedido():
    if mt.finalizar_pedido(session.get('pedidoId')) == 200:
        flash("Pedido finalizado!")
    else:
        flash("Erro ao finalizar pedido!")
    session.pop('pedidoId')
    return main_page()

@app.route('/remover-livro-pedido/<livroId>')
def retirar_item(livroId):
    if mt.remover_livro_pedido(livroId, session.get('pedidoId')) == 200:
        flash("Livro removido do carrinho!")
    else:
        flash("Erro ao remover do carrinho, tente novamente!")
    return car_page()

if __name__ == '__main__':
    app.run()
