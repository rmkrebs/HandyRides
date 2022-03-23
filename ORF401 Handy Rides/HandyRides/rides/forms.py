from django import forms
from .models import Person


class RideForm(forms.Form):
  search_City = forms.CharField(label='Search by City', max_length=64, required = False)
  search_State = forms.CharField(label='Search State', max_length=2, required = False)

class NewRideForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = []
