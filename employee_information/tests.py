from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from employee_information.views import login_user, logoutuser


class TestUrls(SimpleTestCase):
    
    def test_login_url_resolves(self):
        url =reverse("login-user")
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_user)
        
    def test_logout_url_resolved(self):
        url =reverse("logout")
        print(resolve(url))
        self.assertEquals(resolve(url).func, logoutuser)
        
    # def test_logout_url_resolved(self):
    #     url =reverse("logout", args=["some slage"]) for parametraized views
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func, logoutuser)