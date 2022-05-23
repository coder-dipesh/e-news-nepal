from django.test import SimpleTestCase
from django.urls import reverse, resolve
from admins.views import *


class TestUrls(SimpleTestCase):
    # Testing getEditor function via all-editor url
    def test_all_editors_urls_is_resolved(self):
        url = reverse('all-editors')
        view = resolve(url).func
        self.assertEquals(view, getEditor)

    

    # Testing getUsers function via all-users url
    def test_all_users_urls_is_resolved(self):

        url = reverse('all-users')
        view = resolve(url).func
        self.assertEquals(view, getUsers)

    # Testing getCategory function via all-categories url
    def test_all_category(self):
        url = reverse('all-category')
        view = resolve(url).func
        self.assertEquals(view, getCategory)

    # Testing newCategory function via new-category url testing
    def test_new_category(self):
        url = reverse('new-category')
        view = resolve(url).func
        self.assertEquals(view, newCategory)
