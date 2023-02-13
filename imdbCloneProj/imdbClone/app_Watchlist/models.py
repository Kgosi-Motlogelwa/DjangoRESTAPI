from django.db import models

# Create your models here.
class MovieModel(models.Model):
    name = models.CharField(max_length=50)
    desription = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    