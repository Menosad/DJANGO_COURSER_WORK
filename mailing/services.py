import datetime
import smtplib

import pytz
from django.conf import settings
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from mailing.models import Mailing, MailingAttempt


def send_mailing():
    mailing_list = Mailing.objects.filter(at_work=True)
    for mail in mailing_list:
        now = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
        next_send = mail.departure_date + datetime.timedelta(days=mail.periodicity)
        print(f"сейчас - {now}, дата запуска - {mail.departure_date}, следующий запуск - {next_send}")
        # try:
        #     server_response = send_mail(
        #         subject=mail.title,
        #         message=mail.content,
        #         from_email=EMAIL_HOST_USER,
        #         recipient_list=mail.get_recipient_list(),
        #         fail_silently=False,
        #     )
        #     MailingAttempt.objects.create(mailing=mail, status=True, server_response=server_response)
        # except smtplib.SMTPException as error:
        #     MailingAttempt.objects.create(mailing=mail, status=False, server_response=error)
        # except ValueError as value_error:
        #     MailingAttempt.objects.create(mailing=mail, status=False, server_response=value_error)
