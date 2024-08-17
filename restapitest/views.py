from restapitest.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Data
from .serializer import *
from rest_framework import mixins
from rest_framework import generics
from accounts.models import User


class DataList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,
    IsOwnerOrReadOnly]
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,
    IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer