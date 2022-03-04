from multiprocessing import context
from pickle import FALSE, TRUE
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from datetime import datetime
from rater.forms import UserForm,UserProfileForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'rater/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        #profile_form = UserProfileForm(request.POST)

        if user_form.is_valid():# and profile_form.is_valid():
            user = user_form.save()
            print("user:",user.password)
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    
    return render(request, 'rater/login.html', context={'user_form': user_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rater:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rater/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rater:index'))

def contactus(request):
    return render(request, 'rater/contactus.html')