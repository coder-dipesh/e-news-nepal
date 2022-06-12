from django.test import SimpleTestCase
from accounts.views import *
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    def test_urls_enterusername(self):
        url = reverse('reset-password-enter-username')
        view = resolve(url).func
        self.assertEquals(view, enterUsername)

