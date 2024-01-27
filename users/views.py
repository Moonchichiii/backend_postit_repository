from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


from .serializers import UserRegistrationSerializer, TokenObtainWithUserIdSerializer
from profiles.models import Profile 



class UserRegistrationView(generics.CreateAPIView):
    """
    Api view user registration
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    class UserRegistrationView(generics.CreateAPIView):
        queryset = User.objects.all()
        serializer_class = UserRegistrationSerializer

        def create(self, request, *args, **kwargs):
            """
            User registation with jwt token response
            """
            response = super().create(request, *args, **kwargs)
            if response.status_code == status.HTTP_201_CREATED:
                
                user = get_object_or_404(User, username=request.data.get('username'))
                
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



class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        new_password = request.data.get("new_password")
        try:
            validate_password(new_password, user)
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
