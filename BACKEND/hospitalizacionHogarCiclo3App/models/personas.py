import email
from ssl import _PasswordType
from django.db import models

from BACKEND.hospitalizacionHogarCiclo3App.models.tipoPersonas import tipoPersona


class persona(abstractBaseUser, PermissionsMixin):
    id                  =   models.BigAutoField(primary_key=True)
    tipoUsuario         =   models.ForeignKey(tipoPersona, related_name='tipoUsuario_id', on_delete=models.CASCADE)
    password            =   models.CharField('Password', max_length=256)
    primerNombre        =   models.CharField('PrimerNombre', max_length=50)
    segundoNombre       =   models.CharField('SegundoNombre', max_length=50)
    primerApellido      =   models.CharField('PrimerApellido', max_length=50)
    segundoApellido     =   models.CharField('SegundoApellido', max_length=50)
    celular             =   models.CharField('Celular', max_length=50)
    pais                =   models.CharField('Pais', max_length=100)
    departamento        =   models.CharField('Departamento', max_length=100)
    municipio           =   models.CharField('Municipio', max_length=100)
    direccion           =   models.CharField('Direccion', max_length=256)    
    email               =   models.EmailField('Email', max_length=120, unique=True)

    def save(self, **kwargs):
        some_salt       =   'mMj0DrIK7vgTdIYwpkIxN'
        self.password   =   make_password(self.password, some_salt)
        super().save(**kwargs)
        object = UserManager()
    
    USERNAME_FIELD = 'email'



