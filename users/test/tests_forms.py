from django.test import SimpleTestCase
from users.forms import *


class TestForms(SimpleTestCase):
    def test_comment_form(self):
        form = CommentForm(data={
            'content': "Nice article content...",
        })
        self.assertTrue(form.is_valid())

    def test_comment_form(self):
        form = CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_profile_form(self):
        form = ProfileForm(data={
            'firstname': 'John',
            'latname': 'Latn',
            'bio': 'John',
            'phone': '123-456-65656',
            'address': '123 Main Street',
            'profile_pic': 'profile.png',
        })
        self.assertTrue(form.is_valid())

    def test_profile_form(self):
        form = ProfileForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)
