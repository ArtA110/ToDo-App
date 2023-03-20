from rest_framework.permissions import BasePermission
from accounts.models import Profile
from django.shortcuts import get_object_or_404

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            profile_user = get_object_or_404(Profile, user=request.user)
            if profile_user == obj.user or request.user.is_superuser:
                return True
        return False
