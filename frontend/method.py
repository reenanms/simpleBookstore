import requests

URL='http://localhost:3000'

def get_livros():
    r = requests.get(url = URL+'/livro')
    livros = r.json()
    return livros