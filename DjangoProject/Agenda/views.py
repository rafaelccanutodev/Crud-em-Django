from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django import forms

from Agenda.models import Pessoa

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'idade', 'sexo', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),  # ⬅️ ESSENCIAL
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }


def pessoa_list(request):
    lista = Pessoa.objects.all()
    return render(request, 'pessoa_list.html', {'lista': lista})

def pessoa_create(request, template_name='form_pessoa.html'):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data['idade'] <= 0:
            form.add_error('idade', 'Idade inválida')
        else:
            form.save()
            return redirect('pessoa_list')
    return render(request, template_name, {'form': form})

def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect('pessoa_list')

def edit_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pessoa_list')
    return render(request, 'form_pessoa.html', {'form': form})



