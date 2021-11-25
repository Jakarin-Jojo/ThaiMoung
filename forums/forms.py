from django import forms
from .models import *


# topics = Topic.objects.all().values_list('topic_name', 'topic_name')
# topic_list = [item for item in topics]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'topic']


class PostTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name', 'category']


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']


class PostReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['description']
