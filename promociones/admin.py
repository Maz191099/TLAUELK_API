from django.contrib import admin
from .models import Promotions
# Register your models here.

class PromotionsAdmin(admin.ModelAdmin):
    list_display = ('description','image')
    list_per_page = 10
    
admin.site.register(Promotions, PromotionsAdmin)