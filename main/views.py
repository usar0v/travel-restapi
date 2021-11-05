from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics

from .models import Category, Location, City
from .serializers import CategorySerializer, LocationSerializer, CitySerializer, UserSerializer


class ListCategory(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class ListLocation(generics.ListCreateAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer


class DetailLocation(generics.RetrieveUpdateDestroyAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer


class ListCity(generics.ListCreateAPIView):
  queryset = City.objects.all()
  serializer_class = CitySerializer


class DetailCity(generics.RetrieveUpdateDestroyAPIView):
  queryset = City.objects.all()
  serializer_class = CitySerializer


class ListUser(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer