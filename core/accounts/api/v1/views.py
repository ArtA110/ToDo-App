from rest_framework.viewsets import ModelViewSet
from accounts.models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrAdmin
from .filters import UserFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserView(ModelViewSet):
    queryset = User.object.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

# class ProfileView(ModelViewSet):
#     pass
