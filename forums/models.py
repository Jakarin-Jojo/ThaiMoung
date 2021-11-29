from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

CATEGORY = [
    ('', '----------'),
    ('news', 'News'),
    ('harassment', 'Harassment'),
    ('sports', 'Sports'),
    ('games', 'Games'),
    ('fashion', 'Fashion'),
    ('technology', 'Technology'),
    ('music', 'Music'),
    ('movie', 'Movie'),
    ('gourmet', 'Gourmet'),
]


class Topic(models.Model):
    """A class that collect the list of post."""

    topic_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=CATEGORY, default='')  # category of the topic
    topic_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Return a string representation of the topic."""
        return self.topic_name


class Post(models.Model):
    """Post a class that collects values name, description, category, created_at, slug, the user."""

    title = models.CharField(max_length=50)  # title of the forum
    description = models.TextField(max_length=500)  # description of the forum
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # topic of the forum
    post_date = models.DateTimeField(default=timezone.now)  # created date of the forum
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    def __str__(self):
        """Return a string representation of the title of forum."""
        return self.title


class Comment(models.Model):
    """A class that collects values name, description, category, created_at, slug, the user."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    description = models.TextField(max_length=500)
    post_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes_comment')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes_comment')

    def __str__(self):
        """Return a string representation of the comment in forum."""
        return f"{str(self.post)} - {self.description[:20]}"


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    description = models.TextField(max_length=500)
    post_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes_reply')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes_reply')

    def __str__(self):
        """Return a string representation of the reply in comment."""
        return f"{str(self.comment)} - {self.description[:20]}"
