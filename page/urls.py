from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact-us/', views.ContactView.as_view(), name='contact'),
    path('faqs/', views.FaqView.as_view(), name='faqs'),
    path('paivacy-pollicy/', views.PrivacypollicyView.as_view(), name='privacy'),
    path('terms-of-use/', views.TermsofuseView.as_view(), name='terms'),
    path('gallery/', views.images_list, name='gallery'),
    path('images/<category_slug>/', views.images_list, name='images-list-by-category'),
    path('videos/', views.videos_list, name='videos-list'),
    path('videos/<category_slug>/', views.videos_list, name='videos-list-by-category'),
]
