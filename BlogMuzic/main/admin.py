from django.contrib import admin
from .models import Post
from .models import Photo

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['created']