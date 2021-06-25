import requests

URL = 'http://localhost:3000'


def get_livros():
    print("Get livros")
    r = requests.get(url = URL+'/livro')
    if r.status_code != 200:
        print("Erro na requisição dos livros")
        print(r)
    livros = r.json()
    print(livros)
    return livros

    '''    livros = [{
                "anoPublicacao": 2021,
                "autor": "nome do autor",
                "id": 1,
                "isbn": "1234567890123",
                "preco": 12,
                "titulo": "titulo do livro 1"
            }]'''
    return livros


def get_topvendas():
    print("Livros top vendas")
    r = requests.get(url = URL+'/livro/maisVendidos')
    if r.status_code != 200:
        print(r)
    topvendas = r.json()
    print(topvendas)
    return topvendas

    """    topvendas = [{
                    "autor": "nome do autor",
                    "quantidade": 10,
                    "titulo": "titulo do livro mais vendido"
                }]"""
    return topvendas



def get_pedido_id():
    print('get pedido id')
    r = requests.post(url=URL + '/pedido')
    if r.status_code != 200:
        print(r)
    pedido = r.json()
    print(pedido['id'])
    return (pedido['id'])


def add_pedido(id, pedidoId):
    print('add livro ao pedido')
    r = requests.post(url=URL + '/pedido/' + str(pedidoId) + '/add/' + str(id))
    if r.status_code != 200:
        print("Erro adicionando livro ao pedido")
        print(r)
    return r.status_code



def get_pedidos_finalizados():
    print('get pedidos finalizados')
    r = requests.get(url=URL + '/pedido/finalizados')
    if r.status_code != 200:
        print("Erro ao finalizar pedido")
        print(r)
    pedidos_finalizados = r.json()
    print(pedidos_finalizados)
    return pedidos_finalizados


def get_car_itens(pedidoId):
    print("Get itens do carrinho ")
    r = requests.get(url = URL+'/pedido/'+str(pedidoId))
    if r.status_code != 200:
        print("Erro na requisicao")
        print(r)
    livros = r.json()
    print(livros)
    return livros


def finalizar_pedido(pedidoId):
    print('Finalizar pedido')
    r = requests.post(url=URL + '/pedido/' + str(pedidoId) + '/finalizar')
    if r.status_code != 200:
        print("Erro finalizando pedido")
        print(r)
    else:
        print('Pedido finalizado')
    return r.status_code


def remover_livro_pedido(livroId, sessionId):
    r = requests.post(url=URL + '/pedido/' + str(sessionId) + '/rem/' + str(livroId))
    if r.status_code != 200:
        print("Erro removendo livro")
        print(r)
    else:
        print('Livro removido do pedido')
    return r.status_code

