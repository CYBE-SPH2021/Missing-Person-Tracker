from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

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
    
