from django.db import models

# Temporary model
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    organizer = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title
