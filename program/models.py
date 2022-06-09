from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Program(models.Model):
    # relations
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # fields
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.name


class Lecture(models.Model):
    # relations
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    # fields
    name = models.CharField(max_length=50)
    text = models.TextField()
    video = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
