from django.db import models


class Rol(models.Model):

    idRol = models.BigAutoField(primary_key=True)
    tipoUsuario= models.CharField('tipoUsuario', max_length=50)
    permisos = models.IntegerField(default=0)