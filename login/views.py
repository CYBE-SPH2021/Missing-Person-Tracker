from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import SuspectForm


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
            username=request.POST['username'], password=request.POST['password'],is_staff=True)

        if user is not None:
            if user.is_staff==True:
                auth.login(request, user)
                return redirect('/')
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

def suspect(request):
    if request.method == 'POST':
        form = SuspectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'suspect.html', {'form': form, 'img_obj': img_obj})
    else:
        form = SuspectForm()
    return render(request, 'suspect.html', {'form': form})