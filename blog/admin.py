from django.contrib import admin
from .models import Category, Post, Comment

# This code block is for custom filter label
def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'post_category', 'main', 'published', 'published_at']
    list_editable = ['main', 'published']
    search_fields = ['id', 'title', 'content']
    list_filter = [
        ('published', custom_titled_filter('Published')),
        ('post_category', custom_titled_filter('Categories')), 
        ('author__username', custom_titled_filter('Author')), 
        ('main', custom_titled_filter('Main')), 
    ]


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
