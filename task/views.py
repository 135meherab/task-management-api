from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your views here.

class TaskViewSets(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    def get_queryset(self):
        user_id = self.request.query_params.get('user')
        if user_id:
            user = get_object_or_404(User, id = user_id)
            return Task.objects.filter(user = user)
        return super().get_queryset()
        
class TaskCompleteViewSets(viewsets.ViewSet):

    def update(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        task.is_complete = True
        task.save()
        serializer = self.serializer_class(task)
        return Response(serializer.data)
        
class DeleteTask(APIView):
    def delete(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response({'message': 'Task deleted successfully'})
        