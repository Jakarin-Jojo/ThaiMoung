from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


CATEGORY = [
    ('', '----------'),
    ('news', 'News'),
    ('sports', 'Sports'),
    ('games', 'Games'),
    ('fashion', 'Fashion'),
    ('technology', 'Technology'),
]


class Post(models.Model):
    """Post a class that collects values name, description, category, created_at, slug, the user."""

    title = models.CharField(max_length=50)  # title of the forum
    description = models.TextField(max_length=500)  # description of the forum
    category = models.CharField(max_length=20, choices=CATEGORY, default='')  # category of the forum
    post_date = models.DateTimeField(default=timezone.now)  # created date of the forum
    slug = models.SlugField(unique=True, allow_unicode=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    def __str__(self):
        """Return a string representation of the title of forum."""
        return self.title

    def save(self, *args, **kwargs):
        """Save the slug of the forum object."""
        self.slug = self.slug or slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('main')
