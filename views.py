import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'index.html', context)


def about(request):
#    index_html = open('content/index.html').read()
    context = {}
    return render(request, 'index.html', context)
        
def resume(request):
#    resume_html = open('content/resume.html').read()
    context = {}
    return render(request, 'resume.html', context)
    
def interests(request):
#    interests_html = open('content/interests.html').read()
    context ={}
    return render(request, 'interests.html', context)
    
def education(request):
#    education_html = open('content/education.html').read()
    context = {}
    return render(request, 'education.html', context)
    
def github(request):
    response = requests.get('https://api.github.com/users/eduardojoya/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)
