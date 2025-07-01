from django.shortcuts import render,redirect
from . models import Cart, CartItem
from products.models import Products

# Create your views here.

def cart_list(request):
    whos_cart = request.user
    cart_obj, created = Cart.objects.get_or_create(custommer = whos_cart)
    cart_items = cart_obj.cart_items.all()
    total_price = cart_obj.total_price()
    return render(request ,'cart.html', {'cart_items': cart_items, 'total_price':total_price})


def add_to_cart(request,pk):
    item_to_add = Products.objects.get(id = pk)
    user = request.user
    cart, created = Cart.objects.get_or_create(custommer = user)
    chek_exist =  CartItem.objects.filter(cart = cart, product = item_to_add).exists()
    if chek_exist:
       cart_item_obj = CartItem.objects.get(cart=cart, product=item_to_add)
       cart_item_obj.quantity += 1
       cart_item_obj.total_price = cart_item_obj.product.price * cart_item_obj.quantity
       cart_item_obj.save()
       return redirect('cart')
    else:
        cart_item = CartItem.objects.create(cart = cart, product = item_to_add)
        cart_item.total_price = cart_item.product.price
        cart_item.save()
        return redirect('cart')
    

def remove_from_cart(request, pk):
    item_for_removal = CartItem.objects.get(id = pk)
    item_for_removal.delete()
    return redirect('cart')   