from django.urls import path
from pages.views import AboutView, HomeView, ProjectView, ServiceView, ContactView

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('about_us/', AboutView.as_view(), name='about'),
    path('what_we_do/', ServiceView.as_view(), name='service'),
    path('completed_projects/', ProjectView.as_view(), name='project'),
    path('contact_us/', ContactView.as_view(), name='contact'),

]