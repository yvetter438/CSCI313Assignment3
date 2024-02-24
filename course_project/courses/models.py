from django.db import models

# Create your models here.
class Course(models.Model):
    courseID = models.IntegerField(max_length=10,primary_key=True, unique=True, default = "")
    courseTitle = models.CharField(max_length=255, default = "")
    courseDescription = models.TextField()
    numOfCredits = models.PositiveIntegerField(default = "")
    instructor = models.CharField(max_length=255, default = "")
    startDate = models.DateField(default = "")
    