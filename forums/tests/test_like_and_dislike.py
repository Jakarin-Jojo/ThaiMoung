from django.utils import timezone

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from forums.models import Post


class LikeSystem(TestCase):
    """Test for liking posts"""

    def test_submit_likes_without_login(self):
        users = User.objects.create_user(username='tester', password='secret123456')
        post = Post.objects.create(title='test', description='tester', category='New', post_date=timezone.now(),
                                   user=users)
        response = self.client.post(reverse('likes', args=[post.pk]), follow=True)
        self.assertRedirects(response, '/accounts/register_user')
        self.assertEqual(response.status_code, 200)

    def test_submit_likes_with_login(self):
        users = User.objects.create_user(username='tester', password='secret123456')
        self.client.login(username='tester', password='secret123456')
        post = Post.objects.create(title='test', description='tester', category='New', post_date=timezone.now(),
                                   user=users)
        response = self.client.post(reverse('likes', args=[post.pk]), follow=True)
        self.assertRedirects(response, '/forums/detail/1/')
        self.assertEqual(response.status_code, 200)

    def test_submit_dislikes_with_login(self):
        users = User.objects.create_user(username='tester', password='secret123456')
        self.client.login(username='tester', password='secret123456')
        post = Post.objects.create(title='test', description='tester', category='New', post_date=timezone.now(),
                                   user=users)
        response = self.client.post(reverse('dislikes', args=[post.pk]), follow=True)
        self.assertRedirects(response, '/forums/detail/1/')
        self.assertEqual(response.status_code, 200)

    def test_submit_likes_first_and_dislikes_after(self):
        users = User.objects.create_user(username='tester', password='secret123456')
        self.client.login(username='tester', password='secret123456')
        post = Post.objects.create(title='test', description='tester', category='New', post_date=timezone.now(),
                                   user=users)
        self.assertEqual(post.likes.count(), 0)
        response = self.client.post(reverse('likes', args=[post.pk]), follow=True)
        self.assertEqual(post.likes.count(), 1)
        response = self.client.post(reverse('dislikes', args=[post.pk]), follow=True)
        self.assertEqual(post.likes.count(), 0)
        self.assertEqual(post.dislikes.count(), 1)

    def test_submit_dislikes_first_and_likes_after(self):
        users = User.objects.create_user(username='tester', password='secret123456')
        self.client.login(username='tester', password='secret123456')
        post = Post.objects.create(title='test', description='tester', category='New', post_date=timezone.now(),
                                   user=users)
        self.assertEqual(post.dislikes.count(), 0)
        response = self.client.post(reverse('dislikes', args=[post.pk]), follow=True)
        self.assertEqual(post.dislikes.count(), 1)
        response = self.client.post(reverse('likes', args=[post.pk]), follow=True)
        self.assertEqual(post.dislikes.count(), 0)
        self.assertEqual(post.likes.count(), 1)

    def test_submit_like_twice(self):
        users = User.objects.create_user(username='tester', password='secret123456')
        self.client.login(username='tester', password='secret123456')
        post = Post.objects.create(title='test', description='tester', category='New', post_date=timezone.now(),
                                   user=users)
        self.assertEqual(post.likes.count(), 0)
        response = self.client.post(reverse('likes', args=[post.pk]), follow=True)
        self.assertEqual(post.likes.count(), 1)
        response = self.client.post(reverse('likes', args=[post.pk]), follow=True)
        self.assertEqual(post.likes.count(), 0)

    def test_submit_dislike_twice(self):
        users = User.objects.create_user(username='tester', password='secret123456')
        self.client.login(username='tester', password='secret123456')
        post = Post.objects.create(title='test', description='tester', category='New', post_date=timezone.now(),
                                   user=users)
        self.assertEqual(post.dislikes.count(), 0)
        response = self.client.post(reverse('dislikes', args=[post.pk]), follow=True)
        self.assertEqual(post.dislikes.count(), 1)
        response = self.client.post(reverse('dislikes', args=[post.pk]), follow=True)
        self.assertEqual(post.dislikes.count(), 0)