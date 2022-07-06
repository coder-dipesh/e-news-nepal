from django.test import TestCase, Client
from django.urls import reverse


class Test_views(TestCase):
    def test_downloadEditorData(self):
        client = Client()
        response = client.get(reverse('download_editor'))
        response.status_code = 200

    def test_downloadAllNewsData(self):
        client = Client()
        response = client.get(reverse('download_editor'))
        response.status_code = 200
