from django.test import TestCase,Client
from django.urls import reverse


class Test_views(TestCase):
    def test_homepage(self):
        client=Client()
        response=client.get(reverse('home'))
        self.assertTemplateUsed(response,'accounts/home.html')