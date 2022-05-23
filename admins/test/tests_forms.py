from django.test import SimpleTestCase
from admins.forms import *

class TestForms(SimpleTestCase):
    def test_category_form(self):
        form = CategoryForm(data={
            'title': 'Sports',
            'categoryName': 'Football',
            'description': "All about the sports and football",
        })
        self.assertTrue(form.is_valid())

    def test_category_form(self):
        form = CategoryForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)