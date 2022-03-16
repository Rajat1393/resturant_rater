from django.urls import path
from rater import views

#  app_name
app_name = 'rater'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('contactus/', views.contactus, name='contactus'),
    path('rating/', views.rating, name='rating'),
    path('search/', views.search, name='search'),
    path('overview/', views.overview, name='overview'),
    path('redirectRating/',views.redirectRating,name='redirectRating'),
    path('add_review/',views.add_review,name='add_review'),
    path('getuserprofile/',views.getuserprofile,name='getuserprofile'),
    path('updateuserprofile/',views.updateuserprofile,name='updateuserprofile'),

]

