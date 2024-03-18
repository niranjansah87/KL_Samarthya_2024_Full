"""
URL configuration for KLSamarthya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings
from KLSamarthyaApp.views import index
# from AuthSystem.views import home
from AuthSystem.views import loginUser, logOutUser, register,Profile
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('KLSamarthyaApp.urls')),
    path('',index,name="home"),
    path("signup/",register, name="signup"),
    path("login/",loginUser , name="login"),
    path("logout/",logOutUser , name="logout"),
    path('user/<int:pk>/profile/',Profile,name="profile"),
]

# Serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)