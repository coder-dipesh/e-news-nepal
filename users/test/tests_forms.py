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

