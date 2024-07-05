from django.db import models

NULLABLE = {'null': True, 'blank': True}
periodicity_CHOICES = (('', 'раз в день'), ('', 'раз в неделю'), ('', 'раз в месяц'))


class User(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    nickname = models.CharField(max_length=150, verbose_name='никнэйм', unique=True)
    label = models.ImageField(upload_to='labels', **NULLABLE, verbose_name='лэйбел')
    created_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return f"{self.name}({self.nickname})"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('created_at',)


class Mailing(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='никнэйм')
    departure_date = models.DateTimeField(verbose_name='дата отправки')
    at_work = models.BooleanField(default=False, verbose_name='в работе')
    periodicity = models.DateTimeField(verbose_name='периодичность', choices=periodicity_CHOICES)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('title',)
