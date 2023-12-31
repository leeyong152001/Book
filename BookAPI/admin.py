from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Voucher)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)