from django.contrib.auth.models import User


from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView


from .serializers import UserRegistrationSerializer


class UserRegistrationView(generics.CreateAPIView):
     # Queryset all user objects and using serializer for checks
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Retrieving new user
        if response.status_code == status.HTTP_201_CREATED:
            
            user = User.objects.get(username=response.data['username'])
            """
            Generates the jwt tokens for the user both access and refresh token. 
            giving the refresh token instantly to the user to avoid the user to login after the registration quick access instead. 
            """
        
            refresh = RefreshToken.for_user(user)
            response.data.update({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'profile_id': user.profile.id if hasattr(user, 'profile') else None
            })
        return response


class ChangePasswordView(APIView):
     # limiting access for only authenticated users to do changes. 
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
          # post request to change password
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
    # delete only for authenticated users
    permission_classes = [IsAuthenticated]

    def delete(self, request):
          # delete request of users account
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
