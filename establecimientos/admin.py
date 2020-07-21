from django.contrib import admin
from .models import Establishment

# Register your models here.

class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('id','name','schedule')

admin.site.register(Establishment, EstablishmentAdmin)