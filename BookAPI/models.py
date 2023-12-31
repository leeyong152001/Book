from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime as dt

class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self) -> str:
        return self.title


class Book(models.Model):
    book_name = models.CharField(max_length=255, db_index=True)
    book_description = models.TextField()
    book_url = models.ImageField()
    print_length = models.IntegerField()
    language = models.CharField(max_length=255, db_index=True)
    author_name = models.CharField(max_length=255, db_index=True)
    price = models.IntegerField()
    category = models.ManyToManyField(Category)
    # publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    wished_item = models.ForeignKey(Book,on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  "Wishlist - " + self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(5.0)], default=1.0)
    comment = models.TextField()

    def __str__(self):
        return self.user.username + " - " + self.book.book_name

class Cart(models.Model):
    user_id = models.OneToOneField(User, on_delete= models.CASCADE)
    books = models.ManyToManyField(Book)
    time_order = models.DateTimeField(default=dt.datetime.now())

    def __str__(self):
        return "Cart - " + self.user_id.username

class Voucher(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivery_crew', null= True)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    voucher = models.ForeignKey('Voucher', on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.user.username

# class Status(models.Model):
#     value = models.CharField(max_length=255)

#     def __str__(self):
#         return self.value

class OrderItem(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    bookitem = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('bookitem', 'order')

# class OrderHistory(models.Model):
#     ...
