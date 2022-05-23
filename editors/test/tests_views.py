from django.test import TestCase, Client
from django.urls import reverse


class Test_views(TestCase):
    def test_editorProfile(self):
        client = Client()
        response = client.get(reverse('profile'))
        self.assertTemplateUsed(response, 'editors/editorsProfile.html')
