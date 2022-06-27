from django.test import SimpleTestCase
from admins.views import *
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    def test_urls_downloadEditorData(self):
        url = reverse('download_editor')
        view = resolve(url).func
        self.assertEquals(view, downloadEditorData)

    def test_urls_downloadUserData(self):
        url = reverse('download_user')
        view = resolve(url).func
        self.assertEquals(view, downloadUserData)

    def test_urls_downloadAllNews(self):
        url = reverse('download_allnews')
        view = resolve(url).func
        self.assertEquals(view, downloadAllNewsData)

    def test_urls_newsletter(self):
        url = reverse('Newsletters')
        view = resolve(url).func
        self.assertEquals(view, emailNewsletter)
