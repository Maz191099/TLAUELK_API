from django.contrib import admin
# Registro del modelo Product en la rama sandy.
from .models import Product
#Importar recursos de libreria
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#Hacer referencia al modelo de exportacion
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

#Añadir herencia 
class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
#class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'precio')
    search_fields = ('name', 'description')
    list_per_page = 10

    resources_class = ProductResource

admin.site.register(Product, ProductAdmin)
