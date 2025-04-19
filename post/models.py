from django.db import models

from core.models import User

from post.choices import PostTypeChoices, CountryChoices

from shared.base_model import BaseModel


class Post(BaseModel):
    """Post model to store posts."""

    # Relationships
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User who created the post",
        related_name="posts",
    )
    # General fields
    title = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=500, blank=True)
    image = models.URLField(max_length=500, blank=True)
    video = models.URLField(max_length=500, blank=True)
    content = models.TextField(help_text="Content of the post")
    post_type = models.CharField(
        max_length=20,
        choices=PostTypeChoices.choices,
        default=PostTypeChoices.UNDEFINED,
        help_text="Type of the post",
    )

    def __str__(self):
        return self.title


class UserGallery(BaseModel):
    """User gallery model to store user galleries."""

    # Relationships
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User who created the gallery",
        related_name="galleries",
    )
    # General fields
    image = models.URLField(max_length=500)
    title = models.CharField(max_length=500, blank=True)
    content = models.TextField(help_text="Content of the gallery", blank=True)
    country = models.CharField(
        max_length=20,
        choices=CountryChoices.choices,
        help_text="Country of the gallery",
    )

    def __str__(self):
        return self.title
