from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index_view, name='home'),
    # path('about/', views.index_view, name='about'),
    # path('contact/', views.contect_view, name='contact'),
]