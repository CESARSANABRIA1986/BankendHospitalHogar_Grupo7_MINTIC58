from django.db import models

from .User import User


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    especializacion = models.CharField('Especializacion', max_length=100)
    fechaIngreso = models.DateTimeField()