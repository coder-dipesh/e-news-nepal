from django.test import SimpleTestCase
from accounts.views import *
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    def test_urls_search(self):
        url = reverse('search')
        view = resolve(url).func
        self.assertEquals(view, search)
