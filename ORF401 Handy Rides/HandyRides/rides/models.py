from django.db import models

# Create your models here.


class Person(models.Model):
  first_name = models.CharField(max_length=64,default="Unknown")
  last_name = models.CharField(max_length=64,default="Unknown")
  email = models.CharField(max_length=64,default="Unknown")
  origination_city = models.CharField(max_length=64,default="Unknown")
  origination_state = models.CharField(max_length=2,default="UK")
  destination_city = models.CharField(max_length=64,default="Unknown")
  destination_state = models.CharField(max_length=2,default="Unknown")
  date = models.DateField()
  time = models.TimeField()
  taking_passengers = models.BooleanField(default=False)
  seats_available = models.IntegerField(default=0)
  car_make = models.CharField(max_length=64,default="Unknown")
  car_electric = models.BooleanField(default=False)
  car_range = models.CharField(max_length=64,default="Unknown")
  premium = models.BooleanField(default=False)
  blood_type = models.CharField(max_length=3,default="Ukn")
  dnr_order = models.BooleanField(default=False)
  social = models.CharField(max_length=64,default="Unknown")
  smoker = models.BooleanField(default=False)
  convicted_felon = models.BooleanField(default=False)
  blind = models.BooleanField(default=False)
  prefered_music = models.CharField(max_length=64,default="Unknown")
  pets = models.CharField(max_length=64,default="Unknown")
  kids = models.CharField(max_length=64,default="Unknown")
  
