import email
from urllib import response
from django.test import TestCase
from django.urls import reverse
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
from django.test import RequestFactory
from .views import getuserprofile

class BaseTest(TestCase):
    def setUp(self):
        self.login_url = reverse('rater:login')
        self.register_url = reverse('rater:register')
        self.home_url = reverse('rater:index')
        self.overview_url = reverse('rater:overview')
        self.profile_url = reverse('rater:getuserprofile')
        self.search_url = reverse('rater:search')
        self.factory = RequestFactory()
        self.user = {
            "email": "test@gmail.com",
            "username" : "test",
            "password" : "password",
            "password2" : "password"
        }

        self.query = {"query" : "Mister Singh's India"}
        return super().setUp()

class LoginTest(BaseTest):
    def test_view_login_page_correctly(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'rater/login.html')
    
    def test_user_can_login(self):
        response = self.client.post(self.login_url,self.user,format = 'text/html')
        self.assertEqual(response.status_code,200)
    
class RegisterTest(BaseTest):
    def test_view_register_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'rater/register.html')
    
    def test_user_can_register(self):
        response = self.client.post(self.register_url,self.user,format = 'text/html')
        self.assertEqual(response.status_code,200)

class HomePageTest(BaseTest):
    def test_view_home_page_correctly(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'rater/index.html')

class OverviewPageTest(BaseTest):
    def test_view_overview_page_correctly(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'rater/index.html')
    
    def test_search_functionality(self):
        response = self.client.post(self.search_url,self.query,format = 'text/html')
        self.assertEqual(response.status_code,200)
