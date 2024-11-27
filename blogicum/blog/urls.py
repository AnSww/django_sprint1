from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.posts, name='posts'),
    path('category/<slug:category_slug>/', views.category, name='category')
]
