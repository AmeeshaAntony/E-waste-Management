from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.title
        return self.price

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #price = models.DecimalField(max_digits=10, decimal_places=2)
