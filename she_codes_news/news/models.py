from email.mime import image
from django.db import models
from django.contrib.auth import get_user_model
from django.forms import SlugField


class Category(models.Model):
    slug = models.SlugField()

    class Meta:
        ordering = ["slug"]

    def __str__(self):
        return self.slug


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField(null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stories",
    )
