from django import forms
from .models import Profile
Male_Female = (
	('male','MALE'),
	('female','FEMALE')
)

class ProfileForm(forms.Form):
  sex = forms.CharField(max_length=6, label='Sex', required = False, widget = forms.Select(choices=Male_Female))
  age = forms.IntegerField(label='Age', required = False)
  school = forms.CharField(max_length=64, label='School', required = False)
  interning_at = forms.CharField(max_length=64, label='Interning at', required = False)
  hobbies = forms.CharField(max_length=64, label='Hobbies', required = False)

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []
