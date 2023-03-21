from rest_framework import serializers
from accounts.models import User, Profile
from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators
from django.core import exceptions


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    password = serializers.CharField(write_only=True, required=True,
                                     style={'input_type': 'password', 'placeholder': 'Password'})
    confirm_password = serializers.CharField(write_only=True, required=True,
                                             style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = ['email', 'is_active', 'created_date', 'updated_date', 'password', 'confirm_password', 'profile']

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        rep.pop('password', None)
        return rep

    def validate(self, data):
        user = User(email=data['email'], password=data['password'],
                    is_active=data['is_active'])
        password = data.get('password')
        errors = dict()
        try:
            validators.validate_password(password=password, user=user)

        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserSerializer, self).validate(data)

    def create(self, validated_data):
        if validated_data['password'] == validated_data['confirm_password']:
            password = make_password(validated_data['password'])
        else:
            raise serializers.ValidationError({'password': 'password not equal to confirmation!'})
        user = User.object.create(email=validated_data['email'], password=password,
                                  is_active=validated_data['is_active'])
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(user=user, first_name=profile_data.get('first_name', None),
                                         last_name=profile_data.get('last_name', None),
                                         image=profile_data.get('image', None))
        return user


