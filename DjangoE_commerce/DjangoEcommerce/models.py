from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image= models.ImageField(upload_to='products/product_images/', null=True, blank=True)
    image2= models.ImageField(upload_to='products/product_images2/', null=True, blank=True)
    image3= models.ImageField(upload_to='products/product_images3/', null=True, blank=True)


    describtion= models.TextField(null=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
  

    

# Create your models here.
