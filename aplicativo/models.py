from django.db import models

class PersonagemModel(models.Model):
    nome = models.CharField(max_length=100)

from django.db import models

class PessoaModel(models.Model):
    nome = models.CharField(max_length=100)
    personagem_favorito = models.IntegerField(default=0)
