from django.views.generic import View
from django.shortcuts import render
from github import Github

from projects.models import Project

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
    """The projects page for personal website."""
    g = Github("CHANGE_token")
    for repo in g.get_user().get_repos():
        print(repo.description)
    return render(request, 'pages/projects.html')

def contact(request):
    """Tje contact page for personal website."""
    return render(request, 'pages/contact.html')