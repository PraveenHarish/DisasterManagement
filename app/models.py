from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=100)
    disaster = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name