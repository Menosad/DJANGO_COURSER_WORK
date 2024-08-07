from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}
periodicity_CHOICES = (('', 'раз в день'), ('', 'раз в неделю'), ('', 'раз в месяц'))


class Mailing(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержание')
    departure_date = models.DateTimeField(verbose_name='дата и время отправки')
    at_work = models.BooleanField(default=False, verbose_name='в работе')
    periodicity = models.IntegerField(verbose_name='периодичность', choices=periodicity_CHOICES, **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mailings', **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('title',)
