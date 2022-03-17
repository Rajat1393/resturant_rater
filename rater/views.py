from multiprocessing import context
from pickle import FALSE, TRUE
import profile
from unicodedata import name
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from datetime import datetime
from rater.forms import  UserForm,UserProfileForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
import requests
from rater.models import Restaurant, Review ,UserProfile
from datetime import datetime
from django.contrib.auth.models import User
from django.views import View

def index(request):
    return render(request, 'rater/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            print("user:",user.password)
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user     
            profile.website = user.email 
            profile.picture ="profile_images/profile.jpg"    
            profile.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    
    return render(request, 'rater/register.html', context={'user_form': user_form, 'registered': registered})

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

def rating(request):
    return render(request, 'rater/rating.html')

def add_review(request):
    googleplaceid = request.POST['googleplaceid'].strip()
    try:
        restaurant = Restaurant.objects.get(googleplaceid = googleplaceid) 
    except Restaurant.DoesNotExist:
        restaurant = None
    user = request.user

    price = int(request.POST['price'].strip())
    quality = int(request.POST['quality'].strip())
    atmosphere = int(request.POST['atmosphere'].strip())
    review = request.POST['review'].strip()
    ratings = int((price + quality + atmosphere)/3)
    new_review = Review(time = datetime.now(),comments =review,ratings = ratings,restaurant = restaurant,user = user)
    new_review.save()
    contextdict = {}
    contextdict['name'] = restaurant.name
    contextdict['phone'] = restaurant.phoneno
    contextdict['address'] = restaurant.location
    contextdict['googleplaceid'] = restaurant.googleplaceid

    review_list = Review.objects.all().filter(restaurant = restaurant)
    print(review_list)
    if(len(review_list))>0:
        rating = 0
        for review in review_list:
            rating = review.ratings + rating
        rating = int(rating/len(review_list))
        contextdict['rating'] = rating
    else:
        contextdict['rating'] = 5
    contextdict['reviewlist'] = review_list
    return render(request, 'rater/overview.html', context=contextdict)


def search(request):
    query = request.POST['query'].strip()
    getplaceid = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" +query.strip() + "&inputtype=textquery&locationbias=circle:3000@55.8642° N, 4.2518° W &key=AIzaSyAEGrpbyqVAyF1OS_G74NJtdazbOwiHLf0")
    place = getplaceid.json()
    eatery =place['candidates'][0]['place_id']
    response = requests.get('https://maps.googleapis.com/maps/api/place/details/json?place_id='+ eatery+'&fields=formatted_address,name,formatted_phone_number,opening_hours/weekday_text,types&key=AIzaSyAEGrpbyqVAyF1OS_G74NJtdazbOwiHLf0')
    geodata = response.json()
    contextdict = {}
    address = geodata['result']['formatted_address']
    phone = geodata['result']['formatted_phone_number']
    name = geodata['result']['name']
    contextdict['name'] = name
    contextdict['phone'] = phone
    contextdict['address'] = address
    contextdict['googleplaceid'] = eatery.strip()
    dbrestuarant = Restaurant.objects.filter(googleplaceid = eatery.strip()).exists()
    if(not dbrestuarant):
        restaurant = Restaurant(location = address,name = name,description = 'food, drinks',phoneno = phone,googleplaceid = eatery.strip())
        restaurant.save()
        contextdict['reviewlist'] = []
        contextdict['rating'] = 0
    else:
        restaurant = Restaurant.objects.get(googleplaceid = eatery.strip())
        print(restaurant)
        review_list = Review.objects.all().filter(restaurant = restaurant)        
        contextdict['reviewlist'] = review_list
        if(len(review_list))>0:
             rating = 0
             for review in review_list:
                 rating = review.ratings + rating
             rating = int(rating/len(review_list))
             contextdict['rating'] = rating
        else:
             contextdict['rating'] = 5     
    
    return render(request, 'rater/overview.html', context=contextdict)


def overview(request):
    return render(request, 'rater/overview.html')

def redirectRating(request):
    return render(request,'rater/rating.html')

def getuserprofile(request):
    user= request.user
    profile = UserProfile.objects.get(user = user)
    try:
        reviews= Review.objects.all().filter(user = user)
    except Review.DoesNotExist:
        reviews = None
    contextdict = {}
    print(profile)
    contextdict['profile'] = profile
    contextdict['reviews'] = reviews
    return render(request,'rater/profile.html',context=contextdict)


# def updateuserprofile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST(),request.FILEDS)
#         if form.is_valid():
#             img = form.cleaned_data.get("image_field")
#             print('-------')
#             print(img)


def updateuserprofile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        print(user_profile)
    except UserProfile.DoesNotExist:
        return HttpResponse("invalid user_profile!")

    if request.method == "POST":
        update_profile_form = UserProfileForm(data=request.POST, instance=user_profile)
        if update_profile_form.is_valid():
            profile = update_profile_form.save(commit=False)
            print(profile)
            print('here')
            if 'picture' in request.FILES:
                print('in if')
                profile.picture = request.FILES['picture']
            profile.save()
    
    user= request.user
    profile = UserProfile.objects.get(user = user)
    try:
        reviews= Review.objects.all().filter(user = user)
    except Review.DoesNotExist:
        reviews = None
    contextdict = {}
    print(profile)
    contextdict['profile'] = profile
    contextdict['reviews'] = reviews
    return render(request,'rater/profile.html',context=contextdict)
   
