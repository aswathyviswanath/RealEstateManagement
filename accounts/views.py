from .serializer import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView


class RegisterAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class=RegisterSerializer

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response({'message': 'User not created', 'errors': errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class=LoginSerializer

    def post(self, request):

        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            errors = serializer.errors
            return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(
            username=serializer.data['username'], password=serializer.data['password'])

        if user:
            refresh = RefreshToken.for_user(user)

            return Response({'message': 'Login Successful', 'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)

        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
