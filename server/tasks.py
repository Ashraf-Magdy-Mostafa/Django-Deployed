from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_welcome_email(to_email: str):
    send_mail(
        subject="Welcome!",
        message="Your background task ran successfully.",
        from_email=None,  # uses DEFAULT_FROM_EMAIL
        recipient_list=[to_email],
        fail_silently=True,
    )
    return "ok"
