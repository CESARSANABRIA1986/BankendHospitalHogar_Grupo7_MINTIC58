from dataclasses import field, fields
from pyexpat import model
from authApp.models.Account import Account
from rest_framework import serializers

class SerializadorCuenta(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['balance','description']