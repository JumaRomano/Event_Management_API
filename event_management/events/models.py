from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_date = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Event(models.Model):
    ...
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
