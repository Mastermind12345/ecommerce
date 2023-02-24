from django.contrib import admin

# Register your models here.
from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'category', 'price', 'created')


admin.site.register(Products, ProductsAdmin)