from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/livros')
def main_page():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('main_page.html', user=user, posts=posts)

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
