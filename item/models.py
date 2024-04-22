from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"  # atribut special pentru indiicatia cum trebuie sa 
        # fie denumita tabela in panela adminului
        
    def __str__(self):
        return self.name
    
    
class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='item_images')
    created_by = models.ForeignKey(User,related_name = "items",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Items"  
    
    def __str__(self):
        return self.name