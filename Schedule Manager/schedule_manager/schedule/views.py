from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User


# Create your views here.
def login_page(response):
    if response.method == "POST":
        form = UserCreationForm()

        if form.is_valid():
            form.save()

        return redirect("/home")

    else:
        form = UserCreationForm()

    return render(response, "sign-up.html", {"form":form})

# Create your views here.
def public_home_page(request):
    return render(request, "index.html")

def personal_home_page():
    return
