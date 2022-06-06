from django.test import TestCase, Client
from django.urls import reverse


class Test_views(TestCase):
    def test_report_news(self):
        client = Client()
        response = client.get(reverse('report_news'))
        self.assertTemplateUsed(response, 'users/reportnews.html')
        
        def test_about_us(self):
            client = Client()
        response = client.get(reverse('about_us'))
        self.assertTemplateUsed(response, 'users/aboutus.html')

    def test_contact_us(self):
        client = Client()
        response = client.get(reverse('contact_us'))
        self.assertTemplateUsed(response, 'users/contactus.html')