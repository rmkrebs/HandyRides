from django import forms
from .models import Person, Tenet, Apartment, Event


class RideForm(forms.Form):
  search_City = forms.CharField(label='Search by City', max_length=64, required = False)
  search_State = forms.CharField(label='Search State', max_length=2, required = False)

class NewRideForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = []


class TenetForm(forms.Form):
    search_City = forms.CharField(label='City', max_length=64, required = False)
    search_age_21_up = forms.BooleanField(label='Over 21', required = False)
    search_Job_Industry = forms.CharField(label='Job Industry', max_length=64, required = False)
    search_University = forms.CharField(label='School', max_length=64, required = False)
    search_hobbies = forms.CharField(label='Hobbies', max_length=64, required = False)

class NewTenetForm(forms.ModelForm):
    class Meta:
        model = Tenet
        exclude = []

class ApartmentForm(forms.Form):
    search_City = forms.CharField(label='City', max_length=64, required = False)
    search_AC = forms.BooleanField(label='AC', required = False)
    search_Bedrooms = forms.IntegerField(label='# of Bedrooms', required = False)
    search_Bathrooms = forms.IntegerField(label='# of Bathrooms', required = False)
    search_amenitites = forms.CharField(label='Amenitites', max_length=64, required = False)

class NewApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        exclude = []

class EventForm(forms.Form):
    search_City = forms.CharField(label='City', max_length=64, required = False)
    search_Date = forms.DateField(label='Date',required = False)
    search_age_21_up = forms.BooleanField(label='Over 21', required = False)
    

class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = []
