from lib2to3.pgen2 import token
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.serializers.serializerUser import SerializadorUser
from authApp.models.User import User
from authApp.models.Account import Account

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.object.all()
    serializer_class = SerializadorUser
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False )

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail': 'Peticion no autorizada'}
            return Response(stringResponse, status= status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)
