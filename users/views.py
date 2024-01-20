from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError

from .serializers import UserRegistrationSerializer


class UserRegistrationView(CreateAPIView):
    """
    handles user registration requests and returns a response.
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
 
    def create(self, request, *args, **kwargs):
        try:
            
            response = super().create(request, *args, **kwargs)
            if response.status_code == status.HTTP_201_CREATED:
                # Retriving the new user from db. 
                user = User.objects.get(username=request.data['username'])
                # Generating JWT access token. 
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
                    'message': 'Registration successful!'
                }
                return response
        except ValidationError as exc:
            custom_response_data = {
                "errors": exc.detail,
                "message": "Registration failed due to invalid input."
            }
            return Response(custom_response_data, status=status.HTTP_400_BAD_REQUEST)
      