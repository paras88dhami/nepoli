from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
def __str__(self):
    return self.name


class Product(models.Model):
  
    name = models.CharField(max_length=255)
    description = models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
   

    def __str__(self):
        return self.name
    
    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity}) - {self.user if self.user else 'Anonymous'}"

    @property
    def total_price(self):
        return self.quantity * self.product.price


