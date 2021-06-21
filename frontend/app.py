from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/livros')
def main_page():
    return render_template('main_page.html')

@app.route('/sobre')
def about_page():
    return render_template('sobre_nos.html')

@app.route('/carrinho')
def car_page():
    return render_template('carrinho.html')

@app.route('/vendedor')
def acesso_vendedor():
    return render_template('acesso_vendedor.html')

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

@app.route('/cadastro')
def cadastro_livro():
    return render_template('cadastro_livro.html')

if __name__ == '__main__':
    app.run()
