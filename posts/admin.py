from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'profile', 'created_at', 'published']
    list_filter = ['published', 'created_at']
    search_fields = ['title', 'content']
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(published=True)
    make_published.short_description = "Mark selected posts as published"

admin.site.register(Post, PostAdmin)