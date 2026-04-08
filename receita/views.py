from django.shortcuts import render
from .models import Receita, Categoria

# Create your views here.
def receitas(request):
    receitas = Receita.objects.all()
    context = {'receitas': receitas}
    
    return render(request, 'minhas_receitas.html', context)