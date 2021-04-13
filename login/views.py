from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import SuspectForm
import cv2
from django.utils import timezone
import datetime
from .staticrecognizer import static_rec
from .models import acase,detected_missing,Suspect
import os


# Create your views here.
def home(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('register')
        else:
            return render(request, 'login/home.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login/home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        #mobile = request.POST['mobile']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("Username taken")
                return render(request, 'login/register.html',{'error':'Username already exists'})
            elif User.objects.filter(email=email).exists():
                print("Email taken")
                return render(request, 'login/register.html',{'error':'Email has been taken'})
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("User creation successful")
        else:
            print("Passwords don't match")
            return render(request, 'login/register.html', {'error': 'Passwords must match'})
        return redirect("/")
    else:
        return render(request,'login/register.html')
    

def index(request):
    return render(request, 'index.html')


def plogin(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'],is_staff=True, is_superuser=True)

        if user is not None:
            if user.is_staff==True and user.is_superuser==True:
                auth.login(request, user)
                return redirect('/dashboard')
            else:
                return render(request, 'login/plogin.html', {'error': 'username or password is incorrect.'})
        else:
            return render(request, 'login/plogin.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login/plogin.html')

def clogin(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('suspect')
        else:
            return render(request, 'login/clogin.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login/clogin.html')

def cologin(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'],is_staff=True)

        if user is not None:
            if user.is_staff==True:
                auth.login(request, user)
                return redirect('/dashboard')
            else:
                return render(request, 'login/cologin.html', {'error': 'username or password is incorrect.'})
        else:
            return render(request, 'login/cologin.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login/cologin.html')


def suspect(request):
    if request.method == 'POST':
        form = SuspectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            print(img_obj)
            landmark = form.instance.landmark
            locality = form.instance.locality
            city = form.instance.city
            district = form.instance.district
            state = form.instance.state
            zipcode = form.instance.zipcode
            img = str(img_obj)
            string,nowithbrac = img.split("(")
            no1, no2 = nowithbrac.split(")")
            no3 = int(no1)
            pth = Suspect.objects.get(ids = no3)
            image_pth = pth.image
            image_pth1 = "'" + str(image_pth) +"'"
            print(image_pth1) 
            base_dir = os.path.dirname(os.path.abspath(__file__))
            base_dir = os.getcwd()
            img_pth2 = os.path.join(base_dir,"{}/{}".format('media',image_pth))

            name = static_rec(img_pth2)
            phnno, fname, lname = name.split('_')
            timestamp = datetime.datetime.now(timezone.utc)
            x = timestamp.strftime("%Y-%m-%d %H:%M:__%S")
            x1,x2 = x.split(':__')
            
            case_path = os.path.join(base_dir,"{}/{}/{}/{}_{}.jpg".format('media','images','detected_missing',name , x1))
            cpath = 'images/detected_missing/{}_{}.jpg'.format(name, x1)
            img_detected = cv2.imread(img_pth2)
            cv2.imwrite(case_path, img_detected)
            label1 = str(x1)
            #Add data to the database if does not exist earlier
            phnno, fname, lname = name.split('_')
            recognizedcase, created = detected_missing.objects.get_or_create(caseidentifier = phnno + '_' + fname + '_' + lname, image = cpath,landmark = landmark,locality = locality
                                   ,city = city, district = district, state = state , zipcode = zipcode, firstname = fname, lastname = lname, phoneno = phnno, time_detected = label1)
            print(landmark," ",locality," ",city," ",district," ",state," ",zipcode)
            recognizedcase.save()
            return render(request, 'suspect.html', {'form': form, 'img_obj': img_obj})
 
            
            
                       
            
            
    else:
        form = SuspectForm()
    return render(request, 'suspect.html', {'form': form})