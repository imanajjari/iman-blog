from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_view, name='inndex'),
    path('<str:post_id>', views.blog_single, name='single'),
    path('category/<str:cat_name>', views.blog_category, name='blog_category'),
    path('author/<str:author_username>', views.blog_view, name='blog_author'),
    path('tag/<str:tag_name>', views.blog_view, name='blog_tag'),
    path('search/', views.blog_search, name='blog_search'),
]