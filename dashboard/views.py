from django.shortcuts import render
from .models import acase


# Create your views here.

def case(request):
    activeCase = acase.objects
    return render(request,'dashboard/case.html',{'ac':activeCase})

def maps(request):
    return render(request,'dashboard/map.html')

def dashboard(request):
    return render(request,'dashboard/dashboard.html')
