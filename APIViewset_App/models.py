from django.db import models


# Create your models here.
class Student(models.Model):
    stud_id = models.CharField(max_length=10)
    stud_name = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
