from django.test import TestCase
from django.urls import reverse
from forums.models import *


class LikeSystem(TestCase):
    """Test for likes and dislikes posts"""

    def setUp(self) -> None:
        """Setup testcase by create user, topic and post."""
        self.users = User.objects.create_user(username='tester', password='secret123456')
        self.client.login(username='tester', password='secret123456')
        self.topic = Topic.objects.create(topic_name='Hello', category='New')
        self.post = Post.objects.create(title='test', description='tester', topic=Topic.objects.get(topic_name='Hello'),
                                        user=self.users)

    def test_submit_likes_without_login(self):
        """Test submit likes without login ,The web must redirect to register_user"""
        self.client.logout()
        response = self.client.post(reverse('likes', args=[self.post.pk]), follow=True)
        self.assertEqual(self.post.likes.count(), 0)
        self.assertRedirects(response, '/accounts/register_user')
        self.assertEqual(response.status_code, 200)

    def test_submit_likes_with_login(self):
        """Test submit like button when logged The web must add a number of likes."""
        response = self.client.post(reverse('likes', args=[self.post.pk]), follow=True)
        self.assertRedirects(response, '/forums/detail/1/')
        self.assertEqual(self.post.likes.count(), 1)
        self.assertEqual(response.status_code, 200)

    def test_submit_dislikes_with_login(self):
        """Test submit dislike button when logged The web must add a number of dislikes."""
        response = self.client.post(reverse('dislikes', args=[self.post.pk]), follow=True)
        self.assertRedirects(response, '/forums/detail/1/')
        self.assertEqual(response.status_code, 200)

    def test_submit_likes_first_and_dislikes_after(self):
        """Test submit likes first and dislikes after, number of dislikes will increase by  1"""
        self.assertEqual(self.post.likes.count(), 0)
        self.client.post(reverse('likes', args=[self.post.pk]), follow=True)
        self.assertEqual(self.post.likes.count(), 1)
        self.client.post(reverse('dislikes', args=[self.post.pk]), follow=True)
        self.assertEqual(self.post.likes.count(), 0)
        self.assertEqual(self.post.dislikes.count(), 1)

    def test_submit_dislikes_first_and_likes_after(self):
        """Test submit dislikes first and likes after, number of likes will increase by 1"""
        self.assertEqual(self.post.dislikes.count(), 0)
        self.client.post(reverse('dislikes', args=[self.post.pk]), follow=True)
        self.assertEqual(self.post.dislikes.count(), 1)
        self.client.post(reverse('likes', args=[self.post.pk]), follow=True)
        self.assertEqual(self.post.dislikes.count(), 0)
        self.assertEqual(self.post.likes.count(), 1)

    def test_submit_like_twice(self):
        """Test sending likes twice, the number of likes will be the same as the first. """
        self.assertEqual(self.post.likes.count(), 0)
        self.client.post(reverse('likes', args=[self.post.pk]), follow=True)
        self.assertEqual(self.post.likes.count(), 1)
        self.client.post(reverse('likes', args=[self.post.pk]), follow=True)
        self.assertEqual(self.post.likes.count(), 0)

    def test_submit_dislike_twice(self):
        """Test sending dislikes twice, the number of likes will be the same as the first. """
        self.assertEqual(self.post.dislikes.count(), 0)
        self.client.post(reverse('dislikes', args=[self.post.pk]), follow=True)
        self.assertEqual(self.post.dislikes.count(), 1)
        self.client.post(reverse('dislikes', args=[self.post.pk]), follow=True)
        self.assertEqual(self.post.dislikes.count(), 0)
