from rest_framework import serializers

from django.contrib.auth.models import User

from .models import *

class BookSerializers(serializers.ModelSerializer):
    #user = UserSerializer(required=False) 

    class Meta:
        model = Book
        fields = '__all__'
        lookup_field = 'id'

    # def create():
    #     ...

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class CartSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    books_id = BookSerializers(many =True, read_only = True, source='books')

    class Meta:
        model = Cart
        fields = ['user_id', 'books_id','time_order']