from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    
    Image = models.FileField()
    FirstName= models.CharField(max_length=120)
    LastName = models.CharField(max_length=120)
    Roll = models.IntegerField()
    Registration = models.IntegerField()
    Father_name = models.CharField(max_length=120)
    Mother_name = models.CharField(max_length=120)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True, null=True)
    village = models.CharField(max_length= 100)
    Email =  models.EmailField(max_length=70,blank=True, null= True, unique= True)
    address = models.TextField()

    def __str__(self):
        return str(self.Roll)
class Category(models.Model):
    SHIFT_CHOICES = (
        ('1st', 'FirstShift'),
        ('2nd', 'SecondShift')
    )
    category = models.CharField(max_length=3, choices=SHIFT_CHOICES)
    Date = models.DateField(blank=True, null=True)
    In_Time = models.TimeField(default=timezone.now)
    Out_Time = models.TimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.category)
