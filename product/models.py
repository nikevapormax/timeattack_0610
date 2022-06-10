from tkinter import CASCADE
from unicodedata import category
from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = 'category'
            
    category = models.CharField(max_length=30)


class Product(models.Model):
    class Meta:
        db_table = 'product'
        
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField()
    price = models.IntegerField()
    lot = models.IntegerField()
    

class OrderStatus(models.Model):
    class Meta:
        db_table = 'order-status'
        
    complete = models.CharField(max_length=10)
    payed = models.CharField(max_length=10)
    cancel = models.CharField(max_length=10)
    shipping = models.CharField(max_length=10)
    done = models.CharField(max_length=10)
    
class ProductOrder(models.Model):
    class Meta:
        db_table = 'product-order'
        
    complete_cnt = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    
    
class UserOrder(models.Model):
    class Meta:
        db_table = 'user-order'
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    address = models.CharField(max_length=100)
    order_at = models.DateTimeField(auto_now_add=True)
    total_price = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    available = models.BooleanField()
    