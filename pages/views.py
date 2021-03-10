from django.views.generic import View
from django.shortcuts import render
from github import Github
from .projects import Project
import pandas as pd


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
    g = Github("changeToken")
    pj = {'Title': [],
          'Description': [],
          'Language': [],
          'Createdat': [],
          'Size': [],
          'Stars': []
          }
    
    allProjects=[]
    for repo in g.get_user().get_repos():
        project = Project(repo.name, repo.description, repo.language, repo.created_at, repo.size, repo.stargazers_count)
        pj['Title'].append(project.title)
        pj['Description'].append(project.description)
        pj['Language'].append(project.language)
        pj['Createdat'].append(project.date_created)
        pj['Size'].append(project.size)
        pj['Stars'].append(project.stars)
    df = pd.DataFrame(pj, columns= ['Title', 'Description', 'Language', 'Createdat', 'Size', 'Stars'])
    print(df)
    for i in range(df.shape[0]):
        temp = df.loc[i]
        allProjects.append(dict(temp))
    context = {'allProjects': allProjects}
    return render(request, 'pages/projects.html', context)

def contact(request):
    """Tje contact page for personal website."""
    return render(request, 'pages/contact.html')