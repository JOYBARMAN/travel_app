from django.db import models

from core.models import User

from shared.base_model import BaseModel


class Newsletter(BaseModel):
    """Newsletter model to store newsletters."""

    # Relationships
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User newsletter",
        related_name="newsletters",
    )
    # General fields
    email = models.EmailField(
        max_length=500,
        help_text="Email of the subscribed user",
    )

    def __str__(self):
        return self.email


class Contact(BaseModel):
    """Contact model to store contact messages."""

    # Relationships
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User who created the contact",
        related_name="contacts",
    )
    # General fields
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    subject = models.CharField(max_length=500)
    message = models.TextField(help_text="Content of the contact message")

    def __str__(self):
        return self.email
