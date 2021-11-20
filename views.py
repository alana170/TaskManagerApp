from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from . import views 
from django.contrib.auth.models import User
import datetime 
from decimal import Decimal
import json
import os

# login
def index(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "modern_login.html", {"message": "Invalid credentials."})
    
    return render(request, 'modern_login.html')

def logout_view(request):
    logout(request)
    return render(request, "modern_login.html", {"message": "Logged out."})

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        if User.objects.filter(username = username).first():
            return render(request, 'signup.html', {"message":"Username already taken."})
        password = request.POST["password"]
        name = request.POST["name"]
        email = request.POST["email"]
        user = User.objects.create_user(username, email, password)
        user.first_name = name
        user.save()
        return render(request, 'login.html',{"message": "You have successfully created an account. Thank you for registering. "})  
    return render(request, 'signup.html')

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'modern_login.html')
    return render(request, 'home.html')