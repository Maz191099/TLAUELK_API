from django.contrib import admin
from .models import Establishment

# Register your models here.

class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('name','schedule','image')
    search_fields =('name','schedule','direction')

admin.site.register(Establishment, EstablishmentAdmin)