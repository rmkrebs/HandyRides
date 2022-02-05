from django.shortcuts import render

from .models import Person

# relative import of forms
from .forms import RideForm

# Create your views here.


def index(request):

  context = {}

  

  if "search_City" in request.GET:
    search_City = request.GET["search_City"]
    if "search_State" in request.GET:
        search_State = request.GET["search_State"]
        context["people"] = Person.objects.filter(destination_state__icontains=search_State) & (Person.objects.filter(
        origination__icontains=search_City) | Person.objects.filter(destination_city__icontains=search_City))
    else:
        context["people"] = Person.objects.filter(
        origination__icontains=search_City) | Person.objects.filter(destination_city__icontains=search_City)
  else:
    if "search_State" in request.GET:
        search_State = request.GET["search_State"]
        context["people"] = Person.objects.filter(destination_state__icontains=search_State) 

  context["form"] = RideForm()

  return render(request, "index_view.html", context)
