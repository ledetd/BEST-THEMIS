from django.db import models
from django.contrib.auth.models import User


    
class Project(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    project_manager = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    
    def __str__(self):
        return self.name