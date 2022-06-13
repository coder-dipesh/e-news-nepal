from django.test import SimpleTestCase
from admins.views import *
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    def test_urls_allcontact(self):
        url = reverse('all-contacts')
        view = resolve(url).func
        self.assertEquals(view, allContact)