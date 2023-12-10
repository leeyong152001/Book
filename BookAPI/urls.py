from django.urls import path, include
from .views import * 

urlpatterns = [
    path('books/', ALLBookViewSet.as_view()),
    path('books/<int:id>/', DetailBookViewSet.as_view()),
    path('carts/', CartViewSet.as_view()),
    path('carts/<int:user_id>/', CartUserViewSet.as_view()),
]
