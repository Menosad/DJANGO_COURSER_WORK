from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    nickname = models.CharField(max_length=150, verbose_name='никнэйм', unique=True)
    label = models.ImageField(upload_to='labels', **NULLABLE, verbose_name='лэйбел')
