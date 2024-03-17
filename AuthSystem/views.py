from django.http import HttpResponseServerError
# Create your views here.
from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import socket
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
def home(request):
    return render(request, "index.html")



# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         # Check if passwords match
#         if password1 != password2:
#             messages.error(request, 'Passwords do not match')
#             return redirect('signup')

#         # Check if username or email already exists
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username is already taken')
#             return redirect('signup')
#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email is already taken')
#             return redirect('signup')

#         # Create the user
#         user = User.objects.create_user(username=username, email=email, password=password1,
#                                          first_name=first_name, last_name=last_name)
#         user.save()

#         messages.success(request, 'Account created successfully. You can now log in.')
#         return redirect('login')

#     return render(request, 'signup.html')






def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if passwords match
        if password1 != password2:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
        
        # Validate password
        try:
            validate_password(password1)
        except ValidationError as e:
            return render(request, 'signup.html', {'error': ', '.join(e.messages)})

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username is already taken'})
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email is already taken'})

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1,
                                         first_name=first_name, last_name=last_name)
        user.save()

        return redirect('login')

    return render(request, 'signup.html')






# def loginUser(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request,"Login Successfully!!")
#             return redirect("home")
#         else:
#             messages.warning(request,"User or password is not correct!")

#     return render(request, "login.html")

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {'error': 'User or password is not correct!'})

    return render(request, "login.html")







def logOutUser(request):
    logout(request)
    return redirect("home")