from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate, tokens
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator


from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=6, max_length=25, write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password"
        ]

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        if not username.isalnum():
            raise ValueError('username must contains chars as well')

        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=225)
    password = serializers.CharField(max_length=28, write_only=True)
    token = serializers.SerializerMethodField()

    def get_token(self, obj):

        user = User.objects.get(email=obj['email'])

        return {
            'access': user.tokens()['access'],
            'refresh': user.tokens()['refresh'],
        }

    class Meta:
        fields = ['email', 'password', 'token']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        token = attrs.get('token')

        user = authenticate(email=email, password=password)
        if not user:
            raise exceptions.AuthenticationFailed('there is no such user')
        if not user.is_active:
            raise exceptions.AuthenticationFailed('this account is blocked')
        if not user.is_verify:
            raise exceptions.AuthenticationFailed('please verify your email')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens(),
        }
