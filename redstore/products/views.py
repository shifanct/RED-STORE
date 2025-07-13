from django.shortcuts import render
from . models import Category, Products
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def product_list(request):
    all_products = Products.objects.all()
    paginator = Paginator(all_products, 8)

    page_param = request.GET.get('page')
    current_page = request.GET.get('current', '1')

    try:
        current_page = int(current_page)
    except ValueError:
        current_page = 1

    if page_param == 'next_page':
        page_number = current_page + 1
    else:
        try:
            page_number = int(page_param)
        except (TypeError, ValueError):
            page_number = 1

    page_products = paginator.get_page(page_number)

    num_of_pages = paginator.num_pages
    pages_list = list(range(1, num_of_pages + 1))

    return render(request, 'products.html', {
        'products': page_products,
        'pages': pages_list,
        'current_page': page_products.number
    })



@login_required(login_url='/login')
def product_detailed_view(request, pk):
    product = Products.objects.get(pk = pk)
    extra_images = product.product_images.all()
    category_obj = Category.objects.get(name = product.category.name)
    related_products = category_obj.category_products.all()
    print(related_products)
    return render(request, 'product_detailed.html', {'product':product, 'extra_images':extra_images,
                                                     'category_obj':category_obj,'related_products':related_products})