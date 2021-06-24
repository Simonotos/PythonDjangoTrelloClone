from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('saveTile', views.saveTile, name='saveTile'),
]