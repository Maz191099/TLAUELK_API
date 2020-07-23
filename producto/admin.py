from django.contrib import admin
# Registro del modelo Product en la rama sandy.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'precio')
    search_fields = ('name', 'description')
    list_per_page = 10

admin.site.register(Product, ProductAdmin)
