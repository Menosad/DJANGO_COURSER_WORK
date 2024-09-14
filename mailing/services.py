from django.conf import settings
from django.core.mail import send_mail

from mailing.models import Mailing, Client


def send_mailing():
    mailing_list = Mailing.objects.filter(at_work='True')
    for mail in mailing_list:
        user_pk = mail.user.pk
        client_list = Client.objects.filter(user__pk=user_pk)
        print(f"попытка отправки{mail.title} по адресам {client_list}")
        send_mail(
            subject=mail.title,
            message=mail.content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=client_list,
            fail_silently=False,
        )
