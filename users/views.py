from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer
from .utils.auth import jwt_token_generation


class UserRegistrationView(generics.CreateAPIView):
    """
    Queryset all user objects and using serializer for checks
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request)
        if response.status_code == status.HTTP_201_CREATED:
            user = User.objects.get(username=response.data['username'])
            jwt_tokens = jwt_token_generation(user)
            
            response.data.update(jwt_tokens)
        return response


class UserLoginView(APIView):
    """
    user login requests, authenticates the user and generates jtw tokens
    """

    def post(self, request):        
        username = request.data.get('username')
        password = request.data.get('password')

        # authenticating user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User is authenticated, generate JWT tokens from auth utils. 
            refresh = RefreshToken.for_user(user)
            profile_id = user.profile.id if hasattr(user, 'profile') else None
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id,
                'profile_id': profile_id
            })
        else:
            # Authentication failed
            return Response({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)



class ChangePasswordView(APIView):
    # limiting access for only authenticated users to do changes.
    permission_classes = [IsAuthenticated]

    def post(self, request):
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
