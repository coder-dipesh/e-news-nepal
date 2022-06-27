from django.test import TestCase, Client
from django.urls import reverse


class Test_views(TestCase):
    def test_search(self):
        client = Client()
        response = client.get(reverse('search'))
        self.assertTemplateUsed(
            response, 'accounts/home.html')
