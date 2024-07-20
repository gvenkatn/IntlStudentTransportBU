from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)

class Flight(model.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Flight = models.CharField(max_length=20)
    Flight_Number = models.CharField(max_length=20)
    Seat = models.CharField(max_length=20)
    Airport = models.CharField(max_length=20)
    Date = models.DateField()
    EstArrivalTime = models.TimeField()
    Number_of_Bags = models.IntegerField()
