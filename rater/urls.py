from django.urls import path
from rater import views

#  app_name
app_name = 'rater'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('contactus/', views.contactus, name='contactus')
]

