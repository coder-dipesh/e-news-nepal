from django.test import TestCase, Client
from django.urls import reverse


class Test_views(TestCase):
    def test_alleditor(self):
        client = Client()
        response = client.get(reverse('all-editors'))
        self.assertTemplateUsed(response, 'admins/adminEditor/editorPage.html')
