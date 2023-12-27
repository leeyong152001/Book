from django.urls import path, include
from .views import * 
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/',RegisterView.as_view(),name="register"),
    path('login/',LoginAPIView.as_view(),name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('books/<int:id>/', DetailBookViewSet.as_view()),
    path('carts/', CartViewSet.as_view()),
    path('carts/', CartUserViewSet.as_view()),
    path('orders/', OrderViewSet.as_view()),  
    path('comments/', CommentViewSet.as_view()),
    path('ratings/', RatingViewSet.as_view()),
    path('wishlists/', WishListViewSet.as_view()),
]
