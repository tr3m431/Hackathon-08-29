from django.shortcuts import render

# Create your views here.
def public_home_page(request):
    return render(request, "index.html")

def login_page(request):
    return render(request, "sign-up.html")

def personal_home_page():
    return
