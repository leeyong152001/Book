from rest_framework import serializers

from django.contrib.auth.models import User

from .models import * #Book

class BookSerializers(serializers.ModelSerializer):
    #user = UserSerializer(required=False) 

    class Meta:
        model = Book
        fields = '__all__'

    # def create():
    #     ...

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']