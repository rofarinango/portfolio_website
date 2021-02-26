"""Defines URL patterns for pages."""
from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    #Home page
    path('', views.home, name='home'),
    #Page that show about section.
    path('about/', views.about, name='about'),
]