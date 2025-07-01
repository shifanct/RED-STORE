from django.shortcuts import render
from . models import Category, Products

# Create your views here.

def product_list(request):
    all_products = Products.objects.all()
    return render(request, 'products.html', {'products':all_products})

def product_detailed_view(request, pk):
    product = Products.objects.get(pk = pk)
    extra_images = product.product_images.all()
    return render(request, 'product_detailed.html', {'product':product, 'extra_images':extra_images})