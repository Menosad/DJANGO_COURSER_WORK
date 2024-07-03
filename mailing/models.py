from django.db import models

NULLABLE = {'null': True, 'blank': True}


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
