from django.contrib import admin
from .models import Establishment

# Register your models here.

class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('name','schedule','image')
    search_fields =('name','schedule','direction','description')
    list_per_page = 10


admin.site.register(Establishment, EstablishmentAdmin)