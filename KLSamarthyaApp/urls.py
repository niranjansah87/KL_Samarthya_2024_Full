from KLSamarthyaApp.views import *
from django.urls import path

urlpatterns = [
    path("team/",team, name="team"),
    path("gallery/",gallery , name="gallery"),
    path("events/",events , name="events"),
    path("about/",about , name="about"),
    
    
    
]
