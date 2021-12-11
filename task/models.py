from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Project(models.Model):
    '''The Project dataclass which has individual tasks'''
    name = models.CharField(max_length= 50)
    slug = models.SlugField(default="")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("home-page") 
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Projects"

TASK_STATUS = (
    ("New", "New"),
    ("Started", "Started"),
    ("Ongoing", "Ongoing"),
    ("In QA", "In QA"),
    ("Completed", "Completed"),
)

class Task(models.Model):
    '''The Task dataclass to store the task in database'''
    title = models.CharField(max_length= 70)
    task_list = models.ForeignKey(Project, on_delete= models.CASCADE, null= True)
    description = models.TextField(max_length= 500, null= True)
    created_date = models.DateField(default= timezone.now, blank= True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null= True,
        blank= True,
        related_name="task_created_by",
        on_delete= models.CASCADE,
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null= True,
        blank= True,
        related_name="task_assigned_to",
        on_delete= models.CASCADE,
    )
    # assigned_by = models.ForeignKey(User, on_delete= models.CASCADE)
    status = models.CharField(max_length= 50, choices= TASK_STATUS, default= "New")
    # attachments = models.FileField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("task-detail", kwargs= {"pk": self.pk}) 