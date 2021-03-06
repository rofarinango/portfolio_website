"""Defines URL patterns for pages."""
from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    #Home page
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    # Page that show services section.
    path('services/', views.services, name='services'),
    #Page that show skills section.
    path('skills/', views.skills, name='skills'),
    #Page that show teams section.
    path('projects/', views.projects, name='projects'),
    #Page that show contact section.
    path('contact/', views.contact, name='contact')
]