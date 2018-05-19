from django.contrib import admin
from . import models


admin.site.register(models.Product) # This will add Product to admin site
admin.site.register(models.Category) # This will add Category to admin site

# Register your models here.
