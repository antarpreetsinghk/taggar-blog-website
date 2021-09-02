from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('categories/post/<int:id>/', views.post_details, name='post-details'),
    path('categories/<category_slug>/', views.categories, name='categories'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
