from urllib import response

import jwt
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.urls import reverse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.serializers import SignupSerializer, SigninSerializer, EmailVerificationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .util import Util


class SignupView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request):
        data = self.request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(email=serializer.data["email"])
        token = RefreshToken.for_user(User.objects.get(email=serializer.data["email"])).access_token
        relative_link = reverse('email_verify')
        current_link = get_current_site(request).domain
        absolute_url = f"http://{current_link}{relative_link}?token={token}"
        email_body = f"Hi {user.username} use this link below to verify your email address \n {absolute_url}"
        email_data = {
            'email_body': email_body,
            'email_subject': 'Verify your email',
            'email_to': user.email
        }
        Util.send_email(email_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VerifyEmail(APIView):
    serializer_class = EmailVerificationSerializer
    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Token', type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get("token")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
            return Response({
                "email": "Successfully verified",
                "token": token
            }, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({
                'error': 'Token expired',
            }, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.exceptions.DecodeError:
            return Response({
                'error': 'Invalid token',
            }, status=status.HTTP_400_BAD_REQUEST)


class SigninView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SigninSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
