# Generated by Django 5.1 on 2024-08-11 18:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0014_alter_mailing_at_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='recipient_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150, verbose_name='список получателей'), default=None, size=None),
            preserve_default=False,
        ),
    ]
