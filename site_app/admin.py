from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
