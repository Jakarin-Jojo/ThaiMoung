from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class ProfileViewTest(TestCase):
    """Test for profile page."""

    def test_profile_page_with_no_account(self):
        response = self.client.get(reverse('profile', args=('anonymous',)))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/register_user')

    def test_profile_page_with_have_account(self):
        user = User.objects.create_user(username='tester', password='secret123456')
        response = self.client.get(reverse('profile', args=(user.username,)))
        self.assertEqual(response.status_code, 200)
