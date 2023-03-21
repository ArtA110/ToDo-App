from rest_framework.viewsets import ModelViewSet
from accounts.models import User, Profile
from .serializers import UserSerializer
from .permissions import IsOwnerOrAdmin


class UserView(ModelViewSet):
    queryset = User.object.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrAdmin]

# class ProfileView(ModelViewSet):
#     pass