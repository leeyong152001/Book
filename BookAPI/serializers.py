from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from django.contrib import auth

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username']

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        lookup_field = 'id'


class CartSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    books_id = BookSerializers(many =True, source='books')

    class Meta:
        model = Cart
        fields = ['user_id', 'books_id','time_order']

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

# class PublisherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Publisher
#         fields = '__all__'

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
