from typing import Dict

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data: Dict):
        email = validated_data.get('email')
        username = email
        password = validated_data.get('password')

        return User.objects.create_user(username, email, password)
