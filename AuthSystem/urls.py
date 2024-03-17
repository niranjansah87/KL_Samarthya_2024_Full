from django.urls import path
from .views import loginUser, logOutUser, register,home

urlpatterns = [
    path("signup/",register, name="signup"),
    path("login/",loginUser , name="login"),
    path("logout/",logOutUser , name="logout"),
    path("",home, name="home"),
]
