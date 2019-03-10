import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'index.html', context)


def about(request):
    context = {}
    return render(request, 'index.html', context)
        
def resume(request):
    context = {}
    return render(request, 'resume.html', context)
    
def interests(request):
    context ={}
    return render(request, 'interests.html', context)
    
def education(request):
    context = {}
    return render(request, 'education.html', context)
    
def github(request):
    response = requests.get('https://api.github.com/users/eduardojoya/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)
