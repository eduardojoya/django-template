import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    index_html = open('content/index.html').read()
    context = {
        'content': index_html,
    }
    return render(request, 'base.html', context)


def about(request):
    index_html = open('content/index.html').read()
    context = {
        'content': index_html,
    }
    return render(request, 'base.html', context)
        
def resume(request):
    resume_html = open('content/resume.html').read()
    context = {
        'content': resume_html,
    }
    return render(request, 'base.html', context)
    
def interests(request):
    interests_html = open('content/interests.html').read()
    context ={
        'content': interests_html,
    }
    return render(request, 'base.html', context)
    
def education(request):
    education_html = open('content/education.html').read()
    context = {
        'content': education_html,
    }
    return render(request, 'base.html', context)
    
def blog(request):
    blog_html = open('content/blog.html').read()
    context = {
        'content': blog_html,
    }
    return render(request, 'base.html', context)
