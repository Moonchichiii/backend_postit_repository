from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserRegistrationSerializer, TokenObtainWithUserIdSerializer
from profiles.models import Profile 

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user = User.objects.get(username=response.data['username'])
            try:
                profile = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                profile = None

            refresh = RefreshToken.for_user(user)

            response.data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                },
                'profile_id': profile.id if profile else None  
            }
        return response
    
class TokenObtainWithUserIdView(TokenObtainPairView):
    serializer_class = TokenObtainWithUserIdSerializer
