from django.urls import path

from core.views import UserInfoView

urlpatterns = [
    path("", UserInfoView.as_view(), name="user-info"),
]
