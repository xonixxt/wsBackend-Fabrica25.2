from .forms import PessoaForm
from .models import PessoaModel
from django.shortcuts import render, redirect


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



# Create your views here.
