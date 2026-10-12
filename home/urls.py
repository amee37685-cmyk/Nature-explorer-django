from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path('mountains', views.mountains, name='mountains'),
    path('forests', views.forests, name='forests'),
    path('beaches', views.beaches, name='beaches'),
    path('sunsets', views.sunsets, name='sunsets'),
]