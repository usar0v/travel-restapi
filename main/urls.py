from django.contrib import admin
from django.urls import path

from .views import ListCategory, DetailCategory, ListCity, DetailCity, ListLocation, DetailLocation, ListUser, DetailUser

urlpatterns = [
    path('categories/', ListCategory.as_view()),
    path('categories/<int:pk>/', DetailCategory.as_view()),

    path('cities/', ListCity.as_view()),
    path('cities/<int:pk>/', DetailCity.as_view()),

    path('location/', ListLocation.as_view()),
    path('location/<int:pk>/', DetailLocation.as_view()),

    path('users/', ListUser.as_view()),
    path('users/<int:pk>/', DetailUser.as_view()),
]