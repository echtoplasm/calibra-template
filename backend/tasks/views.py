from django.shortcuts import render
from rest_framework import generics, permissions, serializers
from .models import Task
from api.serializers import TaskSerializer, TaskToggleCompleteSerializer

# Create your views here.
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        task_owner = self.request.user
        return Task.objects.filter(task_owner=task_owner).order_by('created_at')
    
class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        task_owner = self.request.user
        return Task.objects.filter(task_owner=task_owner)

class TaskToggleComplete(generics.UpdateAPIView):
    serializer_class = TaskToggleCompleteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        task_owner = self.request.user
        return Task.objects.filter(task_owner=task_owner)
    
    def perform_update(self, serializer):
        serializer.instance.completed = not (serializer.instance.completed)
        serializer.save()





