from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)

class Flight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    AIRPORT_OPTIONS = (
    ('JFK','John F. Kennedy International Airport(JFK)'),
    ('EWR','Newark Liberty International Airport (EWR)'),
    ('LGA','LaGuardia Airport (LGA)'),
    ('OTH','Other')
    )
    airport = models.CharField(max_length=3, choices=AIRPORT_OPTIONS, default='JFK')    
    

    DEST_CHOICES = (
        ('A', 'Arrival'),
        ('F', 'Departure')
    )
    dest = models.CharField(max_length=1, choices=DEST_CHOICES)
    
    flight = models.CharField(max_length=20)
    flight_num = models.CharField(max_length=20)
    seat = models.CharField(max_length=20)
    num_of_bags = models.IntegerField()
    
    arrival_date = models.DateField()
    est_arrival = models.TimeField()

    num_of_bags = models.IntegerField()

    is_cab = models.BooleanField(default=False)

class Cab(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    cab = models.CharField(max_length=20)
    cab_num = models.CharField(max_length=20)
    seats = models.CharField(max_length=20)
    
    meeting_area = models.CharField(max_length=20)
    meeting_time = models.TimeField()

    pickup = models.CharField(max_length=20)
    drop = models.CharField(max_length=20)

    travel_plan = models.CharField(max_length=20, default=None)


class Bus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
     
    NY_PA_OPTIONS = (
        ('OBS','Direct to Binghamton/ OurBus'),
        ('AST','Airport Shuttle'),
        ('TRN','Air Train'),
        ('CAB','Cab or Uber or Lyft'),
        ('OTH','Other')
    )
    nypa_travel = models.CharField(max_length=3, choices=NY_PA_OPTIONS, default='CAB')

    bus_company = models.CharField(max_length=20)
    bus_timing = models.DateTimeField()
    
    meeting_point = models.CharField(max_length=20)
    start_time = models.TimeField()

    travel_plan = models.CharField(max_length=20, default=None)