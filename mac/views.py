# views.py
from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.db import models
from shop.models import product
from shop.models import contact
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,"about.html")

def goals(request):
    return render(request,"goals.html")

def contact(request):
    return render(request,"contact.html")

