from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import send_welcome_email


class PingView(APIView):
    def get(self, request):
        email = request.GET.get("email")
        if email:
            send_welcome_email.delay(email)  # prove worker runs
        return Response({"status": "ok", "queued_email": bool(email)})
