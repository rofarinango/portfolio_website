from django.views.generic import View
from django.shortcuts import render

def home(request):
    """The home page for personal website."""
    return render(request, 'pages/home.html')
def services(request):
    """The services page for personal website."""
    return render(request, 'pages/services.html')

def skills(request):
    """The skills page for personal website."""
    return render(request, 'pages/skills.html')

def projects(request):
    """The teams page for personal website."""
    return render(request, 'pages/projects.html')

def contact(request):
    """Tje contact page for personal website."""
    return render(request, 'pages/contact.html')