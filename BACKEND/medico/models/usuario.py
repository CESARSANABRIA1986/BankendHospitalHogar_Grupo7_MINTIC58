from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password



class AdministradorUsuario(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Los Usuarios debe tener un Username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superUsuario(self, username, password=None):
        
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using = self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length=25, unique=True)
    password = models.CharField('Password', max_length=255)
    name = models.CharField('Name', max_length=50)
    email = models.CharField('Email', max_length=200)


    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = AdministradorUsuario()
    USERNAME_FIELD = 'username'