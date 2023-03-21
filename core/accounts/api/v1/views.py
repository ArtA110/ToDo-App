from rest_framework.viewsets import ModelViewSet
from accounts.models import User, Profile
from .serializers import UserSerializer


class UserView(ModelViewSet):
    queryset = User.object.filter(is_active=True)
    serializer_class = UserSerializer
class ProfileView(ModelViewSet):
    pass