from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Data
from .serializer import DataSerializer
from rest_framework import mixins
from rest_framework import generics


class DataList(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

