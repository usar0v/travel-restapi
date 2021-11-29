
from django.db import models
from django.utils import timezone


class User(models.Model):
  full_name = models.CharField(max_length=50, unique=True)
  phone_number = models.CharField(max_length=12, null=True)
  avatar = models.ImageField(upload_to='user_image/', height_field=None, width_field=None, max_length=100, null=True)
  date_joined = models.DateTimeField(default=timezone.now)

class Category(models.Model):
  title = models.CharField(max_length=155, unique=True)

  class Meta:
    verbose_name_plural = 'Categories'
  def __str__(self):
    return self.title


class Location(models.Model):
  title = models.CharField(max_length=150)
  category = models.ForeignKey(Category, related_name='locations', on_delete=models.CASCADE)
  description = models.TextField()
  picture = models.ImageField(upload_to='picture/', height_field=None, width_field=None, max_length=200, default='picture/default.jpg')
  likes = models.IntegerField(default=0)
  comment = models.TextField(null=True)
  created_by = models.ForeignKey(User, related_name='locations', on_delete=models.CASCADE, null=True)
  date_created = models.DateField(auto_now_add=True)

  class Meta:
    ordering = ['-date_created']

  def __str__(self):
    return self.title

