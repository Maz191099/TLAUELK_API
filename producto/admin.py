from django.contrib import admin
# Registro del modelo Product en la rama sandy.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Product, ProductAdmin)
