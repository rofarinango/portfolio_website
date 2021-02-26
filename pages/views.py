from django.views.generic import View
from django.shortcuts import render

def home(request):
    """The home page for personal website."""
    return render(request, 'pages/base.html')

def about(request):
    """The about page for personal website."""
    return render(request, 'pages/about.html')