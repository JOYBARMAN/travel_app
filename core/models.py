from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from shared.base_model import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields,
        )
        user.save(using=self._db)

        return user

    def create_superuser(
        self, email, first_name, last_name, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, first_name, last_name, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(max_length=50, unique=True, db_index=True)
    password = models.CharField(max_length=128, blank=True)
    new_password = models.CharField(max_length=128, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"uid:{self.uid} {self.email}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password) if self.password else ""
            self.username = self.email if not self.username else self.username

        if self.new_password:
            self.password = make_password(self.new_password)
            self.new_password = ""

        super().save(*args, **kwargs)


class UserDetail(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="details")
    bio = models.TextField(blank=True, help_text="Short biography of the user")
    badge = models.CharField(
        max_length=250, blank=True, help_text="User's badge or title"
    )
    profile_photo = models.URLField(
        max_length=500, blank=True, help_text="URL to the profile photo"
    )
    contact_number = models.CharField(
        max_length=15, blank=True, help_text="User's contact number"
    )
    contact_email = models.EmailField(
        max_length=255, blank=True, help_text="User's contact email"
    )
    location = models.CharField(max_length=100, blank=True, help_text="User's location")
    address = models.CharField(max_length=255, blank=True)
    facebook_link = models.URLField(
        max_length=500, blank=True, help_text="Facebook profile link"
    )
    twitter_link = models.URLField(
        max_length=500, blank=True, help_text="Twitter profile link"
    )
    instagram_link = models.URLField(
        max_length=500, blank=True, help_text="Instagram profile link"
    )
    linkedin_link = models.URLField(
        max_length=500, blank=True, help_text="LinkedIn profile link"
    )
    youtube_link = models.URLField(
        max_length=500, blank=True, help_text="YouTube channel link"
    )
    website_link = models.URLField(
        max_length=500, blank=True, help_text="Personal website link"
    )

    def __str__(self):
        return f"User Details for {self.user.email}"


class Context(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="context")
    home_banner = models.TextField(
        blank=True, help_text="Content of home tab banner for the user"
    )
    travel_guide = models.TextField(
        blank=True, help_text="Content of travel guide tab for the user"
    )
    about_me = models.TextField(
        blank=True, help_text="Content of about me tab for the user"
    )
    visited_place = models.TextField(
        blank=True, help_text="Content of visited place tab for the user"
    )
    gallery = models.TextField(
        blank=True, help_text="Content of gallery tab for the user"
    )

    def __str__(self):
        return f"Context for {self.user.email}"


class DynamicBanner(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="banners",
    )
    home = models.URLField(
        max_length=500, blank=True, help_text="URL to the home section banner"
    )
    home_travel = models.URLField(
        max_length=500,
        blank=True,
        help_text="URL to the home travel section banner",
    )
    newsletter = models.URLField(
        max_length=500, blank=True, help_text="URL to the newsletter section banner"
    )
    contact = models.URLField(
        max_length=500, blank=True, help_text="URL to the contact section banner"
    )
    about = models.URLField(
        max_length=500, blank=True, help_text="URL to the about section banner"
    )
    visited_place = models.URLField(
        max_length=500,
        blank=True,
        help_text="URL to the visited place section banner",
    )
    visited_place_explore = models.URLField(
        max_length=500,
        blank=True,
        help_text="URL to the visited place explore section banner",
    )

    def __str__(self):
        return f"Dynamic Banner for {self.user.email}"
