# wsBackend-Fabrica25.2 

Sistema em Django para gerenciar pessoas e consultar personagens via API (Dragon Ball).




## Funcionalidades

- ✅ Adicionar pessoas, editar personagens favoritos e exclusão
- ✅ Consultar personagens por nome usando API externa  
- ✅ Exibição de imagem, raça, gênero e descrição  
- ✅ Interface com fundo estilizado e links destacados


# Stacks utilizadas

- Python 3.13  
- Django 5.2.6  
- SQLite (banco de dados)  
- HTML + CSS (inline para estilização de fundo e links) 

# Estrutura do Projeto

**project/**  
Contém as configurações principais do Django (settings, urls e wsgi).

**aplicativo/**  
Aplicativo principal do projeto, com:
- `models.py` – definição dos models do Django.
- `views.py` – lógica das views.
- `forms.py` – formulários do Django.
- `api.py` – funções para consumir API externa.
- `templates/aplicativo/` – arquivos HTML.
- `migrations/` – migrations do banco de dados.

**db.sqlite3** – banco de dados local.  
**manage.py** – script principal do Django.  
**requirements.txt** – dependências do projeto.  
**README.md** – documentação do projeto.



# Instalação

Clone o repositório:

git clone https://github.com/xonixxt/wsBackend-Fabrica25.2.git
cd wsBackend-Fabrica25.2

Crie e ative um ambiente virtual:

python -m venv venv
## Windows
venv\Scripts\activate
## Linux/Mac
source venv/bin/activate


### Instale as dependências:

pip install -r requirements.txt


Crie o banco de dados e aplique:

python manage.py migrations

python manage.py migrate


### Execute o servidor:

python manage.py runserver


Acesse o sistema no navegador:

http://127.0.0.1:8000/


    
# Observações

Para consultar personagens, informe o nome EM ESPANHOL

Ex:

Em português alguns nomes como Goku, Vegeta, Bulma serão os mesmos, porém nomes como Freeza em espanhol deverá ser escrito Freezer na hora da consulta.

Requer conexão com a internet para a API de personagens.
# Melhorias

🧾 Integração com banco de dados MySQL ou PostgreSQL

Para lidar com volumes maiores de dados e facilitar o deploy em produção.

🔑 Autenticação e autorização de usuários

Diferentes níveis de acesso (admin, usuário comum) garantindo segurança na edição e exclusão de registros.

🔎 Paginação e busca avançada

Filtros por nome, raça ou gênero e paginação para listas grandes de pessoas ou personagens.
