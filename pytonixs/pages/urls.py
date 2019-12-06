from django.urls import path
from pages import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about_us/', views.about, name='about'),
    path('what_we_do/', views.service, name='service'),
    path('completed_projects/', views.project, name='project'),
    path('contact_us/', views.ContactView.as_view(), name='contact'),
    path('blog/', views.list, name='list'),
]