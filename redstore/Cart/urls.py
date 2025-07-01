from django.urls import path
from . import views


urlpatterns = [
    path('cart/',views.cart_list, name = 'cart'),
    path('add_to_cart/<pk>', views.add_to_cart, name = 'add_to_cart'),
    path('remove_from_cart/<pk>',views.remove_from_cart, name = 'remove_from_cart')
]