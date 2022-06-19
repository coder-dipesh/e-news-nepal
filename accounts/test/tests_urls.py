from django.test import SimpleTestCase
from accounts.views import *
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    def test_urls_socialLogin(self):
        url = reverse('social-login')
        view = resolve(url).func
        self.assertEquals(view, socialLogin)
