"""Tests for Registration."""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class RegistrationViewTests(TestCase):
    """Tests for sign in and sign up."""
    def setUp(self) -> None:
        self.credentials = {
            'username': 'tester',
            'password': 'secret123456',
            'email': 'testerman@gmail.com'}
        User.objects.create_user(**self.credentials)
        self.client.login(username='tester', password='secret123456')

    def test_main_view(self):
        """Tests that after we get into the page, we must get a status code of 200"""
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_create_topic_view(self):
        """Tests that after we get into the page, we must get a status code of 200"""
        response = self.client.get(reverse('create_topic'))
        self.assertTemplateUsed(response, 'forums/create_topic.html')
        self.assertEqual(response.status_code, 200)

    def test_create_forum_view(self):
        """Tests that after we get into the page, we must get a status code of 200"""
        response = self.client.get(reverse('create_forum'))
        self.assertTemplateUsed(response, 'forums/create_forum.html')
        self.assertEqual(response.status_code, 200)
