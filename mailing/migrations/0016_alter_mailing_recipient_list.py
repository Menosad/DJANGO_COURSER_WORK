# Generated by Django 5.1 on 2024-08-12 14:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0015_mailing_recipient_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='recipient_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=150, null=True, verbose_name='список получателей'), size=None),
        ),
    ]