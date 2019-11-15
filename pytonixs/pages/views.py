from django.shortcuts import render
from django.urls import reverse_lazy
from .models import NewClient
from django.views.generic import FormView
from .models import NewClient
from .forms import ContactForm


def home(request):
    template = 'welcome/index.html'
    context = {
        'title': 'welcome'
    }
    return render(request, template, context)


def about(request):
    template = 'about_us/about.html'
    context = {
        'title': 'who_we_are'
    }
    return render(request, template, context)


def service(request):
    template = 'what_we_do/service.html'
    context = {
        'title': 'What we do'
    }
    return render(request, template, context)


def project(request):
    template = 'completed_projects/projects.html'
    context = {
        'title': 'completed projects'
    }
    return render(request, template, context)


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact_us/contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super(ContactView, self).form_valid(form)