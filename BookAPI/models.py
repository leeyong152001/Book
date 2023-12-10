from django.db import models
from django.contrib.auth.models import User

import datetime as dt

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=255, db_index=True)
    book_description = models.TextField()
    book_url = models.ImageField()
    print_length = models.IntegerField()
    language = models.CharField(max_length=255, db_index=True)
    author_name = models.CharField(max_length=255, db_index=True)
    price = models.IntegerField()

    def __str__(self):
        return self.book_name


class Cart(models.Model):
    user_id = models.OneToOneField(User, on_delete= models.CASCADE)
    books = models.ManyToManyField(Book)
    time_order = models.DateTimeField(default=dt.datetime.now())

    def __str__(self):
        return "Cart - " + self.user_id.username

class Discount:
    ...