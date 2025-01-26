from django.shortcuts import render
from rest_framework import request
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer
from core.permissions import IsOwner


class TaskListView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'id'

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)



