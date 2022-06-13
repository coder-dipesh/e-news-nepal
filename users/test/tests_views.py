from django.test import TestCase, Client
from django.urls import reverse

class Test_views(TestCase):
    def test_about(self):
        client = Client()
        response = client.get(reverse('about_us'))
        self.assertTemplateUsed(response, 'users/aboutus.html')

    def test_contact(self):
        client = Client()
        response = client.get(reverse('contact_us'))
        self.assertTemplateUsed(response, 'users/contactus.html')