from .forms import PessoaForm
from .models import PessoaModel
from django.shortcuts import render, redirect, get_object_or_404
from .api import get_personagem_por_id


def lista_pessoas(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aplicativo:pessoas_lista')
    else:
        form = PessoaForm()

    pessoas = PessoaModel.objects.all()
    contexto = {'pessoas': pessoas, 'form': form}
    return render(request, 'aplicativo/pessoas_lista.html', contexto)

def detalhes_pessoa(request, pk):
    pessoa = get_object_or_404(PessoaModel, pk=pk)
    personagem = None
    if pessoa.personagem_favorito:
        personagem = get_personagem_por_id(pessoa.personagem_favorito)
    return render(request, 'aplicativo/detalhes_pessoa.html', {'pessoa': pessoa, 'personagem': personagem})

def pessoa_excluir(request, pk):
    pessoa = get_object_or_404(PessoaModel, pk=pk)
    pessoa.delete()
    return redirect('aplicativo:pessoas_lista')



# Create your views here.
