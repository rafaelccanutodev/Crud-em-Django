import datetime
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.PositiveIntegerField(validators=[MinValueValidator(2000)], null=False)
    valor = models.FloatField(null=False)
    data_cadastro = models.DateTimeField(default=datetime.datetime.now, null=False)


    