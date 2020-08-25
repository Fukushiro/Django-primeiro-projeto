
from django.db import models
from django.contrib.auth.models import User
import math

# pessoa


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

# marca


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} - {self.nome}'

# veiculo


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()
    proprietario = models.ForeignKey(
        Pessoa, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'{self.marca.nome} - {self.placa}'


class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'Parametros gerais'

# rotativo


class MovRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False, auto_now_add=False)
    checkout = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    veiculo = models.ForeignKey(Veiculo,  on_delete=models.DO_NOTHING)
    pago = models.BooleanField(default=False)

    def horas_total(self):
        if self.checkout == None:
            return 0
        return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)

    def total(self):
        return self.valor_hora * self.horas_total()

    def veiculoShow(self):
        return f'{self.veiculo.marca.nome} - {self.veiculo.placa}'

    def __str__(self):
        return f'{self.veiculo.placa}'

# mensalista


class Mensalista(models.Model):
    veiculo = models.ForeignKey(
        Veiculo,  on_delete=models.DO_NOTHING)
    inicio = models.DateField(auto_now=False, auto_now_add=False)
    #parametro = models.ForeignKey(Parametros, on_delete=models.DO_NOTHING)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def veiculoShow(self):
        return f'{self.veiculo}'

    def valorMes(self):
        return f'{self.parametro.valor_mes}'

    def __str__(self):
        return f'{self.veiculo} - {self.inicio}'


class MovMensalista(models.Model):
    mensalista = models.ForeignKey(
        Mensalista,  on_delete=models.DO_NOTHING)
    data_pagamento = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.mensalista} - {self.total}'

# profile
