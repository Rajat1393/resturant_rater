from django.test import TestCase
from django.urls import reverse

class BaseTest(TestCase):
    def setUp(self):
        self.login_url = reverse('rater:login')
        self.register_url = reverse('rater:register')
        return super().setUp()

class LoginTest(BaseTest):
    def test_view_login_page_correctly(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'rater/login.html')

class RegisterTest(BaseTest):
    def test_view_register_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'rater/register.html')

class HomePageTest(BaseTest):
    def test_view_home_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'rater/register.html')
