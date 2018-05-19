from django.contrib import admin
from . import models
import decimal

#admin.site.register(models.Product) # This will add Product to admin site
admin.site.register(models.Category) # This will add Category to admin site

admin.site.site_header = "Coretabs Online Shop Administration"

admin.site.site_title = "Coretabs Online Shop Administration"

admin.site.index_title = ""


def make_price_zero(modeladmin, request, queryset):
    queryset.update(price=0)


make_price_zero.short_description = "Make selected products free"


def discount(self, request, queryset):
    for product in queryset:
        product.price = product.price * decimal.Decimal('0.8')
        product.save()


discount.short_description = 'Apply 20%% DISCOUNT'



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_at'
    search_fields = ['name']
    list_display = ('name', 'price', 'stock', 'category')
    list_filter = ('category', 'create_at')
    actions = [make_price_zero, discount]



# Register your models here.
