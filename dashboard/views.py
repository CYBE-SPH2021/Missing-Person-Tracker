from django.shortcuts import render
from .models import acase
from .recognizer import Recognizer
from .forms import AddCaseForm


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
    if request.method == 'POST':
        form = AddCaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'dashboard/addcase.html', {'form': form, 'img_obj': img_obj})
    else:
        form = AddCaseForm()
    return render(request, 'dashboard/addcase.html', {'form': form})

