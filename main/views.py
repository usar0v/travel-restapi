from rest_framework import generics

from .models import Category, Location, User
from .serializers import CategorySerializer, LocationSerializer, UserSerializer


class ListCategory(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class ListLocation(generics.ListCreateAPIView):
  # print(Location.data.get('id'))
  queryset = Location.objects.all()
  serializer_class = LocationSerializer


class DetailLocation(generics.RetrieveUpdateDestroyAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer


class ListUser(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer