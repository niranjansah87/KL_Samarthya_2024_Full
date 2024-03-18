from django.urls import path
from .views import loginUser, logOutUser,home, register,Profile

urlpatterns = [
    path('',home,name="home"),
]
