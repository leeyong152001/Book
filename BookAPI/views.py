# from django.shortcuts import render
# from django.shortcuts import get_object_or_404

from rest_framework import generics, viewsets, status, views
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .serializers import *
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user

class GetUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self,request):
        user = request.user
        return Response({user.id,user.username})


class BlacklistRefreshView(views.APIView):
    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Success")

class ALLBookViewSet(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class DetailBookViewSet(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = 'id'
    serializer_class = BookSerializers

class CartViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAdminUser]

class CartUserViewSet(generics.ListCreateAPIView, generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class CommentViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class WishListViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [IsAuthenticated]
