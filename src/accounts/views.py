from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=first_name, 
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password1)
                user.save()
                print("user created...", flush=True)
                return redirect('login')

        else:
            messages.info(request, "Password doesn't match")
            return redirect('register')

    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')