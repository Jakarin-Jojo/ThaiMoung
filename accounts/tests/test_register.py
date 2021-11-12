from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class RegistrationTest(TestCase):

    def test_registration_page(self):
        """"""
        response = self.client.get(reverse('register_user'))
        self.assertTemplateUsed(response, 'accounts/sign_in_and_sign_up.html')
        self.assertEqual(response.status_code, 200)

    def test_registration_successful(self):
        """"""
        response = self.client.post(reverse('register_user'), {'username': 'test', 'email': 'testuser1@gmail.com',
                                                               'password1': 'secret123456',
                                                               'password2': 'secret123456'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/register_user')
