from rest_framework import status, views
from rest_framework.response import Response

from authApp.serializers.serializerRol import SerializadorRol

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RolCreateView(views.APIView):
    
    def post(self, request):
        serializer = SerializadorRol(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(status=status.HTTP_201_CREATED)