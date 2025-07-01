from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name



class Products(models.Model):
    category = models.ForeignKey(Category, related_name = 'category_products', on_delete=models.CASCADE)
    product = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.SmallIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product
    
class product_images(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_images')
    extra_images = models.ImageField(upload_to='extra_product_images/')

    def __str__(self):
        return f"{self.product.product}' image"



# Add an additional model reviews for allow users to add their own experiance with this product.