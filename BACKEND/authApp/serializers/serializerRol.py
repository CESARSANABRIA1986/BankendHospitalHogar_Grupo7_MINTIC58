from dataclasses import field, fields
from pyexpat import model
from authApp.models.Rol import Rol

from rest_framework import serializers

class SerializadorRol(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ["tipoUsuario"]