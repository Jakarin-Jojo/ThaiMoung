from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class SignInTest(TestCase):

    def setUp(self):
        """Initialize a user with username, email, password and first name."""
        self.credentials = {
            'username': 'testuser',
            'password': 'secret123456',
            'email': 'testerman@gmail.com'}
        User.objects.create_user(**self.credentials)

    def test_sign_in_successful(self):
        response = self.client.post(reverse('login'), {'username': 'testuser',
                                    'password': 'secret123456'}, follow=True)
        self.assertRedirects(response, '/forums/')

    def test_sign_in_with_wrong_password(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '123456798'}, follow=True)
        self.assertContains(response, 'Username or Password is incorrect.')

    def test_sign_in_with_wrong_username(self):
        response = self.client.post(reverse('login'), {'username': 'usertest', 'password': 'secret123456'}, follow=True)
        self.assertContains(response, 'Username or Password is incorrect.')
