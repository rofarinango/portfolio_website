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
    g = Github("90ba7886e92a721681180a2cefc8929df131af7f")
    for repo in g.get_user().get_repos():
        print(repo.description)
    return render(request, 'pages/projects.html')

def contact(request):
    """Tje contact page for personal website."""
    return render(request, 'pages/contact.html')