from django.shortcuts import render

# Create your views here.
def case(request):
    return render(request,'dashboard/case.html')

def maps(request):
    return render(request,'dashboard/map.html')
