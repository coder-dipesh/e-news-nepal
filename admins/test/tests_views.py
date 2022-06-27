from django.test import TestCase, Client
from django.urls import reverse


class Test_views(TestCase):
    def test_downloadEditorData(self):
        client = Client()
        response = client.get(reverse('download_editor'))
        response.status_code = 200

    def test_downloadUserData(self):
        client = Client()
        response = client.get(reverse('download_user'))
        response.status_code = 200

    def test_downloadAllnewsData(self):
        client = Client()
        response = client.get(reverse('download_allnews'))
        response.status_code = 200

    def test_newsletter(self):
        client = Client()
        response = client.get(reverse('Newsletters'))
        self.assertTemplateUsed(response, 'admins/Subscribe/Newsletter.html')
