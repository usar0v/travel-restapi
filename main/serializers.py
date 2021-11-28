from rest_framework import serializers
from .models import Category, Location
from django.contrib.auth.models import User


class LocationSerializer(serializers.ModelSerializer):
  # created_by = serializers.ReadOnlyField(source='created_by.username')
  # picture = serializers.PrimaryKeyRelatedField(many=True, queryset=image)
  class Meta:
    model = Location
    fields = ('id', 'title', 'category', 'likes', 'comment', 'description', 'picture', 'date_created', 'created_by')


class CategorySerializer(serializers.ModelSerializer):
  locations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  locations = LocationSerializer(many=True, read_only=True)
  class Meta:
    model = Category
    depth = 2
    fields = ('id', 'title', 'locations')


class UserSerializer(serializers.ModelSerializer):
  locations = serializers.PrimaryKeyRelatedField(many=True, queryset=Location.objects.all())
  locations = LocationSerializer(many=True, read_only=True)

  class Meta:
    model = User
    fields = ['id', 'username', 'avatar', 'phone_number', 'date_joined', 'locations']