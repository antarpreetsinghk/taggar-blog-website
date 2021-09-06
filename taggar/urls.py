from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import StaticViewsSitemap, PostViewsSitemap, CategoryViewsSitemap
from django.views.generic import TemplateView


admin.site.site_header = 'Taggar Associates'

sitemaps = {
    'sitemap': StaticViewsSitemap,
    'post': PostViewsSitemap,
    'category': CategoryViewsSitemap
}

urlpatterns = [
    path('', include('blog.urls')),
    path('pages/', include('page.urls')),
    path('admin/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(template_name='page/robots.txt', content_type='text/plain')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
