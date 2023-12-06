from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    book_name = models.TextField(max_length=255)
    book_description = models.TextField(max_length=255)
    book_url = models.TextField(max_length=255)
    print_length = models.IntegerField()
    language = models.TextField()
    author_name = models.TextField()
    price = models.IntegerField()


class Cart:
    ...

class Discount:
    ...