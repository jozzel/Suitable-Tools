from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from . import forms


# Create your views here.

def index(request):
    title = "Home Page"
    context = {
        "title" : title
    }
    return render(request, "index.html", context=context)

def register_view(request):
        if request.method == "POST":
            form = forms.RegistrationForm(request.POST)
            if form.is_valid():
                form.save(request)
                return redirect("/login/")
        else:
             form = forms.RegistrationForm()
        
        context = {
            "title": "Registration Page",
            "form": form
        }
        return render(request,"registration/register.html", context=context)

def logout_view(request):
    logout(request)
    return redirect("/login/")

def sale_view(request):
    title = " Discounted Prices for Used Tools - starting at $2 each item"
    context = {
        "title" : title
    }
    print("inside the sale_view function")
    return render(request,"sale.html", context=context)

def new_view(request):
    title = " New Tools - starting at $5 each item"
    context = {
        "title" : title
    }
    return render(request,"new.html", context=context)

def home_view(request):
    title = "Suitable Tools"
    context = {
        "title" : title
    }
    return render(request,"home.html", context=context)