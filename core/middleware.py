from django.http import JsonResponse
from django.contrib.auth import get_user_model


User = get_user_model()


class UserNameAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        username = request.headers.get("username")
        print(f"Username from headers: {username}")

        if not username:
            return JsonResponse({"detail": "Missing username in headers."}, status=400)

        try:
            # Get the user with the provided username
            user = User.objects.select_related(
                "details",
                "banners",
                "context",
            ).get(username=username)

            request.user = user

        except User.DoesNotExist:
            return JsonResponse(
                {"detail": "User with provided username not found."}, status=404
            )

        response = self.get_response(request)
        return response
