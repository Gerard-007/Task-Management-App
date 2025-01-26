from urllib import response
from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from apps.authentication.serializers import SignupSerializer



class SignupView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request):
        data = self.request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
