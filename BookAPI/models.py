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

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self) -> str:
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivery_crew', null= True)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)

class OrderItem(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    bookitem = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('bookitem', 'order')