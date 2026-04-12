from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Receita, Categoria
from .forms import ReceitaForm

# Create your views here.
def receitas(request):
    receitas = Receita.objects.all()
    context = {'receitas': receitas}
    
    return render(request, 'minhas_receitas.html', context)

def detalhes_receita(request, id_receita):
    receita = Receita.objects.get(id=id_receita)
    context = {'receita': receita}

    return render(request, 'detalhes_receita.html', context)

def nova_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receita criada com sucesso!')
            return redirect(receitas)
    else:
        form=ReceitaForm()
    
    return render(request, 'nova_receita.html', {'form': form})