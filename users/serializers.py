from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    # unique email and username validation
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(), message="Email is already in use!")])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all(), message="Username is already in use!")])

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
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
