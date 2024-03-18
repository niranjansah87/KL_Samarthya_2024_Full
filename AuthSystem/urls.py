from django.urls import path
from .views import loginUser, logOutUser, register,Profile

urlpatterns = [
    path("signup/",register, name="signup"),
    path("login/",loginUser , name="login"),
    path("logout/",logOutUser , name="logout"),
    # path("",home, name="home"),
    path('user/<int:pk>/profile/',Profile,name="profile"),
    
]
