from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from products.models import Products

# Create your views here.

def register(request):
    form_type = 'register'
    register_error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username = username).exists():

            # Add this error message on templtes
            register_error_message = 'Username Already Exists'
            print(register_error_message)
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            auth_login(request,user)
            return redirect('home_page')
                  
    return render(request, 'account.html', {'register_error_message':register_error_message, 'form_type': form_type})

def login(request):
    form_type = 'login'
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
    return render(request, 'account.html',{'error_message':error_message,'form_type': form_type})

@login_required(login_url='/login')
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='/login')
def home_page(request):
    Latest_products = Products.objects.order_by('-updated_at')[:8]
    return render(request, 'home.html',{'latest_products':Latest_products})

def reset_password(request):
    error_message = None
    if request.method == 'POST':
        username =  request.POST.get('username')
        email =  request.POST.get('email')
        try:
           user_obj = User.objects.get(username = username, email = email)
           user_id = user_obj.id
           return redirect('confirm_password',user_id)
        except:
            error_message = 'username or email is not valid.'
              
    return render(request, 'reset_password.html', {'error_message':error_message})

def confirm_password(request, user_id):
    error_message = None
    user = User.objects.get(pk = user_id)
    print(user.username)
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user.set_password(confirm_password)
            user.save()
            return redirect('login')
        else:
            error_message = 'passwords do not match'
    return render(request, 'confirm_password.html', {'error_message':error_message})