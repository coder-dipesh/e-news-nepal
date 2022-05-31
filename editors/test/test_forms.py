from django.test import SimpleTestCase
from editors.forms import *


class TestForms(SimpleTestCase):
    def test_news_form(self):
        form = NewsForm(data={
            'title': 'Sports',
            'category': 'Football',
            'content': "All about the sports and football",
            'image': 'image.jpg',
        })
        self.assertTrue(form.is_valid())

    def test_news_form(self):
        form = NewsForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)