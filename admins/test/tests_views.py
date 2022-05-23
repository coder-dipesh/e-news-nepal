from django.test import TestCase, Client
from django.urls import reverse


class Test_views(TestCase):
    def test_allEditors(self):
        client = Client()
        response = client.get(reverse('all-editors'))
        self.assertTemplateUsed(response, 'admins/adminEditor/editorPage.html')

    def test_allUsers(self):
        client = Client()
        response = client.get(reverse('all-users'))
        self.assertTemplateUsed(response, 'admins/allUsers.html')

    def test_allCategory(self):
        client = Client()
        response = client.get(reverse('all-category'))
        self.assertTemplateUsed(response, 'admins/Category/categoryPage.html')

    def test_newCategory(self):
        client = Client()
        response = client.get(reverse('new-category'))
        self.assertTemplateUsed(response, 'admins/Category/newCategory.html')
