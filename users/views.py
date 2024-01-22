from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegistrationSerializer, TokenObtainWithUserIdSerializer
from rest_framework.exceptions import ValidationError


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user = User.objects.get(username=request.data['username'])
            refresh = RefreshToken.for_user(user)

            response.set_cookie(
                key='refresh_token',
                value=str(refresh),
                httponly=True,
                samesite='None',
                secure=False,
            )
            response.data = {
                'access': str(refresh.access_token),
                'user': UserRegistrationSerializer(user).data,
                'message': 'Registration successful!'
            }
        return response


class TokenObtainWithUserIdView(TokenObtainPairView):
    serializer_class = TokenObtainWithUserIdSerializer
