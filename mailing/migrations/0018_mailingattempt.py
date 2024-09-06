# Generated by Django 5.1 on 2024-08-22 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0017_alter_mailing_recipient_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_try', models.DateTimeField(auto_now=True, verbose_name='дата последней попытки')),
                ('status', models.BooleanField(verbose_name='статус рассылки')),
                ('server_response', models.TextField(blank=True, null=True, verbose_name='ответ сервера')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='рассылка')),
            ],
        ),
    ]