from django.test import SimpleTestCase
from django.urls import reverse, resolve
from admins.views import *


class TestUrls(SimpleTestCase):
    def test_all_editors_urls_is_resolved(self):
        url = reverse('all-editors')
        view = resolve(url).func
        self.assertEquals(view, getEditor)
