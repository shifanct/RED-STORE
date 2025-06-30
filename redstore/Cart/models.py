from django.db import models
from django.contrib.auth.models import User
from products.models import Products  

class Cart(models.Model):
    custommer = models.OneToOneField(User, related_name='user_cart', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.custommer.username}'s cart"
    
    def total_price(self):
        return sum(item.subtotal() for item in self.cart_items.all())




class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='cart')
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cart.custommer.username}'s {self.product.product}"

    def subtotal(self):
        return self.product.price * self.quantity
