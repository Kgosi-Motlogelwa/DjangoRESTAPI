from django.db import models

# Create your models here.
class NotesModel(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)   # On every edit to database, time taken (auto_now)
    created = models.DateTimeField(auto_now_add=True)   # On first creation (auto_now_add)
    
    def __str__(self):
        return self.body[0:50] # First 50 characters of body list
