from django.shortcuts import render
from .models import acase
from .recognizer import Recognizer


# Create your views here.

def case(request):
    activeCase = acase.objects
    return render(request,'dashboard/case.html',{'ac':activeCase})

def maps(request):
    return render(request,'dashboard/map.html')

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def realrec(request):
    names=Recognizer()
    return render(request,'dashboard/webcamon.html')

def addcase(request):
    return render(request,'dashboard/addcase.html')

