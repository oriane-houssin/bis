from django.contrib import admin

from .models import Author, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', )
    
