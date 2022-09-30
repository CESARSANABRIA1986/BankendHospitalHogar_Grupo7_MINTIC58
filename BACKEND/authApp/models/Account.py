from django.db import models
from datetime import datetime

from .User import User


class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    especializacion = models.CharField('Especializacion', max_length=100)
    fechaIngreso = models.DateField()
    descripcion = models.CharField('Descripcion', max_length=250)