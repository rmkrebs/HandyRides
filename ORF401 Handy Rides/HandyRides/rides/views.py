

from django.shortcuts import render, redirect
from .models import Person, Tenet, Event, Apartment

# relative import of forms
from .forms import RideForm, NewRideForm, TenetForm, NewTenetForm, ApartmentForm, NewApartmentForm, EventForm, NewEventForm

# Create your views here.

def index_event(request):
    context = {}
   
    if "search_City" in request.GET:
        search_Date = request.GET["search_Date"]
        search_City = request.GET["search_City"]
        search_age_21_up = False
        if "search_age_21_up" in request.GET:
            search_age_21_up = True
       
        context["events"] = Event.objects.filter(city__icontains=search_City) & Event.objects.filter(date__icontains=search_Date) & Event.objects.filter(age_21_up=search_age_21_up) 
    
    context["event_form"] = EventForm()
    
    return render(request, "events.html", context)

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
   
    if "search_City" in request.GET:
        search_University = request.GET["search_University"]
        search_City = request.GET["search_City"]
        search_Job_Industry = request.GET["search_Job_Industry"]
        search_hobbies = request.GET["search_hobbies"]

        context["people"] = Tenet.objects.filter(university__icontains=search_University) & Tenet.objects.filter(city__icontains=search_City) & Tenet.objects.filter(job_industry__icontains=search_Job_Industry) & Tenet.objects.filter(hobbies__icontains=search_hobbies)
    
    context["tenet_form"] = TenetForm()
    
    return render(request, "tenets.html", context)



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
    if "search_City" in request.GET:
        search_City = request.GET["search_City"]
        search_AC = False
        if "search_AC" in request.GET:
            search_AC = True
        search_Bedrooms =  request.GET["search_Bedrooms"]
        search_Bathrooms =  request.GET["search_Bathrooms"]
        search_amenities =  request.GET["search_amenities"]
       
        context["apartments"] = Apartment.objects.filter(city__icontains=search_City) & Apartment.objects.filter(ac=search_AC) & Apartment.objects.filter(bedrooms__icontains=search_Bedrooms) & Apartment.objects.filter(bathrooms__icontains=search_Bathrooms) & Apartment.objects.filter(amenities__icontains=search_amenities)

    context["apartment_form"] = ApartmentForm()
    
    return render(request, "apartments.html", context)

def create_apartment(request):
    context = {}
    context["new_apartment_form"] = NewApartmentForm()
    if request.method == "POST":
        new_apartment = NewApartmentForm(request.POST)
        new_apartment.save()
        return redirect("/addapartment")
    return render(request,"addapartment.html", context)



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
