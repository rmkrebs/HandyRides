

from django.shortcuts import render, redirect
from .models import Person, Tenet, Event, Apartment

# relative import of forms
from .forms import RideForm, NewRideForm, TenetForm, NewTenetForm, ApartmentForm, NewApartmentForm, EventForm, NewEventForm

# Create your views here.

def index_event(request):
    context = {}

def create_event(request):
    context = {}
    context["new_event_form"] = NewEventForm()
    if request.method == "POST":
        new_event = NewEventForm(request.POST)
        new_event.save()
        return redirect("/addevent")
    return render(request,"addevent.html", context)

def index_tenet(request):
    context = {}

def create_tenet(request):
    context = {}
    context["new_tenet_form"] = NewTenetForm()
    if request.method == "POST":
        new_tenet = NewTenetForm(request.POST)
        new_tenet.save()
        return redirect("/addtenet")
    return render(request,"addtenet.html", context)


def index_apartment(request):
    context = {}

def create_apartment(request):
    context = {}
    context["new_apartment_form"] = NewApartmentForm()
    if request.method == "POST":
        new_apartment = NewApartmentForm(request.POST)
        new_apartment.save()
        return redirect("/addappartment")
    return render(request,"addappartment.html", context)



def index_ride(request):

  context = {}



  if "search_City" in request.GET:
    search_City = request.GET["search_City"]
    if "search_State" in request.GET:
        search_State = request.GET["search_State"]
        context["people"] = Person.objects.filter(destination_state__icontains=search_State) & (Person.objects.filter(origination_city__icontains=search_City) | Person.objects.filter(destination_city__icontains=search_City))
    else:
        context["people"] = Person.objects.filter(origination_city__icontains=search_City) | Person.objects.filter(destination_city__icontains=search_City)
  else:
    if "search_State" in request.GET:
        search_State = request.GET["search_State"]
        context["people"] = Person.objects.filter(destination_state__icontains=search_State)

  context["form"] = RideForm()

  context["new_ride_form"] = NewRideForm()

  return render(request, "index_view.html", context)

def create_ride(request):
    context ={}
    context["new_ride_form"] = NewRideForm()
    if request.method == "POST":
        new_ride = NewRideForm(request.POST)
        new_ride.save()
        return redirect("/addride")
    return render(request,"addride.html", context)
