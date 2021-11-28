"""Tests for the models."""
from django.test import TestCase
from forums.models import *


class TopicModelTest(TestCase):
    """Tests of the topic model."""

    def setUp(self) -> None:
        Topic.objects.create(topic_name='Batman', category='movie')

    def test_topic_name_label(self):
        topic = Topic.objects.get(id=1)
        field_label = topic._meta.get_field('topic_name').verbose_name
        self.assertEqual(field_label, 'topic name')

    def test_category_label(self):
        topic = Topic.objects.get(id=1)
        field_label = topic._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_topic_date_label(self):
        topic = Topic.objects.get(id=1)
        field_label = topic._meta.get_field('topic_date').verbose_name
        self.assertEqual(field_label, 'topic date')

    def test_topic_name_max_length(self):
        topic = Topic.objects.get(id=1)
        field_label = topic._meta.get_field('topic_name').max_length
        self.assertEqual(field_label, 20)

    def test_object_name_is_topic_name(self):
        topic = Topic.objects.get(id=1)
        expected_object_name = topic.topic_name
        self.assertEqual(str(topic), expected_object_name)

    def test_get_absolute_url(self):
        topic = Topic.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(topic.get_absolute_url(), '/forums/')


class PostModelTest(TestCase):
    """Tests of the post model."""

    def setUp(self) -> None:
        Topic.objects.create(topic_name='Batman', category='movie')
        Post.objects.create(title='Batman 007',
                            description='How do you feel after watching the movie?',
                            topic=Topic.objects.get(id=1))

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_topic_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('topic').verbose_name
        self.assertEqual(field_label, 'topic')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').max_length
        self.assertEqual(field_label, 50)

    def test_description_max_length(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('description').max_length
        self.assertEqual(field_label, 500)

    def test_object_name_is_title(self):
        post = Post.objects.get(id=1)
        expected_object_name = post.title
        self.assertEqual(str(post), expected_object_name)

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(post.get_absolute_url(), '/forums/')


class CommentModelTest(TestCase):
    """Tests of the comment model."""

    def setUp(self) -> None:
        Topic.objects.create(topic_name='Batman', category='movie')
        Post.objects.create(title='Batman 007',
                            description='How do you feel after watching the movie?',
                            topic=Topic.objects.get(id=1))
        Comment.objects.create(post=Post.objects.get(id=1),
                               description='In my opinion, I think Batman is the beginning of the Wuhan virus.')

    def test_post_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('post').verbose_name
        self.assertEqual(field_label, 'post')

    def test_description_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('description').max_length
        self.assertEqual(field_label, 500)

    def test_object_name_is_title_dash_description_20_char(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f'{comment.post.title} - {comment.description[:20]}'
        self.assertEqual(str(comment), expected_object_name)

    def test_get_absolute_url(self):
        comment = Comment.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(comment.get_absolute_url(), '/forums/')


class ReplyModelTest(TestCase):
    """Tests of the reply model."""

    def setUp(self) -> None:
        Topic.objects.create(topic_name='Batman', category='movie')
        Post.objects.create(title='Batman 007',
                            description='How do you feel after watching the movie?',
                            topic=Topic.objects.get(id=1))
        Comment.objects.create(post=Post.objects.get(id=1),
                               description='In my opinion, I think Batman is the beginning of the Wuhan virus.')
        Reply.objects.create(comment=Comment.objects.get(id=1),
                             description="What's wrong with you man. We just eat him (Chinese number one!!!)")

    def test_comment_label(self):
        reply = Reply.objects.get(id=1)
        field_label = reply._meta.get_field('comment').verbose_name
        self.assertEqual(field_label, 'comment')

    def test_description_label(self):
        reply = Reply.objects.get(id=1)
        field_label = reply._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        reply = Reply.objects.get(id=1)
        field_label = reply._meta.get_field('description').max_length
        self.assertEqual(field_label, 500)

    def test_object_name_is_str_comment_dash_description_20_char(self):
        reply = Reply.objects.get(id=1)
        expected_object_name = f"{str(reply.comment)} - {reply.description[:20]}"
        self.assertEqual(str(reply), expected_object_name)

    def test_get_absolute_url(self):
        reply = Reply.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(reply.get_absolute_url(), '/forums/')
