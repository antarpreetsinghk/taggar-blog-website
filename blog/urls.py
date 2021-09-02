from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('categories/post/<int:id>/', views.post_details, name='post-details'),
    path('categories/<category_slug>/', views.categories, name='categories'),
]
