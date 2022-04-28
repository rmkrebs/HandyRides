"""HandyRides URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rides import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('rides/', include('rides.urls')),
    path('addride/', TemplateView.as_view(template_name="addride.html")),
    path('events/', views.index_event,name="index_event"),
    path('addevent/', views.create_event,name="create_event"),
    path('tenets/', views.index_tenet,name="index_tenet"),
    path('addtenet/', views.create_tenet,name="create_tenet"),
    path('apartments/', views.index_apartment,name="index_apartment"),
    path('addapartment/', views.create_apartment,name="create_apartment")
]
