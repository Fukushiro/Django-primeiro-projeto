from django.shortcuts import render, redirect
from django.http import HttpResponse

from core.models import (Pessoa,
                         Veiculo,
                         Marca,
                         MovRotativo,
                         Mensalista,
                         MovMensalista,
                         Parametros,
                         Marca)
from core.forms import (PessoaForm,
                        VeiculoForm,
                        MovRotForm,
                        MensalistaForm,
                        MovMensalistaForm,
                        MarcaForm,)

from django.contrib.auth import authenticate
import datetime
# Create your views here.


def home(request):

    context = {

    }

    return render(request, 'core/index.html', context)

# pessoas


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    context = {
        'lista_pessoas': pessoas,
        'form': form,
    }
    return render(request, 'core/lista_pessoa.html', context)


def adicionar_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def update_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST or None, instance=pessoa)
        if form.is_valid():
            form.save()

        return redirect('core_update_pessoa', id)
    else:

        form = PessoaForm(instance=pessoa)

        context = {
            'pessoa': pessoa,
            'form': form,
        }
        return render(request, 'core/update_pessoa.html', context)
# veiculos


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    initial = {
        # 'marca': [(1, 1), (2, 2)],
    }

    form = VeiculoForm(initial=initial)

    context = {
        'veiculos': veiculos,
        'form': form,
    }
    return render(request, 'core/lista_veiculo.html', context)


def adicionar_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def update_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)

    if request.method == 'POST':
        form = VeiculoForm(request.POST or None, instance=veiculo)
        if form.is_valid():
            form.save()

        return redirect('core_update_veiculo', id)
    else:
        form = VeiculoForm(instance=veiculo)

        context = {
            'form': form,
            'veiculo': veiculo,

        }
        return render(request, 'core/update_veiculo.html', context)

# rotativos


def lista_mov_rot(request):
    parametros = Parametros.objects.first()

    movimentos_rotativos = MovRotativo.objects.all()
    form = MovRotForm(
        initial={'valor_hora': parametros.valor_hora, }
    )

    context = {
        'movimentos': movimentos_rotativos,
        'form': form,
    }
    return render(request, 'core/mov_rot.html', context)


def adicionar_mov_rot(request):
    form = MovRotForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_mov_rot')


def update_mov_rot(request, id):
    mov = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        form = MovRotForm(request.POST or None, instance=mov)
        if form.is_valid():
            form.save()
        return redirect('core_update_mov_rot', id)
    else:
        form = MovRotForm(instance=mov)
        context = {
            'mov': mov,
            'form': form,
        }
        return render(request, 'core/update_mov_rot.html', context)
# mensalistas


def lista_mensalista(request):
    mensalista = Mensalista.objects.all()
    form = MensalistaForm()
    context = {
        'mensalistas': mensalista,
        'form': form,
    }
    return render(request, 'core/mensalista.html', context)


def add_mensalista(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')


def update_mensalista(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        form = MensalistaForm(request.POST or None, instance=mensalista)
        if form.is_valid():
            form.save()
        return redirect('core_update_mensalista', id)
    else:
        form = MensalistaForm(instance=mensalista)
        context = {
            'form': form,
            'mensalista': mensalista,
        }
        return render(request, 'core/update_mensalista.html', context)
# movimento mensalista


def lista_mov_mensalista(request):
    movimentos = MovMensalista.objects.all()
    form = MovMensalistaForm()
    context = {
        'movimentos': movimentos,
        'form': form,
    }
    return render(request, 'core/mov_mensalista.html', context)


def adicionar_mov_mensalista(request):

    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_mov_mensalista')


def update_mov_mensalista(request, id):
    mov_mensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        return redirect('core_update_mov_mensalista')
    else:
        form = MovMensalistaForm(instance=mov_mensalista)
        c = {
            'form': form,
            'mov_mensalista': mov_mensalista,
        }
        return render(request, 'core/update_mov_mensalista.html', c)
# marca


def lista_marca(request):
    marcas = Marca.objects.all()
    if request.method == 'POST':
        form = MarcaForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('core_marca')
    form = MarcaForm()
    context = {
        'marcas': marcas,
        'form': form,

    }
    return render(request, 'core/marca/lista_marca.html', context)
