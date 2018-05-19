from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product/list.html', {'products': products})



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product/detail.html', {'product': product})


def product_list_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'shop/product/category_by_product.html', {'category': category})

# Create your views heree.
