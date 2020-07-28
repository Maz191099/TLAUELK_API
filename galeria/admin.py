from django.contrib import admin
from .models import Gallery

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id','image')
    search_fields =('id',)
    list_per_page = 10


admin.site.register(Gallery, GalleryAdmin)