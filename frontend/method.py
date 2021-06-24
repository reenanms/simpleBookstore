import requests

URL = 'http://localhost:3000'


def get_livros():
    '''
    r = requests.get(url = URL+'/livro')
    livros = r.json()
    print(livros)
    return livros
    '''
    livros = [
        {
            "anoPublicacao": 2021,
            "autor": "nome do autor",
            "id": 1,
            "isbn": "1234567890123",
            "preco": 12,
            "titulo": "titulo do livro 1"
        },
        {
            "anoPublicacao": 2021,
            "autor": "nome do autor",
            "id": 3,
            "isbn": "1234567890123",
            "preco": 20,
            "titulo": "titulo do livro 2"
        },
        {
            "anoPublicacao": 2018,
            "autor": "nome do autor",
            "id": 2,
            "isbn": "154897848",
            "preco": 23.3,
            "titulo": "titulo do livro 3"
        },
        {
            "anoPublicacao": 2018,
            "autor": "nome do autor",
            "id": 2,
            "isbn": "154897848",
            "preco": 23.3,
            "titulo": "titulo do livro 3"
        },
        {
            "anoPublicacao": 2018,
            "autor": "nome do autor",
            "id": 2,
            "isbn": "154897848",
            "preco": 23.3,
            "titulo": "titulo do livro 3"
        }
    ]
    return livros


def get_topvendas():
    '''
    r = requests.get(url = URL+'/livro/maisVendidos')
    top = r.json()
    print(top)
    return top
    '''
    topvendas = [
        {
            "autor": "nome do autor",
            "quantidade": 10,
            "titulo": "titulo do livro mais vendido"
        },
        {
            "autor": "nome do autor",
            "quantidade": 8,
            "titulo": "titulo do segundo livro mais vendido"
        },
        {
            "autor": "nome do autor",
            "quantidade": 8,
            "titulo": "titulo do segundo livro mais vendido"
        }
    ]
    return topvendas


def get_pedido_id():
    r = requests.post(url=URL + '/pedido')
    pedido = r.json()
    print(pedido.id)
    return (pedido.id)


def add_pedido(id):
    r = requests.post(url=URL + '/pedido/' + session.get('pedidoId') + '/add/' + id)
    return r.status_code


def get_pedidos_finalizados():
    p = requests.get(url=URL + '/pedido/finalizados')
    pedidos_finalizados = p.json()
    print(pedidos_finalizados)
    return pedidos_finalizados


def get_car_itens(pedidoId):
    itens = [{
        "cliente": {
            "nome": "nome do cliente"
        },
        "dataPedido": "Wed, 16 Jun 2021 22:18:05 GMT",
        "finalizado": 'true',
        "id": 1,
        "livros": [
            {
                "id": 1,
                "preco": 1.11,
                "quantidade": 1,
                "titulo": "titulo do livro"
            }
        ]
    }]

    return itens


def finalizar_pedido(pedidoId):
    r = requests.post(url=URL + '/pedido/' + pedidoId + '/finalizar')
    return r.status_code


def remover_livro_pedido(livroId, sessionId):
    r = requests.post(url=URL + '/pedido/' + sessionId + '/rem/' + livroId)
    return r.status_code

