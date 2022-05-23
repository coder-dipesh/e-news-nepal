from django.test import SimpleTestCase
from django.urls import reverse, resolve
from editors.views import *


class TestUrls(SimpleTestCase):
    # Testing editorProfile function via profile url
    def test_editors_profile_urls_is_resolved(self):
        url = reverse('profile')
        view = resolve(url).func
        self.assertEquals(view, editorProfile)
