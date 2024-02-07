from django.urls import path
#function view
from . import views

urlpatterns = [
    #funtion view path('', views.home, name='blog-home'), or class view path('', ListView.as_view, name='blog-home')
    path('about/', views.about, name='blog-about'),
]
