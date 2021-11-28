"""Tests for create methods."""
from django.test import TestCase
from forums.forms import *


class CreateTopicTest(TestCase):
    """Tests for create topic."""

    def test_create_topic_full_fill(self):
        form_data = {'topic_name': 'Batman', 'category': 'movie'}
        form = PostTopicForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_topic_not_fill_topic_name(self):
        form_data = {'topic_name': '', 'category': 'movie'}
        form = PostTopicForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_create_topic_not_fill_category(self):
        form_data = {'topic_name': 'Batman', 'category': ''}
        form = PostTopicForm(data=form_data)
        self.assertFalse(form.is_valid())


class CreatePostTest(TestCase):
    """Tests for create post."""

    def setUp(self) -> None:
        Topic.objects.create(topic_name='Batman', category='movie')

    def test_create_post_full_fill(self):
        form_data = {'title': 'Batman 007',
                     'description': 'How do you feel after watching the movie?',
                     'topic': Topic.objects.get(id=1)}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_post_not_fill_title(self):
        form_data = {'title': '',
                     'description': 'How do you feel after watching the movie?',
                     'topic': Topic.objects.get(id=1)}
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_create_post_not_fill_description(self):
        form_data = {'title': 'Batman 007',
                     'description': '',
                     'topic': Topic.objects.get(id=1)}
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_create_post_not_select_topic(self):
        form_data = {'title': 'Batman 007',
                     'description': 'How do you feel after watching the movie?'}
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())


class CreateCommentTest(TestCase):
    """Tests for create comment."""

    def setUp(self) -> None:
        Topic.objects.create(topic_name='Batman', category='movie')
        Post.objects.create(title='Batman 007',
                            description='How do you feel after watching the movie?',
                            topic=Topic.objects.get(id=1))

    def test_create_comment_full_fill(self):
        form_data = {'description': 'In my opinion, I think Batman is the beginning of the Wuhan virus.'}
        form = PostCommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_comment_not_fill_description(self):
        form = PostCommentForm()
        self.assertFalse(form.is_valid())


class CreateReplyTest(TestCase):
    """Tests for reply topic."""

    def setUp(self) -> None:
        Topic.objects.create(topic_name='Batman', category='movie')
        Post.objects.create(title='Batman 007',
                            description='How do you feel after watching the movie?',
                            topic=Topic.objects.get(id=1))
        Comment.objects.create(post=Post.objects.get(id=1),
                               description='In my opinion, I think Batman is the beginning of the Wuhan virus.')

    def test_create_reply_full_fill(self):
        form_data = {'description': "What's wrong with you man. We just eat him (Chinese number one!!!)"}
        form = PostReplyForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_reply_not_fill_description(self):
        form = PostReplyForm()
        self.assertFalse(form.is_valid())
