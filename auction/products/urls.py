from django.urls import path
from .views import *
urlpatterns = [
    path('', views_index, name='products_index'),
]