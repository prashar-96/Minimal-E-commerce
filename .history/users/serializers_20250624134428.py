# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'is_admin')

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['is_admin'] = user.is_admin
#         return token

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.BooleanField(read_only=True)  # Explicitly declare the field
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_admin')
        extra_kwargs = {
            'email': {'required': False},  # Optional: adjust as needed
            'id': {'read_only': True} 
        }

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        if user.is_admin is not None:
            token['is_admin'] = user.is_admin
        token['username'] = user.username
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['is_admin'] = self.user.is_admin
        return data