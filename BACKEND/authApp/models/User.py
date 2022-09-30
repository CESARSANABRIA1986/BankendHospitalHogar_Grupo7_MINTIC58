from logging import RootLogger
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):

        if not username:
            raise ValueError('User must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

        
class User(AbstractBaseUser, PermissionsMixin):
    id                  =   models.IntegerField('id', primary_key=True)
    username            =   models.CharField('username', max_length=50, unique=True)
    password            =   models.CharField('Password', max_length=256)
    primerNombre        =   models.CharField('PrimerNombre', max_length=50)
    segundoNombre       =   models.CharField('SegundoNombre', max_length=50)
    primerApellido      =   models.CharField('PrimerApellido', max_length=50)
    segundoApellido     =   models.CharField('SegundoApellido', max_length=50)
    celular             =   models.CharField('Celular', max_length=50)
    pais                =   models.CharField('Pais', max_length=100)
    departamento        =   models.CharField('Departamento', max_length=100)
    municipio           =   models.CharField('Municipio', max_length=100)
    barrio              =   models.CharField('Barrio', max_length=256)
    direccion           =   models.CharField('Direccion', max_length=256)    
    email               =   models.EmailField('Email', max_length=250)

    def save(self, **kwargs):
        some_salt       =   'mMUj0DrIK6vgtdIYepkIxN'
        self.password   =   make_password(self.password, some_salt)
        super().save(**kwargs)

    object = UserManager()
    USERNAME_FIELD = 'username'