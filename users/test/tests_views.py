from django.test import TestCase, Client
from django.urls import reverse


class Test_views(TestCase):
    def test_report_news(self):
        client = Client()
        response = client.get(reverse('report_news'))
        self.assertTemplateUsed(response, 'users/reportnews.html')
        