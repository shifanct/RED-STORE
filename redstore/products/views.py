from django.shortcuts import render

# Create your views here.

def product_list(request):
    return render(request, 'products.html')

def product_detailed_view(request):
    pass