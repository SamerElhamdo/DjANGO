from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ('name',)



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    decription = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
