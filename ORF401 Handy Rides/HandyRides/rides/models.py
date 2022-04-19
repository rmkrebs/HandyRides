from django.db import models

# Create your models here.

Male_Female = (
	('male','MALE'),
	('female','FEMALE')
)
class Profile(models.Model):
  first_name = models.CharField(max_length=64)
  sex = models.CharField(max_length=6, choices=Male_Female)
  age = models.IntegerField()
  school = models.CharField(max_length=64)
  interning_at = models.CharField(max_length=64)
  hobbies = models.CharField(max_length=64)
  bio_blurb = models.CharField(max_length=150)


class Events(models.Model):
	event_name = models.CharField(max_length=64)
	event_type = models.CharField(max_length=64)
	drinks = models.BinaryField()
	entry_fee = models.IntegerField()


class Housing(models.Model);
	address = models.CharField(max_length=150)
	num_bedrooms = models.IntegerField()
	num_bathrooms = models.IntegerField()
	pets = models.BinaryField()
	furnished = models.BinaryField()
	rent = models.IntegerField()
	