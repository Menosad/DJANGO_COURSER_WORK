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

    def send_mail(self):
        client_list = self.recipient_list.split(',')
        recipient_list = []
        for mail in client_list:
            edit = mail.replace(' ', '')
            recipient_list.append(edit)
        print(f"{recipient_list}: тип{type(recipient_list)}")
        print(f"{recipient_list[0]}: тип{type(recipient_list[0])}")
        # send_mail(
        #     subject=self.title,
        #     message=self.content,
        #     from_email=EMAIL_HOST_USER,
        #     recipient_list=self.recipient_list,
        #    )

    def __str__(self):
        return f"{self.title}"

    def send(self):
        send_mail(
            subject=self.title,
            message=self.content,
            from_email=EMAIL_HOST_USER,
            recipient_list=self.recipient_list,
           )

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('title',)
