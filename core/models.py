from django.db import models


class Pessoa(models.Model):
    nome = models.CharField( max_length=100)    
    endereco = models.CharField(_ max_length=200)
    telefone = models.CharField( max_length=20)



class Marcas(models.Model):
    nome = models.CharField(_ max_length=50)

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, = on_delete=models.DO_NOTHING)