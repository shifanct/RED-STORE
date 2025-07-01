from django.contrib import admin
from . models import Products, Category, product_images

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(product_images)