from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('skills/', views.skill_list, name='skill_list'),
    path('desired-projetcs/', views.desired_project_list, name='desired_project_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]