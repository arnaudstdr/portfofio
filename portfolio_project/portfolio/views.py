from django.shortcuts import render, get_object_or_404
from .models import Project, Skills, DesiredProject, About
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html')

def project_list(request):
    projects = Project.objects.all()
    for project in projects:
        project.technology_list = project.technologies.split(' - ')
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def skill_list(request):
    skills = Skills.objects.all()
    return render(request, 'skills.html', {'skills': skills})

def desired_project_list(request):
    desired_projects = DesiredProject.objects.all()
    return render(request, 'desired_projects.html', {'desired_projects': desired_projects})

def about(request):
    about_info = About.objects.first()
    return render(request, 'about.html', {'about': about_info})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Message de {name}',
                message,
                email,
                ['arnaud.stadler@ikmail.com'],
            )
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')