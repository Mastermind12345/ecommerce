from django.db import models

# Create your models here.


class Products(models.Model):
    CP = 'Consumer products'
    IP = 'Industrial products'
    SP = 'Service products'
    CATEGORIES = (
        (CP, 'Consumer products'),
        (IP, 'Industrial products'),
        (SP, 'Service products'),
    )
    name = models.CharField(max_length=60)  # Name of Product
    price = models.IntegerField(default=0)  # Price of Product
    category = models.CharField(max_length=60, choices=CATEGORIES, default=CP)  # category of Product
    description = models.CharField(max_length=500, default='', blank=True, null=True)  # Description of Product
    image = models.ImageField(upload_to='uploads/products/', max_length=500, blank=True, null=True)  # Image of Product
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name