from django.contrib import admin
from .models import Establishment

#Importar recursos de libreria
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#Hacer referencia al modelo de exportacion
class EstablishmentResource(resources.ModelResource):
    class Meta:
        model = Establishment


# Register your models here.

class EstablishmentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name','schedule','image')
    search_fields =('name','schedule','direction','description')
    list_per_page = 10
    
    resources_class = EstablishmentResource

admin.site.register(Establishment, EstablishmentAdmin)