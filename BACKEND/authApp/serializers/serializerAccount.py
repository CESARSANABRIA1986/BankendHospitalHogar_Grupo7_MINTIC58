from dataclasses import field, fields
from pyexpat import model
from authApp.models.Account import Account
from rest_framework import serializers

class SerializadorAccount(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['especializacion','fechaIngreso', 'descripcion']