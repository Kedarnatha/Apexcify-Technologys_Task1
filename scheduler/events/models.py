from django.db import models
from django.utils.dateformat import DateFormat


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
