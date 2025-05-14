from django.db import models

# Create your models here.
class Student(models.Model):
    regNo  = models.CharField(unique=True, max_length=10)
    name   = models.CharField(max_length=30)
    feeBal = models.IntegerField(default=0)

    def __str__(self):
        return self.name

 
