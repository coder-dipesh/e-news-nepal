from django.test import TestCase, Client
from django.urls import reverse


class Test_views(TestCase):
    def test_resetpassword(self):
        client = Client()
        response = client.get(reverse('reset-password-enter-username'))
        self.assertTemplateUsed(
            response, 'accounts/resetPassword/resetPasswordEnterUsername.html')