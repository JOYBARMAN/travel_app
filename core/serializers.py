from rest_framework import serializers

from core.models import User, UserDetail, Context, DynamicBanner


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = [
            "uid",
            "bio",
            "badge",
            "profile_photo",
            "contact_number",
            "contact_email",
            "location",
            "address",
            "facebook_link",
            "twitter_link",
            "instagram_link",
            "linkedin_link",
            "youtube_link",
            "website_link",
            "created_at",
            "updated_at",
            "status",
        ]


class ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Context
        fields = [
            "home_banner",
            "travel_guide",
            "about_me",
            "visited_place",
            "gallery",
            "created_at",
            "updated_at",
        ]


class DynamicBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicBanner
        fields = [
            "home",
            "home_travel",
            "newsletter",
            "contact",
            "about",
            "visited_place",
            "visited_place_explore",
            "created_at",
            "updated_at",
        ]


class UserInfoSerializer(serializers.ModelSerializer):
    details = UserDetailSerializer(read_only=True)
    banners = DynamicBannerSerializer(read_only=True)
    context = ContextSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "uid",
            "email",
            "username",
            "first_name",
            "last_name",
            "phone",
            "last_login",
            "status",
            "created_at",
            "updated_at",
            "details",
            "banners",
            "context",
        ]
        read_only_fields = fields
