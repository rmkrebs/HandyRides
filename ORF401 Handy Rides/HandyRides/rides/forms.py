from django import forms


class RideForm(forms.Form):
  search_City = forms.CharField(label='Search by City', max_length=64, required = False)
  search_State = forms.CharField(label='Search State', max_length=2, required = False)

#onclick="return checkForm();"
