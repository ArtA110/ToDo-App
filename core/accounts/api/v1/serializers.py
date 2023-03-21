from rest_framework import serializers
from accounts.models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ['email', 'is_active', 'created_date', 'updated_date', 'profile']

    def create(self, validated_data):
        user = User.object.create(email=validated_data['email'], is_active=validated_data['is_active'])
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(user=user, first_name=profile_data.get('first_name', None),
                                         last_name=profile_data.get('last_name', None),
                                         image=profile_data.get('image', None))
        return user


