import datetime
import smtplib

import pytz
from django.conf import settings
from django.core.mail import send_mail
from django.db import models

from config.settings import EMAIL_HOST_USER
from users.models import User

NULLABLE = {'null': True, 'blank': True}
periodicity_CHOICES = (('', 'раз в день'), ('', 'раз в неделю'), ('', 'раз в месяц'))


class Mailing(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок', unique=True)
    content = models.TextField(verbose_name='содержание')
    departure_date = models.DateTimeField(verbose_name='дата и время отправки')
    next_send_date = models.DateTimeField(verbose_name='дата следующей отправки', **NULLABLE)
    at_work = models.BooleanField(default=False, verbose_name='в работе', null=True)
    periodicity = models.IntegerField(verbose_name='периодичность', choices=periodicity_CHOICES, **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mailings', **NULLABLE)
    recipient_list = models.TextField(verbose_name='список получателей', **NULLABLE)

    def get_recipient_list(self):
        client_list = self.recipient_list.split(',')
        recipient_list = []
        for mail in client_list:
            edit = mail.replace(' ', '')
            recipient_list.append(edit)
        return recipient_list

    def __str__(self):
        return f"{self.title}"

    def send(self):
        zone = pytz.timezone(settings.TIME_ZONE)
        now = datetime.datetime.now(zone)
        try:
            server_response = send_mail(
                subject=self.title,
                message=self.content,
                from_email=EMAIL_HOST_USER,
                recipient_list=self.get_recipient_list(),
                fail_silently=False,
               )
            MailingAttempt.objects.create(mailing=self, last_try=now, status=True, server_response=server_response)
        except smtplib.SMTPException as error:
            MailingAttempt.objects.create(mailing=self, last_try=now, status=False, server_response=error)
        except ValueError as value_error:
            MailingAttempt.objects.create(mailing=self, last_try=now, status=False, server_response=value_error)

    def activate(self, start_date):
        stop_date = start_date + datetime.timedelta(days=30)
        offset = datetime.timedelta(hours=3)
        date = datetime.datetime.now(tz=datetime.timezone.utc)
        now = date + offset
        if stop_date > now > start_date:
            self.at_work = True
            self.save()
        else:
            self.at_work = False
            self.save()

class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('title',)


class MailingAttempt(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')
    last_try = models.DateTimeField(verbose_name='дата последней попытки', auto_now=True)
    status = models.BooleanField(verbose_name='статус рассылки')
    server_response = models.TextField(verbose_name='ответ сервера', **NULLABLE)

    def __repr__(self):
        return f"попытка {self.mailing.title}"


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя клиента')
    email = models.EmailField(verbose_name='почта клиента', unique=True)
    user = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE, **NULLABLE)

    def __repr__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('name',)
