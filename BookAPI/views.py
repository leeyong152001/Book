from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import *
from .models import *


# Create your views here.
class HomeViewSet(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookALLViewSet(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [IsAuthenticated]

class BookDeleteViewSet(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [IsAdminUser]


class BookDetailViewSet(generics.ListAPIView):
    ...

class CartViewSet(generics.ListCreateAPIView):
    ...