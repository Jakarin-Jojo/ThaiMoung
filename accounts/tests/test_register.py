from django.test import TestCase
from django.urls import reverse


class RegistrationTest(TestCase):
    """Testing for registration"""

    def test_registration_page(self):
        """If the sign-up page is available, the web will display the sign-up page and the status code is 200."""
        response = self.client.get(reverse('register_user'))
        self.assertTemplateUsed(response, 'accounts/sign_in_and_sign_up.html')
        self.assertEqual(response.status_code, 200)

    def test_registration_successful(self):
        """If the user sign up success, the web will redirect to the login page"""
        response = self.client.post(reverse('register_user'), {'username': 'test', 'email': 'testuser1@gmail.com',
                                                               'password1': 'secret123456',
                                                               'password2': 'secret123456'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/register_user')
