from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Location, City


class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model = Category
    fields = ('id', 'title')


class LocationSerializer(serializers.ModelSerializer):
  # created_by = serializers.ReadOnlyField(source='created_by.username')
  # picture = serializers.PrimaryKeyRelatedField(many=True, queryset=image)
  class Meta:
    model = Location
    fields = ('id', 'title', 'category', 'description', 'picture', 'date_created', 'created_by')


class CitySerializer(serializers.ModelSerializer):
  # created_by = serializers.ReadOnlyField(source='created_by.username', read_only=False)
  class Meta:
    model = City
    fields = ('id', 'product_tag', 'category', 'price', 'picture', 'status', 'date_created', 'created_by')


class UserSerializer(serializers.ModelSerializer):
  locations = serializers.PrimaryKeyRelatedField(many=True, queryset=Location.objects.all())
  cities = serializers.PrimaryKeyRelatedField(many=True, queryset=City.objects.all())

  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'date_joined', 'locations', 'cities']