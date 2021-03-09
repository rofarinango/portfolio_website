from django.views.generic import View
from django.shortcuts import render
from github import Github

class Project:
    "A project class from our repository on Github."
    title = ""
    description = ""
    language = ""
    date_created = ""
    size = 0
    stars = 0
    def __init__(self, title, description, language, date_created, size, stars):
        self.title = title
        self.description = description
        self.language = language
        self.date_created = date_created
        self.size = size
        self. stars = stars

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
<<<<<<< HEAD
    g = Github("90ba7886e92a721681180a2cefc8929df131af7f")
||||||| 13368a8
    g = Github("CHANGE_token")
=======
    g = Github("CHANGE_token")
    projects = []
>>>>>>> 3c09507a27865bd3ec983eccf0b663373a8f9cc4
    for repo in g.get_user().get_repos():
        project = Project(repo.name, repo.description, repo.language, repo.created_at, repo.size, repo.stargazers_count)
        projects.append(project)
    context = {'projects': projects}
    return render(request, 'pages/projects.html', context)

def contact(request):
    """Tje contact page for personal website."""
    return render(request, 'pages/contact.html')