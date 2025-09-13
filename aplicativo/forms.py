from django import forms
import requests
from .models import PessoaModel

class PessoaForm(forms.ModelForm):
    personagem_favorito = forms.IntegerField(label="Personagem Favorito (ID)")

    class Meta:
        model = PessoaModel
        fields = ['nome', 'personagem_favorito']

    def clean_personagem_favorito(self):
        personagem_id = self.cleaned_data['personagem_favorito']
        url = f'https://dragonball-api.com/api/characters/{personagem_id}'
        resposta = requests.get(url)
        if resposta.status_code != 200:
            raise forms.ValidationError("Personagem com o ID não existe na API")
        return personagem_id
