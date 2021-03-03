from django.forms import ModelForm
from django import forms
from core.models import (Pessoa,
                         Veiculo,
                         MovRotativo,
                         Mensalista,
                         MovMensalista,
                         Marca)
from django.contrib.admin import widgets
# inputs
import datetime


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    #input_formats = ['%y-%m-%dT%H:%M']
    # format = '%y-%m-%dT%H:%M'
    pass


class DateInput(forms.DateInput):
    input_type = 'date'
    attrs = {'value': datetime.datetime.now().strftime("%d-%m-%Y")}


# forms
# pessoas


class PessoaForm(ModelForm):

    class Meta:
        model = Pessoa
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)

        self.fields['nome'].widget = forms.TextInput(
            attrs={'placeholder': 'nome'})

        self.fields['endereco'].widget = forms.TextInput(
            attrs={'placeholder': 'endereço'})

        self.fields['telefone'].widget = forms.TextInput(
            attrs={'placeholder': 'telefone'})

# veiculos


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


# rotativos
class MovRotForm(ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__'
        widgets = {
            'checkin': DateTimeInput(format='%Y-%m-%dT%H:%M'),
            'checkout': DateTimeInput(format='%Y-%m-%dT%H:%M'),
        }

# mensalistas


class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'
        widgets = {
            'inicio': DateInput(format='%Y-%m-%d'),
        }

# mov mensalista


class MovMensalistaForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'
        widgets = {
            'data_pagamento': DateInput(format='%Y-%m-%d'),
        }

# marca


class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
