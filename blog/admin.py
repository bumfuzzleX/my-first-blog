from django.contrib import admin
from .models import Post

class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content','image','created_date','published_date')

# Register your models here.

admin.site.register(Post, BlogAdmin)