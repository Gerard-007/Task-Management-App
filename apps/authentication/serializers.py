from django.contrib import auth
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .apps import AuthenticationConfig
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=60,
        min_length=6,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'dob', 'age', 'password']

    def validate(self, attrs):
        email = attrs.get("email", '')
        username = attrs.get("username", '')

        if not username.isalnum():
            raise serializers.ValidationError("Username should only contain alphanumeric characters")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']



class SigninSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, min_length=6, write_only=True)
    email=serializers.EmailField(max_length=225, min_length=4)
    username=serializers.CharField(max_length=120, read_only=True)
    tokens=serializers.CharField(max_length=555, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get("email", '')
        password = attrs.get("password", '')
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid email or password")
        if not user.is_active:
            raise AuthenticationFailed("Your account is inactive")
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }
