from django.shortcuts import render
from .models import Projects, Skills, DesiredProject, About
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'portfolio/templates/home.html')

def project_list(request):
    projects = Projects.objects.all()
    return render(request, 'portfolio/templates/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = Projects.objects.get(id=pk)
    return render(request, 'portfolio/templates/project_detail.html', {'project': project})

def skill_list(request):
    skills = Skills.objects.all()
    return render(request, 'portfolio/templates/skills.html', {'skills': skills})

def desired_project_list(request):
    desired_projects = DesiredProject.objects.all()
    return render(request, 'portfolio/templates/desired_projects.html', {'desired_projects': desired_projects})

def about(request):
    about_info = About.objects.first()
    return render(request, 'portfolio/templates/about.html', {'about': about_info})

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
            return render(request, 'portfolio/templates/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'portfolio/templates/contact.html', {'form': form})