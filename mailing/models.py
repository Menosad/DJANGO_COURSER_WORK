import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.db import models

from config.settings import EMAIL_HOST_USER
from users.models import User

NULLABLE = {'null': True, 'blank': True}
periodicity_CHOICES = (('', 'раз в день'), ('', 'раз в неделю'), ('', 'раз в месяц'))


class Mailing(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержание')
    departure_date = models.DateTimeField(verbose_name='дата и время отправки')
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
        send_mail(
            subject=self.title,
            message=self.content,
            from_email=EMAIL_HOST_USER,
            recipient_list=self.get_recipient_list(),
            fail_silently=False,
           )

    def activate(self, start_date):
        from django.utils import timezone
        tz = timezone.get_default_timezone()
        stop_date = start_date + datetime.timedelta(days=30)
        now = datetime.datetime.now(tz=tz)
        if stop_date > now > start_date:
            self.at_work = True
        else:
            self.at_work = False


    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('title',)
