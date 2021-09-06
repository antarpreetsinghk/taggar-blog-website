from django.contrib import sitemaps
from django.urls import reverse
from .models import Post, Category

class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            'home',
            'about',
            'gallery',
            'videos-list',
            'terms',
            'privacy',
            'contact',
            'search',
            'register',
            'login',
        ]

    def location(self, items):
        return reverse(items)


class PostViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return Post.objects.filter(published=True)


class CategoryViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return Category.objects.all()
