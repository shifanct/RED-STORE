from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username = username).exists():

            # Add this error message on templtes
            error_message = 'Username Already Exists'
            print(error_message)
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            return redirect('home_page')
                  
    return render(request, 'account.html', {'error_message':error_message})

def login(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            auth_login(request, user)
            return redirect('home_page')
        else:
            error_message = 'Invalid Username or Password'
            print(error_message)
    return render(request, 'account.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='/login')
def home_page(request):
    return HttpResponse('Welcome Your Autherizated Now.')