from django.urls import reverse
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import (
    RegisterSerializer,
    LoginSerializer
)

import jwt


class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_qs = User.objects.filter(email=request.data['email'])
        if user_qs.exists():
            user = user_qs[0]
            token = RefreshToken.for_user(user)
            domain = get_current_site(request).domain
            relative_link = reverse("user:verify")
            activation_link = f"http://localhost:3000/register/verifing/{token}"

            message = EmailMessage(
                'Verify your account :',
                f"hello dear {user.username}, \n thank you for your registration in our site \n one more step left - \n verify your account through this link - : {activation_link}",
                "support@example.com",
                [user.email, ]
            )
            message.send()
            data = {
                "token": str(token),
                **serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)


class VerifyACountAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        token = request.GET.get('token')
        try:
            playload = jwt.decode(token, settings.SECRET_KEY, 'HS256')
            user_id = playload['user_id']
            user = User.objects.get(id=user_id)
            user.is_verify = True
            user.save()
            return Response({'success: ': 'Your account is activated'}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError:
            return Response({'error: ': 'token is expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'error: ': 'token is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
