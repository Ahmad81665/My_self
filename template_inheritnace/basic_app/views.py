from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'basic_app/index.html')


def about(request):
    return render(request, 'basic_app/about.html')

def projects(request):
    return render(request, 'basic_app/projects.html')    


def skills(request):
    return render(request, 'basic_app/skills.html')


def contact(request):
    return render(request, 'basic_app/contact.html')


def relative(request):
    return render(request, 'basic_app/relative_url_templates.html') 