from django.shortcuts import render
from . models import Category, Products
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def product_list(request):
    all_products = Products.objects.all()
    paginator = Paginator(all_products, 8)  
    page_number = request.GET.get('page') 
    page_products = paginator.get_page(page_number)
    num_of_pages = paginator.num_pages
    dict ={'pages':[]}
    lst = []
    for i in range(1,num_of_pages+1):
        lst.append(i)
    dict['pages'] = lst
    print(dict)

    return render(request, 'products.html', {'products': page_products, 'pages':dict['pages']})

@login_required(login_url='/login')
def product_detailed_view(request, pk):
    product = Products.objects.get(pk = pk)
    extra_images = product.product_images.all()
    category_obj = Category.objects.get(name = product.category.name)
    related_products = category_obj.category_products.all()
    print(related_products)
    return render(request, 'product_detailed.html', {'product':product, 'extra_images':extra_images,
                                                     'category_obj':category_obj,'related_products':related_products})