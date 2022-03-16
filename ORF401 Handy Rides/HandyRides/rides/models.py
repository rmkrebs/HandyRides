from django.db import models

# Create your models here.


class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64)
  email = models.CharField(max_length=64)
  origination_city = models.CharField(max_length=64)
  origination_state = models.CharField(max_length=2)
  destination_city = models.CharField(max_length=64)
  destination_state = models.CharField(max_length=2)
  date = models.DateField()
  time = models.TimeField()
  taking_passengers = models.BooleanField(default=False)
  seats_available = models.IntegerField(default=0)
  car_make = models.CharField(max_length=64)
  car_electric = models.BooleanField(default=False)
  car_range = models.CharField(max_length=64)
  premium = models.BooleanField(default=False)
  blood_type = models.CharField(max_length=3)
  dnr_order = models.BooleanField(default=False)
  social = models.CharField(max_length=64)
  smoker = models.BooleanField(default=False)
  convicted_felon = models.BooleanField(default=False)
  blind = models.BooleanField(default=False)
  prefered_music = models.CharField(max_length=64)
  pets = models.CharField(max_length=64)
  kids = models.CharField(max_length=64)
  
