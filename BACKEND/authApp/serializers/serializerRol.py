from rest_framework import serializers
from authApp.models.User import User
from authApp.models.Rol import Rol


class SerializadorRol(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['idRol',"idUser",'tipoUsuario']