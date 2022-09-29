from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authApp.serializers.serializerUser import SerializadorUser


class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = SerializadorUser(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)