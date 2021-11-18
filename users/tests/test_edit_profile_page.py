from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class EditProfileViewTest(TestCase):
    """Test for EditProfile page."""

    def test_edit_profile_page_without_edit_profile(self):
        user = User.objects.create_user(username='tester', password='secret123456')
        self.client.login(username='tester', password='secret123456')
        response = self.client.get(reverse('edit_profile', args=['tester']))
        self.assertEqual(response.status_code, 200)

    def test_edit_profile_page_with_edit_profile(self):
        user = User.objects.create_user(username='tester', password='secret123456', email='user1@gmail.com')
        self.client.login(username='tester', password='secret123456')

        self.assertEqual(user.username, 'tester')
        response = self.client.get(reverse('edit_profile', args=['tester']))

        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('edit_profile', args=['tester']), {
            'username': 'user1'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
