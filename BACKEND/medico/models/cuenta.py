from django.db import models
from .user import Usuario

class Persona(models.Model):
    cedula = models.IntegerField(primary_key=True)
    primernombre = models.CharField(max_length=20)
    segundonombre = models.CharField(max_length=20, blank=True, null=True)
    primerapellido = models.CharField(max_length=20)
    segundoapellido = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    pais = models.CharField(max_length=20, blank=True, null=True)
    departamento = models.CharField(max_length=20, blank=True, null=True)
    municipio = models.CharField(max_length=30, blank=True, null=True)
    barrio = models.CharField(max_length=30, blank=True, null=True)
    idtipopersonas = models.ForeignKey('Tipopersona', models.DO_NOTHING, db_column='idtipopersonas', blank=True, null=True)
    contraseña = models.CharField(max_length=16)
    correelectronico = models.CharField(max_length=50, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    idespecialidad = models.ForeignKey(Especializacion, models.DO_NOTHING, db_column='idespecialidad', blank=True, null=True)