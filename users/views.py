from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


from rest_framework import generics, serializers, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny 
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import UserRegistrationSerializer




# Create your views here.


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    authentication_classes = []
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        confirm_password = serializer.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")

        try:
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return token.key
        except ValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    """
    API view for user logout.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
        removes the user's token on logout
        """
        request.auth.delete()
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
