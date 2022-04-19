

from django.shortcuts import render, redirect
from .models import Profile

# relative import of forms
from .forms import ProfileForm

from .forms import ProfileForm, NewProfileForm

# Create your views here.



def index(request):

  context = {}



  if "search_City" in request.GET:
    search_City = request.GET["search_City"]
    if "search_State" in request.GET:
        search_State = request.GET["search_State"]
        context["people"] = Profile.objects.filter(destination_state__icontains=search_State) & (Profile.objects.filter(origination_city__icontains=search_City) | Person.objects.filter(destination_city__icontains=search_City))
    else:
        context["people"] = Profile.objects.filter(origination_city__icontains=search_City) | Profile.objects.filter(destination_city__icontains=search_City)
  else:
    if "search_State" in request.GET:
        search_State = request.GET["search_State"]
        context["people"] = Profile.objects.filter(destination_state__icontains=search_State)

  context["form"] = ProfileForm()

  context["new_profile_form"] = NewProfileForm()

  return render(request, "index_view.html", context)

def create(request):
    context ={}
    context["new_profile_form"] = NewProfileForm()
    if request.method == "POST":
        new_profile = NewProfileForm(request.POST)
        new_profile.save()
        return redirect("/addprofile")
    return render(request,"addprofile.html", context)
