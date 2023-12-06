from django.urls import path, include
from .views import * 

urlpatterns = [
    path('', HomeViewSet.as_view()),
]
