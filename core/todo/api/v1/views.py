from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from todo.models import Task
from .permissions import IsOwnerOrAdmin
from .filters import TaskFilter
from django_filters.rest_framework import DjangoFilterBackend


class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
