from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.db.models import Q


# Create your views here.
from .models import  *

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'marca', 'ano', 'valor', 'data_cadastro']


def cadastrar_carro(request, template_name='carro_form.html'):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('carro_list')
    return render(request, template_name, {'form': form})


def listar_carro(request, template_name='carro_list.html'):
    query = request.GET.get('busca')
    if query:
        carros = Carro.objects.filter(
            Q(modelo__icontains=query) |
            Q(marca__icontains=query) |
            Q(ano__icontains=query)  # se ano for CharField, se for IntegerField use exact
        )
    else:
        carros = Carro.objects.all()
    return render(request, template_name, {'lista': carros})


def deletar_carro(request, id):
    # lógica para deletar o carro com o id recebido
    carro = Carro.objects.get(id=id)
    carro.delete()
    return redirect('carro_list')

def editar_carro(request, id):
    carro = Carro.objects.get(id=id)
    form = CarroForm(request.POST or None, instance=carro)
    if form.is_valid():
        form.save()
        return redirect('carro_list')
    return render(request, 'carro_form.html', {'form': form})