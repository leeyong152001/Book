# from django.shortcuts import render
# from django.shortcuts import get_object_or_404

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import *
from .models import *

# Create your views here.
class ALLBookViewSet(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class DetailBookViewSet(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    lookup_field = 'id'
    serializer_class = BookSerializers

class CartViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAdminUser]

class CartUserViewSet(generics.ListCreateAPIView, generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Cart.objects.all()
    lookup_field = 'user_id'
    serializer_class = CartSerializer