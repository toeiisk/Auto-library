from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import auth_logout
from django.contrib.auth.models import User, Group
from datetime import date


# Create your views here.
def index(request):
    return render (request, 'index.html')

def auth_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            
            login(request, user)
            next_url = request.POST.get('next_url')
            if next_url:

                return redirect(next_url)

            else:    

                return redirect('index')
        else:
            error = "Username or Password Incorrect!!"
            context['username'] = username
            context['password'] = password
            context['error'] = "Username or Password Incorrect!!"
            return render(request, 'login.html', context)
        pass
    else:
        return render(request, 'login.html', context)

def register(request):
    context = {}
    if request.method == 'POST':
        try:

            user = User.objects.create_user(

            first_name=request.POST.get('firstname'),

            last_name=request.POST.get('lastname'),

            username=request.POST.get('username'),

            password=request.POST.get('password'),

            email=request.POST.get('email')

            )

            group = Group.objects.get(name='User')

            user.groups.add(group)

            user.save()

            return redirect('login')

        except Exception as e:

            context['error'] = str(e)
    
    return render(request, 'register.html')

def my_logout(request):
    logout(request)
    return redirect('index')

# d0 = date(2008, 8, 18)
#     d1 = date(2008, 9, 26)
#     amount = d1 - d0
#     if amount.days > 7:
#         amount = amount * 10
#         print(amount.days)
#     else:
#         print(amount.days)
