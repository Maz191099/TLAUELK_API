from django.contrib import admin
from .models import Commentary
# Register your models here.61

class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('content', 'score')
    search_fields =('name','content','score')
    list_per_page = 10

admin.site.register(Commentary, CommentaryAdmin)