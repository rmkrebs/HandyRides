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
  


class Tenet(models.Model):
	name = models.CharField(max_length=64)
	city = models.CharField(max_length=64)
	age_21_up = models.BooleanField(default=False)
	job_industry = models.CharField(max_length=64)
	university = models.CharField(max_length=64)
	bio = models.CharField(max_length=250)
	hobbies = models.CharField(max_length=64)
	

class Apartment(models.Model):
	address = models.CharField(max_length=128)
	city = models.CharField(max_length=64)
	rent = models.IntegerField(default=0)
	ac = models.BooleanField(default=False)
	bedrooms = models.IntegerField(default=0)
	bathrooms = models.IntegerField(default=0)
	amenities = models.CharField(max_length=250)

class Event(models.Model):
	name = models.CharField(max_length=64, default="N/a")
	address = models.CharField(max_length=128)
	city = models.CharField(max_length=64)
	date = models.DateField()
	time = models.TimeField()
	age_21_up = models.BooleanField(default=False)
	byob = models.BooleanField(default=False)
	entry_fee = models.IntegerField(default=0)
	description = models.CharField(max_length=250) 