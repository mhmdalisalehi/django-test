from rest_framework import serializers
from .models import Data
from accounts.models import User


class DataSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Data
        fields = ['name', 'description','owner']


class UserSerializer(serializers.ModelSerializer):
    data = serializers.PrimaryKeyRelatedField(many=True, queryset=Data.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email','data']

