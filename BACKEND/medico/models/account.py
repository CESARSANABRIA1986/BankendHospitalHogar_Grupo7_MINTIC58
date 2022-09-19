from django.db import models
from .user import Usuario

class Cuenta(models.Model):
    id=models.AutoField(primary_key=true)
    user = models.ForeignKey(Usuario, related_name='account', on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    description =models.CharField(default='',max_length=100)
    name =models.CharField(default='', max_length=50)