from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from todo.models import Task
from .permissions import IsOwnerOrAdmin


class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrAdmin]