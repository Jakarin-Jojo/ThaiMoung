"""Tests for create methods."""
from django.test import TestCase
from django.urls import reverse

from forums.views import *


class CreateTopic(TestCase):
    """Tests for create topic."""

    def setUp(self):
        """Initialize a user with username, email, password and first name."""
        self.credentials = {
            'username': 'tester',
            'password': 'secret123456',
            'email': 'testerman@gmail.com'}
        User.objects.create_user(**self.credentials)

    def test_create_topic_without_login(self):
        response = self.client.post(reverse('create_topic'),
                                    {'topic_name': 'Batman', 'category': 'movie'},
                                    follow=True)
        self.assertRedirects(response, '/accounts/register_user')
        self.assertEqual(Topic.objects.count(), 0)

    def test_create_topic_with_login(self):
        self.client.login(username='tester', password='secret123456')
        response = self.client.post(reverse('create_topic'),
                                    {'topic_name': 'Batman', 'category': 'movie'},
                                    follow=True)
        self.assertRedirects(response, '/forums/')
        self.assertEqual(Topic.objects.count(), 1)


class CreatePost(TestCase):
    """Tests for create post."""

    def setUp(self):
        """Initialize a user with username, email, password and first name."""
        self.credentials = {
            'username': 'tester',
            'password': 'secret123456',
            'email': 'testerman@gmail.com'}
        self.user = User.objects.create_user(**self.credentials)
        self.topic = Topic.objects.create(topic_name='Batman', category='movie')

    def test_create_post_without_login(self):
        response = self.client.post(reverse('create_forum'),
                                    {'title': 'Batman 007',
                                     'description': 'How do you feel after watching the movie?',
                                     'topic': self.topic.topic_name,
                                     'user': self.user},
                                    follow=True)
        self.assertRedirects(response, '/accounts/register_user')
        self.assertEqual(Post.objects.count(), 0)

    # def test_create_post_with_login(self):
    #     self.client.login(username='tester', password='secret123456')
    #     # post = Post.objects.create(title='Batman 5',
    #     #                     description='How do you feel after watching the movie?',
    #     #                     topic=Topic.objects.get(id=1))
    #     response = self.client.post(reverse('create_forum'), {
    #         'title': 'Batman 007',
    #         'description': 'How do you feel after watching the movie?',
    #         'topic': self.topic,
    #         'user': self.user},
    #         follow=True)
    #     self.assertTemplateUsed(response, 'forums/create_forum.html')
    #     self.assertEqual(Post.objects.count(), 1)
    #     self.assertRedirects(response, f'/forums/topic_{self.topic.pk}')  # f'/forums/topic_{self.topic.pk}'

    # def test_create_topic_already_created(self):
    #     self.client.login(username='tester', password='secret123456')
    #     response = self.client.post(reverse('create_topic'),
    #                                 {'topic_name': 'Batman', 'category': 'movie'},
    #                                 follow=True)
    #     messages = list(response.context['messages'])
    #     self.assertEqual(str(messages[0]), 'Topic Batman is already exists.')
    #     self.assertRedirects(response, '/forums/')


class CreateComment(TestCase):
    """Tests for create topic."""

    def setUp(self):
        """Initialize a user with username, email, password and first name."""
        self.credentials = {
            'username': 'tester',
            'password': 'secret123456',
            'email': 'testerman@gmail.com'}
        self.user = User.objects.create_user(**self.credentials)
        self.topic = Topic.objects.create(topic_name='Batman', category='movie')
        self.post = Post.objects.create(title='Batman 5',
                                        description='How do you feel after watching the movie?',
                                        topic=self.topic,
                                        user=self.user)

    def test_create_comment_without_login(self):
        response = self.client.post(reverse('create_comment', args=[self.post.pk]),
                                    {'post': self.post,
                                     'description': 'Hello',
                                     'user': self.user},
                                    follow=True)
        self.assertRedirects(response, '/accounts/register_user')
        self.assertEqual(Comment.objects.count(), 0)

    def test_create_comment_with_login(self):
        self.client.login(username='tester', password='secret123456')
        response = self.client.post(reverse('create_comment', args=[self.post.pk]),
                                    {'post': self.post,
                                     'description': 'Hello',
                                     'user': self.user},
                                    follow=True)
        self.assertRedirects(response, f'/forums/detail/{self.post.pk}/')
        self.assertEqual(Comment.objects.count(), 1)


class CreateReply(TestCase):
    """Tests for create topic."""

    def setUp(self):
        """Initialize a user with username, email, password and first name."""
        self.credentials = {
            'username': 'tester',
            'password': 'secret123456',
            'email': 'testerman@gmail.com'}
        self.user = User.objects.create_user(**self.credentials)
        self.topic = Topic.objects.create(topic_name='Batman', category='movie')
        self.post = Post.objects.create(title='Batman 5',
                                        description='How do you feel after watching the movie?',
                                        topic=self.topic,
                                        user=self.user)
        self.comment = Comment.objects.create(post=self.post,
                                              description='Hello',
                                              user=self.user)

    def test_create_comment_without_login(self):
        response = self.client.post(reverse('create_reply', args=[self.post.pk, self.comment.pk]),
                                    {'comment': self.comment,
                                     'description': 'Hooray',
                                     'user': self.user},
                                    follow=True)
        self.assertRedirects(response, '/accounts/register_user')
        self.assertEqual(Reply.objects.count(), 0)

    def test_create_comment_with_login(self):
        self.client.login(username='tester', password='secret123456')
        response = self.client.post(reverse('create_reply', args=[self.post.pk, self.comment.pk]),
                                    {'comment': self.comment,
                                     'description': 'Hooray',
                                     'user': self.user},
                                    follow=True)
        self.assertRedirects(response, f'/forums/detail/{self.post.pk}/')
        self.assertEqual(Reply.objects.count(), 1)
