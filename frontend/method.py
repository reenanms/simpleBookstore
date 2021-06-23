import requests

URL='http://localhost:3000'

def get_livros():
    '''
    r = requests.get(url = URL+'/livro')
    livros = r.json()
    print(livros)
    '''
    livros = [
        {
            'id': '128391',
            'titulo': 'O sol é para todos',
            'autor': 'Jose da silva',
            'preco': '18.90',
        },
        {
            'id': '11548',
            'titulo': 'Eu amo Joana',
            'autor': 'João da silva',
            'preco': '15.90',
        },
        {
            'id': '85468',
            'titulo': 'A vida',
            'autor': 'Maria da silva',
            'preco': '120.00',
        }
    ]
    return livros

def add_pedido(id):
    #fazer post do livro
    return 'ok'

def get_pedido_id():
    #fazer get do id do pedido
    return ('1')