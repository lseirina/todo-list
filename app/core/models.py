"""
Models for app.
"""
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """Model for tasks."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.title