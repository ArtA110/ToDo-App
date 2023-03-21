from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from todo.models import Task
from .permissions import IsOwnerOrAdmin
from .filters import TaskFilter
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import DefaultPagination
from rest_framework import filters


class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrAdmin]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = TaskFilter
    pagination_class = DefaultPagination
    ordering_fields = ['created_date', 'published_date']
