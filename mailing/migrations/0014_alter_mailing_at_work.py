# Generated by Django 5.0.6 on 2024-08-08 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0013_mailing_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='at_work',
            field=models.BooleanField(default=False, null=True, verbose_name='в работе'),
        ),
    ]
