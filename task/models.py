from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    '''The Task dataclass to store the task in database'''
    title = models.CharField(max_length= 50)
    description = models.TextField(max_length= 500)
    assigned = models.ForeignKey(User, on_delete= models.CASCADE)
    # attachments = models.FileField()

    def __str__(self):
        return self.title