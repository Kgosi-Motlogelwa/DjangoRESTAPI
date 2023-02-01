from django.db import models

# Create your models here.
class StudentModel(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  description = models.TextField()
  date_enrolled = models.DateTimeField(auto_now=True)

  # Returns a human readable string version of the object
  def __str__(self):
    return self.name


# print(Student)