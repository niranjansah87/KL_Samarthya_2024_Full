from KLSamarthyaApp.views import *
from django.urls import path

urlpatterns = [
    # path("home/",home, name="home"),
    path("",index, name="home"),
    path("team/",team, name="team"),
    path("gallery/",gallery , name="gallery"),
    path("events/",events , name="events"),
    path("about/",about , name="about"),
    
    
    
]
