import requests

def get_personagem_por_nome(nome):
    url = f'https://dragonball-api.com/api/characters?name={nome}'
    resposta = requests.get(url)

    if resposta.status_code != 200:
        return None

    dados = resposta.json()

    if not dados:
        return None

    personagem = dados[0]

    return {
        'id': personagem.get('id'),
        'name': personagem.get('name'),
        'image': personagem.get('image'),
        'race': personagem.get('race'),
        'gender': personagem.get('gender'),
        'description': personagem.get('description')
    }

def get_personagem_por_id(id):
    url = f'https://dragonball-api.com/api/characters/{id}'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    return None
