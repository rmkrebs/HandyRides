from django.urls import path

from . import views

app_name = 'rides'
urlpatterns = [
    path('', views.index_ride, name='index_ride'),
    path('create', views.create_ride, name='create_ride')

]
