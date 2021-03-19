from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        print(username,password,user)
        if user is not None:
            auth.login(request, user)
            print("Login successful")
            return redirect("/")
        else:
            print("User invalid")
            return redirect("/")
    else:
        return render(request,'login/home.html')

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
            elif User.objects.filter(email=email).exists():
                print("Email taken")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("User creation successful")
        else:
            print("Passwords don't match")
        return redirect("/")
    else:
        return render(request,'login/register.html')
    
