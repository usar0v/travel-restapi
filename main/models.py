from django.db import models


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
  picture = models.ImageField(upload_to='picture/', height_field=None, width_field=None, max_length=100, default='picture/default.jpg')
  created_by = models.ForeignKey('auth.User', related_name='locations', on_delete=models.CASCADE, null=True)
  date_created = models.DateField(auto_now_add=True)

  class Meta:
    ordering = ['-date_created']

  def __str__(self):
    return self.title


class City(models.Model):
  product_tag = models.CharField(max_length=10)
  name = models.CharField(max_length=150)
  category = models.ForeignKey(Category, related_name='cities', on_delete=models.CASCADE)
  price = models.IntegerField()
  picture = models.ImageField(upload_to='staticfiles/picture/', height_field=None, width_field=None, max_length=100, default='default.jpg')
  created_by = models.ForeignKey('auth.User', related_name='cities', on_delete=models.CASCADE, null=True)
  status = models.BooleanField(default=True)
  date_created = models.DateField(auto_now_add=True)

  class Meta:
    ordering = ['-date_created']
    verbose_name_plural = 'Cities'

  def __str__(self):
    return '{} {}'.format(self.product_tag, self.name)
