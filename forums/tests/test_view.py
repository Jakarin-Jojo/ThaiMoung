"""Tests for Registration."""
from django.test import TestCase
from django.urls import reverse


class RegistrationViewTests(TestCase):
    """Tests for sign in and sign up."""

    def test_main_view(self):
        """Tests that after we get into the page, we must get a status code of 200"""
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_create_topic_view(self):
        """Tests that after we get into the page, we must get a status code of 200"""
        response = self.client.get(reverse('create_topic'))
        self.assertEqual(response.status_code, 302)

    def test_create_forum_view(self):
        """Tests that after we get into the page, we must get a status code of 200"""
        response = self.client.get(reverse('create_forum'))
        self.assertEqual(response.status_code, 302)
