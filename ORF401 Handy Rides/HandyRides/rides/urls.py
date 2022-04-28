from django.urls import path

from . import views

app_name = 'rides'
urlpatterns = [
    path('', views.index_ride, name='index_ride'),
    path('create', views.create_ride, name='create_ride'),
    path('create_tenet', views.create_tenet, name='create_tenet'),
    path('index_tenet', views.index_tenet, name='index_tenet'),
    path('index_event', views.index_event, name='index_event'),
    path('create_event', views.create_event, name='create_event'),
    path('index_apartment', views.index_apartment, name='index_apartment'),
    path('create_apartment', views.create_apartment,name='create_apartment')
]
