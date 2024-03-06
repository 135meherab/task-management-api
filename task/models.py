import os
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PRIORITY = [
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),

]


    
class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(choices = PRIORITY, max_length=10)
    is_complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='task/media/uploads/')
    task = models.ForeignKey(Task, on_delete = models.CASCADE, null = True , blank = True)
    def __str__(self):
        return os.path.basename(self.image.name)