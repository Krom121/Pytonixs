from django.shortcuts import render
from .models import NewClient


def home(request):
    template = 'welcome/index.html'
    context = {
        'title': 'welcome'
    }
    return render(request, template, context)



def about(request):
    return render(request, "about_us/about.html", {'title': 'Who we are'})



def service(request):
    return render(request, "what_we_do/service.html",{'title': 'What we do'})


def project(request):
    return render(request, "completed_projects/projects.html",{'title': 'Completed works'})



def contact(request):
    return render(request, "contact_us/contact.html", {'title': 'Contact us'})


