from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def projects_view(request, *args, **kwargs):
    return render(request, 'projects.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})