from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from todo.models import Task

class TaskList(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer