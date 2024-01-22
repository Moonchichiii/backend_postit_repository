from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

    
class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    # unique email and username validation
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(), message="Email is already in use!")])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all(), message="Username is already in use!")])

    class Meta:
        model = User
        fields = ('id','username', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        # validating password with django defualt validators. 
        validate_password(value)
        return value

    def validate(self, data):
        # Extra check if passwords match, and then removed from data. 
        if data['password'] != data.pop('confirm_password'):
            raise ValidationError({'confirm_password': ["Passwords don't match."]})
        return data
    
    def create(self, validated_data):
        # creating user with validated data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user




class TokenObtainWithUserIdSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = user.id
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        # adding the user_id to the token response.
        data["user_id"] = self.user.id

        return data
