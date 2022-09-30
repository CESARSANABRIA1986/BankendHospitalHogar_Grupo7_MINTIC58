from django.db import models

from .User import User

class Rol(models.Model):
    idRol = models.BigAutoField(primary_key=True)
    idUser = models.ForeignKey(User, related_name='id_User', on_delete=models.CASCADE)
    tipoUsuario= models.CharField('tipoUsuario', max_length=50)
    permisos = models.IntegerField(default=0)