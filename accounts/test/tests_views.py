from django.test import TestCase, Client
from django.urls import reverse

class Test_views(TestCase):
    def test_share(self):
        client = Client()
        response = client.get(reverse('viewnews'))
        self.assertTemplateUsed(response, 'accounts/viewnews.html')

