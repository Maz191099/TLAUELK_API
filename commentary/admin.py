from django.contrib import admin
from .models import Commentary
# Register your models here.61

class CommentaryAdmin(admin.ModelAdmin):
    com_display = ('id','content', 'score')
    

admin.site.register(Commentary, CommentaryAdmin)
