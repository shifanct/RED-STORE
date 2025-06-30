from django.shortcuts import render,redirect
from . models import Cart, CartItem
from products.models import Products

# Create your views here.

def cart_list(request):
    whos_cart = request.user
    cart_obj = Cart.objects.get(custommer = whos_cart)
    cart_items = cart_obj.cart_items.all()
    print(cart_items)
    
    return render(request ,'cart.html', {'cart_items': cart_items})


def add_to_cart(request,pk):
    item_to_add = Products.objects.get(id = pk)
    user = request.user
    cart, created = Cart.objects.get_or_create(custommer = user)
    cartitem_obj =  CartItem.objects.filter(cart = cart, product = item_to_add).exists()
    if cartitem_obj:
        cartitem_obj.quantity +=1
        return redirect('cart')
    else:
        cart_item = CartItem.objects.create(cart = cart, product = item_to_add)
        cart_item.save()
        return redirect('cart')