from django.test import SimpleTestCase
from django.urls import reverse,resolve
from accounts.views import *

class TestUrls(SimpleTestCase):
    def test_signin_urls_is_resolved(self):
      url=reverse('sign-in')
      view=resolve(url).func
      self.assertEquals(view,signIn)