from django.test import SimpleTestCase
from editors.views import *
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase) :
     def test_my_news_urls_is_resolved(self):
         url = reverse('my-news')
         view = resolve(url).func
         self.assertEquals(view, myNews)
         
    def test_add_news_urls_is_resolved(self):
        url = reverse('add-news')
        view = resolve(url).func
        self.assertEquals(view, addNews)