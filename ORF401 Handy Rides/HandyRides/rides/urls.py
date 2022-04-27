from django.urls import path

from . import views

app_name = 'rides'
urlpatterns = [
    path('', views.index_rides, name='index_rides'),
    path('create', views.create_rides, name='create_rides')

]
