from ast import mod
from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )

    description = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(default=datetime.date.today)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


# Create your models here.
