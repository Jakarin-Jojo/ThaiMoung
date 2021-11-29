from django.test import TestCase
from django.urls import reverse
from forums.models import *


class LikesCommentSystem(TestCase):
    """Test for likes and dislikes reply comments"""

    def setUp(self) -> None:
        """setup testcase by create user, topic ,post, comment and reply."""
        self.users = User.objects.create_user(username='tester', password='secret123456')
        self.topic = Topic.objects.create(topic_name='Hello', category='New')
        self.post = Post.objects.create(title='test', description='tester', topic=self.topic, user=self.users)
        self.comment = Comment.objects.create(post=self.post, description='test', user=self.users)
        self.reply = Reply.objects.create(comment=self.comment, description='Test Like', user=self.users)
        self.client.login(username='tester', password='secret123456')

    def test_submit_likes_comment_without_login(self):
        """Test submit likes reply comment without login ,The web must redirect to register_user"""
        self.client.logout()
        response = self.client.post(reverse('likes_reply', args=[self.post.pk, self.comment.pk, self.reply.pk]),
                                    follow=True)
        self.assertEqual(self.reply.likes.count(), 0)
        self.assertRedirects(response, '/accounts/register_user')
        self.assertEqual(response.status_code, 200)

    def test_submit_likes_with_login(self):
        """Test submit like button when logged The web must add a number of likes."""
        response = self.client.post(reverse('likes_reply', args=[self.post.pk, self.comment.pk, self.reply.pk]),
                                    follow=True)
        self.assertRedirects(response, '/forums/detail/1/')
        self.assertEqual(self.reply.likes.count(), 1)
        self.assertEqual(response.status_code, 200)

    def test_submit_dislikes_with_login(self):
        """Test submit dislike button when logged The web must add a number of dislikes."""
        response = self.client.post(reverse('dislikes_reply', args=[self.post.pk, self.comment.pk, self.reply.pk]),
                                    follow=True)
        self.assertRedirects(response, '/forums/detail/1/')
        self.assertEqual(self.reply.likes.count(), 0)
        self.assertEqual(self.reply.dislikes.count(), 1)
        self.assertEqual(response.status_code, 200)

    def test_submit_likes_first_and_dislikes_after(self):
        """Test submit likes first and dislikes after, number of dislikes will increase by  1"""
        self.client.post(reverse('dislikes_reply', args=[self.post.pk, self.comment.pk, self.reply.pk]), follow=True)
        self.assertEqual(self.reply.likes.count(), 0)
        self.client.post(reverse('likes_reply', args=[self.post.pk, self.comment.pk, self.reply.pk]), follow=True)
        self.assertEqual(self.reply.likes.count(), 1)
        self.client.post(reverse('dislikes_reply', args=[self.post.pk, self.comment.pk, self.reply.pk]), follow=True)
        self.assertEqual(self.reply.likes.count(), 0)
        self.assertEqual(self.reply.dislikes.count(), 1)

    def test_submit_dislikes_first_and_likes_after(self):
        """Test submit dislikes first and likes after, number of likes will increase by 1"""
        self.assertEqual(self.reply.dislikes.count(), 0)
        self.client.post(reverse('dislikes_reply', args=[self.post.pk, self.comment.pk, self.reply.pk]), follow=True)
        self.assertEqual(self.reply.dislikes.count(), 1)
        self.client.post(reverse('likes_reply', args=[self.post.pk, self.comment.pk, self.reply.pk]), follow=True)
        self.assertEqual(self.reply.dislikes.count(), 0)
        self.assertEqual(self.reply.likes.count(), 1)

    def test_submit_like_twice(self):
        """Test sending likes twice, the number of likes will be the same as the first. """
        self.assertEqual(self.reply.likes.count(), 0)
        self.client.post(reverse('likes_reply', args=[self.post.pk, self.comment.pk, self.reply.pk]), follow=True)
        self.assertEqual(self.reply.likes.count(), 1)
        self.client.post(reverse('likes_reply', args=[self.post.pk, self.comment.pk, self.reply.pk]), follow=True)
        self.assertEqual(self.reply.likes.count(), 0)

    def test_submit_dislike_twice(self):
        """Test sending dislikes twice, the number of likes will be the same as the first. """
        self.assertEqual(self.reply.dislikes.count(), 0)
        self.client.post(reverse('dislikes_reply', args=[self.post.pk, self.comment.pk, self.reply.pk]), follow=True)
        self.assertEqual(self.reply.dislikes.count(), 1)
        self.client.post(reverse('dislikes_reply', args=[self.post.pk, self.comment.pk, self.reply.pk]), follow=True)
        self.assertEqual(self.reply.dislikes.count(), 0)
