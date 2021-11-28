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


class PostFormTest(TestCase):
    """Tests of the post form."""

    def test_title_label(self):
        form = PostForm()
        self.assertEqual(form.fields['title'].label is None or form.fields['title'].label, 'Title')

    def test_description_label(self):
        form = PostForm()
        self.assertEqual(form.fields['description'].label is None or form.fields['description'].label, 'Description')

    def test_topic_label(self):
        form = PostForm()
        self.assertEqual(form.fields['topic'].label is None or form.fields['topic'].label, 'Topic')


class CommentFormTest(TestCase):
    """Tests of the comment form."""

    def test_description_label(self):
        form = PostCommentForm()
        self.assertEqual(form.fields['description'].label is None or form.fields['description'].label, 'Description')


class ReplyFormTest(TestCase):
    """Tests of the reply form."""

    def test_description_label(self):
        form = PostReplyForm()
        self.assertEqual(form.fields['description'].label is None or form.fields['description'].label, 'Description')

