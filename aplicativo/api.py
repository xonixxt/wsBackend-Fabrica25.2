import requests

def get_personagem_por_nome(nome):
    url = 'https://dragonball-api.com/api/characters'
    resposta = requests.get(url)
    dados = resposta.json()
    personagens = dados.get('items', [])

    for p in personagens:
        if p.get('name', '').lower() == nome.lower():
            return p
    return None

def get_personagem_por_id(id):
    url = f'https://dragonball-api.com/api/characters/{id}'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    return None
