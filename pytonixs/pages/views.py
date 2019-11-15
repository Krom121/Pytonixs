from django.shortcuts import render
from django.urls import reverse_lazy
from .models import NewClient
from django.views.generic import FormView , View, ListView
from .models import NewClient
from .forms import ContactForm
from blog.models import Post


def home(request):
    template = 'welcome/index.html'
    contact_form = ContactForm()
    if request.method == 'POST':
        if form.is_valid():
            contact_form.save()
    context = {
        'title': 'welcome',
        'contact_form': contact_form
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

def list(request):
        return render(request, "blog/post/list.html", {'title': 'Our blogs'})