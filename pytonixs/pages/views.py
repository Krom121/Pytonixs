from django.shortcuts import render
from django.urls import reverse_lazy
from .models import NewClient
from django.views.generic import FormView ,ListView, TemplateView
from .models import NewClient
from .forms import ContactForm
from blog.models import Post


class HomeView(TemplateView):
    template_name = 'welcome/index.html'



class AboutView(TemplateView):
    template_name = 'about_us/about.html'


class ServiceView(TemplateView):
    template_name = 'what_we_do/service.html'


class ProjectView(TemplateView):
    template_name = 'completed_projects/projects.html'


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact_us/contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super(ContactView, self).form_valid(form)
