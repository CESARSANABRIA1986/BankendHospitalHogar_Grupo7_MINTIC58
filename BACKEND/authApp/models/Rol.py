from pyexpat import model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Rol(models.Model):
    class TipoUsuario(models.TextChoices):
        PACIENTE = 'PA', _('Paciente')
        ACUDIENTE = 'AC', _('Acudiente')
        MEDICO = 'MD', _('Medico')
        ENFERMERO = 'EF', _('Enfermero')
    tipoUsuario= models.CharField(primary_key=True, max_length=3, choices=TipoUsuario.choices)
    permisos = models.IntegerField(default=0)