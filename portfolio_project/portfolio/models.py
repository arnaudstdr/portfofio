from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.TextField(max_length=200)
    project_link = models.URLField(max_length=200)
    demo_link = models.URLField(max_length=200, blank=True, null=False)
    image = models.ImageField(upload_to='project_images/', blank=True, null=False)

    def __str__(self):
        return self.title
    
class Skills(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, blank=True, null=True)   # ex : "Débutant", "Intermédiaire", "Exepert"

    def __str__(self):
        return self.name
    
class DesiredProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    required_skills = models.ManyToManyField(Skills)

    def __str__(self):
        return self.title
    
class About(models.Model):
    content = models.TextField()
