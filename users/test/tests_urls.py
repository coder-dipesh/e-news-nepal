from django.test import SimpleTestCase
from users.views import *
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):
    def test_urls_about(self):
        url = reverse('about_us')
        view = resolve(url).func
        self.assertEquals(view, about_us)

        
    def test_urls_contact(self):
        url = reverse('contact_us')
        view = resolve(url).func
        self.assertEquals(view, contact_us)