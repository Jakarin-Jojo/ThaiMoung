"""Tests for the forms."""
from django.test import TestCase
from forums.forms import *


class TopicFormTest(TestCase):
    """Tests of the topic form."""

    def test_topic_name_label(self):
        form = PostTopicForm()
        self.assertEqual(form.fields['topic_name'].label is None or form.fields['topic_name'].label, 'Topic name')

    def test_category_label(self):
        form = PostTopicForm()
        self.assertEqual(form.fields['category'].label is None or form.fields['category'].label, 'Category')

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


class PostFormTest(TestCase):
    """Tests of the post form."""

    def setUp(self) -> None:
        Topic.objects.create(topic_name='Batman', category='movie')

    def test_title_label(self):
        form = PostForm()
        self.assertEqual(form.fields['title'].label is None or form.fields['title'].label, 'Title')

    def test_description_label(self):
        form = PostForm()
        self.assertEqual(form.fields['description'].label is None or form.fields['description'].label, 'Description')

    def test_topic_label(self):
        form = PostForm()
        self.assertEqual(form.fields['topic'].label is None or form.fields['topic'].label, 'Topic')

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


class CommentFormTest(TestCase):
    """Tests of the comment form."""

    def setUp(self) -> None:
        Topic.objects.create(topic_name='Batman', category='movie')
        Post.objects.create(title='Batman 007',
                            description='How do you feel after watching the movie?',
                            topic=Topic.objects.get(id=1))

    def test_description_label(self):
        form = PostCommentForm()
        self.assertEqual(form.fields['description'].label is None or form.fields['description'].label, 'Description')

    def test_create_comment_full_fill(self):
        form_data = {'description': 'In my opinion, I think Batman is the beginning of the Wuhan virus.'}
        form = PostCommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_comment_not_fill_description(self):
        form = PostCommentForm()
        self.assertFalse(form.is_valid())


class ReplyFormTest(TestCase):
    """Tests of the reply form."""

    def setUp(self) -> None:
        Topic.objects.create(topic_name='Batman', category='movie')
        Post.objects.create(title='Batman 007',
                            description='How do you feel after watching the movie?',
                            topic=Topic.objects.get(id=1))
        Comment.objects.create(post=Post.objects.get(id=1),
                               description='In my opinion, I think Batman is the beginning of the Wuhan virus.')

    def test_description_label(self):
        form = PostReplyForm()
        self.assertEqual(form.fields['description'].label is None or form.fields['description'].label, 'Description')

    def test_create_reply_full_fill(self):
        form_data = {'description': "What's wrong with you man. We just eat him (Chinese number one!!!)"}
        form = PostReplyForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_reply_not_fill_description(self):
        form = PostReplyForm()
        self.assertFalse(form.is_valid())

