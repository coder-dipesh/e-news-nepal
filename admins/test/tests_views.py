from django.test import TestCase, Client
from django.urls import reverse


class Test_views(TestCase):
    def test_myNews(self):
        client = Client()
        response = client.get(reverse('all-news'))
        self.assertTemplateNotUsed(response, 'admins/Allnews/Allnews.html')
