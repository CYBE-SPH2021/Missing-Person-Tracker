from django.shortcuts import render
from .models import acase, detected_missing, track_vehicle
from vehicle.models import  detected_missing_vehicle
from .recognizer import Recognizer
from vehicle.license_plate_detector import main
from vehicle.plate_recognition import main1
from .forms import AddCaseForm, VehicleForm


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
    print(names)
    """ cases = acase.objects
    for case in cases:
        if (acase.phoneno + acase.firstname + acase.lastname) in names:
             """
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

def detectedmissing(request):
    detectedmCase = detected_missing.objects
    return render(request,'dashboard/detectedmissing.html',{'dmp':detectedmCase})

def information(request):
    return render(request,'dashboard/case/information.html')

def vehicle(request):
    vehicleCase = track_vehicle.objects
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            veh_obj = form.instance.vehicle_no
            return render(request, 'dashboard/vehicle.html', {'form': form, 'veh_obj': veh_obj, 'vc': vehicleCase})
    else:
        form = VehicleForm()
    return render(request, 'dashboard/vehicle.html', {'form': form, 'vc':vehicleCase})

def track_vehicles(request):
    main()
    num, img_path, x = main1()
    #path,timestamp = img_path('_')

    num = str(num)
    timestamp = str(x)

    print(num)
    print(img_path)
    recognizedcase = detected_missing_vehicle.objects.create(image = img_path,landmark = 'MGM Hospital',locality = 'CBD Belapur',city = 'Navi Mumbai', district = 'Thane', state = 'Maharashtra' , zipcode = '400614', vehicle_no = num, time_detected = timestamp)
    case_detection = track_vehicle.objects.all()

    print(case_detection.count())
    for rcase in case_detection.iterator():
        if rcase.vehicle_no == recognizedcase.vehicle_no:
            recognizedcase.save()
    return render(request, 'dashboard/dashboard.html')

def vehicle_case(request):
    activeCase = detected_missing_vehicle.objects
    return render(request,'dashboard/vehicle_case.html',{'ac':activeCase})

