from django.contrib import admin

# Register your models here.
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'code','created_at')
    exclude = ('created_at', 'updated_at', 'code', 'slug')
    ordering = ['-created_at']
    search_fields = ['title', 'code', ]
    pass


class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
