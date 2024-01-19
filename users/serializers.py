from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError({"confirm_password": "Passwords don't match!"})
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({"username": "Username is already in use!"})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "Email is already in use!"})
        return data
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
