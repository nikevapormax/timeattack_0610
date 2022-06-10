from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'user'
        
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    
    