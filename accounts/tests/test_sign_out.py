from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class SignOutTest(TestCase):
    """Testing for sign out."""

    def setUp(self):
        """Initialize a user with username, email, password."""
        self.credentials = {
            'username': 'tester',
            'password': 'secret123456',
            'email': 'tester@gmail.com'}
        User.objects.create_user(**self.credentials)

    def test_sign_out(self):
        """If the user sign out, it will redirect to main page."""
        response = self.client.post(reverse('login'), {'username': 'tester',
                                    'password': 'secret123456'}, follow=True)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/forums/')
