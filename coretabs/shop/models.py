from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decmal_places=2)
    stock = models.PositiveIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    decription = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

class Meta:
    ordering = ('name',)
