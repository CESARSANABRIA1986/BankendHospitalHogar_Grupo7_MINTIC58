from rest_framework import serializers
from datetime import datetime
from authApp.models.User import User
from authApp.models.Account import Account
from authApp.models.Rol import Rol
from authApp.serializers.serializerAccount import SerializadorAccount
from authApp.serializers.serializerRol import SerializadorRol
from drf_writable_nested import WritableNestedModelSerializer
from setuptools.config._validate_pyproject.fastjsonschema_validations import validate

class SerializadorUser(WritableNestedModelSerializer, serializers.ModelSerializer):
    account = SerializadorAccount(many = True)

    class Meta:

        model = User

        fields = ['id','username','password', 'password','primerNombre','segundoNombre', 'primerApellido', 'segundoApellido','celular','pais', 'departamento','municipio','barrio','direccion', 'email', 'account']

        def create(self, validated_data):
            accountData = validated_data.pop('account')
            userInstance = User.objects.create(**validated_data)
            Account.objects.create(user=userInstance, **accountData)
            return userInstance


        def to_representation(self, obj):
            user = User.objects.get(id=obj.id)
            account = Account.objects.get(user = obj.id)

            return {

                "id": user.id,
                "username" : user.username,
                "password": user.password,
                "primerNombre":user.primerNombre,
                "segundoNombre":user.segundoNombre,
                "primerApellido":user.primerApellido,
                "segundoApellido":user.segundoApellido,
                "celular": user.celular,
                "pais": user.pais,
                "departamento": user.departamento,
                "municipio":user.municipio,
                "barrio": user.barrio,
                "direccion": user.direccion,
                "email": user.email,
                "account":{
                    "id": account.id,
                    "especializacion": account.especializacion,
                    "fechaIngreso": account.fechaIngreso,
                    "descripcion": account.descripcion,
                }
            }