from rest_framework import generics

from core.models import User
from core.serializers import UserInfoSerializer


class UserInfoView(generics.RetrieveAPIView):
    """
    View to retrieve user information.
    """

    serializer_class = UserInfoSerializer

    def get_object(self):
        return self.request.user
