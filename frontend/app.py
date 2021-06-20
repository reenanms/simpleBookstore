from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/books')
def main_page():
    return render_template('main_page.html')

@app.route('/about')
def about_page():
    return render_template('sobre_nos.html')

@app.route('/carrinho')
def car_page():
    return render_template('carrinho.html')

@app.route('/vendedor')
def login_vendedor():
    return render_template('acesso_vendedor.html')


if __name__ == '__main__':
    app.run()
