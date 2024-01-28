from rest_framework import serializers

from django.contrib.auth.models import User

from django.contrib.auth.password_validation import validate_password
        
    # fields to be included in serialization
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}  

    # Validating password using built in validator
    def validate_password(self, value):    
        validate_password(value)
        return value

    def create(self, validated_data):        
        return User.objects.create_user(**validated_data)