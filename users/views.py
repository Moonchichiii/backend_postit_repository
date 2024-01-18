from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import UserRegistrationSerializer

class UserRegistrationView(CreateAPIView):
    """
    user registration    
    
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        creates a new user instance       
        
        """
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)
        return response