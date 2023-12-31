from django.urls import path, include
from .views import * 

urlpatterns = [
    path('blacklist/', BlacklistRefreshView.as_view()),
    path('books/', ALLBookViewSet.as_view()),
    path('books/<int:id>/', DetailBookViewSet.as_view()),
    path('carts/', CartViewSet.as_view()),
    path('cart/', CartUserViewSet.as_view()),
    path('orders/', OrderViewSet.as_view()),  
    path('comments/', CommentViewSet.as_view()),
    path('wishlists/', WishListViewSet.as_view()),
    path('user/',GetUser.as_view()),
]
