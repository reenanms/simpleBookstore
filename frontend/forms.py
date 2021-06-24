from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class form_cadastro_livro(FlaskForm):
    titulo = StringField('Título')
    isbn = StringField('ISBN')
    autor = StringField('Autor')
    anoPublicacao = StringField('Ano publicação')
    estoque = StringField('Estoque')
    preco = StringField('Preço')
    cadastrar = SubmitField('Cadastrar')